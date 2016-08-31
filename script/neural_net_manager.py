#coding:utf-8
from neural_net import neural_net

class neural_net_manager(object):
    def __init__(self):
        self.objs = dict()

    def __get_name(self,name1,name2):
        return "NN_%s_%s" % (name1,name2)

    def get_module(self,component1,component2):
        name = self.__get_name(component1.name,component2.name)

        return self.objs.setdefault(
            name,
            neural_net(
                name,
                component1,
                component2
            )
        )
         
    def generate_source(self):
        return "\n".join(
            obj.generate_source()
            for obj
            in self.objs.values()
        )
