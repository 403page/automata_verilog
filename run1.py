import sys

from antlr4 import *
from automata_verilogParser import automata_verilogParser
from automata_verilogLexer  import automata_verilogLexer
from compile_Listener import compiler

input_file     = open('CHIP.output.v', 'r')
lines = ''
verilog_design = compiler()
line  = input_file.readline()
while line:
    lines = lines + line
    #print('line')
    if ';' in line:
        input_data     = InputStream(lines)
        lexer_data     = automata_verilogLexer(input_data)
        data_stream    = CommonTokenStream(lexer_data)
        parser_data    = automata_verilogParser(data_stream)
        tree           = parser_data.verilog_design()
        walker         = ParseTreeWalker()
        walker.walk(verilog_design, tree)
        lines = ''
        #print('module')
    line = input_file.readline()

print('module list: %s'%verilog_design.get_module_list())
print('black box list: %s'%verilog_design.get_bb_list())

elab_data = verilog_design.create_elab_data('arbiter_1')
verilog_design.elab()
elab_data.force_value('/arbiter_1', 'IN0', 'H')
elab_data.get_instance('/arbiter_1/icc_place54').get_node_dict()
#elab_data.observe_value('/ahb_mux', 'IN0')
#elab_data.force_value('/test_module', 'd', 'H')
#elab_data.observe_value('/test_module', 'd')
#elab_data.pulse_clock([['/test_module', 'clk']], 1)
