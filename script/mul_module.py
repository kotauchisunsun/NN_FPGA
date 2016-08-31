#coding:utf-8
from gen_float import generate_float

class mul_module(object):
    def __init__(self,name,width):
        self.name      = name
        self.width     = width

    def generate_source(self):
        return generate_float(self.name,self.width)
