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

main: 'main' '(' ')' block;

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
assign_t: '=' {compi.add_op('=')} super_exp {compi.assign_var()}';' | assign_op {compi.add_op($assign_op.text)} super_exp {compi.assign_var()} ';';

var_type: 'int' | 'float' | 'char' | 'string';

custom_type: ID;

assign_op: '+' '=' | '-' '=' | '*' '=' | '/' '=';   

type_meth: var_type | 'void';

statement: assign | cond | r_return | read | write | r_while | floop | call_void;


func: type_meth 'meth' ID '(' func_t;
func_t: param func_k | func_k;
func_k: ')' ';' func_p;
func_p: var_dec block | block;

param: var_type ID param_t | custom_type ID param_t;
param_t: ',' param | ;

block: '{' block_t;
block_t: statement block_t | statement '}' | '}';

r_return: 'return' '(' {compi.add_op('(')} super_exp ')' {compi.close_parens()} ';';

call: var '(' call_t;
call_t: call_args ')' | ')';

call_args: super_exp call_args_t | call call_args_t;
call_args_t: ',' call_args | ;

call_void: call ';';

read: 'read' '(' {compi.add_op('(')} read_t;
read_t: var {compi.call_method('read')} read_k;
read_k: ',' read_t | ')' {compi.close_parens()} ';';

write: 'write' '(' {compi.add_op('(')} write_t;
write_t: super_exp {compi.call_method('write')} write_k | CONST_STR {compi.get_const($CONST_STR.text, "string"); compi.call_method('write')} write_k | call write_k;
write_k: ',' write_t | ')' {compi.close_parens()} ';'; 

cond: 'cond' '(' {compi.add_op('(')} super_exp ')' {compi.close_parens()} 'then' block cond_t;
cond_t: 'else' block | ;

r_while: 'while' '(' {compi.add_op('(')} super_exp ')' {compi.close_parens()} 'do' block;

floop: 'floop' var 'to' super_exp 'do' block;

super_exp: expression super_exp_t;
super_exp_t: 'and' super_exp | 'or' super_exp | ;

expression: '!' exp expression_t | exp expression_t {compi.arithmetic_operation()};
expression_t: '>' {compi.add_op('>')} exp | '<' {compi.add_op('<')} exp | '<=' {compi.add_op('<=')} exp | '>=' {compi.add_op('>=')} exp | '==' {compi.add_op('==')} exp | '!=' {compi.add_op('!=')} exp | ;

exp: term exp_t {compi.arithmetic_operation()};
exp_t: '+' {compi.add_op('+')} exp | '-' {compi.add_op('-')} exp | ;

term: factor term_t {compi.arithmetic_operation()};
term_t: '*' {compi.add_op('*')} term | '/' {compi.add_op('/')} term | ;

factor: '(' {compi.add_op('(')} expression ')' {compi.close_parens()} | var_const | call | factor_t;
factor_t: '+' var_const | '-' var_const;

var_const: var | CONST_INT {compi.get_const($CONST_INT.text, "int")} | CONST_FLOAT {compi.get_const($CONST_FLOAT.text, "float")} | CONST_STR {compi.get_const($CONST_STR.text, "string")};
