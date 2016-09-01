#coding:utf-8
from itertools import chain

def generate_neural_layer(name,width,input_num,unit_num,nn_module_name):
    bias_num = unit_num

    nns = [
        "nn_unit%04d" % i
        for i
        in range(unit_num)
    ]

    input_vals = [
        "input_%04d"%(i)
        for i
        in range(input_num)
    ]

    input_definition = "\n".join(
        "input wire [width:1] %s;"%(v)
        for v
        in input_vals
    )

    bias_vals = [
        "bias_%04d" % i
        for i
        in range(unit_num)
    ]

    bias_definition = "\n".join(
        "input [width:1] %s;" % v
        for v
        in bias_vals
    )

    output_vals = [
        "output_%04d"%(i)
        for i
        in range(unit_num)
    ]

    output_definition = "\n".join(
        "output wire [width:1] %s;"%(v)
        for v
        in output_vals
    )

    nn_output_vals = [
        "nn_output_%04d"%(i)
        for i
        in range(unit_num)
    ]

    nn_output_definition = "\n".join(
        "wire %s;"%(v)
        for v
        in nn_output_vals
    )

    coeff_dict = {
        name : [
            "coeff_%04d_for_%s"%(i,name)
            for i
            in range(input_num)
        ]
        for name
        in nns
    }

    coeff_vals = list(chain(*coeff_dict.values()))

    coeff_definition = "\n".join(
        "input wire [width:1] %s;"%(v)
        for v
        in chain(*coeff_dict.values())
    )

    assign_operation = "\n".join(
        "assign {output_val} = ({nn_output_val}) << (width/2);".format(
            output_val=output_val,
            nn_output_val=nn_output_val
        )
        for nn_output_val,output_val
        in zip(nn_output_vals,output_vals)
    )

    nns_definition = "\n".join(
        "%s %s(%s);"%(
            nn_module_name,
            nns_name,
            ",".join(
                input_vals + coeff_dict[nns_name] + [bias_vals[i]] + [nn_output_vals[i]]
            )
        )  
        for i,nns_name
        in enumerate(nns)
    )

    return """
module {name}({params});
parameter width = {width};
{input_definition}
{bias_definition}
{coeff_definition}
{output_definition}
{nn_output_definition}
{nns_definition}
{assign_operation}

endmodule
""".format(
    name = name,
    params = ",".join(input_vals+coeff_vals+bias_vals+output_vals),
    width = width,
    input_definition = input_definition,
    bias_definition = bias_definition,
    coeff_definition = coeff_definition,
    output_definition = output_definition,
    nn_output_definition = nn_output_definition,
    nns_definition = nns_definition,
    assign_operation = assign_operation
)

if __name__=="__main__":
    print generate_neural_layer("NEURAL_LAYER",16,2,2,"CALC_NEURAL");
