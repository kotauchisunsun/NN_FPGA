"""
A * B
= A0 * 2^N * B0 * 2^N
= A0 * B0 * 2^N * 2^N

C = C0 * 2^N
C0 = A0 * B0 * 2^N

"""

def generate_float(mul_name,width):
    conf = {
        "mul_name":mul_name,
        "width":width
    }

    mul_function =  "0 \n+%s"%(
        "+".join(
            "( (B2[ %d]) ? A2 << %d : 0 )\n"%(i+1,i)
            for i
            in range(width)
        )
    )

    return  """
module {mul_name} ( A, B, out ) ;
parameter width = {width};
parameter half      = width/2;
input  [width:1] A,B;
output [width:1] out ;
wire [2*width:1] temp;

assign temp = A*B;
assign out = temp[half+width:half+1];

endmodule 

//-------------------------------------------------
""".format(
    mul_name=mul_name,
    width=width,
    func=mul_function
)

if __name__=="__main__":
    print generate_float(
        "MUL_FIX_POINT_FLOAT",
        16
    )
