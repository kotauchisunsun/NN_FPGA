#coding:utf-8
from manager_factory import manager_factory

def construct_neural_net(width,input_num,structure,output_num):
    full_structure = [input_num] + structure + [output_num]   
    mf = manager_factory()
    
    nls = [
        mf.nlm.get_module(
            width,
            a,
            b
        )
        for a,b
        in zip(
            full_structure[0:-1],
            full_structure[1:]
        )
    ]

    while len(nls)!=1:
        layer1 = nls.pop(0)
        layer2 = nls.pop(0)

        nls.insert(
            0,
            mf.nnm.get_module(
                layer1,
                layer2
            )
        )
    
    print nls[0].name
    with open("generate.v","w") as f:
        print>>f,mf.generate_source()
        print 'saved to generate.v'

if __name__=="__main__":
    mf = manager_factory()

    width = 16

    print construct_neural_net(width,2,[2],2)
    #print construct_neural_net(width,320,[160,80,40,20],10)
