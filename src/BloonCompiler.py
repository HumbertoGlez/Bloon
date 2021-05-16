import attr
from typing import Dict, Any, List
from collections import deque
from queue import Queue
from tools import operation_result_type

# Class used to create methods
@attr.s
class Method:
    # Method type given as string
    m_type: str = attr.ib()
    # Dictionary of variables, the keys are strings with the possible types, 
    # values are dictionaries for the variables of corresponding type
    m_vars: Dict[str, Any] = attr.ib(attr.Factory(dict))
    # CHECK PARAM TABLE stuff, some thing might not be needed
    m_param_count: int = attr.ib(0)
    m_vars_counts: Dict[str, int] = attr.ib(attr.Factory(dict))
    m_param_types: List[str] = attr.ib(attr.Factory(list))
    m_start: int = attr.ib(0)
    m_temp: int = attr.ib(0)

    def get_address(self, v_type):
        if v_type in self.m_vars_counts:
            self.m_vars_counts[v_type] += 1
        else:
            self.m_vars_counts[v_type] = 0
        return self.m_vars_counts[v_type]


@attr.s
class Var:
    address: int = attr.ib()
    # By default variables are created as not global
    isGlobal: bool = attr.ib(False)
    dimensions: int = attr.ib(0)

@attr.s
class Operand:
    op_id: str = attr.ib()
    op_addr: int = attr.ib(None)
    isGlobal: bool = attr.ib(False)
    dimensions: int = attr.ib(0)

@attr.s
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
        "read": Method('void', {}),
        "write": Method('void', {}),
    }
    method_stack = deque(["global"])
    operator_stack = deque()
    operand_stack = deque()
    type_stack = deque()
    quad_queue = Queue()
    newVar_count = 0
    constants = {'int': {}, 'float': {}, 'string': {}, 'char': {}}
    gotos = []

def define_method(self, method_type, method_id):
    if  method_id in self.meth_dir:
        raise Exception("Method {} was already defined".format(method_id))
    else:
        self.method_stack.append(method_id)
        self.meth_dir[method_id] = Method(method_type, {'int': {}, 'float': {}, 'string': {}, 'char': {}, 'custom': {}})
        self.meth_dir[method_id].m_start = len(self.quad_queue)

def process_method(self):
    method_id = self.method_stack[-1]
    method = self.meth_dir[method_id]
    if method.m_type != 'void':
        result = self.operand_stack.pop()
        self.type_stack.pop()
        self.quad_queue.put(Quadruple("RETURN", result))
    
    self.quad_queue.put(Quadruple("ENDMETH"))
    self.method_stack.pop()
    
def define_param(self, param_type, param_id, param_dim = False):
    method_id = self.method_stack[-1]
    method = self.meth_dir[method_id]
    dimensions = 0
    if param_dim == 'arr':
        dimensions = 1
    elif param_dim == 'mat':
        dimensions = 2
    address = method.get_address(param_type)
    method.m_vars[param_type][param_id] = Var(address, False, dimensions)
    method.m_param_count += 1
    method.m_param_types.append(param_type)

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
        while self.newVar_count > 0:
            var_id = self.operand_stack.pop().op_id
            self.newVar_count = self.newVar_count - 1
            for given_type, var_dir in var_table.items():
                if var_id in var_dir:
                    raise Exception(f"A variable named {var_id} was already defined with type {given_type}")
            else:
                isGlobal = self.method_stack[-1] == "global"
                var_dir = self.get_var_dir(v_type)
                address = method.get_address(v_type)
                var_dir[var_id] = Var(address, isGlobal)
                    
    else:
        raise Exception(f"Unknown error at variable declaration of type {v_type}.")
  

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
        left_oper = self.operand_stack.pop()
        left_type = self.type_stack.pop()
        result_type = operation_result_type(op, left_type, right_type)

        # method = self.method_stack[-1]
        # res_oper = Operand(f't{self.temp}', method == 'global')
        # self.operand_stack.append(res_oper)
        # self.type_stack.append(result_type)
        self.quad_queue.put(Quadruple(op, left_oper, right_oper, left_oper))
        # self.temp = self.temp + 1
        # self.assign_var()
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

    method_id = self.method_stack[-1]
    method = self.meth_dir[method_id]
    res_op = Operand(f't{method.m_temp}', method_id == 'global')
    self.operand_stack.append(res_op)
    self.type_stack.append(result_type)
    self.quad_queue.put(Quadruple(oper, left_op, right_op, res_op))
    method.m_temp += 1

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
        address = method.get_address(const_type)
        dir[const_id] = Var(address, True, None)
    self.operand_stack.append(Operand(const_id, True))
    self.type_stack.append(const_type)
    self.constants[const_type] = const_id

