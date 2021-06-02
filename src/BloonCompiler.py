import attr
import copy
from typing import Dict, Any, List
from collections import deque
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
    m_param_addrs: List[Any] = attr.ib(attr.Factory(list))
    m_param_refs: List[Any] = attr.ib(attr.Factory(list))
    m_param_types: List[str] = attr.ib(attr.Factory(list))
    m_start: int = attr.ib(0)
    m_end: int = attr.ib(0)
    m_temps: Dict[str, int] = {'int': 0, 'float': 0, 'char': 0, 'string': 0, 'Any': 0}
    m_temp_count: int = attr.ib(0)
    m_member_addrs: Dict[str, Any] = attr.ib(attr.Factory(dict))
    m_member_data: Dict[str, Any] = attr.ib(attr.Factory(dict))
    m_obj_vars_refs: Dict[str, Any] = attr.ib(attr.Factory(dict))
    def get_address(self, v_type):
        if v_type in self.m_vars_counts:
            self.m_vars_counts[v_type] += 1
        else:
            self.m_vars_counts[v_type] = 0
        # print("got address ", self.m_vars_counts[v_type], " for", v_type, "in method ", self.m_type)
        return self.m_vars_counts[v_type]

@attr.s
class Attribute:
    a_id: str = attr.ib()
    a_type: str = attr.ib()
    dims: int = attr.ib(0)
    dimSizes: List[int] = attr.ib(attr.Factory(list))

@attr.s
class MyClass:
    c_id: str = attr.ib()
    attributes: Dict[str, Attribute] = attr.ib(attr.Factory(dict))
    methods: Dict[str, Method] = attr.ib(attr.Factory(dict))

@attr.s
class Dim:
    lowerLim: int = attr.ib(0)
    upperLim: int = attr.ib(0)
    m_or_k: int = attr.ib(0)


@attr.s
class Var:
    address: int = attr.ib()
    # By default variables are created as not global
    isGlobal: bool = attr.ib(False)
    dimensions: List[Dim] = attr.ib(attr.Factory(list))
    class_id: str = attr.ib(None)
    next: int = attr.ib(None)
    isRef: Any = attr.ib(False)
    refAmount: Any = attr.ib(False)

@attr.s
class Operand:
    op_id: str = attr.ib()
    op_type: str = attr.ib(None)
    op_addr: int = attr.ib(None)
    isGlobal: bool = attr.ib(False)
    dimensions: int = attr.ib(0)
    dims: List[Dim] = attr.ib(attr.Factory(list))
    next: int = attr.ib(None)
    isRef: Any = attr.ib(False)
    refAmount: Any = attr.ib(False)

@attr.s
class Quadruple:
    operator = attr.ib()
    left_op: Operand = attr.ib(None)
    right_op: Operand = attr.ib(None)
    ans: Any = attr.ib(None)


