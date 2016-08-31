def composit(module_name,layer1_name,layer2_name,width,input1_num,coefficient1_num,input2_num,coefficient2_num,output_num):
    input1_vals = [
        "input1_%04d_val" % i
        for i
        in range(input1_num)
    ]

    input1_def = "\n".join( "input wire [width:1] %s;"%v
        for v
        in input1_vals
    )

    coefficient1_vals = [
        "coeff1_%04d_val" % i
        for i
        in range(coefficient1_num)
    ]

    coefficient1_def = "\n".join(
        "input wire [width:1] %s;"%v
        for v
        in coefficient1_vals
    )

    output1_vals = input2_vals = [
        "input2_%04d_val" % i
        for i
        in range(input2_num)
    ]

    input2_def = "\n".join(
        "wire [width:1] %s;"%v
        for v
        in input2_vals
    )

    coefficient2_vals = [
        "coeff2_%04d_val" % i
        for i
        in range(coefficient2_num)
    ]

    coefficient2_def = "\n".join(
        "input wire [width:1] %s;"%v
        for v
        in coefficient2_vals
    )

    output2_vals = [
        "output2_%04d_val" % i
        for i
        in range(output_num)
    ]

    output2_def = "\n".join(
        "output wire [width:1] %s;"%v
        for v
        in output2_vals
    )

    nl_vals = [
        "nl1",
        "nl2"
    ]

    n1_def = "%s %s(%s);"%(
        layer1_name,
        "nl1",
        ",".join(input1_vals+coefficient1_vals+output1_vals)
    )

    n2_def = "%s %s(%s);"%(
        layer2_name,
        "nl2",
        ",".join(input2_vals+coefficient2_vals+output2_vals)
    )

    return """
module {module_name}({params});
parameter width = {width};
{input1_def}
{input2_def}
{coefficient1_def}
{coefficient2_def}
{output2_def}
{n1_def}
{n2_def}

endmodule
""".format(
    module_name = module_name,
    params = ",".join(input1_vals+coefficient1_vals+coefficient2_vals+output2_vals),
    width = width,
    input1_def = input1_def,
    input2_def = input2_def,
    coefficient1_def = coefficient1_def,
    coefficient2_def = coefficient2_def,
    output2_def = output2_def,
    n1_def = n1_def,
    n2_def = n2_def
)

if __name__=="__main__":
    print composit("STRUCT_NEURAL","NEURAL_LAYER","NEURAL_LAYER",16,2,4,2,4,2)
