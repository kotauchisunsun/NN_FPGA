/* STRUCT_NEURAL */

module STRUCT_NEURAL(
    inputA,
    inputB,
    coeff111, //depth,neural,signal_source
    coeff112,
    coeff121,
    coeff122,
    coeff211,
    coeff212,
    coeff221,
    coeff222,
    bias11,
    bias12,
    bias21,
    bias22,
    out1,
    out2
);

parameter width = 16;
input  [width:1] inputA,inputB,coeff111,coeff112,coeff121,coeff122,coeff211,coeff212,coeff221,coeff222;
input  [width:1] bias11,bias12,bias21,bias22;

output [width:1]  out1,out2;
wire [width:1] p_result11,p_result12;
wire [width:1] q_result11,q_result12;
wire [width:1] result11,result12,result21,result22;

NEURAL_LAYER nl1(    inputA,    inputB,coeff111,coeff112,coeff121,coeff122,bias11,bias12,q_result11,q_result12);
NEURAL_LAYER nl2(q_result11,q_result12,coeff211,coeff212,coeff221,coeff222,bias21,bias22,      out1,      out2);

endmodule
