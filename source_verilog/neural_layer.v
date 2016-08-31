/* NEURAL_LAYER */

module NEURAL_LAYER( inputA, inputB , coeff11, coeff12, coeff21, coeff22, out1 , out2 );
parameter width = 16;

input [width:1] inputA,inputB,coeff11,coeff12,coeff21,coeff22;
output [width:1] out1,out2;
wire n_out1,n_out2;

CALC_NEURAL n1(inputA,inputB,coeff11,coeff12,n_out1);
CALC_NEURAL n2(inputA,inputB,coeff21,coeff22,n_out2);

assign out1 = n_out1 << (width/2);
assign out2 = n_out2 << (width/2);

endmodule
