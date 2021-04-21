# Generated from Bloon.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BloonParser import BloonParser
else:
    from BloonParser import BloonParser

    from BloonCompiler import Compiler
    compi = Compiler()


# This class defines a complete listener for a parse tree produced by BloonParser.
class BloonListener(ParseTreeListener):

    # Enter a parse tree produced by BloonParser#program.
    def enterProgram(self, ctx:BloonParser.ProgramContext):
        pass

    # Exit a parse tree produced by BloonParser#program.
    def exitProgram(self, ctx:BloonParser.ProgramContext):
        pass


    # Enter a parse tree produced by BloonParser#program_t.
    def enterProgram_t(self, ctx:BloonParser.Program_tContext):
        pass

    # Exit a parse tree produced by BloonParser#program_t.
    def exitProgram_t(self, ctx:BloonParser.Program_tContext):
        pass


    # Enter a parse tree produced by BloonParser#main.
    def enterMain(self, ctx:BloonParser.MainContext):
        pass

    # Exit a parse tree produced by BloonParser#main.
    def exitMain(self, ctx:BloonParser.MainContext):
        pass


    # Enter a parse tree produced by BloonParser#r_class.
    def enterR_class(self, ctx:BloonParser.R_classContext):
        pass

    # Exit a parse tree produced by BloonParser#r_class.
    def exitR_class(self, ctx:BloonParser.R_classContext):
        pass


    # Enter a parse tree produced by BloonParser#class_t.
    def enterClass_t(self, ctx:BloonParser.Class_tContext):
        pass

    # Exit a parse tree produced by BloonParser#class_t.
    def exitClass_t(self, ctx:BloonParser.Class_tContext):
        pass


    # Enter a parse tree produced by BloonParser#class_k.
    def enterClass_k(self, ctx:BloonParser.Class_kContext):
        pass

    # Exit a parse tree produced by BloonParser#class_k.
    def exitClass_k(self, ctx:BloonParser.Class_kContext):
        pass


    # Enter a parse tree produced by BloonParser#class_j.
    def enterClass_j(self, ctx:BloonParser.Class_jContext):
        pass

    # Exit a parse tree produced by BloonParser#class_j.
    def exitClass_j(self, ctx:BloonParser.Class_jContext):
        pass


    # Enter a parse tree produced by BloonParser#class_l.
    def enterClass_l(self, ctx:BloonParser.Class_lContext):
        pass

    # Exit a parse tree produced by BloonParser#class_l.
    def exitClass_l(self, ctx:BloonParser.Class_lContext):
        pass


    # Enter a parse tree produced by BloonParser#class_p.
    def enterClass_p(self, ctx:BloonParser.Class_pContext):
        pass

    # Exit a parse tree produced by BloonParser#class_p.
    def exitClass_p(self, ctx:BloonParser.Class_pContext):
        pass


    # Enter a parse tree produced by BloonParser#var.
    def enterVar(self, ctx:BloonParser.VarContext):
        pass

    # Exit a parse tree produced by BloonParser#var.
    def exitVar(self, ctx:BloonParser.VarContext):
        pass


    # Enter a parse tree produced by BloonParser#var_t.
    def enterVar_t(self, ctx:BloonParser.Var_tContext):
        pass

    # Exit a parse tree produced by BloonParser#var_t.
    def exitVar_t(self, ctx:BloonParser.Var_tContext):
        pass


    # Enter a parse tree produced by BloonParser#var_k.
    def enterVar_k(self, ctx:BloonParser.Var_kContext):
        pass

    # Exit a parse tree produced by BloonParser#var_k.
    def exitVar_k(self, ctx:BloonParser.Var_kContext):
        pass


    # Enter a parse tree produced by BloonParser#var_dec.
    def enterVar_dec(self, ctx:BloonParser.Var_decContext):
        pass

    # Exit a parse tree produced by BloonParser#var_dec.
    def exitVar_dec(self, ctx:BloonParser.Var_decContext):
        pass


    # Enter a parse tree produced by BloonParser#var_dec_t.
    def enterVar_dec_t(self, ctx:BloonParser.Var_dec_tContext):
        pass

    # Exit a parse tree produced by BloonParser#var_dec_t.
    def exitVar_dec_t(self, ctx:BloonParser.Var_dec_tContext):
        pass


    # Enter a parse tree produced by BloonParser#var_dec_l.
    def enterVar_dec_l(self, ctx:BloonParser.Var_dec_lContext):
        pass

    # Exit a parse tree produced by BloonParser#var_dec_l.
    def exitVar_dec_l(self, ctx:BloonParser.Var_dec_lContext):
        pass


    # Enter a parse tree produced by BloonParser#arr_idx.
    def enterArr_idx(self, ctx:BloonParser.Arr_idxContext):
        pass

    # Exit a parse tree produced by BloonParser#arr_idx.
    def exitArr_idx(self, ctx:BloonParser.Arr_idxContext):
        pass


    # Enter a parse tree produced by BloonParser#arr_idx_t.
    def enterArr_idx_t(self, ctx:BloonParser.Arr_idx_tContext):
        pass

    # Exit a parse tree produced by BloonParser#arr_idx_t.
    def exitArr_idx_t(self, ctx:BloonParser.Arr_idx_tContext):
        pass


    # Enter a parse tree produced by BloonParser#arr.
    def enterArr(self, ctx:BloonParser.ArrContext):
        pass

    # Exit a parse tree produced by BloonParser#arr.
    def exitArr(self, ctx:BloonParser.ArrContext):
        pass


    # Enter a parse tree produced by BloonParser#arr_t.
    def enterArr_t(self, ctx:BloonParser.Arr_tContext):
        pass

    # Exit a parse tree produced by BloonParser#arr_t.
    def exitArr_t(self, ctx:BloonParser.Arr_tContext):
        pass


    # Enter a parse tree produced by BloonParser#assign.
    def enterAssign(self, ctx:BloonParser.AssignContext):
        pass

    # Exit a parse tree produced by BloonParser#assign.
    def exitAssign(self, ctx:BloonParser.AssignContext):
        pass


    # Enter a parse tree produced by BloonParser#assign_t.
    def enterAssign_t(self, ctx:BloonParser.Assign_tContext):
        pass

    # Exit a parse tree produced by BloonParser#assign_t.
    def exitAssign_t(self, ctx:BloonParser.Assign_tContext):
        pass


    # Enter a parse tree produced by BloonParser#var_type.
    def enterVar_type(self, ctx:BloonParser.Var_typeContext):
        pass

    # Exit a parse tree produced by BloonParser#var_type.
    def exitVar_type(self, ctx:BloonParser.Var_typeContext):
        pass


    # Enter a parse tree produced by BloonParser#custom_type.
    def enterCustom_type(self, ctx:BloonParser.Custom_typeContext):
        pass

    # Exit a parse tree produced by BloonParser#custom_type.
    def exitCustom_type(self, ctx:BloonParser.Custom_typeContext):
        pass


    # Enter a parse tree produced by BloonParser#assign_op.
    def enterAssign_op(self, ctx:BloonParser.Assign_opContext):
        pass

    # Exit a parse tree produced by BloonParser#assign_op.
    def exitAssign_op(self, ctx:BloonParser.Assign_opContext):
        pass


    # Enter a parse tree produced by BloonParser#type_meth.
    def enterType_meth(self, ctx:BloonParser.Type_methContext):
        pass

    # Exit a parse tree produced by BloonParser#type_meth.
    def exitType_meth(self, ctx:BloonParser.Type_methContext):
        pass


    # Enter a parse tree produced by BloonParser#statement.
    def enterStatement(self, ctx:BloonParser.StatementContext):
        pass

    # Exit a parse tree produced by BloonParser#statement.
    def exitStatement(self, ctx:BloonParser.StatementContext):
        pass


    # Enter a parse tree produced by BloonParser#func.
    def enterFunc(self, ctx:BloonParser.FuncContext):
        pass

    # Exit a parse tree produced by BloonParser#func.
    def exitFunc(self, ctx:BloonParser.FuncContext):
        pass


    # Enter a parse tree produced by BloonParser#func_t.
    def enterFunc_t(self, ctx:BloonParser.Func_tContext):
        pass

    # Exit a parse tree produced by BloonParser#func_t.
    def exitFunc_t(self, ctx:BloonParser.Func_tContext):
        pass


    # Enter a parse tree produced by BloonParser#func_k.
    def enterFunc_k(self, ctx:BloonParser.Func_kContext):
        pass

    # Exit a parse tree produced by BloonParser#func_k.
    def exitFunc_k(self, ctx:BloonParser.Func_kContext):
        pass


    # Enter a parse tree produced by BloonParser#func_p.
    def enterFunc_p(self, ctx:BloonParser.Func_pContext):
        pass

    # Exit a parse tree produced by BloonParser#func_p.
    def exitFunc_p(self, ctx:BloonParser.Func_pContext):
        pass


    # Enter a parse tree produced by BloonParser#param.
    def enterParam(self, ctx:BloonParser.ParamContext):
        pass

    # Exit a parse tree produced by BloonParser#param.
    def exitParam(self, ctx:BloonParser.ParamContext):
        pass


    # Enter a parse tree produced by BloonParser#param_t.
    def enterParam_t(self, ctx:BloonParser.Param_tContext):
        pass

    # Exit a parse tree produced by BloonParser#param_t.
    def exitParam_t(self, ctx:BloonParser.Param_tContext):
        pass


    # Enter a parse tree produced by BloonParser#block.
    def enterBlock(self, ctx:BloonParser.BlockContext):
        pass

    # Exit a parse tree produced by BloonParser#block.
    def exitBlock(self, ctx:BloonParser.BlockContext):
        pass


    # Enter a parse tree produced by BloonParser#block_t.
    def enterBlock_t(self, ctx:BloonParser.Block_tContext):
        pass

    # Exit a parse tree produced by BloonParser#block_t.
    def exitBlock_t(self, ctx:BloonParser.Block_tContext):
        pass


    # Enter a parse tree produced by BloonParser#r_return.
    def enterR_return(self, ctx:BloonParser.R_returnContext):
        pass

    # Exit a parse tree produced by BloonParser#r_return.
    def exitR_return(self, ctx:BloonParser.R_returnContext):
        pass


    # Enter a parse tree produced by BloonParser#call.
    def enterCall(self, ctx:BloonParser.CallContext):
        pass

    # Exit a parse tree produced by BloonParser#call.
    def exitCall(self, ctx:BloonParser.CallContext):
        pass


    # Enter a parse tree produced by BloonParser#call_t.
    def enterCall_t(self, ctx:BloonParser.Call_tContext):
        pass

    # Exit a parse tree produced by BloonParser#call_t.
    def exitCall_t(self, ctx:BloonParser.Call_tContext):
        pass


    # Enter a parse tree produced by BloonParser#call_args.
    def enterCall_args(self, ctx:BloonParser.Call_argsContext):
        pass

    # Exit a parse tree produced by BloonParser#call_args.
    def exitCall_args(self, ctx:BloonParser.Call_argsContext):
        pass


    # Enter a parse tree produced by BloonParser#call_args_t.
    def enterCall_args_t(self, ctx:BloonParser.Call_args_tContext):
        pass

    # Exit a parse tree produced by BloonParser#call_args_t.
    def exitCall_args_t(self, ctx:BloonParser.Call_args_tContext):
        pass


    # Enter a parse tree produced by BloonParser#call_void.
    def enterCall_void(self, ctx:BloonParser.Call_voidContext):
        pass

    # Exit a parse tree produced by BloonParser#call_void.
    def exitCall_void(self, ctx:BloonParser.Call_voidContext):
        pass


    # Enter a parse tree produced by BloonParser#read.
    def enterRead(self, ctx:BloonParser.ReadContext):
        pass

    # Exit a parse tree produced by BloonParser#read.
    def exitRead(self, ctx:BloonParser.ReadContext):
        pass


    # Enter a parse tree produced by BloonParser#read_t.
    def enterRead_t(self, ctx:BloonParser.Read_tContext):
        pass

    # Exit a parse tree produced by BloonParser#read_t.
    def exitRead_t(self, ctx:BloonParser.Read_tContext):
        pass


    # Enter a parse tree produced by BloonParser#read_k.
    def enterRead_k(self, ctx:BloonParser.Read_kContext):
        pass

    # Exit a parse tree produced by BloonParser#read_k.
    def exitRead_k(self, ctx:BloonParser.Read_kContext):
        pass


    # Enter a parse tree produced by BloonParser#write.
    def enterWrite(self, ctx:BloonParser.WriteContext):
        pass

    # Exit a parse tree produced by BloonParser#write.
    def exitWrite(self, ctx:BloonParser.WriteContext):
        pass


    # Enter a parse tree produced by BloonParser#write_t.
    def enterWrite_t(self, ctx:BloonParser.Write_tContext):
        pass

    # Exit a parse tree produced by BloonParser#write_t.
    def exitWrite_t(self, ctx:BloonParser.Write_tContext):
        pass


    # Enter a parse tree produced by BloonParser#write_k.
    def enterWrite_k(self, ctx:BloonParser.Write_kContext):
        pass

    # Exit a parse tree produced by BloonParser#write_k.
    def exitWrite_k(self, ctx:BloonParser.Write_kContext):
        pass


    # Enter a parse tree produced by BloonParser#cond.
    def enterCond(self, ctx:BloonParser.CondContext):
        pass

    # Exit a parse tree produced by BloonParser#cond.
    def exitCond(self, ctx:BloonParser.CondContext):
        pass


    # Enter a parse tree produced by BloonParser#cond_t.
    def enterCond_t(self, ctx:BloonParser.Cond_tContext):
        pass

    # Exit a parse tree produced by BloonParser#cond_t.
    def exitCond_t(self, ctx:BloonParser.Cond_tContext):
        pass


    # Enter a parse tree produced by BloonParser#r_while.
    def enterR_while(self, ctx:BloonParser.R_whileContext):
        pass

    # Exit a parse tree produced by BloonParser#r_while.
    def exitR_while(self, ctx:BloonParser.R_whileContext):
        pass


    # Enter a parse tree produced by BloonParser#floop.
    def enterFloop(self, ctx:BloonParser.FloopContext):
        pass

    # Exit a parse tree produced by BloonParser#floop.
    def exitFloop(self, ctx:BloonParser.FloopContext):
        pass


    # Enter a parse tree produced by BloonParser#super_exp.
    def enterSuper_exp(self, ctx:BloonParser.Super_expContext):
        pass

    # Exit a parse tree produced by BloonParser#super_exp.
    def exitSuper_exp(self, ctx:BloonParser.Super_expContext):
        pass


    # Enter a parse tree produced by BloonParser#super_exp_t.
    def enterSuper_exp_t(self, ctx:BloonParser.Super_exp_tContext):
        pass

    # Exit a parse tree produced by BloonParser#super_exp_t.
    def exitSuper_exp_t(self, ctx:BloonParser.Super_exp_tContext):
        pass


    # Enter a parse tree produced by BloonParser#expression.
    def enterExpression(self, ctx:BloonParser.ExpressionContext):
        pass

    # Exit a parse tree produced by BloonParser#expression.
    def exitExpression(self, ctx:BloonParser.ExpressionContext):
        pass


    # Enter a parse tree produced by BloonParser#expression_t.
    def enterExpression_t(self, ctx:BloonParser.Expression_tContext):
        pass

    # Exit a parse tree produced by BloonParser#expression_t.
    def exitExpression_t(self, ctx:BloonParser.Expression_tContext):
        pass


    # Enter a parse tree produced by BloonParser#exp.
    def enterExp(self, ctx:BloonParser.ExpContext):
        pass

    # Exit a parse tree produced by BloonParser#exp.
    def exitExp(self, ctx:BloonParser.ExpContext):
        pass


    # Enter a parse tree produced by BloonParser#exp_t.
    def enterExp_t(self, ctx:BloonParser.Exp_tContext):
        pass

    # Exit a parse tree produced by BloonParser#exp_t.
    def exitExp_t(self, ctx:BloonParser.Exp_tContext):
        pass


    # Enter a parse tree produced by BloonParser#term.
    def enterTerm(self, ctx:BloonParser.TermContext):
        pass

    # Exit a parse tree produced by BloonParser#term.
    def exitTerm(self, ctx:BloonParser.TermContext):
        pass


    # Enter a parse tree produced by BloonParser#term_t.
    def enterTerm_t(self, ctx:BloonParser.Term_tContext):
        pass

    # Exit a parse tree produced by BloonParser#term_t.
    def exitTerm_t(self, ctx:BloonParser.Term_tContext):
        pass


    # Enter a parse tree produced by BloonParser#factor.
    def enterFactor(self, ctx:BloonParser.FactorContext):
        pass

    # Exit a parse tree produced by BloonParser#factor.
    def exitFactor(self, ctx:BloonParser.FactorContext):
        pass


    # Enter a parse tree produced by BloonParser#factor_t.
    def enterFactor_t(self, ctx:BloonParser.Factor_tContext):
        pass

    # Exit a parse tree produced by BloonParser#factor_t.
    def exitFactor_t(self, ctx:BloonParser.Factor_tContext):
        pass


    # Enter a parse tree produced by BloonParser#var_const.
    def enterVar_const(self, ctx:BloonParser.Var_constContext):
        pass

    # Exit a parse tree produced by BloonParser#var_const.
    def exitVar_const(self, ctx:BloonParser.Var_constContext):
        pass



del BloonParser