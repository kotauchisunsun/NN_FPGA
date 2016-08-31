#coding:utf-8
from mul_module import mul_module

class mul_module_manager(object):
    def __init__(self):
        self.objs = dict()

    def __get_name(self,width):
        return "MUL_%02d" % width

    def get_module(self,width):
        name = self.__get_name(width)

        return self.objs.setdefault(
            name,
            mul_module(name,width)
        )

    def generate_source(self):
        return "\n".join(
            obj.generate_source()
            for obj
            in self.objs.values()
        )
