module FIX_POINT_FLOAT_TEST;

reg  [16:1] A,B,bias;
wire [16:1] mul_out;

MUL_FIX_POINT_FLOAT w ( A, B, mul_out ) ;

initial begin
    $dumpfile("fix_point_float_test.vcd");
    $dumpvars(0,FIX_POINT_FLOAT_TEST);
    $monitor (
        "%t: A = %04x , B = %04x , mul_out = %04x", $time,
        A,
        B,
        mul_out,
    );
        A = 16'h0100; B = 16'h0100;
    #10 A = 16'h0100; B = 16'h0200;
    #10 A = 16'h0200; B = 16'h0100;
    #10 A = 16'h0100; B = 16'h0080;
    #10 A = 16'h0300; B = 16'h0100;
    #10 A = 16'h0300; B = 16'h0300;
    #10 A = 16'h0030; B = 16'h0030;
    #10 A = 16'h00a0; B = 16'h0040;
    #10 A = 16'h0300; B = (~(16'h0200) + 16'h0001);
    #10 A = 16'h0000; B = 16'hfa00;
    #10 A = 16'h0100; B = -(16'h0100);
    #10 $finish;
end

endmodule
