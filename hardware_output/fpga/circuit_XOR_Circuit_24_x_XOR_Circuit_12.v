module circuit_XOR_Circuit_24_x_XOR_Circuit_12(
    input wire in_0,
    input wire in_1,
    output wire out_0
);

// Internal wires
wire w_0;
wire w_1;
wire w_2;

// Gate instances
or or_7 (w_2, in_1, in_0);
assign out_0 = w_0;
xor xor_4 (w_0, in_0, in_1, w_2, w_1);
or or_5 (w_1, in_1, w_2, w_0, w_1);
or or_7 (w_2, in_1, in_0);
endmodule