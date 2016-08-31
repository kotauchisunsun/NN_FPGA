#coding:utf-8
from mul_module_manager import mul_module_manager
from neural_module_manager import neural_module_manager
from neural_layer_manager import neural_layer_manager
from neural_net_manager import neural_net_manager

class manager_factory(object):
    def __init__(self):
        self.mmm = mul_module_manager()
        self.nmm = neural_module_manager(self.mmm)
        self.nlm = neural_layer_manager(self.nmm)
        self.nnm = neural_net_manager()

    def generate_source(self):
        return "\n".join(
            obj.generate_source()
            for obj
            in [
               self.mmm,
               self.nmm,
               self.nlm,
               self.nnm
            ]
        )
