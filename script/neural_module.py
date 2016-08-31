#coding:utf-8
from gen_nm import generate_neural

class neural_module(object):
    def __init__(self,name,input_num,mm):
        self.mm = mm

        self.name = name
        self.width = mm.width

        self.input_num = input_num
        self.coefficient_num = input_num
        self.output_num = 1


    def generate_source(self):
        return generate_neural(
            self.name,
            self.mm.name,
            self.width,
            self.input_num
        )

