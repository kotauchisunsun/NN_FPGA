module NEURAL_LAYER_TEST;

reg [16:1] A,B,cAA,cAB,cBA,cBB,b1,b2;
wire [16:1] o1,o2;
NEURAL_LAYER nl(A,B,cAA,cAB,cBA,cBB,b1,b2,o1,o2);

initial begin
    $dumpfile("neural_layer_test.vcd");
    $dumpvars(0,NEURAL_LAYER_TEST);
    $monitor (
        "%t: A=%04x B=%04x cAA=%04x cAB=%04x cBA=%04x cBB=%04x b1=%04x b2=%04x o1=%04x o2=%04x",
        $time,A,B,cAA,cAB,cBA,cBB,b1,b2,o1,o2
    );

        A=16'h0100; B=16'h0100; cAA=16'h0000; cAB=16'h0000; cBA=16'h0000; cBB=16'h0000; b1=16'h0000; b2=16'h0000;
    #10 A=16'h0100; B=16'h0100; cAA=16'h0100; cAB=16'h0100; cBA=16'h0000; cBB=16'h0000; b1=16'h0000; b2=16'h0000;
    #10 A=16'h0100; B=16'h0100; cAA=16'h0000; cAB=16'h0000; cBA=16'h0100; cBB=16'h0100; b1=16'h0000; b2=16'h0000;
    #10 A=16'h0100; B=16'h0100; cAA=16'h0100; cAB=16'h0100; cBA=16'h0100; cBB=16'h0100; b1=16'h0000; b2=16'h0000;
    #10 A=16'h0100; B=16'h0100; cAA=16'hFFFF; cAB=16'hFFFF; cBA=16'h0100; cBB=16'h0100; b1=16'h0000; b2=16'h0000;
    #10 A=16'h0100; B=16'h0100; cAA=16'h0000; cAB=16'h0000; cBA=16'h0000; cBB=16'h0000; b1=16'h0100; b2=16'h0100;
    #10 A=16'h0100; B=16'h0100; cAA=16'h0100; cAB=16'h0100; cBA=16'h0000; cBB=16'h0000; b1=16'h0100; b2=16'h0100;
    #10 A=16'h0100; B=16'h0100; cAA=16'h0000; cAB=16'h0000; cBA=16'h0100; cBB=16'h0100; b1=16'h0100; b2=16'h0100;
    #10 A=16'h0100; B=16'h0100; cAA=16'h0100; cAB=16'h0100; cBA=16'h0100; cBB=16'h0100; b1=16'h0100; b2=16'h0100;
    #10 A=16'h0100; B=16'h0100; cAA=16'hFFFF; cAB=16'hFFFF; cBA=16'h0100; cBB=16'h0100; b1=16'h0100; b2=16'h0100;

end

endmodule