def verify_method(self, id):
    if id not in self.meth_dir:
        raise Exception(f"Method {id} was not declared.")

def call_method(self, id):
    method = self.meth_dir[id]
    for i in range(method.m_param_count):
        self.quad_queue.put(Quadruple("PARAM", None, None, self.operand_stack.pop()))
    if id == 'read':
        variable = self.operand_stack.pop()
        variable_type = self.type_stack.pop()
        if check_var_exists(variable.op_id, self.meth_dir[self.method_stack[-1]].m_vars) or check_var_exists(variable.op_id, self.meth_dir['global'].m_vars):
            self.quad_queue.put(Quadruple("READ", None, None, variable))
    elif id == 'write':
        self.quad_queue.put(Quadruple("WRITE"))
        self.operand_stack.append(Operand('', True))
    else:
        self.quad_queue.put(Quadruple("ERA", res=id))
        method_id = self.method_stack[-1]
        method_type = method.m_type
        address = None
        if method_type != 'void':
            address = self.meth_dir[method_id].get_address(method_type)
            self.meth_dir[method_id].m_vars[method_type][f"t{self.meth_dir[method_id].m_temp}"] = Var(address)
            rtn_op = Operand(f"t{self.meth_dir[method_id].m_temp}", address, method_id == 'global')
            self.operand_stack.append(rtn_op)
            self.meth_dir[method_id].m_temp += 1
        
        self.quad_queue.put(Quadruple("GOSUB", id, address, method.m_start))

def fill(self, quad_idx, cont):
    self.quad_queue[quad_idx].ans = cont
    
def condition(self):
    exp_type = self.type_stack.pop()
    if (exp_type != 'int'):
        raise Exception("Unexpected type for condition")
    else:
        result = self.operand_stack.pop()
        self.quad_queue.put(Quadruple("GOTOFALSE", result))
        self.gotos.append(len(self.quad_queue) - 1)

def end_condition(self):
    end = self.gotos.pop()
    self.fill(end, len(self.quad_queue))

def else_condition(self):
    self.quad_queue.put(Quadruple("GOTO"))
    false = self.gotos.pop()
    self.gotos.append(len(self.quad_queue) - 1)
    self.fill(false, len(self.quad_queue) - 1)

def while_condition(self):
    self.gotos.append(len(self.quad_queue))

def while_expression(self):
    exp_type = self.type_stack.pop()
    if(exp_type != 'int'):
        raise Exception("Unexpected type for condition")
    else:
        result = self.operand_stack.pop()
        self.quad_queue.put(Quadruple("GOTOFALSE", result))
        self.gotos.append(len(self.quad_queue) - 1)

def while_end(self):
    end = self.gotos.pop()
    rtn = self.gotos.pop()
    self.quad_queue.put("GOTO", rtn)
    self.fill(end, len(self.quad_queue))

def floop(self):
    exp_type = self.type_stack.pop()  
    if (exp_type != 'int'):
        raise Exception("Unexpected type for floop loop expression, expected integer")
    else:
        exp = self.operand_stack.pop()
        # We dont pop the variable to increase its value later on at the end of iteration
        var = self.operand_stack[-1]
        var_type = self.type_stack[1]
        result_type = operation_result_type('<=', var_type, exp_type)
        method_id = self.method_stack[-1]
        method = self.meth_dir[method_id]
        res_op = Operand(f't{method.m_temp}', method_id == 'global')

        self.operand_stack.append(res_op)
        self.type_stack.append(result_type)

        self.quad_queue.put(Quadruple('<=', var, exp, res_op))
        method.m_temp += 1
        # Set goto for the quadruple where the loop condition is done
        self.gotos.append(len(self.quad_queue) - 1)

def floop_check(self):
    compare_res = self.operand_stack.pop()
    self.type_stack.pop()
    self.quad_queue.put(Quadruple("GOTOFALSE", compare_res))
    # Set goto for the quadruple to later on fill it
    self.gotos.append(len(self.quad_queue - 1))

def floop_end(self):
    false_quad = self.gotos.pop()
    compare_quad = self.gotos.pop()
    var = self.operand_stack[-1]
    # IMPORTANT, special quadruple to add 1 to the given operand
    self.quad_queue.put(Quadruple("+_1", var, None, var))
    self.quad_queue.put(Quadruple("GOTO", compare_quad))
    self.fill(false_quad, len(self.quad_queue))

