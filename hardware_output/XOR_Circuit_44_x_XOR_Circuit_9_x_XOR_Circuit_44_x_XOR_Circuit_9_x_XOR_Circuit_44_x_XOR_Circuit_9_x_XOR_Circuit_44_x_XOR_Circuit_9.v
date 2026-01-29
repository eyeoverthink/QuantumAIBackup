module circuit_XOR_Circuit_44_x_XOR_Circuit_9_x_XOR_Circuit_44_x_XOR_Circuit_9_x_XOR_Circuit_44_x_XOR_Circuit_9_x_XOR_Circuit_44_x_XOR_Circuit_9(
    input wire in_0,
    input wire in_1,
    output wire out_0
);

// Internal wires
wire w_0;

// Gate instances
xor xor_5 (w_0, in_0, in_1);
assign out_0 = w_0;
endmodule