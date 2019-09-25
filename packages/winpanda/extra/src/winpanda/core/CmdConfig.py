"""Interface for Command config"""
import abc
from core.ClusterConfig import ClusterConfig


class CmdConfig(metaclass=abc.ABCMeta):
    def __init__(self, options):
        self.cluster_conf = ClusterConfig(options)
        self.options = options
        print("DEBUG:",__name__, "__init__() Executed", "options::{}".format(options))


