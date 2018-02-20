from base import *
from devices import *

class Photon(Board):

    @staticmethod
    def match(dev):
        return dev["vid"]=="2B04" and dev["pid"]=="C006"

    def reset(self):
        pass

    def burn(self,bin,outfn=None):
        return False,"Must be put in DFU mode first!"

