import attr
from typing import Dict, Any
from collections import deque
from queue import Queue

# Class used to create methods
@attr.s
class Method:
    # Method type given as string
    m_type: str = attr.ib()
    # Dictionary of variables, the keys are strings with the possible types, 
    # values are dictionaries for the variables of corresponding type
    m_vars: Dict[str, Any] = attr.ib(attr.Factory(dict))

@attrs.s
class Var:
    # By default variables are created as not global
    isGlobal: bool = attr.ib(False)
    dimensions: int = attr.ib(0)

@attrs.s
class Operand:
    op_id: str = attr.ib()
    # op_type: str = attr.ib()
    isGlobal: bool = attr.ib(False)
    dimensions: int = attr.ib(0)

@attrs.s
class Quadruple:
    operator = attr.ib()
    left_op: Operand = attr.ib(None)
    right_op: Operand = attr.ib(None)
    ans: Any = attr.ib(None)


class Compiler:
    # Dictionary of methods, key is string with id
    meth_dir = {
        "global": Method('void', {'int': {}, 'float': {}, 'string': {}, 'char': {}, 'custom': {}}),
        "main": Method('int',  {'int': {}, 'float': {}, 'string': {}, 'char': {}, 'custom': {}}),
        "read": Method('void', {})
    }
    method_stack = deque(["global"])
    operator_stack = deque()
    operand_stack = deque()
    type_stack = deque()
    quad_queue = Queue()
    temp = 0
    newVar_count = 0

def add_method(self, method_type, method_id):
    if  m_name in self.meth_dir:
        raise Exception("Method {} was already defined".format(method_id))
    else:
        self.method_stack.append(method_id)
        self.meth_dir[method_id] = Method(method_type, {'int': {}, 'float': {}, 'string': {}, 'char': {}, 'custom': {}})

def add_param(self, param_type, param_id):
    method_id = self.method_stack[-1]
    method = self.meth_dir[method_id]
    method.m_vars[param_type][param_id] = Var()

def get_var_dir(self, var_type, isGlobal=False):
    method_id =  "global" if isGlobal else self.method_stack[-1]
    method = self.meth_dir[method_id]
    var_dir = method.m_vars[var_type]
    return var_dir

# Needs revision for arrays, etc
def define_var(self, v_type):
    method = self.meth_dir[self.method_stack[-1]]
    var_table = method.m_vars
    if self.newVar_count > 0:
        var_id = self.operand_stack.pop().op_id
        self.newVar_count = self.newVar_count - 1
    else:
        raise Exception(f"Unknown error at variable declaration of type {v_type}.")

    for given_type, var_dir in var_table.items():
        if var_id in var_dir:
            raise Exception(f"A variable named {var_id} was already defined with type {given_type}")
    else:
        isGlobal = self.method_stack[-1] == "global"
        var_dir = self.get_var_dir(v_type)
        var_dir[var_id] = Var(isGlobal)

def assign_var(self):
    method = self.meth_dir[self.method_stack[-1]]
    var_table = method.m_vars
    res = self.operand_stack.pop()
    res_type = self.type_stack.pop()
    left_op = self.operand_stack.pop()
    left_type = self.type_stack.pop()

    isGlobal = self.method_stack[-1] == 'global'

    self.quad_queue.put(Quadruple('ASSIGN', res, None, left_op))

def arithmetic_assign(self, op):
    op = op.strip('=')
    if op in ['+', '-', '*', '/']:
        right_oper = self.operand_stack.pop()
        right_type = self.type_stack.pop()
        left_oper = self.operand_stack[-1]
        left_type = self.type_stack[-1]
        result_type = operation_result_type(op, left_type, right_type)

        method = self.method_stack[-1]
        res_oper = Operand(f't{self.temp}', method == 'global')
        self.operand_stack.append(res_oper)
        self.quad_queue.put(Quadruple(op, left_oper, right_oper, res_oper))
        self.temp = self.temp + 1
        self.assign_var()
    else:
        raise Exception(f'Invalid operator: {op} for assignment')

def add_operand(self, o):
    self.operand_stack.append(Operand(o))

def add_op(self, op):
    self.operator_stack.append(op)

def add_type(self, t):
    self.type_stack.append(t)

def get_var(self, id):
    #We first check in the current scope
    myVariables = self.meth_dir[self.method_stack[-1]].m_vars
    for vType, varDir in myVariables.items():
        if id in varDir:
            var = varDir[id]
            myType = vType
            self.operand_stack.append(Operand(id, False))
            self.type_stack.append(myType)
            break
    # If we dont find it, we check the global scope
    else:
        myVariables = self.meth_dir['global'].m_vars
        for vType, varDir in myVariables.items():
            if id in varDir:
                var = varDir[id]
                myType = vType
                self.operand_stack.append(Operand(id, myType, True))
                self.type_stack.append(myType)
                break
        else:
            raise Exception(f'{id} was not defined.')


def arithmetic_operation(self):
    right_op = self.operand_stack.pop()
    right_type = self.type_stack.pop()
    left_op = self.operand_stack.pop()
    left_type = self.type_stack.pop()
    oper = self.operator_stack.pop()
    result_type = operation_result_type(oper, left_type, right_type)

    method = self.method_stack[-1]
    res_op = Operand(f't{self.temp}', method == 'global')
    self.operand_stack.append(res_op)
    self.quad_queue.put(Quadruple(oper, left_op, right_op, res_op))
    self.temp = self.temp + 1

def increase_varCount(self):
    self.newVar_count = self.newVar_count + 1

def open_parens(self):
    self.operator_stack.append('(')

def close_parens(self):
    if self.operator_stack[-1] == '(':
        self.operator_stack.pop()
    else:
        raise Exception("Missing Parenthesis.")

def check_var_exists(self, id, var_dir):
    for vType, varDir in var_dir.items():
        if id in varDir:
            return True
    # If we dont find it, we check the global scope
    else:
        raise Exception(f'{id} was not defined.')

def get_const(self, const_id, const_type):
    dir = self.get_var_dir(const_type, isGlobal=True)
    if const_id not in dir:
        dir = self.get_var_dir(const_type, isGlobal=True)
        method = self.meth_dir['global']
        dir[const_id] = Var(True, None)
    self.operand_stack.append(Operand(const_id, True))
    self.type_stack.append(const_type)

def call_method(self, id):
    method = self.meth_dir[id]
    if id == 'read':
        variable = self.operand_stack.pop()
        variable_type = self.type_stack.pop()
        if check_var_exists(variable.op_id, self.meth_dir[self.method_stack[-1]].m_vars) or check_var_exists(variable.op_id, self.meth_dir['global'].m_vars):
            self.quad_queue.put(Quadruple("READ", None, None, variable))
    elif id == 'write':
        res = self.operand_stack.pop()
        res_type = self.type_stack.pop()
        self.quad_queue.put(Quadruple("WRITE", None, None, res))