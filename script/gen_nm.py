def generate_neural(module_name,mul_func_name,width,input_num):
    input_vals = [
        "in_%04d"%i
        for i
        in range(input_num)
    ]

    coeff_vals = [
        "coeff_%04d"%i
        for i
        in range(input_num)
    ]

    mul_results = [
        "results_%04d"%i
        for i
        in range(input_num)
    ]

    return """
module {module_name}({inputs},{coeffs},out);
parameter width = {width};

input [width:1] {inputs};
input [width:1] {coeffs};
output out;
wire [width:1] {results};
wire [width:1] add_result;

{muls}
assign add_result = {adds};

assign out = add_result!=0 && ~add_result[width];

endmodule
""".format(
    module_name = module_name,
    width = width,
    inputs=",".join(input_vals),
    coeffs=",".join(coeff_vals),
    results=",".join(mul_results),
    muls="\n".join(
        "{mul_func_name} m{idx:04d} ( {i:8s} , {c:8s} , {r:8s} );".format(
            mul_func_name = mul_func_name,
            idx=idx,
            i=i,
            c=c,
            r=r
        )
         for idx,(i,c,r)
         in enumerate(zip(input_vals,coeff_vals,mul_results))
    ),
    adds=" + ".join(mul_results)
)

if __name__=="__main__":
    print generate_neural("CALC_NEURAL","MUL_FIX_POINT",16,2)
