#coding:utf-8
from gen_nl import generate_neural_layer

class neural_layer(object):
    def __init__(self,name,module_num,nm):
        self.nm = nm
        self.module_num = module_num

        self.name = name
        self.width = nm.width

        self.input_num = nm.input_num
        self.bias_num = module_num
        self.coefficient_num = nm.coefficient_num * module_num
        self.output_num = nm.output_num * module_num

    def generate_source(self):
        return generate_neural_layer(
            self.name,
            self.width,
            self.input_num,
            self.module_num,
            self.nm.name
        )

