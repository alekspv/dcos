import configparser

class PkgConfig(object):
   

    def __str__(self):
        return self.__repr__()

    def __init__(self):
        self.pkg_info =dict()
        self.svc_conf = configparser.ConfigParser()
        self.pkg_ini= configparser.ConfigParser()
        

       
 
