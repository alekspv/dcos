"""Winpanda: Windows service management: NSSM-based manager definition.

Ref:
  [1] NSSM - the Non-Sucking Service Manager
      https://nssm.cc/description
  [2] nssm/README.txt
      https://git.nssm.cc/nssm/nssm/src/master/README.txt
"""
import sys
from subprocess import PIPE, run

from . import base


@base.svcm_type('nssm')
class WinSvcManagerNSSM(base.WindowsServiceManager):
    """NSSM-based Windows service manager."""
#    INSTALL = 'nssm install'
#    SET = 'nssm set'
#    RUN = 'nssm start'
    BLOCK = 'main'
    SERVICE_NAME = 'servicename'
    OPTIONS = ('servicename', 'Application', 'AppDirectory', 'AppParameters',
               'DisplayName', 'Description', 'Start', 'DependOnService', 'AppStdout',
               'AppStderr', 'AppEnvironmentExtra'
               )

    nssm = 'nssm'

    __type_name__ = 'nssm'

    def __init__(self, svcm_opts=None):
        """Constructor.

        :param svcm_opts: dict, service manager options:
                         {
                             'executor':     <string>,
                             'exec_path':   <string>
                         }
        """
        self.verify_svcm_options(svcm_opts)
        super(WinSvcManagerNSSM, self).__init__(svcm_opts=svcm_opts)

    def verify_svcm_options(self, path_to_nssm):
        if path_to_nssm is not None:
            self.nssm = path_to_nssm
        try:
            result = run(self.nssm, stdout=PIPE, stderr=PIPE, universal_newlines=True)
            status = result.returncode
        except FileNotFoundError:
            sys.stderr.write('nssm not found')
        if status != 1:
            sys.stderr.write('nssm not run')

    def cmd(self, command):
        """execute system command
        """
        result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        if result.returncode:
            sys.stderr.write(result.stderr)

    def init_sets(self, config_file):
        """initializing service parameters
        """
        command = []
        try:
            from configparser import ConfigParser
        except ImportError:
            from ConfigParser import ConfigParser  # ver. < 3.0
        self.config = ConfigParser()

        self.config.read(config_file)

        for option in self.OPTIONS:
            if self.config.has_option(self.BLOCK, option):
                if option == self.SERVICE_NAME:
                    command.append('{} {} {} {}'.format(
                        self.nssm, 'install', self.config.get
                        (self.BLOCK, option), 'confirm'))
                    self.service_name = self.config.get(self.BLOCK,
                                                        self.SERVICE_NAME)
                elif self.config.has_option(self.BLOCK, option):
                    command.append('{} {} {} {} {}'.format
                                   (self.nssm, 'install', self.service_name, option,
                                    self.config.get(self.BLOCK, option)))
        return command

    def setup(self, config_file):
        for i in self.init_sets(config_file):
            self.cmd(i)

    def remove(self, service_name):
        self.cmd('{} remove {} confirm'.format(self.nssm, service_name))

    def start(self, service_name):
        self.cmd('{} start {}'.format(self.nssm, service_name))

    def stop(self, service_name):
        self.cmd('{} stop {}'.format(self.nssm, service_name))

    def enable(self, service_name):
        self.cmd('{} {} {} {}'.format(self.nssm, 'set', service_name,
                                      'Start SERVICE_AUTO_START'))

    def disable(self, service_name):
        self.cmd('{} {} {} {}'.format(self.nssm, 'set', service_name,
                                      'Start SERVICE_DISABLED'))

    def status(self, service_name):
        result = run('nssm status {}'.format(service_name),
                     stdout=PIPE, stderr=PIPE, universal_newlines=True)
        print(result.stdout)
