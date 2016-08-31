module STRUCT_NEURAL_TEST;

reg [16:1]
    inputA,
    inputB,
    c111,
    c112,
    c121,
    c122,
    c211,
    c212,
    c221,
    c222;

wire [16:1]
    out1,
    out2;

STRUCT_NEURAL sn(
    inputA,
    inputB,
    c111,
    c112,
    c121,
    c122,
    c211,
    c212,
    c221,
    c222,
    out1,
    out2
);

parameter P0 = 16'h0000;
parameter P1 = 16'h0100;

initial begin
    $dumpfile("neural_test.vcd");
    $dumpvars(0,STRUCT_NEURAL_TEST);
    $monitor (
        "%t: A = %04x , B = %04x , %04x %04x %04x %04x %04x %04x %04x %04x   %04x %04x",
        $time,
        inputA,
        inputB,
        c111,
        c112,
        c121,
        c122,
        c211,
        c212,
        c221,
        c222,
        out1,
        out2
    );
    
        inputA=P0; inputB=P0; c111=P0; c112=P0; c121=P0; c122=P0; c211=P0; c212=P0; c221=P0; c222=P0;
     #1 inputA=P1; inputB=P1; c111=P1; c112=P1; c121=P1; c122=P1; c211=P1; c212=P1; c221=P1; c222=P1;
     #1 inputA=P1; inputB=P1; c111=P0; c112=P0; c121=P1; c122=P1; c211=P1; c212=P1; c221=P1; c222=P1;
     #1 inputA=P1; inputB=P1; c111=P0; c112=P0; c121=P1; c122=P1; c211=P1; c212=P0; c221=P1; c222=P0;
     #1 inputA=P1; inputB=P1; c111=P1; c112=P1; c121=P0; c122=P0; c211=P1; c212=P1; c221=P1; c222=P1;
     #1 inputA=P1; inputB=P1; c111=P0; c112=P0; c121=P0; c122=P0; c211=P1; c212=P1; c221=P1; c222=P1;
     #1 inputA=P1; inputB=P1; c111=P1; c112=P1; c121=P1; c122=P1; c211=P0; c212=P0; c221=P1; c222=P1;
     #1 inputA=P1; inputB=P1; c111=P1; c112=P1; c121=P1; c122=P1; c211=P0; c212=P0; c221=P0; c222=P0;
     #1 $finish;
end

endmodule
