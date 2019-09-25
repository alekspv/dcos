"""Setup Command implementation
test example:
from core.SetupCommand import SetupCommand
cmd = SetupCommand({'basepath':'./dcos','pkgID':'mesos--08458064bac9e3236fd5b0fece4300f88acb1b10'})
# cmd.configure("asd")
cmd.fetch_active_pkg_list(cmd.setup_cmd_config)

"""

import abc
from core.Command import Command
from core.ClusterConfig import ClusterConfig
from core.SetupCmdConfig import SetupCmdConfig
from os import linesep

class SetupCommand(Command):
    def __init__(self,options):
        #super().__init__(options)
        #super().configure(options)
        self.setup_cmd_config = SetupCmdConfig(options)
        print("DEBUG::",__name__, "__init__ Executed","options:: {}".format(options),linesep)
    
    def fetch_active_pkg_list(self, setup_cmd_config):
        pkg_ids = [1,2,3]
        return pkg_ids
        
    def create_pkg_repo(self, pkg_ids):
        pass