module test_module(m1i0, m1i1, m1s, m1o, m2o, m2s, m2i0, m2i1, a0, a1, ao, oo, o0, o1, x, clk, d, q);
output m1o;
output m2o;
input m1s;
input m2s;
input m1i0;
input m2i0;
input m1i1;
input m2i1;

input clk, d;
output q;

input[5:0] a0;
input[5:0] a1;
output[5:0] ao;
input x;

input[7:0] o0;
input[7:0] o1;
output[7:0] oo;

mux_lib mux_u1(.o(m1o), .s(m1s), .i0(m1i0), .i1(m1i1));
mux_lib mux_u2(m2o, m2s, m2i0, m2i1);
and2_bus_lib and2_bus_u(ao, a0, a1);
or_lib or_u(.i0(o0[0]), .i1(o1[3]), .o(oo[5]));
dff_lib dff_u(.q(q), .clk(clk), .d(d));

endmodule

module mux_lib(o, s, i0, i1);
output o;
input s, i0, i1;

assign o = (i0&s)|(i1&~(s));

endmodule

module and2_bus_lib (o, i0, i1);
output[5:0] o;
input[5:0] i0;
input[5:0] i1;


endmodule

module or_lib (o, i0, i1);
output o;
input i0,i1;

assign o = i0 | i1;

endmodule

module dff_lib(q, clk ,d);
output q;
input clk, d;

always@( posedge clk ) begin
    q <= d;
end

endmodule
