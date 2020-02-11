# Generated from automata_verilog.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .automata_verilogParser import automata_verilogParser
else:
    from automata_verilogParser import automata_verilogParser

# This class defines a complete listener for a parse tree produced by automata_verilogParser.
class automata_verilogListener(ParseTreeListener):

    # Enter a parse tree produced by automata_verilogParser#verilog_design.
    def enterVerilog_design(self, ctx:automata_verilogParser.Verilog_designContext):
        pass

    # Exit a parse tree produced by automata_verilogParser#verilog_design.
    def exitVerilog_design(self, ctx:automata_verilogParser.Verilog_designContext):
        pass


    # Enter a parse tree produced by automata_verilogParser#module_lines.
    def enterModule_lines(self, ctx:automata_verilogParser.Module_linesContext):
        pass

    # Exit a parse tree produced by automata_verilogParser#module_lines.
    def exitModule_lines(self, ctx:automata_verilogParser.Module_linesContext):
        pass


    # Enter a parse tree produced by automata_verilogParser#module_define.
    def enterModule_define(self, ctx:automata_verilogParser.Module_defineContext):
        pass

    # Exit a parse tree produced by automata_verilogParser#module_define.
    def exitModule_define(self, ctx:automata_verilogParser.Module_defineContext):
        pass


    # Enter a parse tree produced by automata_verilogParser#end_module.
    def enterEnd_module(self, ctx:automata_verilogParser.End_moduleContext):
        pass

    # Exit a parse tree produced by automata_verilogParser#end_module.
    def exitEnd_module(self, ctx:automata_verilogParser.End_moduleContext):
        pass


    # Enter a parse tree produced by automata_verilogParser#module_pin_single_pin.
    def enterModule_pin_single_pin(self, ctx:automata_verilogParser.Module_pin_single_pinContext):
        pass

    # Exit a parse tree produced by automata_verilogParser#module_pin_single_pin.
    def exitModule_pin_single_pin(self, ctx:automata_verilogParser.Module_pin_single_pinContext):
        pass


    # Enter a parse tree produced by automata_verilogParser#node_bus_define.
    def enterNode_bus_define(self, ctx:automata_verilogParser.Node_bus_defineContext):
        pass

    # Exit a parse tree produced by automata_verilogParser#node_bus_define.
    def exitNode_bus_define(self, ctx:automata_verilogParser.Node_bus_defineContext):
        pass


    # Enter a parse tree produced by automata_verilogParser#node_pin_define.
    def enterNode_pin_define(self, ctx:automata_verilogParser.Node_pin_defineContext):
        pass

    # Exit a parse tree produced by automata_verilogParser#node_pin_define.
    def exitNode_pin_define(self, ctx:automata_verilogParser.Node_pin_defineContext):
        pass


    # Enter a parse tree produced by automata_verilogParser#single_node_in_node_define.
    def enterSingle_node_in_node_define(self, ctx:automata_verilogParser.Single_node_in_node_defineContext):
        pass

    # Exit a parse tree produced by automata_verilogParser#single_node_in_node_define.
    def exitSingle_node_in_node_define(self, ctx:automata_verilogParser.Single_node_in_node_defineContext):
        pass


    # Enter a parse tree produced by automata_verilogParser#assign_define.
    def enterAssign_define(self, ctx:automata_verilogParser.Assign_defineContext):
        pass

    # Exit a parse tree produced by automata_verilogParser#assign_define.
    def exitAssign_define(self, ctx:automata_verilogParser.Assign_defineContext):
        pass


    # Enter a parse tree produced by automata_verilogParser#always_edge.
    def enterAlways_edge(self, ctx:automata_verilogParser.Always_edgeContext):
        pass

    # Exit a parse tree produced by automata_verilogParser#always_edge.
    def exitAlways_edge(self, ctx:automata_verilogParser.Always_edgeContext):
        pass


    # Enter a parse tree produced by automata_verilogParser#always_level.
    def enterAlways_level(self, ctx:automata_verilogParser.Always_levelContext):
        pass

    # Exit a parse tree produced by automata_verilogParser#always_level.
    def exitAlways_level(self, ctx:automata_verilogParser.Always_levelContext):
        pass


    # Enter a parse tree produced by automata_verilogParser#edge_clock_trigger.
    def enterEdge_clock_trigger(self, ctx:automata_verilogParser.Edge_clock_triggerContext):
        pass

    # Exit a parse tree produced by automata_verilogParser#edge_clock_trigger.
    def exitEdge_clock_trigger(self, ctx:automata_verilogParser.Edge_clock_triggerContext):
        pass


    # Enter a parse tree produced by automata_verilogParser#multi_edge_trigger.
    def enterMulti_edge_trigger(self, ctx:automata_verilogParser.Multi_edge_triggerContext):
        pass

    # Exit a parse tree produced by automata_verilogParser#multi_edge_trigger.
    def exitMulti_edge_trigger(self, ctx:automata_verilogParser.Multi_edge_triggerContext):
        pass


    # Enter a parse tree produced by automata_verilogParser#level_clock_trigger.
    def enterLevel_clock_trigger(self, ctx:automata_verilogParser.Level_clock_triggerContext):
        pass

    # Exit a parse tree produced by automata_verilogParser#level_clock_trigger.
    def exitLevel_clock_trigger(self, ctx:automata_verilogParser.Level_clock_triggerContext):
        pass


    # Enter a parse tree produced by automata_verilogParser#multi_level_trigger.
    def enterMulti_level_trigger(self, ctx:automata_verilogParser.Multi_level_triggerContext):
        pass

    # Exit a parse tree produced by automata_verilogParser#multi_level_trigger.
    def exitMulti_level_trigger(self, ctx:automata_verilogParser.Multi_level_triggerContext):
        pass


    # Enter a parse tree produced by automata_verilogParser#begin_proc.
    def enterBegin_proc(self, ctx:automata_verilogParser.Begin_procContext):
        pass

    # Exit a parse tree produced by automata_verilogParser#begin_proc.
    def exitBegin_proc(self, ctx:automata_verilogParser.Begin_procContext):
        pass


    # Enter a parse tree produced by automata_verilogParser#if_proc.
    def enterIf_proc(self, ctx:automata_verilogParser.If_procContext):
        pass

    # Exit a parse tree produced by automata_verilogParser#if_proc.
    def exitIf_proc(self, ctx:automata_verilogParser.If_procContext):
        pass


    # Enter a parse tree produced by automata_verilogParser#eq_situation.
    def enterEq_situation(self, ctx:automata_verilogParser.Eq_situationContext):
        pass

    # Exit a parse tree produced by automata_verilogParser#eq_situation.
    def exitEq_situation(self, ctx:automata_verilogParser.Eq_situationContext):
        pass


    # Enter a parse tree produced by automata_verilogParser#blocked_connect.
    def enterBlocked_connect(self, ctx:automata_verilogParser.Blocked_connectContext):
        pass

    # Exit a parse tree produced by automata_verilogParser#blocked_connect.
    def exitBlocked_connect(self, ctx:automata_verilogParser.Blocked_connectContext):
        pass


    # Enter a parse tree produced by automata_verilogParser#non_blocked_connect.
    def enterNon_blocked_connect(self, ctx:automata_verilogParser.Non_blocked_connectContext):
        pass

    # Exit a parse tree produced by automata_verilogParser#non_blocked_connect.
    def exitNon_blocked_connect(self, ctx:automata_verilogParser.Non_blocked_connectContext):
        pass


    # Enter a parse tree produced by automata_verilogParser#not_expr.
    def enterNot_expr(self, ctx:automata_verilogParser.Not_exprContext):
        pass

    # Exit a parse tree produced by automata_verilogParser#not_expr.
    def exitNot_expr(self, ctx:automata_verilogParser.Not_exprContext):
        pass


    # Enter a parse tree produced by automata_verilogParser#sub_expr.
    def enterSub_expr(self, ctx:automata_verilogParser.Sub_exprContext):
        pass

    # Exit a parse tree produced by automata_verilogParser#sub_expr.
    def exitSub_expr(self, ctx:automata_verilogParser.Sub_exprContext):
        pass


    # Enter a parse tree produced by automata_verilogParser#expr_node_name.
    def enterExpr_node_name(self, ctx:automata_verilogParser.Expr_node_nameContext):
        pass

    # Exit a parse tree produced by automata_verilogParser#expr_node_name.
    def exitExpr_node_name(self, ctx:automata_verilogParser.Expr_node_nameContext):
        pass


    # Enter a parse tree produced by automata_verilogParser#and_expr.
    def enterAnd_expr(self, ctx:automata_verilogParser.And_exprContext):
        pass

    # Exit a parse tree produced by automata_verilogParser#and_expr.
    def exitAnd_expr(self, ctx:automata_verilogParser.And_exprContext):
        pass


    # Enter a parse tree produced by automata_verilogParser#or_expr.
    def enterOr_expr(self, ctx:automata_verilogParser.Or_exprContext):
        pass

    # Exit a parse tree produced by automata_verilogParser#or_expr.
    def exitOr_expr(self, ctx:automata_verilogParser.Or_exprContext):
        pass


    # Enter a parse tree produced by automata_verilogParser#instance_define.
    def enterInstance_define(self, ctx:automata_verilogParser.Instance_defineContext):
        pass

    # Exit a parse tree produced by automata_verilogParser#instance_define.
    def exitInstance_define(self, ctx:automata_verilogParser.Instance_defineContext):
        pass


    # Enter a parse tree produced by automata_verilogParser#pin_connection_with_dot.
    def enterPin_connection_with_dot(self, ctx:automata_verilogParser.Pin_connection_with_dotContext):
        pass

    # Exit a parse tree produced by automata_verilogParser#pin_connection_with_dot.
    def exitPin_connection_with_dot(self, ctx:automata_verilogParser.Pin_connection_with_dotContext):
        pass


    # Enter a parse tree produced by automata_verilogParser#with_dot_connection.
    def enterWith_dot_connection(self, ctx:automata_verilogParser.With_dot_connectionContext):
        pass

    # Exit a parse tree produced by automata_verilogParser#with_dot_connection.
    def exitWith_dot_connection(self, ctx:automata_verilogParser.With_dot_connectionContext):
        pass


    # Enter a parse tree produced by automata_verilogParser#pin_connection_wo_dot.
    def enterPin_connection_wo_dot(self, ctx:automata_verilogParser.Pin_connection_wo_dotContext):
        pass

    # Exit a parse tree produced by automata_verilogParser#pin_connection_wo_dot.
    def exitPin_connection_wo_dot(self, ctx:automata_verilogParser.Pin_connection_wo_dotContext):
        pass


    # Enter a parse tree produced by automata_verilogParser#wo_dot_connection.
    def enterWo_dot_connection(self, ctx:automata_verilogParser.Wo_dot_connectionContext):
        pass

    # Exit a parse tree produced by automata_verilogParser#wo_dot_connection.
    def exitWo_dot_connection(self, ctx:automata_verilogParser.Wo_dot_connectionContext):
        pass


    # Enter a parse tree produced by automata_verilogParser#node_name_bit.
    def enterNode_name_bit(self, ctx:automata_verilogParser.Node_name_bitContext):
        pass

    # Exit a parse tree produced by automata_verilogParser#node_name_bit.
    def exitNode_name_bit(self, ctx:automata_verilogParser.Node_name_bitContext):
        pass


    # Enter a parse tree produced by automata_verilogParser#node_name_pin_or_bus.
    def enterNode_name_pin_or_bus(self, ctx:automata_verilogParser.Node_name_pin_or_busContext):
        pass

    # Exit a parse tree produced by automata_verilogParser#node_name_pin_or_bus.
    def exitNode_name_pin_or_bus(self, ctx:automata_verilogParser.Node_name_pin_or_busContext):
        pass


    # Enter a parse tree produced by automata_verilogParser#node_value.
    def enterNode_value(self, ctx:automata_verilogParser.Node_valueContext):
        pass

    # Exit a parse tree produced by automata_verilogParser#node_value.
    def exitNode_value(self, ctx:automata_verilogParser.Node_valueContext):
        pass


    # Enter a parse tree produced by automata_verilogParser#bus_name_multi_bit.
    def enterBus_name_multi_bit(self, ctx:automata_verilogParser.Bus_name_multi_bitContext):
        pass

    # Exit a parse tree produced by automata_verilogParser#bus_name_multi_bit.
    def exitBus_name_multi_bit(self, ctx:automata_verilogParser.Bus_name_multi_bitContext):
        pass


    # Enter a parse tree produced by automata_verilogParser#bus_name_connection.
    def enterBus_name_connection(self, ctx:automata_verilogParser.Bus_name_connectionContext):
        pass

    # Exit a parse tree produced by automata_verilogParser#bus_name_connection.
    def exitBus_name_connection(self, ctx:automata_verilogParser.Bus_name_connectionContext):
        pass


    # Enter a parse tree produced by automata_verilogParser#bus_name_single_node.
    def enterBus_name_single_node(self, ctx:automata_verilogParser.Bus_name_single_nodeContext):
        pass

    # Exit a parse tree produced by automata_verilogParser#bus_name_single_node.
    def exitBus_name_single_node(self, ctx:automata_verilogParser.Bus_name_single_nodeContext):
        pass

