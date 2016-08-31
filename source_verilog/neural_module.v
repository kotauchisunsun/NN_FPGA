/* EASY_NEURAL */

module CALC_NEURAL( inputA , inputB , coeffA , coeffB , out );
parameter width = 16;

input  [width:1] inputA,inputB,coeffA,coeffB;
output out;
wire [width:1] resultA,resultB,add_result;

MUL_FIX_POINT_FLOAT m1 (  inputA,  coeffA,   resultA );
MUL_FIX_POINT_FLOAT m2 (  inputB,  coeffB,   resultB );

assign add_result = resultA + resultB;
assign out = add_result!=0 && ~add_result[width];

endmodule
