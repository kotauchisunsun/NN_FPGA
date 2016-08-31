#coding:utf-8
from neural_layer import neural_layer

class neural_layer_manager(object):
    def __init__(self,nmm):
        self.nmm  = nmm
        self.objs = dict()

    def __get_name(self,width,input_num,module_num):
        return "NL_%03d_%04d_%04d" % (width,input_num,module_num)

    def get_module(self,width,input_num,module_num):
        name = self.__get_name(width,input_num,module_num)

        return self.objs.setdefault(
            name,
            neural_layer(
                name,
                module_num,
                self.nmm.get_module(
                    width,
                    input_num
                )
            )
        )
         
    def generate_source(self):
        return "\n".join(
            obj.generate_source()
            for obj
            in self.objs.values()
        )
