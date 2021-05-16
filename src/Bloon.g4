grammar Bloon;

@header {
    from BloonCompiler import Compiler
    compi = Compiler()
}

/*
 * Lexer Rules
 */

ID: [A-Za-z_]([A-Za-z_]|[0-9])*;
CONST_INT: [1-9][0-9]*|[0];
CONST_FLOAT: (([1-9][0-9]*|[0])[.])[0-9]+;
CONST_STR: ["].*? ["];
WHITESPACE: [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

/*
 * Parser Rules
 */

program: 'program' ID ';' program_t;
program_t: r_class program_t | var_dec program_t | func program_t | main;

main: 'main' '(' {compi.open_parens()} ')' {compi.close_parens()} block;

r_class: 'class' ID class_t;
class_t: '<' 'inherits' ID '>' class_k | class_k;
class_k: ';' '{' class_j;
class_j: 'attributes' '<' var_dec '>' class_l | class_l;
class_l: 'methods' '<' class_p | '}' ';';
class_p: func '>' '}' ';' | func class_p;

var: ID var_t {compi.get_var($ID.text)};
var_t: arr_idx var_k | var_k;
var_k: '.' var | ;

var_dec: 'vars' var_dec_t;
var_dec_t: ID (arr)? {compi.add_operand($ID.text); compi.increase_varCount()} (',' var_dec_t | ':' (var_type {compi.define_var($var_type.text)}';' var_dec_l | custom_type {compi.define_var($custom_type.text)} ';' var_dec_l));
var_dec_l: var_dec_t | ;

arr_idx: '[' exp arr_idx_t;
arr_idx_t: ',' exp ']' | ']';

arr: '[' CONST_INT arr_t;
arr_t: ',' CONST_INT ']' | ']';

assign: var assign_t;
assign_t: '=' super_exp {compi.assign_var()}';' | assign_op super_exp {compi.arithmetic_assign($assign_op.text)} ';';

var_type: 'int' | 'float' | 'char' | 'string';

custom_type: ID;

assign_op: '+=' | '-=' | '*=' | '/=';   

type_meth: var_type | 'void';

statement: assign | cond | r_return | read | write | r_while | floop | call_void;


func: type_meth 'meth' ID {compi.define_method($type_meth.text, $ID.text)} '(' {compi.open_parens()} func_t;
func_t: param func_k | func_k;
func_k: ')' {compi.close_parens()} ';' func_p;
func_p: var_dec block {compi.process_method()} | block {compi.process_method()};

param: 
        var_type ID {compi.define_param($var_type.text, $ID.text)} param_t 
        | var_type ID p_dim {compi.define_param($var_type.text, $ID.text, $p_dim.text)} param_t
        | custom_type ID {compi.define_param($var_type.text, $ID.text)} param_t
        | custom_type ID p_dim {compi.define_param($var_type.text, $ID.text, $p_dim.text)} param_t;
param_t: ',' param | ;
p_dim: 'arr' | 'mat';

block: '{' block_t;
block_t: statement block_t | statement '}' | '}';

r_return: 'return' '(' {compi.open_parens()} super_exp ')' {compi.close_parens()} ';';

call: ID {compi.verify_method($ID.text)}'(' {compi.open_parens()} super_exp? ( ',' super_exp )* ')' {compi.close_parens(); compi.call_method($ID.text)};

call_void: call ';';

read: 'read' '('  {compi.open_parens()} read_t;
read_t: var {compi.call_method('read')} read_k;
read_k: ',' read_t | ')' {compi.close_parens()} ';';

write: 'write' '(' {compi.open_parens()} write_t;
write_t: super_exp {compi.call_method('write')} write_k | CONST_STR {compi.get_const($CONST_STR.text, "string"); compi.call_method('write')} write_k | call write_k;
write_k: ',' write_t | ')' {compi.close_parens()} ';'; 

cond: 'cond' '(' {compi.open_parens()} super_exp ')' {compi.close_parens(); compi.condition()} 'then' block cond_t {compi.end_condition()};
cond_t: 'else' {compi.else_condition()} block | ;

r_while: 'while' {compi.while_condition()} '(' {compi.open_parens()} super_exp ')' {compi.close_parens(); compi.while_expression()} 'do' block {compi.while_end()};

floop: 'floop' var 'to' super_exp {compi.floop()} 'do' {compi.floop_check()} block {compi.floop_end()};

super_exp: expression super_exp_t;
super_exp_t: 'and' super_exp | 'or' super_exp | ;

expression: '!' exp expression_t | exp expression_t {compi.arithmetic_operation()};
expression_t: '>' {compi.add_op('>')} exp | '<' {compi.add_op('<')} exp | '<=' {compi.add_op('<=')} exp | '>=' {compi.add_op('>=')} exp | '==' {compi.add_op('==')} exp | '!=' {compi.add_op('!=')} exp | ;

exp: term exp_t {compi.arithmetic_operation()};
exp_t: '+' {compi.add_op('+')} exp | '-' {compi.add_op('-')} exp | ;

term: factor term_t {compi.arithmetic_operation()};
term_t: '*' {compi.add_op('*')} term | '/' {compi.add_op('/')} term | ;

factor: '(' {compi.open_parens()} expression ')' {compi.close_parens()} | var_const | call | factor_t;
factor_t: '+' var_const | '-' var_const;

var_const: var | CONST_INT {compi.get_const($CONST_INT.text, "int")} | CONST_FLOAT {compi.get_const($CONST_FLOAT.text, "float")} | CONST_STR {compi.get_const($CONST_STR.text, "string")};
