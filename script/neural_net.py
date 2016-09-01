#coding:utf-8
from composit_nl import composit

class neural_net(object):
    def __init__(self,name,component1,component2):
        self.component1 = component1
        self.component2 = component2

        self.name = name
        self.width = component1.width

        self.input_num = component1.input_num
        self.coefficient_num = component1.coefficient_num + component2.coefficient_num
        self.bias_num = component1.bias_num + component2.bias_num
        self.output_num = component2.output_num

    def generate_source(self):
        return composit(
            self.name,
            self.component1.name,
            self.component2.name,
            self.width,
            self.component1.input_num,
            self.component1.coefficient_num,
            self.component1.bias_num,
            self.component2.input_num,
            self.component2.coefficient_num,
            self.component2.bias_num,
            self.output_num
        )
