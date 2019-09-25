"""Class for reading and parsing Cluster config"""
class ClusterConfig(object):
    def __init__(self, options):
        self.masters = list()
        self.roles = list()
        self.dist_storage_url = str()

    def readClusterConfig(parameter_list):
        pass