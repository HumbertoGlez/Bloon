grammar Bloon;

@header {
from BloonCompiler import Compiler
compi = Compiler()
quad_queue = None
meth_dir = None
class_dir = None
constants = None
}

/*
 * Lexer Rules
 */

ID: [A-Za-z_]([A-Za-z_]|[0-9])*;
CONST_INT: [1-9][0-9]*|[0];
CONST_FLOAT: (([1-9][0-9]*|[0])[.])[0-9]+;
CONST_STR: ["].*? ["];
CONST_CHAR: ['].['];
WHITESPACE: [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

/*
 * Parser Rules
 */

program: 'program' ID ';' program_t {compi.save_state(self)} EOF;
program_t: r_class program_t | var_dec program_t | func program_t | main;

main: 'main' '(' {compi.open_parens()} ')' {compi.close_parens(); compi.main_method()} block;

r_class: 'class' ID {compi.add_operand($ID.text)} class_t;
class_t: '<' 'inherits' ID '>' {compi.add_operand($ID.text); compi.define_class(True)} class_k | {compi.define_class()} class_k;
class_k: '{' ( 'attributes' ':' class_att | class_l ); 
class_att: (ID {compi.add_operand($ID.text); compi.increase_varCount()} | ID '[' CONST_INT {compi.add_limit($CONST_INT.text)} (',' CONST_INT {compi.add_limit($CONST_INT.text)} ']' {compi.add_operand($ID.text, 2);} | ']' {compi.add_operand($ID.text, 1)}) {compi.increase_varCount()}) (',' class_att | ':' var_type {compi.define_attr($var_type.text)} ';' (class_att | class_l) );
class_l: {compi.add_att_to_parent_meths()} ('methods' ':' class_p | '}' ';' {compi.end_class()});
class_p: class_func '}' ';' {compi.end_class()} | class_func class_p;

class_func: type_meth 'meth' ID {compi.define_method($type_meth.text, $ID.text, True)} '(' {compi.open_parens()} c_func_t;
c_func_t: param c_func_k | c_func_k;
c_func_k: ')' {compi.close_parens()} c_func_p;
c_func_p: var_dec block {compi.process_method()} | block {compi.process_method()};

var: ID {compi.add_operand($ID.text)} var_t;
var_t: arr_idx | arr_idx '.' var {compi.get_var(True)} | '.' ID {compi.add_operand($ID.text); compi.get_var(True)} | {compi.get_var()};
arr_idx: '[' exp (',' exp ']' {compi.get_array_item(2)} | ']' {compi.get_array_item(1)});

var_dec: 'vars' var_dec_t;
var_dec_t: (ID '[' CONST_INT {compi.add_limit($CONST_INT.text)} (',' CONST_INT {compi.add_limit($CONST_INT.text)} ']' {compi.add_operand($ID.text, 2);} | ']' {compi.add_operand($ID.text, 1)}) {compi.increase_varCount()} | ID {compi.add_operand($ID.text); compi.increase_varCount()}) (',' var_dec_t | ':' (var_type {compi.define_var($var_type.text)}';' var_dec_l | custom_type {compi.define_var($custom_type.text)} ';' var_dec_l));
var_dec_l: var_dec_t | ;

assign: var assign_t;
assign_t: '=' super_exp {compi.assign_var()}';' | assign_op super_exp {compi.arithmetic_assign($assign_op.text)} ';';

var_type: 'int' | 'float' | 'char' | 'string';

custom_type: ID;

assign_op: '+=' | '-=' | '*=' | '/=';   

type_meth: var_type | 'void';

statement: assign | cond | r_return | read | write | r_while | floop | call_void;


func: type_meth 'meth' ID {compi.define_method($type_meth.text, $ID.text)} '(' {compi.open_parens()} func_t;
func_t: param func_k | func_k;
func_k: ')' {compi.close_parens()} func_p;
func_p: var_dec block {compi.process_method()} | block {compi.process_method()};

param: 
        var_type ID {compi.define_param($var_type.text, $ID.text)} param_t 
        | var_type ID ('[' CONST_INT ']' {compi.add_limit($CONST_INT.text); compi.define_param($var_type.text, $ID.text, 1)} | '[' CONST_INT {compi.add_limit($CONST_INT.text)} ',' CONST_INT {compi.add_limit($CONST_INT.text)} ']'  {compi.define_param($var_type.text, $ID.text, 2)}) param_t
        | custom_type ID {compi.define_param($custom_type.text, $ID.text)} param_t
        | custom_type ID ('[' CONST_INT ']' {compi.add_limit($CONST_INT.text); compi.define_param($custom_type.text, $ID.text, 1)} | '[' CONST_INT {compi.add_limit($CONST_INT.text)} ',' CONST_INT {compi.add_limit($CONST_INT.text)} ']'  {compi.define_param($custom_type.text, $ID.text, 2)}) param_t;
param_t: ',' param | ;

block: '{' block_t;
block_t: statement block_t | statement '}' | '}';

r_return: 'return' '(' {compi.open_parens()} super_exp ')' {compi.close_parens(); compi.rtn_stmt()} ';';

call: ID {compi.verify_method($ID.text)} '(' {compi.open_parens()} super_exp? ( ',' super_exp )* ')' {compi.close_parens(); compi.call_method($ID.text)} | call_class_meth;
call_class_meth:  ID {compi.add_operand($ID.text)} '.' ID {compi.verify_method($ID.text, True)} '(' {compi.open_parens()} super_exp? ( ',' super_exp )* ')' {compi.close_parens(); compi.call_method($ID.text, True)};
call_void: call ';';

read: 'read' '('  {compi.open_parens()} read_t;
read_t: var {compi.call_method('read')} read_k;
read_k: ',' read_t | ')' {compi.close_parens()} ';';

write: 'write' '(' {compi.open_parens()} write_t;
write_t: super_exp {compi.call_method('write')} write_k | CONST_STR {compi.get_const($CONST_STR.text, "string"); compi.call_method('write')} write_k | call write_k;
write_k: ',' write_t | ')' {compi.close_parens(); compi.new_write()} ';'; 

cond: 'cond' '(' {compi.open_parens()} super_exp ')' {compi.close_parens(); compi.condition()} 'then' block cond_t {compi.end_condition()};
cond_t: 'else' {compi.else_condition()} block | ;

r_while: 'while' {compi.while_condition()} '(' {compi.open_parens()} super_exp ')' {compi.close_parens(); compi.while_expression()} 'do' block {compi.while_end()};

floop: 'floop' var 'to' super_exp {compi.floop()} 'do' {compi.floop_check()} block {compi.floop_end()};

super_exp: '!' expression {compi.logic_operation('NOT')} super_exp_t | expression super_exp_t;
super_exp_t: 'and' super_exp {compi.logic_operation('AND')} (super_exp | ) | 'or' super_exp {compi.logic_operation('OR')} (super_exp | ) | ;

expression: exp (
                    (
                        '>' {compi.add_op('>')}
                        | '<' {compi.add_op('<')}
                        | '>=' {compi.add_op('>=')}
                        | '<=' {compi.add_op('<=')}
                        | '==' {compi.add_op('==')}
                        | '!=' {compi.add_op('!=')}
                    ) exp {compi.arithmetic_operation('>', '<', '>=', '<=', '==', '!=')}
                )*;

exp: term (('+' {compi.add_op('+')} | '-' {compi.add_op('-')}) term {compi.arithmetic_operation('+', '-')})*;

term: factor (('*' {compi.add_op('*')} | '/' {compi.add_op('/')} | '%' {compi.add_op('%')}) factor {compi.arithmetic_operation('*', '/', '%')})*;

factor: '(' {compi.open_parens()} expression ')' {compi.close_parens()} | var_const | call | factor_t;
factor_t: var_const | '-' {compi.set_negative()} var_const;

var_const: var | CONST_INT {compi.get_const($CONST_INT.text, "int")} | CONST_FLOAT {compi.get_const($CONST_FLOAT.text, "float")} | CONST_STR {compi.get_const($CONST_STR.text, "string")} | CONST_CHAR {compi.get_const($CONST_CHAR.text, "char")};