import attr
from typing import Dict, Any
from collections import deque

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

class Compiler:
    # Dictionary of methods, key is string with id
    meth_dir = {
        "global": Method('void', {'int': {}, 'float': {}, 'string': {}, 'char': {}, 'custom': {}}),
        "main": Method('int',  {'int': {}, 'float': {}, 'string': {}, 'char': {}, 'custom': {}})
    }
    method_stack = deque(["global"])

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

def add_var(self, var_type, var_id):
    method = self.meth_dir[self.method_stack[-1]]
    var_table = method.m_vars
    for given_type, var_dir in var_table.items():
        if var_id in var_dir:
            raise Exception("A variable named {var_id} was already defined with type {given_type}")
    else:
        isGlobal = self.method_stack[-1] == "global"
        var_dir = self.get_var_dir(var_type)
        var_dir[var_id] = Var(isGlobal)