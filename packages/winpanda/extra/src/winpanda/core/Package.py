""" test example

from core.Package import Package
from utils import *

options = {
            'basepath': "./dcos",
            'pkgId':'mesos--08458064bac9e3236fd5b0fece4300f88acb1b10'           
}


Pkg=Package(options['basepath'], options['pkgId'])"""

import abc
from core.Pkgconfig import PkgConfig
from pathlib import Path, PurePath
import json
import configparser
from os import linesep


class Package(object):
    """Package class for DC/OS distribution.
    """
    def __init__(self, basepath, pkgId):
        """Initialiser.
        """
        self.basepath=basepath
        self.pkgId=pkgId
        self.pkgConfig = PkgConfig()
        self.pkinfofile='pkginfo.json'
        self.inifile ='package.ini'
        self.svcfile ='package.nssm'
        self.readpkginfo(basepath,pkgId)
        self.readini(basepath,pkgId)
        self.readsvc(basepath,pkgId)


    def __repr__(self):
        return (
            '<%s(dse="%s")>' % (self.__class__.__name__, self.dse_opts)
        )

    def __str__(self):
        return self.__repr__()

  
    def readpkginfo(self, basepath, pkgId):
        P1 = Path(basepath)
        P1=P1.joinpath(pkgId,self.pkinfofile)

        if P1.exists():
            with open(P1,'r') as f:
                packageInfo= json.load(f)
        
        
        self.pkgConfig.pkg_info.update(packageInfo)
        print("Package DEBUG:",self.pkgConfig.pkg_info,linesep)
       

    def readini(self, basepath, pkgId):
        inipath=Path(basepath)
        inipath=inipath.joinpath(pkgId,self.inifile)
        if inipath.exists():
            #pkg_ini = configparser.ConfigParser(strict=False)
            pkg_ini = configparser.ConfigParser()
            with open(inipath, 'r') as f:
                pkg_ini.read_file(f)
            self.pkgConfig.pkg_ini=pkg_ini


    def readsvc(self, basepath, pkgId):
        svcpath=Path(basepath)
        svcpath=svcpath.joinpath(pkgId,self.svcfile)
        if svcpath.exists():
            pkg_svc = configparser.ConfigParser()
            with open(svcpath, 'r') as f:
                pkg_svc.read_file(f)
            self.pkgConfig.svc_conf=pkg_svc
           

    def savestate(self):
        pass

    def createinstaller(self, PkgConfig):
        pass   

    def install(self,installer):
        pass

