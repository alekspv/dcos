"""interface for winpanda Command"""

import abc
from core.CmdConfig import CmdConfig
from os import linesep

class Command(metaclass=abc.ABCMeta):
    
    def __init__(self, options):
        self.config = CmdConfig(options)
        self.options = options
        print("DEBUG::",__name__, "__init__ Executed","options:: {}".format(options),linesep)

    def configure(self, options):
        print("DEBUG::",__name__, "configure() Executed", "options::{}".format(options),linesep)

    def execute(self, config):
        raise NotImplementedError