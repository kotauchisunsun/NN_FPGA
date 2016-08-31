module NEURAL_MODULE_TEST;

reg [16:1] A,B,cA,cB;
wire [1:1] f;

CALC_NEURAL cn ( A, B, cA, cB, f);

initial begin
    $dumpfile("neural_MODULE_test.vcd");
    $dumpvars(0,NEURAL_MODULE_TEST);
    $monitor (
        "%t: A = %04x , B = %04x , cA = %04x , cB = %04x , f = %d",
        $time,
        A,
        B,
        cA,
        cB,
        f
    );
    
        A = 16'h0100; B = 16'h0100; cA = 16'h0100; cB = 16'h0100;
    #10 A = 16'h0100; B = 16'h0100; cA = 16'h0100; cB = -(16'h0100);
    #10 A = 16'h0080; B = 16'h0100; cA = 16'h0100; cB = -(16'h0100);
    #10 A = 16'h0F00; B = 16'h0F01; cA = 16'h0100; cB = -(16'h0100);
    #10 A = 16'h0F01; B = 16'h0F00; cA = 16'h0100; cB = -(16'h0100);
    #10 A =-(16'h0100); B = -(16'h0100); cA = -(16'h0100); cB = -(16'h0100);
    #10 A = 16'h0000; B = -(16'h0100); cA = -(16'h0100); cB = -(16'h0100);
    #10 A = 16'h0000; B = 16'h0100; cA = -(16'h0100); cB = -(16'h0100);
    #10 $finish;
end

endmodule
