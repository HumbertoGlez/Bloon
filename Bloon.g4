grammar Bloon;

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

var: ID var_t;
var_t: arr_idx var_k | var_k;
var_k: '.' var | ;

var_dec: 'vars' var_dec_t;
var_dec_t: ID arr var_dec_k | ID var_dec_k;
var_dec_k: ',' var_dec_t | ':' var_type ';' var_dec_p;
var_dec_p: var_dec_t | ;

arr_idx: '[' exp arr_idx_t;
arr_idx_t: ',' exp ']' | ']';

arr: '[' CONST_INT arr_t;
arr_t: ',' CONST_INT ']' | ']';

assign: var assign_t;
assign_t: '=' super_exp ';' | assign_op super_exp ';';

var_type: 'int' | 'float' | 'char' | ID;

assign_op: '+' '=' | '-' '=' | '*' '=' | '/' '=';   

type_meth: var_type | 'void';

statement: assign | cond | r_return | read | write | r_while | floop | call_void;


func: type_meth 'meth' ID '(' func_t;
func_t: param func_k | func_k;
func_k: ')' ';' func_p;
func_p: var_dec block | block;

param: var_type ID param_t;
param_t: ',' param | ;

block: '{' block_t;
block_t: statement block_t | statement '}' | '}';

r_return: 'return' '(' super_exp ')' ';';

call: var '(' call_t;
call_t: call_args ')' | ')';

call_args: super_exp call_args_t | call call_args_t;
call_args_t: ',' call_args | ;

call_void: call ';';

read: 'read' '(' read_t;
read_t: var read_k;
read_k: ',' read_t | ')' ';';

write: 'write' '(' write_t;
write_t: super_exp write_k | call write_k;
write_k: ',' write_t | ')' ';'; 

cond: 'cond' '(' super_exp ')' 'then' block cond_t;
cond_t: 'else' block | ;

r_while: 'while' '(' super_exp ')' 'do' block;

floop: 'floop' var 'to' super_exp 'do' block;

super_exp: expression super_exp_t;
super_exp_t: 'and' super_exp | 'or' super_exp | ;

expression: '!' exp expression_t | exp expression_t;
expression_t: '>' exp | '<' exp | '<=' exp | '>=' exp | '==' exp | '!=' exp | ;

exp: term exp_t;
exp_t: '+' exp | '-' exp | ;

term: factor term_t;
term_t: '*' term | '/' term | ;

factor: '(' expression ')' | var_const | call | factor_t;
factor_t: '+' var_const | '-' var_const;

var_const: var | CONST_INT | CONST_FLOAT | CONST_STR;
