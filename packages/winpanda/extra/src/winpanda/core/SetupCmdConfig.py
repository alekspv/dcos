import abc
from core.CmdConfig import CmdConfig
from core.Package import Package
from os import linesep


class SetupCmdConfig(CmdConfig):
    
    def __init__(self, options):
        self.packages = Package(options['basepath'],options['pkgID'])

        print("DEBUG:",__name__, "__init__ Executed","options:: {}".format(options),linesep)
        
    
    def get_packages(self, options):
        packages_list = [1,2,3]
        return packages_list
    def create_treeinfo(self,packages):
        pass