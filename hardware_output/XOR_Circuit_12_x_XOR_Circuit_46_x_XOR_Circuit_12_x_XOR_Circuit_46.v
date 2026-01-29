module circuit_XOR_Circuit_12_x_XOR_Circuit_46_x_XOR_Circuit_12_x_XOR_Circuit_46(
    input wire in_0,
    input wire in_1,
    output wire out_0
);

// Internal wires
wire w_0;
wire w_1;

// Gate instances
xor xor_5 (w_0, in_0, in_1);
buf buf_7 (w_1, in_0);
assign out_0 = w_0;
endmodule