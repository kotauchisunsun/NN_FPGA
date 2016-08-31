#coding:utf-8
from neural_module import neural_module

class neural_module_manager(object):
    def __init__(self,mmm):
        self.mmm  = mmm
        self.objs = dict()

    def __get_name(self,width,input_num):
        return "NM_%03d_%04d" % (width,input_num)

    def get_module(self,width,input_num):
        name = self.__get_name(width,input_num)

        return self.objs.setdefault(
            name,
            neural_module(
                name,
                input_num,
                self.mmm.get_module(width)
            )
        )
         
    def generate_source(self):
        return "\n".join(
            obj.generate_source()
            for obj
            in self.objs.values()
        )