class Compiler:
    # Dictionary of methods, key is string with id
    meth_dir = {
        "global": Method('void', {'int': {}, 'float': {}, 'string': {}, 'char': {}, 'Any': {}}),
        "main": Method('int',  {'int': {}, 'float': {}, 'string': {}, 'char': {}, 'Any': {}}),
        "read": Method('void', {}),
        "write": Method('void', {}),
    }
    class_dir = {}
    method_stack = deque(["global"])
    # Stack to keep track of where the methods in method stack are stored, False = meth dir
    methodLoc_stack = deque([False])
    operator_stack = deque()
    operand_stack = deque()
    class_stack = deque()
    # initialize quad queue with go to main, later to be filled
    quad_queue = [Quadruple("GOTO")]
    gotos = []
    newVar_count = 0
    constants = {'int': {}, 'float': {}, 'string': {}, 'char': {}}
    upperLimits = []
    negative = False
    floop_stack = deque()
    basicTypes = ['int', 'float', 'char', 'string']
    currClass = ''
    parentId = ''

    def define_class(self, isBaby=False):
        if isBaby:           
            parentId = self.operand_stack.pop().op_id
            babyId = self.operand_stack.pop().op_id
            if babyId in self.class_dir:
                raise Exception("Class {} was already defined".format(babyId))
            elif parentId not in self.class_dir:
                raise Exception("Parent class {} does not exist".format(parentId))
            else:
                self.class_stack.append(babyId)
                self.methodLoc_stack.append(babyId)
                self.class_dir[babyId] = copy.deepcopy(self.class_dir[parentId])
                self.class_dir[babyId].c_id = babyId
        else:
            babyId = self.operand_stack.pop().op_id
            if babyId in self.class_dir:
                raise Exception("Class {} was already defined".format(babyId))
            else:
                self.class_stack.append(babyId)
                self.methodLoc_stack.append(babyId)
                self.class_dir[babyId] = MyClass(babyId)
    
    def define_attr(self, a_type):
        cl = self.class_dir[self.class_stack[-1]]
        attr_table = cl.attributes
        if self.newVar_count > 0:
            while self.newVar_count > 0:
                a = self.operand_stack.pop()
                attr_id = a.op_id
                self.newVar_count = self.newVar_count - 1
                if attr_id in attr_table:
                    raise Exception(f'An attribute named {attr_id} was already defined in class {self.class_stack[-1]}')
                else:
                    if a.dimensions == 1:
                        limit = self.upperLimits.pop()
                        attr_table[a.op_id] = Attribute(a.op_id, a_type, 1, [limit])
                    elif a.dimensions == 2:
                        limit2 = self.upperLimits.pop()
                        limit = self.upperLimits.pop()
                        attr_table[a.op_id] = Attribute(a.op_id, a_type, 2, [limit, limit2])
                    else:
                        attr_table[a.op_id] = Attribute(a.op_id, a_type)                      
        else:
            raise Exception(f"Unknown error at attribute declaration of type {a_type}.")
    
    def add_att_to_parent_meths(self):
        for mName, m in self.class_dir[self.class_stack[-1]].methods.items():
            self.allocate_attributes(self.class_dir[self.class_stack[-1]], mName)

    def end_class(self):
        self.class_stack.pop()
        self.methodLoc_stack.pop()

    def allocate_attributes(self, classObj, method_id):
        cl_id = classObj.c_id
        method = self.class_dir[cl_id].methods[method_id]
        var_table = method.m_vars
        isGlobal = False
        if 'this' in var_table['Any']:
            address = var_table['Any']['this'].address
        else:
            address = method.get_address('Any')
        method.m_member_addrs['this'] = address
        method.m_member_data['this'] = ['Any', 0]
        var_table['Any']['this'] = Var(address, isGlobal, class_id=cl_id)
        for key in classObj.attributes:
            a = classObj.attributes[key]
            v_name = f'this.{a.a_id}'
            if a.dims == 1:
                limit = a.dimSizes[0]
                size = limit
                dim = Dim(0, limit - 1, 0)
                dims = [dim]
                nxt_a = None
                if v_name in var_table[a.a_type]:
                    address = var_table[a.a_type][v_name].address
                    if size > 1:
                        nxt_a = var_table[a.a_type][v_name].next
                else:
                    address = method.get_address(a.a_type)
                    if size > 1:
                        nxt_a = method.get_address(a.a_type)
                method.m_member_addrs[v_name] = [address]
                method.m_member_data[v_name] = [a.a_type, 1, dims]
                var_table[a.a_type][v_name] = Var(address, isGlobal, dims, cl_id, nxt_a)
                for j in range(1, size):
                    if f'{v_name}{j}' in var_table[a.a_type]:
                        address = var_table[a.a_type][f'{v_name}{j}'].address
                        nxt_a = var_table[a.a_type][f'{v_name}{j}'].next if size > j + 1 else None
                    else:
                        address = nxt_a
                        nxt_a = method.get_address(a.a_type) if size > j + 1 else None
                    var_table[a.a_type][f'{v_name}{j}'] = Var(address, isGlobal, class_id=cl_id, next=nxt_a)
                    method.m_member_addrs[v_name].append(address)
            elif a.dims == 2:
                limit = a.dimSizes[0]
                limit2 = a.dimSizes[1]
                size = limit * limit2
                m1 = size / limit
                dim = Dim(0, limit - 1, m1)
                dims = [dim]
                minusK = 0
                dim = Dim(0, limit2 - 1, minusK)
                dims.append(dim)
                nxt_a = None
                if v_name in var_table[a.a_type]:
                    address = var_table[a.a_type][v_name].address
                    if size > 1:
                        nxt_a = var_table[a.a_type][v_name].next
                else:
                    address = method.get_address(a.a_type)
                    if size > 1:
                        nxt_a = method.get_address(a.a_type)
                method.m_member_addrs[v_name] = [address]
                method.m_member_data[v_name] = [a.a_type, 2, dims]
                var_table[a.a_type][v_name] = Var(address, isGlobal, dims, class_id=cl_id, next=nxt_a)
                for j in range(1, size):
                    if f'{v_name}{j}' in var_table[a.a_type]:
                        address = var_table[a.a_type][f'{v_name}{j}'].address
                        nxt_a = var_table[a.a_type][f'{v_name}{j}'].next if size > j + 1 else None
                    else:
                        address = nxt_a
                        nxt_a = method.get_address(a.a_type) if size > j + 1 else None
                    var_table[a.a_type][f'{v_name}{j}'] = Var(address, isGlobal, class_id=cl_id, next=nxt_a)
                    method.m_member_addrs[v_name].append(address)
            else:
                if v_name in var_table[a.a_type]:
                    address = var_table[a.a_type][v_name].address
                else:
                    address = method.get_address(a.a_type)
                method.m_member_addrs[v_name] = address
                method.m_member_data[v_name] = [a.a_type, 0]
                var_table[a.a_type][v_name] = Var(address, isGlobal, class_id=cl_id)

    def define_method(self, method_type, method_id, isClass = False):
        if method_type not in self.basicTypes and method_type not in self.class_dir and method_type != 'void':
            raise Exception("Invalid return type for method {}".format(method_id))
        elif method_type not in self.basicTypes and method_type != 'void':
            mt = method_type
            method_type = 'Any'

        if isClass:
            if method_id in self.class_dir[self.class_stack[-1]].methods:
                raise Exception("Method {} was already defined in this class".format(method_id))
            elif method_id == self.class_stack[-1]:
                raise Exception("Method cannot be named exactly like parent class")
            else:
                myC = self.class_dir[self.class_stack[-1]]
                self.method_stack.append(method_id)
                if self.methodLoc_stack[-1] != self.class_stack[-1]:
                    self.methodLoc_stack.append(self.class_stack[-1])
                myC.methods[method_id] = Method(method_type, {'int': {}, 'float': {}, 'string': {}, 'char': {}, 'Any': {}})
                myC.methods[method_id].m_start = len(self.quad_queue)
                self.allocate_attributes(myC, method_id);

        elif  method_id in self.meth_dir:
            raise Exception("Method {} was already defined or is a reserved word".format(method_id))
        else:
            self.method_stack.append(method_id)
            self.methodLoc_stack.append(False)
            self.meth_dir[method_id] = Method(method_type, {'int': {}, 'float': {}, 'string': {}, 'char': {}, 'Any': {}})
            self.meth_dir[method_id].m_start = len(self.quad_queue)

    def process_method(self):
        if not self.methodLoc_stack[-1] or self.method_stack[-1] == 'global':
            self.quad_queue.append(Quadruple("ENDMETH"))
            self.meth_dir[self.method_stack[-1]].m_end = len(self.quad_queue) - 1
        else:
            self.quad_queue.append(Quadruple("ENDMETH", ans='cl'))
            self.class_dir[self.class_stack[-1]].methods[self.method_stack[-1]].m_end = len(self.quad_queue) - 1
        self.method_stack.pop()
        
    def define_param(self, param_type, param_id, param_dim = False):
        pt = param_type
        if param_type not in self.basicTypes and param_type not in self.class_dir:
            raise Exception(f'{param_type} is not a valid type or a previously defined class.')
        elif param_type not in self.basicTypes:
            param_type = 'Any'
        method_id = self.method_stack[-1]
        method = self.meth_dir[method_id] if not self.methodLoc_stack[-1] or self.method_stack[-1] == 'global' else self.class_dir[self.class_stack[-1]].methods[method_id]
        if param_dim == 1:
            limit = self.upperLimits.pop()
            size = limit
            dim = Dim(0, limit - 1, 0)
            dims = [dim]
            refAddr = method.get_address('int')
            method.m_vars['int'][f'rf-{param_id}'] = Var(refAddr, False, dims)
            refAmount = method.get_address('int')
            method.m_vars['int'][f'rfa-{param_id}'] = Var(refAmount, False, dims)
            method.m_param_refs.append([refAddr, refAmount])
            address = method.get_address(param_type)
            nxt_a = None
            if size > 1:
                nxt_a = method.get_address(param_type)
            method.m_param_addrs.append([address])
            if pt not in self.basicTypes:
                method.m_vars[param_type][param_id] = Var(address, False, dims, pt, nxt_a, True)
                self.define_object_variables(method, False, param_id, pt, True)
            else:
                method.m_vars[param_type][param_id] = Var(address, False, dims, next=nxt_a, isRef=True)
            for i in range(1, size):
                address = nxt_a
                nxt_a = method.get_address(param_type)
                if pt not in self.basicTypes:
                    method.m_vars[param_type][f'{param_id}{i}'] = Var(address, False, class_id=pt, next=nxt_a, isRef=True)
                    self.define_object_variables(method, False, f'{param_id}{i}', pt, True)
                else:
                    method.m_vars[param_type][f'{param_id}{i}'] = Var(address, False, next=nxt_a, isRef=True)
                method.m_param_addrs[-1].append(address)
        elif param_dim == 2:
            limit2 = self.upperLimits.pop()
            limit = self.upperLimits.pop()
            size = limit * limit2
            m1 = size / limit
            dim = Dim(0, limit - 1, m1)
            dims = [dim]
            m2 = m1 / limit2
            minusK = 0
            dim = Dim(0, limit2 - 1, minusK)
            dims.append(dim)
            refAddr = method.get_address('int')
            method.m_vars['int'][f'rf-{param_id}'] = Var(refAddr, False, dims)
            refAmount = method.get_address('int')
            method.m_vars['int'][f'rfa-{param_id}'] = Var(refAmount, False, dims)
            method.m_param_refs.append([refAddr, refAmount])
            address = method.get_address(param_type)
            nxt_a = None
            if size > 1:
                nxt_a = method.get_address(param_type)
            method.m_param_addrs.append([address])
            if pt not in self.basicTypes:
                method.m_vars[param_type][param_id] = Var(address, False, dims, pt, nxt_a, True)
                self.define_object_variables(method, False, param_id, pt, True)
            else:
                method.m_vars[param_type][param_id] = Var(address, False, dims, next=nxt_a, isRef=True)
            for i in range(1, size):
                address = nxt_a
                nxt_a = method.get_address(param_type)
                if pt not in self.basicTypes:
                    method.m_vars[param_type][f'{param_id}{i}'] = Var(address, False, class_id=pt, next=nxt_a, isRef = True)
                    self.define_object_variables(method, False, f'{param_id}{i}', pt, True)
                else:
                    method.m_vars[param_type][f'{param_id}{i}'] = Var(address, False, next=nxt_a, isRef=True)
                method.m_param_addrs[-1].append(address)
        else:
            address = method.get_address(param_type)
            method.m_param_addrs.append(address)
            if pt not in self.basicTypes:
                method.m_vars[param_type][param_id] = Var(address, False, class_id=pt)
                self.define_object_variables(method, False, param_id, pt)
            else:
                method.m_vars[param_type][param_id] = Var(address, False)
        method.m_param_count += 1
        method.m_param_types.append(param_type)
        # print(param_type)

    def get_var_dir(self, var_type, isGlobal=False):
        if var_type not in self.basicTypes and var_type in self.class_dir:
            var_type = 'Any'
        method_id =  "global" if isGlobal else self.method_stack[-1]
        method = self.meth_dir[method_id] if not self.methodLoc_stack[-1] or method_id == 'global' else self.class_dir[self.class_stack[-1]].methods[method_id]
        var_dir = method.m_vars[var_type]
        return var_dir

    def set_negative(self):
        self.negative = True
    
    def define_object_variables(self, method, isGlobal, objId, objType, isRef=False):
        for key in self.class_dir[objType].attributes:
            cl = self.class_dir[objType]
            a = cl.attributes[key]
            var_dir = self.get_var_dir(a.a_type, isGlobal)
            v_name = objId + '.' + a.a_id
            if a.dims == 1:
                limit = a.dimSizes[0]
                size = limit
                dim = Dim(0, limit - 1, 0)
                dims = [dim]
                address = method.get_address(a.a_type)
                nxt_a = None
                if size > 1:
                    nxt_a = method.get_address(a.a_type)
                var_dir[v_name] = Var(address, isGlobal, dims, next=nxt_a, isRef=isRef)
                method.m_obj_vars_refs[v_name] = [[address], a.a_type, isGlobal, 1, dims]
                for j in range(1, size):
                    address = nxt_a
                    nxt_a = method.get_address(a.a_type) if size > j + 1 else None
                    var_dir[f'{v_name}{j}'] = Var(address, isGlobal, next=nxt_a, isRef=isRef)
                    method.m_obj_vars_refs[v_name][0].append(address)                    
            elif a.dims == 2:
                limit = a.dimSizes[0]
                limit2 = a.dimSizes[1]
                size = limit * limit2
                m1 = size / limit
                dim = Dim(0, limit - 1, m1)
                dims = [dim]
                minusK = 0
                dim = Dim(0, limit2 - 1, minusK)
                dims.append(dim)
                address = method.get_address(a.a_type)
                nxt_a = None
                if size > 1:
                    nxt_a = method.get_address(a.a_type)
                var_dir[v_name] = Var(address, isGlobal, dims, next = nxt_a, isRef=isRef)
                method.m_obj_vars_refs[v_name] = [[address], a.a_type, isGlobal, 2, dims]
                for j in range(1, size):
                    address = nxt_a
                    nxt_a = method.get_address(a.a_type) if size > j + 1 else None
                    var_dir[f'{v_name}{j}'] = Var(address, isGlobal, next=nxt_a, isRef=isRef)
                    method.m_obj_vars_refs[v_name][0].append(address)
            else:
                address = method.get_address(a.a_type)
                var_dir[v_name] = Var(address, isGlobal, isRef=isRef)
                method.m_obj_vars_refs[v_name] = [address, a.a_type, isGlobal, 0]

    # Needs revision for classes
    def define_var(self, v_type):
        vt = v_type
        if v_type not in self.basicTypes and v_type not in self.class_dir:
            raise Exception(f'{v_type} is not a valid type or a previously defined class.')
        elif v_type not in self.basicTypes:
            v_type = 'Any'
        method = self.meth_dir[self.method_stack[-1]] if not self.methodLoc_stack[-1] or self.method_stack[-1] == 'global' else self.class_dir[self.class_stack[-1]].methods[self.method_stack[-1]]
        var_table = method.m_vars
        
        if self.newVar_count > 0:
            while self.newVar_count > 0:
                var = self.operand_stack.pop()
                var_id = var.op_id
                self.newVar_count = self.newVar_count - 1
                if var_id == 'this':
                    raise Exception(f'A variable cannot be named with the keyword "this"')
                for given_type, var_dir in var_table.items():
                    if var_id in var_dir:
                        raise Exception(f"A variable named {var_id} was already defined with type {given_type}")
                else:
                    isGlobal = self.method_stack[-1] == "global"
                    var_dir = self.get_var_dir(v_type, isGlobal)
                    if var.dimensions == 1:
                        limit = self.upperLimits.pop()
                        size = limit
                        dim = Dim(0, limit - 1, 0)
                        dims = [dim]
                        address = method.get_address(v_type)
                        nxt_a = None
                        if size > 1:
                            nxt_a = method.get_address(v_type)
                        if vt not in self.basicTypes:
                            var_dir[var_id] = Var(address, isGlobal, dims, vt, nxt_a)    
                            self.define_object_variables(method, isGlobal, var_id, vt)
                        else:
                            var_dir[var_id] = Var(address, isGlobal, dims, next=nxt_a)
                        for i in range(1, size):
                            address = nxt_a
                            nxt_a = method.get_address(v_type) if size > i + 1 else None
                            if vt not in self.basicTypes:
                                var_dir[f'{var_id}{i}'] = Var(address, isGlobal, class_id=vt, next=nxt_a)
                                self.define_object_variables(method, isGlobal, f'{var_id}{i}', vt)
                            else:
                                var_dir[f'{var_id}{i}'] = Var(address, isGlobal, next=nxt_a)

                    elif var.dimensions == 2:
                        limit = self.upperLimits.pop(-2)
                        limit2 = self.upperLimits.pop()
                        size = limit * limit2
                        m1 = size / limit
                        dim = Dim(0, limit - 1, m1)
                        dims = [dim]
                        m2 = m1 / limit2
                        minusK = 0
                        dim = Dim(0, limit2 - 1, minusK)
                        dims.append(dim)
                        address = method.get_address(v_type)
                        nxt_a = None
                        if size > 1:
                            nxt_a = method.get_address(v_type)
                        if vt not in self.basicTypes:
                            var_dir[var_id] = Var(address, isGlobal, dims, class_id=vt, next=nxt_a)
                            self.define_object_variables(method, isGlobal, var_id, vt)
                        else:
                            var_dir[var_id] = Var(address, isGlobal, dims, next=nxt_a)

                        for i in range(1, size):
                            address = nxt_a
                            nxt_a = method.get_address(v_type) if size > i + 1 else None
                            if vt not in self.basicTypes:
                                var_dir[f'{var_id}{i}'] = Var(address, isGlobal, class_id=vt, next=nxt_a)
                                self.define_object_variables(method, isGlobal, f'{var_id}{i}', vt)
                            else:
                                var_dir[f'{var_id}{i}'] = Var(address, isGlobal, next=nxt_a)
                    else:
                        address = method.get_address(v_type)
                        if vt not in self.basicTypes:
                            var_dir[var_id] = Var(address, isGlobal, class_id=vt)
                            self.define_object_variables(method, isGlobal, var_id, vt)                        
                        else:
                            var_dir[var_id] = Var(address, isGlobal)
        else:
            raise Exception(f"Unknown error at variable declaration of type {vt}.")
    
    def add_limit(self, limit):
        self.upperLimits.append(int(limit))

    def assign_var(self):
        method = self.meth_dir[self.method_stack[-1]] if not self.methodLoc_stack[-1] or self.method_stack[-1] == 'global' else self.class_dir[self.class_stack[-1]].methods[self.method_stack[-1]]
        var_table = method.m_vars
        res = self.operand_stack.pop()
        
        res_type = res.op_type
        left_op = self.operand_stack.pop()
        # print(left_op)
        # print(res)
        left_type = left_op.op_type
        op_type = operation_result_type(left_type, res_type, '=')
        isGlobal = self.method_stack[-1] == 'global'
        self.quad_queue.append(Quadruple('ASSIGN', res, None, left_op))

    def arithmetic_assign(self, op):
        op = op.strip('=')
        if op in ['+', '-', '*', '/']:
            right_oper = self.operand_stack.pop()
            right_type = right_oper.op_type
            left_oper = self.operand_stack.pop()
            left_type = left_oper.op_type
            result_type = operation_result_type(left_type, right_type, op)
            self.quad_queue.append(Quadruple(op, left_oper, right_oper, left_oper))
        else:
            raise Exception(f'Invalid operator: {op} for assignment')

    def add_operand(self, o, dims=0):
        self.operand_stack.append(Operand(o, dimensions=dims))

    def add_op(self, op):
        self.operator_stack.append(op)

    def get_array_item(self, dimensions):
        method = self.meth_dir[self.method_stack[-1]] if not self.methodLoc_stack[-1] or self.method_stack[-1] == 'global' else self.class_dir[self.class_stack[-1]].methods[self.method_stack[-1]]
        myVariables = method.m_vars
        if dimensions == 1:
            row = self.operand_stack.pop()
            id = self.operand_stack.pop().op_id
            for vType, varList in myVariables.items():
                if id in varList:
                    var = varList[id]
                    myType = vType
                    if len(var.dimensions) == 0:
                        raise Exception(f'Variable {id} is not an array')
                    else:
                        myDim = var.dimensions[0]
                        self.operator_stack.append('FakeBottom')
                        self.quad_queue.append(Quadruple('VERIFY', row, myDim.lowerLim, myDim.upperLim))
                        offset = 0
                        address = method.get_address('int')
                        temp_address = Operand(f't{method.m_temp_count}', 'int', address, self.method_stack[-1] == 'global') 
                        method.m_temp_count += 1
                        method.m_temps['int'] += 1
                        self.quad_queue.append(Quadruple('+', row, Operand(var.address, 'int'), temp_address))
                        if var.isRef:
                            self.operand_stack.append(Operand(f'rf-{id}', 'int'))
                            self.get_var()
                            refAddress = self.operand_stack.pop()
                            address = method.get_address('int')
                            actualRefAddress = Operand(f't{method.m_temp_count}', 'int', address, self.method_stack[-1] == 'global')
                            method.m_temp_count += 1
                            method.m_temps['int'] += 1
                            self.quad_queue.append(Quadruple('+', row, refAddress, actualRefAddress))
                            isRef = actualRefAddress
                            self.operand_stack.append(Operand(f'rfa-{id}', 'int'))
                            self.get_var()
                            refAmount = self.operand_stack.pop()
                        else:
                            isRef = False
                            refAmount = False
                        self.operand_stack.append(Operand(f'{id}[{row.op_id}]', myType, temp_address, self.method_stack[-1] == 'global', 1, isRef=isRef, refAmount=refAmount))
                        self.operator_stack.pop() # Eliminates FakeBottom

        elif dimensions == 2:
            col = self.operand_stack.pop()
            row = self.operand_stack.pop()
            id = self.operand_stack.pop().op_id
            for vType, varList in myVariables.items():
                if id in varList:
                    var = varList[id]
                    myType = vType
                    if len(var.dimensions) == 0:
                        raise Exception(f'Variable {id} is not an array')
                    else:
                        myDim = var.dimensions[0]
                        offset = 0
                        self.operator_stack.append('FakeBottom')

                        self.quad_queue.append(Quadruple('VERIFY', row, myDim.lowerLim, myDim.upperLim))
                        address = method.get_address('int')
                        temp_address = Operand(f't{method.m_temp_count}', 'int', address, self.method_stack[-1] == 'global')
                        method.m_temp_count += 1
                        method.m_temps['int'] += 1
                        self.quad_queue.append(Quadruple('*', row, Operand(myDim.m_or_k, 'int'), temp_address))

                        myDim = var.dimensions[1]
                        self.quad_queue.append(Quadruple('VERIFY', col, myDim.lowerLim, myDim.upperLim))
                        aux2 = col
                        aux1 = temp_address
                        address = method.get_address('int')
                        temp_address2 = Operand(f't{method.m_temp_count}', 'int', address, self.method_stack[-1] == 'global')
                        method.m_temp_count += 1
                        method.m_temps['int'] += 1
                        self.quad_queue.append(Quadruple('+', aux1, aux2, temp_address2))

                        aux1 = temp_address2
                        address = method.get_address('int')
                        temp_address = Operand(f't{method.m_temp_count}', 'int', address, self.method_stack[-1] == 'global')
                        method.m_temp_count += 1
                        method.m_temps['int'] += 1
                        self.quad_queue.append(Quadruple('+', aux1, Operand(var.address, 'int'), temp_address))
                        if var.isRef:
                            self.operand_stack.append(Operand(f'rf-{id}', 'int'))
                            self.get_var()
                            refAddress = self.operand_stack.pop()
                            address = method.get_address('int')
                            actualRefAddress = Operand(f't{method.m_temp_count}', 'int', address, self.method_stack[-1] == 'global')
                            method.m_temp_count += 1
                            method.m_temps['int'] += 1
                            self.quad_queue.append(Quadruple('+', aux1, refAddress, actualRefAddress))
                            isRef = actualRefAddress
                            self.operand_stack.append(Operand(f'rfa-{id}', 'int'))
                            self.get_var()
                            refAmount = self.operand_stack.pop()
                        else:
                            isRef = False
                            refAmount = False
                        self.operand_stack.append(Operand(f'{id}[{row.op_id},{col.op_id}]', myType, temp_address, self.method_stack[-1] == 'global', 2, isRef=isRef, refAmount=refAmount))
                        self.operator_stack.pop() # Eliminates FakeBottom

    def get_var(self, fromClass = False):
        if fromClass:
            var = self.operand_stack.pop()
            parentVar = self.operand_stack.pop()
            id = parentVar.op_id + '.' + var.op_id
        else:
            id = self.operand_stack.pop().op_id
        if self.negative:
            id = f'-{id}'
            self.negative = False
        #We first check in the current scope
        method = self.meth_dir[self.method_stack[-1]] if not self.methodLoc_stack[-1] or self.method_stack[-1] == 'global' else self.class_dir[self.class_stack[-1]].methods[self.method_stack[-1]]
        myVariables = method.m_vars
        for vType, varDir in myVariables.items():
            if id in varDir:
                var = varDir[id]
                myType = vType
                isGlobal = self.method_stack[-1] == 'global'
                if var.isRef:
                    self.operand_stack.append(Operand(f'rfa-{id}', 'int'))
                    self.get_var()
                    refAmount = self.operand_stack.pop()
                else:
                    refAmount = False
                self.operand_stack.append(Operand(id, myType, var.address, isGlobal, len(var.dimensions), var.dimensions, var.next, var.isRef, refAmount))
                break
        # If we dont find it, we check the global scope
        else:
            myVariables = self.meth_dir['global'].m_vars
            for vType, varDir in myVariables.items():
                if id in varDir:
                    var = varDir[id]
                    myType = vType
                    if var.isRef:
                        self.operand_stack.append(Operand(f'rfa-{id}', 'int'))
                        self.get_var()
                        refAmount = self.operand_stack.pop()
                    else:
                        refAmount = False
                    self.operand_stack.append(Operand(id, myType, var.address, True, len(var.dimensions), var.dimensions, var.next, var.isRef, refAmount))
                    break
            else:
                raise Exception(f'{id} was not defined.')

    def get_var_obj(self, id):
        method = self.meth_dir[self.method_stack[-1]] if not self.methodLoc_stack[-1] or self.method_stack[-1] == 'global' else self.class_dir[self.class_stack[-1]].methods[self.method_stack[-1]]
        myVariables = method.m_vars
        for vType, varDir in myVariables.items():
            if id in varDir:
                var = varDir[id]
                return var
        # If we dont find it, we check the global scope
        else:
            myVariables = self.meth_dir['global'].m_vars
            for vType, varDir in myVariables.items():
                if id in varDir:
                    var = varDir[id]
                    return var
            else:
                raise Exception(f'{id} was not defined.')

    def arithmetic_operation(self, *ops):
        if self.operator_stack[-1] in ops:
            right_op = self.operand_stack.pop()
            right_type = right_op.op_type
            left_op = self.operand_stack.pop()
            left_type = left_op.op_type
            oper = self.operator_stack.pop()
            result_type = operation_result_type(left_type, right_type, oper)
        
            method_id = self.method_stack[-1]
            method = self.meth_dir[method_id] if not self.methodLoc_stack[-1] or self.method_stack[-1] == 'global' else self.class_dir[self.class_stack[-1]].methods[method_id]
            address = method.get_address(result_type)
            res_op = Operand(f't{method.m_temp_count}', result_type, address, method_id == 'global')
            self.operand_stack.append(res_op)
            self.quad_queue.append(Quadruple(oper, left_op, right_op, res_op))
            method.m_temp_count += 1
            method.m_temps[result_type] += 1
    
    def logic_operation(self, op):
        method_id = self.method_stack[-1]
        method = self.meth_dir[method_id] if not self.methodLoc_stack[-1] or self.method_stack[-1] == 'global' else self.class_dir[self.class_stack[-1]].methods[method_id]
        address = method.get_address('int')
        res_op = Operand(f't{method.m_temp_count}', 'int', address, method_id == 'global')
        if op == 'NOT':
            left_op = self.operand_stack.pop()
            self.operand_stack.append(res_op)
            self.quad_queue.append(Quadruple('NOT', left_op, None, res_op))
        else:
            right_op = self.operand_stack.pop()
            left_op = self.operand_stack.pop()
            self.operand_stack.append(res_op)
            self.quad_queue.append(Quadruple(op, left_op, right_op, res_op))
        
        method.m_temp_count += 1
        method.m_temps['int'] += 1

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

    def add_const(self, val, const_type):
        dir = self.get_var_dir(const_type, isGlobal=True)
        method = self.meth_dir['global']
        address = method.get_address(const_type)
        val = val.strip('"')
        val = val.replace("'", "")
        dir[val] = Var(address, True)
        self.constants[const_type][address] = val
        return address

    def get_const(self, const_id, const_type):
        if self.negative:
            const_id = f'-{const_id}'
            self.negative = False
        dir = self.get_var_dir(const_type, isGlobal=True)
        if const_id not in dir:
            address = self.add_const(const_id, const_type)
        else:
            address = dir[const_id].address        
        self.operand_stack.append(Operand(const_id, const_type, address, True))
    
    def new_write(self):
        self.quad_queue.append(Quadruple("NEWLINE"))
    
    def rtn_stmt(self):
        rtn_op = self.operand_stack.pop()
        if not self.methodLoc_stack[-1] or self.method_stack[-1] == 'global':
            self.quad_queue.append(Quadruple("RETURN", None, Operand(f'{self.method_stack[-1]}'), rtn_op))
        else:
            self.quad_queue.append(Quadruple("RETURN", Operand(self.methodLoc_stack[-1]), Operand(f'{self.method_stack[-1]}'), rtn_op))

    def verify_method(self, id, cl = False):
        if not cl and id not in self.meth_dir:
            raise Exception(f"Method {id} was not declared.")
        elif cl:
            self.parentId = self.operand_stack.pop().op_id
            cl_var = self.get_var_obj(self.parentId)
            clName = cl_var.class_id
            if id in self.class_dir[clName].methods:
                self.currClass = clName;
                return
            else:
                raise Exception(f"Method {id} was not declared in class {clName}.")

    def call_method(self, id, cl = False):
        if cl:
            cl = self.currClass
        method = self.meth_dir[id] if not cl else self.class_dir[cl].methods[id]
        if id == 'read':
            variable = self.operand_stack.pop()
            self.quad_queue.append(Quadruple("READ", None, None, variable))
        elif id == 'write':
            res = self.operand_stack.pop()
            self.quad_queue.append(Quadruple("WRITE", None, None, res))
        else:
            method_id = self.method_stack[-1]
            method_type = method.m_type
            meth = self.meth_dir[method_id] if not self.methodLoc_stack[-1] or self.method_stack[-1] == 'global' else self.class_dir[self.class_stack[-1]].methods[method_id]
            address = None
            rtn_op = None
            # Create temp for return value if not void
            if method_type != 'void':
                address = meth.get_address(method_type)
                meth.m_vars[method_type][f"t{meth.m_temp_count}"] = Var(address)
                rtn_op = Operand(f"t{meth.m_temp_count}", method_type, address, method_id == 'global')
                meth.m_temp_count += 1
                # We dont add this temporal to the count per type because it was already added to var table
            # Use method signature to pass arguments to parameters
            if cl == False:
                self.quad_queue.append(Quadruple("ERA", ans=id))
            else:
                self.quad_queue.append(Quadruple("ERA", [self.methodLoc_stack[-1], self.method_stack[-1], cl, id, self.parentId], Operand(cl), ans=id))
            for i in range(method.m_param_count):
                argument = self.operand_stack.pop()
                if argument.op_type == method.m_param_types[method.m_param_count -1 - i]:
                    self.quad_queue.append(Quadruple("PARAM", argument, None, method.m_param_count -1 - i))
                else:
                    raise Exception(f"Invalid argument at method {id} call")
            if cl:
                count = 1
                for key in self.class_dir[cl].attributes:
                    a = self.class_dir[cl].attributes[key]
                    self.add_operand(f'{self.parentId}.{a.a_id}')
                    self.get_var()
                    arg = self.operand_stack.pop()
                    self.quad_queue.append(Quadruple("MEMBERVAR", arg, None, method.m_member_addrs[f'this.{a.a_id}']))
                    count += 1

            if rtn_op != None:
                self.operand_stack.append(rtn_op)
            
            # GOSUB with the initial address of the method, and the address of the temp to store the return value if not void
            self.quad_queue.append(Quadruple("GOSUB", id, address, method.m_start))

    def fill(self, quad_idx, cont):
        self.quad_queue[quad_idx].ans = cont
        
    def condition(self):
        result = self.operand_stack.pop()
        if (result.op_type != 'int'):
            raise Exception("Unexpected type for condition")
        else:
            self.quad_queue.append(Quadruple("GOTOFALSE", result))
            self.gotos.append(len(self.quad_queue) - 1)

    def end_condition(self):
        end = self.gotos.pop()
        self.fill(end, len(self.quad_queue))

    def else_condition(self):
        self.quad_queue.append(Quadruple("GOTO"))
        false = self.gotos.pop()
        self.gotos.append(len(self.quad_queue) - 1)
        self.fill(false, len(self.quad_queue))

    def while_condition(self):
        self.gotos.append(len(self.quad_queue))

    def while_expression(self):
        result = self.operand_stack.pop()
        if(result.op_type != 'int'):
            raise Exception("Unexpected type for condition")
        else:
            self.quad_queue.append(Quadruple("GOTOFALSE", result))
            self.gotos.append(len(self.quad_queue) - 1)

    def while_end(self):
        end = self.gotos.pop()
        rtn = self.gotos.pop()
        self.quad_queue.append(Quadruple("GOTO", ans=rtn))
        self.fill(end, len(self.quad_queue))

    def floop(self):
        exp = self.operand_stack.pop()
        if (exp.op_type != 'int'):
            raise Exception("Unexpected type for floop loop expression, expected integer")
        else:
            # We dont pop the variable to increase its value later on at the end of iteration
            self.floop_stack.append(self.operand_stack.pop())
            result_type = operation_result_type(self.floop_stack[-1].op_type, exp.op_type, '<=')
            method_id = self.method_stack[-1]
            method = self.meth_dir[method_id] if not self.methodLoc_stack[-1] or self.method_stack[-1] == 'global' else self.class_dir[self.class_stack[-1]].methods[method_id]
            address = method.get_address(result_type)
            res_op = Operand(f't{method.m_temp_count}', result_type, address, method_id == 'global')

            self.operand_stack.append(res_op)
            self.quad_queue.append(Quadruple('<=', self.floop_stack[-1], exp, res_op))
            method.m_temp_count += 1
            method.m_temps[result_type] += 1
            # Set goto for the quadruple where the loop condition is done
            self.gotos.append(len(self.quad_queue) - 1)

    def floop_check(self):
        compare_res = self.operand_stack.pop()
        self.quad_queue.append(Quadruple("GOTOFALSE", compare_res))
        # Set goto for the quadruple to later on fill it
        self.gotos.append(len(self.quad_queue) - 1)

    def floop_end(self):
        false_quad = self.gotos.pop()
        compare_quad = self.gotos.pop()
        var = self.floop_stack.pop()
        # special quadruple to add 1 to the given operand
        self.quad_queue.append(Quadruple("+_1", var, None, var))
        self.quad_queue.append(Quadruple("GOTO", ans=compare_quad))
        self.fill(false_quad, len(self.quad_queue))
    
    def main_method(self):
        self.meth_dir['main'].m_start = len(self.quad_queue)
        # My gotoMain will always be my first quadruple
        gotoMain = 0
        self.fill(gotoMain, self.meth_dir['main'].m_start)

    def save_state(self, parser):
        parser.quad_queue = self.quad_queue
        parser.meth_dir = self.meth_dir
        parser.class_dir = self.class_dir
        parser.constants = self.constants