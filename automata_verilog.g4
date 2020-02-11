grammar automata_verilog;

verilog_design          : module_lines+;

module_lines            : module_define
                        | node_define
                        | assign_define
                        | always_edge
                        | always_level
                        | instance_define
                        | end_module
                        ;


module_define           :  MODULE_MARK NAME '(' module_pins ')' LINE_END
                        ;

end_module              :  END_MODULE_MARK
                        ;

module_pins             :  (NAME ',')* NAME                                     # module_pin_single_pin
                        ;

node_define             :  NODE_TYPE   '[' NUM ':' NUM ']' NAME LINE_END        # node_bus_define
                        |  NODE_TYPE   node_define_list LINE_END                # node_pin_define
                        ;

node_define_list        :  (NAME ',')* NAME                                     # single_node_in_node_define
                        ;

assign_define           :  ASSIGN_MARK node_name '=' expr LINE_END
                        ;

always_edge             :  'always' '@' '(' edge_situation ')' begin_proc
                        ;

always_level            :  'always' '@' '(' level_situation ')' begin_proc
                        ;

edge_situation          :  edge_situation 'or' edge_situation                   # multi_edge_trigger
                        |  'posedge' node_name                                  # edge_clock_trigger
                        ;

level_situation         :  level_situation 'or' level_situation                 # multi_level_trigger
                        |  node_name                                            # level_clock_trigger
                        ;


begin_proc              :  'begin' blocked_connect* non_blocked_connect* if_proc* 'end'
                        ;

if_proc                 :  'if' '(' eq_situation ')' begin_proc 'else' begin_proc
                        ;

eq_situation            :  node_name '==' expr
                        ;

blocked_connect         :  node_name '=' expr LINE_END
                        ;

non_blocked_connect     :  node_name '<=' expr LINE_END
                        ;


expr                    :  '~' expr                                             # not_expr
                        |  expr '|' expr                                        # or_expr
                        |  expr '&' expr                                        # and_expr
                        |  '(' expr ')'                                         # sub_expr
                        |  node_name                                            # expr_node_name
                        ;

instance_define         :  NAME NAME '(' (pin_connection_with_dot|pin_connection_wo_dot) ')' LINE_END
                        ;

pin_connection_with_dot :  (with_dot_connection ',')* with_dot_connection
                        ;

with_dot_connection     :  '.' bus_name '(' bus_name ')'
                        ;

pin_connection_wo_dot   :  (wo_dot_connection ',')* wo_dot_connection
                        ;

wo_dot_connection       :  bus_name
                        ;

node_name               :  NAME '[' NUM ']'                                     # node_name_bit
                        |  NAME                                                 # node_name_pin_or_bus
                        |  BYTE_MARK NUM                                        # node_value
                        ;

bus_name                :  NAME '[' NUM ':' NUM ']'                             # bus_name_multi_bit
                        |  '{' (node_name ',')* node_name '}'                   # bus_name_connection
                        |  node_name                                            # bus_name_single_node
                        ;

MODULE_MARK: 'module';
END_MODULE_MARK: 'endmodule';
NODE_TYPE: 'input' | 'output' | 'inout' | 'wire' | 'reg'; 
ASSIGN_MARK: 'assign';
INSTANCE_CONNECTION: '.';
LINE_END: ';';
NUM: [0-9]+;
NAME: [a-zA-Z0-9_\\/!]+;
BYTE_MARK: '1\'b';

WS: [ \t\r\n]+ -> skip;
