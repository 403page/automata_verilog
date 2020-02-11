from automata_verilogListener import automata_verilogListener
from netlist_class_define import *

# This class defines a complete listener for a parse tree produced by automata_verilogParser.
class compiler(automata_verilogListener):
    def __init__(self):
        super().__init__()
        # save data for listener
        self._module_dict     = {}
        self._black_dict      = {}
        self._elab_data       = None
        # store data for walker in compile
        self._current_module  = None
        self._current_inst    = None
        self._current_pin     = None
        self._current_ref     = None
        self._instance_connection_index   = 0
        self._bus_queue       = []
        self._node_name_queue = []
        # store data for walker in expr
        self._current_result_node         = None
        self._current_sub_node_name       = None
        self._calc_queue                  = []
        # store data for seq logic
        self._current_clock_list          = []
        self._current_connecting_list     = []
        self._current_clock_type          = None

    def get_module_list(self):
        return self._module_dict.keys()

    def get_bb_list(self):
        return self._black_dict.keys()

    # create elab data after compile
    def create_elab_data(self, top_name):
        self._elab_data = elab_data_class(self._module_dict, self._black_dict, top_name)
        return self._elab_data

    def elab(self):
        self._elab_data.inst_elab()
        self._elab_data.connection_elab()
        return

    # module NAME ( pin_define );
    def enterModule_define(self, ctx):
        # copy module from blackbox
        module_name = ctx.NAME().getText()
        # if black box, copy from black box dict
        if module_name in self._black_dict.keys():
            self._current_module = self._black_dict[module_name]
            # no longer black box
            self._black_dict.pop(module_name)
        # if not black box
        else:
            # create a new module
            self._current_module = module_class(module_name)
        print('[Info] Parsing module: %s'%module_name)

        # calc index
        self._calc_index = 0
        self._calc_queue = []
        return

    # endmodule
    def enterEnd_module(self, ctx):
        # raise current module to dict
        self._module_dict[self._current_module.get_name()] = self._current_module
        print('[Info] Compile completed for module: %s'%self._current_module.get_name())
        # release data
        self._current_module = None

        # calc index
        self._calc_index = 0
        self._calc_queue = []
        return

    # pin_name in module define
    def enterModule_pin_single_pin(self, ctx):
        for ctx_pin in ctx.NAME():
            self._current_module.add_pin(ctx_pin.getText())
        return

    # NODE_TYPE[NUM:NUM] NAME;
    def enterNode_bus_define(self, ctx):
        # add bus by name and width
        self._current_module.add_bus(ctx.NAME().getText(), int(ctx.NUM(0).getText()), ctx.NODE_TYPE().getText())
        return

    # NODE_TYPE node_define_list;
    def enterNode_pin_define(self, ctx):
        self._current_node_type = ctx.NODE_TYPE().getText()
        return

    # NODE_TYPE (NAME,)* NAME;
    def enterSingle_node_in_node_define(self, ctx):
        for ctx_node in ctx.NAME():
            self._current_module.add_node(ctx_node.getText(), self._current_node_type)
        return

    # assign node_name = expr;
    def enterAssign_define(self, ctx):
        return

    # assign node_name = expr;
    def exitAssign_define(self, ctx):
        # get leaf node name
        node_base_name = ctx.node_name().NAME().getText()
        try:
            node_bus_str = '__busbit__%s__'%ctx.node_name.NUM().getText()
        except:
            node_bus_str = ''
        node_base_name = node_base_name + node_bus_str

        right_node = self._calc_queue.pop()
        self._current_module.add_buf(node_base_name, right_node)
        #print('%s = %s'%(node_base_name, right_node))
        return

    # Enter a parse tree produced by automata_verilogParser#and_expr.
    def exitAnd_expr(self, ctx):
        result = '_calc_web_node_%s'%self._calc_index
        self._calc_index = self._calc_index + 1
        i0 = self._calc_queue.pop()
        i1 = self._calc_queue.pop()
        self._calc_queue.append(result)
        self._current_module.add_and(result, i0, i1)
        #print('%s = %s and %s'%(result, i0, i1))
        return

    # Enter a parse tree produced by automata_verilogParser#and_expr.
    def exitOr_expr(self, ctx):
        result = '_calc_web_node_%s'%self._calc_index
        self._calc_index = self._calc_index + 1
        i0 = self._calc_queue.pop()
        i1 = self._calc_queue.pop()
        self._calc_queue.append(result)
        self._current_module.add_or(result, i0, i1)
        #print('%s = %s or %s'%(result, i0, i1))
        return

    # Enter a parse tree produced by automata_verilogParser#and_expr.
    def exitNot_expr(self, ctx):
        result = '_calc_web_node_%s'%self._calc_index
        self._calc_index = self._calc_index + 1
        i = self._calc_queue.pop()
        self._calc_queue.append(result)
        self._current_module.add_inv(result, i)
        #print('%s = not %s'%(result, i))
        return

    # Enter a parse tree produced by automata_verilogParser#expr_node_name.
    def enterExpr_node_name(self, ctx):
        try:
            # get leaf node name
            node_base_name = ctx.node_name().NAME().getText()
        except:
            if ctx.node_name().NUM().getText() == '0':
                node_base_name = 'Tielow'
            elif ctx.node_name().NUM().getText() == '1':
                node_base_name = 'TieHigh'
            self._calc_queue.append(node_base_name)
        try:
            node_bus_str = '__busbit__%s__'%ctx.node_name.NUM().getText()
        except:
            node_bus_str = ''
        node_base_name = node_base_name + node_bus_str
        self._calc_queue.append(node_base_name)
        return

    # INST_REF INST_NAME( instance_connection );
    def enterInstance_define(self, ctx):
        ref_name   =  ctx.NAME(0).getText()
        inst_name  =  ctx.NAME(1).getText()
        #print('[Info] Adding instance: %s'%(inst_name))
        # update current instance data for walker
        self._current_instance            = instance_class_lite(ref_name, inst_name)
        self._current_ref                 = ref_name
        self._instance_connection_index   = 0

        # add black box for currently not defined module
        if not ref_name in self._module_dict.keys():
            self._black_dict[ref_name] = module_class(ref_name)
        return

    # exit inst define
    def exitInstance_define(self, ctx):
        # raise current instance to current module
        self._current_module.add_instance(self._current_instance.get_name(), self._current_instance)
        # release data
        self._current_instance = None
        self._current_ref      = None
        self._instance_connection_index = 0
        self._current_connecting_list   = []
        return

    # .INST_PIN(MODULE_PIN[NUM])
    def exitWith_dot_connection(self, ctx):
        inst_pin_name_list     = self._bus_queue.pop(0)
        module_pin_name_list   = self._bus_queue.pop(0)
        if len(inst_pin_name_list) == len(module_pin_name_list):
            inst_pin_name   = inst_pin_name_list.pop(0)
            module_pin_name = module_pin_name_list.pop(0)
            if not self._current_module.get_bus_width(module_pin_name):
                self._current_module.connection_request_pin_by_name(self._current_instance.get_name(), \
                module_pin_name, inst_pin_name)
            else:
                for i in range(0, self._current_module.get_bus_width(module_pin_name)):
                    self._current_module.connection_request_pin_by_name(self._current_instance.get_name(), \
                    '%s__busbit__%s__'%(module_pin_name, i), '%s__busbit__%s__'%(inst_pin_name, i))
        else:
            inst_pin_name = inst_pin_name_list.pop(0)
            i = 0
            for module_pin_name in module_pin_name_list:
                self._current_module.connection_request_pin_by_name(self._current_instance.get_name(), \
                module_pin_name, '%s__busbit__%s__'%(inst_pin_name, i))
                i += 1
        return

    # (MODULE_PIN[NUM], MODULE_PIN[NUM])
    def exitWo_dot_connection(self, ctx):
        module_pin_name_list   = self._bus_queue.pop(0)
        bus_index = 0
        for module_pin_name in module_pin_name_list:
            self._current_module.connection_request_pin_by_index(self._current_instance.get_name(), \
            module_pin_name, self._instance_connection_index, bus_index)
            bus_index += 1
        self._instance_connection_index += 1
        return

    # NAME [ NUM : NUM ]
    def exitBus_name_multi_bit(self, ctx):
        self._bus_queue.append(['%s__busbit__%s__'%(ctx.NAME().getText(), i) \
                                             for i in range(int(ctx.NUM(1).getText()), int(ctx.NUM(0).getText()))])
        self._node_name_queue = []
        return

    # { (node_name ,)* node_name }
    def exitBus_name_connection(self, ctx):
        self._bus_queue.append(self._node_name_queue)
        self._node_name_queue = []
        return

    # node_name
    def exitBus_name_single_node(self, ctx):
        self._bus_queue.append(self._node_name_queue)
        self._node_name_queue = []
        return

    # NAME [ NUM ]
    def enterNode_name_bit(self, ctx):
        self._node_name_queue.append('%s__busbit__%s__'%(ctx.NAME().getText(), ctx.NUM().getText()))
        return

    # NAME
    def enterNode_name_pin_or_bus(self, ctx):
        self._node_name_queue.append(ctx.NAME().getText())
        return

    # 1'b0 1'b1
    def enterNode_value(self, ctx):
        if ctx.NUM().getText() == '0':
            self._node_name_queue.append('Tielow')
        elif ctx.NUM().getText() == '1':
            self._node_name_queue.append('Tiehigh')
        return

    # Enter a parse tree produced by automata_verilogParser#bus_name.
    def enterBus_name(self, ctx):
        self._current_connecting_list     = []
        return

    # Exit a parse tree produced by automata_verilogParser#bus_name.
    def exitBus_name(self, ctx):
        self._current_connecting_list     = []
        return

    # always@(posiedge node_name) begin end
    def enterAlways_edge(self, ctx):
        self._current_clock_list = []
        self._current_clock_type = 'edge'
        return
    def exitAlways_edge(self, ctx):
        return

    # posiedge node_name
    def enterEdge_clock_trigger(self, ctx):
        clock_name = ctx.node_name().NAME().getText()
        # try if bus bit
        try:
            clock_bus_str = '__busbit__%s__'%ctx.NUM().getText()
        except:
            clock_bus_str = ''
        clock_name = clock_name + clock_bus_str
        self._current_clock_list.append(clock_name)
        return

    # node_name '<=' expr LINE_END
    def enterNon_blocked_connect(self, ctx):
        return
    def exitNon_blocked_connect(self, ctx):
        # get leaf node name
        node_base_name = ctx.node_name().NAME().getText()
        try:
            node_bus_str = '__busbit__%s__'%ctx.node_name.NUM().getText()
        except:
            node_bus_str = ''
        node_base_name = node_base_name + node_bus_str

        right_node = self._calc_queue.pop()
        clock_name = self._current_clock_list.pop()
        self._current_module.add_ff(node_base_name, right_node, clock_name)
        #print('ff %s = %s'%(node_base_name, right_node))
        return
