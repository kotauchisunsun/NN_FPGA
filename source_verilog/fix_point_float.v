/* FIX_POINT_FLOAT */

module ADD_FIX_POINT_FLOAT ( A, B, out );
parameter width = 16;
input  [width:1] A,B;
output [width:1] out;

assign out = A + B;

endmodule


//-------------------------------------------------


module SUB_FIX_POINT_FLOAT ( A, B, out ) ;
parameter width = 16;
input  [width:1] A,B;
output [width:1] out;

assign out = A - B;

endmodule


//-------------------------------------------------



module MUL_FIX_POINT_FLOAT ( A, B, out ) ;
parameter width = 16;
input  [width:1] A,B;
output [width:1] out ;
genvar i;

parameter half      = width/2;
parameter half_mask = ((1<<(half+1))-1);
parameter top_mask  = half_mask << (half);

wire [width:1] A2,B2;
wire [2*width:1] temp;
wire [1:1] flag;

assign flag = A[width] ^ B[width];

assign A2 = A[width] ? -A : A;
assign B2 = B[width] ? -B : B;

assign temp = (
    0
    + ( (B2[ 1]) ? A2 << (  1 - 1 ) : 0 )
    + ( (B2[ 2]) ? A2 << (  2 - 1 ) : 0 )
    + ( (B2[ 3]) ? A2 << (  3 - 1 ) : 0 )
    + ( (B2[ 4]) ? A2 << (  4 - 1 ) : 0 )
    + ( (B2[ 5]) ? A2 << (  5 - 1 ) : 0 )
    + ( (B2[ 6]) ? A2 << (  6 - 1 ) : 0 )
    + ( (B2[ 7]) ? A2 << (  7 - 1 ) : 0 )
    + ( (B2[ 8]) ? A2 << (  8 - 1 ) : 0 )
    + ( (B2[ 9]) ? A2 << (  9 - 1 ) : 0 )
    + ( (B2[10]) ? A2 << ( 10 - 1 ) : 0 )
    + ( (B2[11]) ? A2 << ( 11 - 1 ) : 0 )
    + ( (B2[12]) ? A2 << ( 12 - 1 ) : 0 )
    + ( (B2[13]) ? A2 << ( 13 - 1 ) : 0 )
    + ( (B2[14]) ? A2 << ( 14 - 1 ) : 0 )
    + ( (B2[15]) ? A2 << ( 15 - 1 ) : 0 )
    + ( (B2[16]) ? A2 << ( 16 - 1 ) : 0 )
);

assign out = flag[1] ? -temp[width+half+1:half+1] : temp[width+half+1:half+1];

endmodule 



//-------------------------------------------------




module DIV_FIX_POINT_FLOAT ( A, B, out ) ;
//include bugs
parameter width = 16;
parameter half  = width/2;
input  [width:1] A,B;
output [width:1] out;

assign out = (
    0
    + ( (B[ 1]) ? A >> (  1 - 1 - half ) : 0 )
    + ( (B[ 2]) ? A >> (  2 - 1 - half ) : 0 )
    + ( (B[ 3]) ? A >> (  3 - 1 - half ) : 0 )
    + ( (B[ 4]) ? A >> (  4 - 1 - half ) : 0 )
    + ( (B[ 5]) ? A >> (  5 - 1 - half ) : 0 )
    + ( (B[ 6]) ? A >> (  6 - 1 - half ) : 0 )
    + ( (B[ 7]) ? A >> (  7 - 1 - half ) : 0 )
    + ( (B[ 8]) ? A >> (  8 - 1 - half ) : 0 )
    + ( (B[ 9]) ? A >> (  9 - 1 - half ) : 0 )
    + ( (B[10]) ? A >> ( 10 - 1 - half ) : 0 )
    + ( (B[11]) ? A >> ( 11 - 1 - half ) : 0 )
    + ( (B[12]) ? A >> ( 12 - 1 - half ) : 0 )
    + ( (B[13]) ? A >> ( 13 - 1 - half ) : 0 )
    + ( (B[14]) ? A >> ( 14 - 1 - half ) : 0 )
    + ( (B[15]) ? A >> ( 15 - 1 - half ) : 0 )
    + ( (B[16]) ? A >> ( 16 - 1 - half ) : 0 )
);

endmodule
