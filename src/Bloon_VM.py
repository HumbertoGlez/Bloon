from collections import deque

import attr

from tools import operation_result_type

class VirtualMachine():
    quad_queue = []
    meth_dir = {}
    class_dir = {}
    mem = [None]*10000
    mem_stack = [mem]
    t_mem = []
    call_stack = []
    arguments = []
    param_addrs = []
    param_refs = []
    attribute_refs = []
    INT_START = 0
    FLOAT_START = 1500
    CHAR_START = 3000
    STRING_START = 4500
    UNSPECIFIED = 6000
    localInt_start = []
    localFloat_start = []
    localChar_start = []
    localString_start = []
    localUnspecified_start = []
    messages = []
    classAttRefStack = []

    def __init__(self, parser, **kwargs):
        self.quad_queue = parser.quad_queue
        self.meth_dir = parser.meth_dir
        self.class_dir = parser.class_dir
        constants = parser.constants
        # Assign all constants to a memory address upon init
        for const_type, consts in constants.items():
            for address, value in consts.items():
                if const_type == 'int':
                    value = int(value)
                elif const_type == 'float':
                    value = float(value)
                elif const_type == 'string':
                    value = str(value)
                self.register_value(address, value, const_type, True)
    
    def register_value(self, address, value, v_type, isglobal=False, isRef=False, memRef=False, older=False):
        intStart = 0
        floatStart = 0
        charStart = 0
        strStart = 0
        uStart = 0
        if isglobal:
            curr_memory = self.mem_stack[0]
            intStart = self.INT_START
            floatStart = self.FLOAT_START
            charStart = self.CHAR_START
            strStart = self.STRING_START
            uStart = self.UNSPECIFIED
        elif not older:
            curr_memory = self.mem
            intStart = self.localInt_start[-1]
            floatStart = self.localFloat_start[-1]
            charStart = self.localChar_start[-1]
            strStart = self.localString_start[-1]
            uStart = self.localUnspecified_start[-1]
        else:
            curr_memory = self.mem
            intStart = self.localInt_start[-2]
            floatStart = self.localFloat_start[-2]
            charStart = self.localChar_start[-2]
            strStart = self.localString_start[-2]
            uStart = self.localUnspecified_start[-2]
        
        if type(address) is int:
            if v_type == 'int':
                curr_memory[intStart + address] = value
            elif v_type == 'float':
                # print("assigned ", value, " to ", floatStart+address)
                curr_memory[floatStart + address] = value
            elif v_type == 'char':
                curr_memory[charStart + address] = value
            elif v_type == 'string':
                # print("assigned ", value, " to ", strStart+address)
                curr_memory[strStart + address] = value
            elif v_type == 'Any':
                curr_memory[uStart + address] = address
        else:
            if v_type == 'int':
                curr_memory[intStart + self.get_value(address.op_addr, 'int', address.isGlobal)] = value
            elif v_type == 'float':
                curr_memory[floatStart + self.get_value(address.op_addr, 'int', address.isGlobal)] = value
            elif v_type == 'char':
                curr_memory[charStart + self.get_value(address.op_addr, 'int', address.isGlobal)] = value
            elif v_type == 'string':
                curr_memory[strStart + self.get_value(address.op_addr, 'int', address.isGlobal)] = value
            elif v_type == 'Any':
                curr_memory[uStart + self.get_value(address.op_addr, 'int', address.isGlobal)] = address

        if isRef:
            memRef = self.get_value(memRef.op_addr, memRef.op_type, memRef.isGlobal)
            curr_memory = self.mem_stack[memRef]
            intStart = self.INT_START if len(self.mem_stack) == 2 else self.localInt_start[memRef]
            floatStart = self.FLOAT_START if len(self.mem_stack) == 2 else self.localFloat_start[memRef]
            charStart = self.CHAR_START if len(self.mem_stack) == 2 else self.localChar_start[memRef]
            strStart = self.STRING_START if len(self.mem_stack) == 2 else self.localString_start[memRef]
            uStart = self.UNSPECIFIED if len(self.mem_stack) == 2 else self.localUnspecified_start[memRef]

            if v_type == 'int':
                curr_memory[intStart + self.get_value(isRef.op_addr, isRef.op_type, isRef.isGlobal)] = value
            elif v_type == 'float':
                # print("assigned ", value, " to ", floatStart+address)
                curr_memory[floatStart + self.get_value(isRef.op_addr, isRef.op_type, isRef.isGlobal)] = value
            elif v_type == 'char':
                curr_memory[charStart + self.get_value(isRef.op_addr, isRef.op_type, isRef.isGlobal)] = value
            elif v_type == 'string':
                # print("assigned ", value, " to ", strStart+address)
                curr_memory[strStart + self.get_value(isRef.op_addr, isRef.op_type, isRef.isGlobal)] = value
            elif v_type == 'Any':
                curr_memory[uStart + self.get_value(isRef.op_addr, isRef.op_type, isRef.isGlobal)] = self.get_value(isRef.op_addr, isRef.op_type, isRef.isGlobal)

    def get_value(self, address, v_type, isglobal=False, dims=False, older=False):
        intStart = 0
        floatStart = 0
        charStart = 0
        strStart = 0
        uStart = 0
        if isglobal:
            curr_memory = self.mem_stack[0]
            intStart = self.INT_START
            floatStart = self.FLOAT_START
            charStart = self.CHAR_START
            strStart = self.STRING_START
            uStart = self.UNSPECIFIED
        elif not older:
            curr_memory = self.mem
            intStart = self.localInt_start[-1]
            floatStart = self.localFloat_start[-1]
            charStart = self.localChar_start[-1]
            strStart = self.localString_start[-1]
            uStart = self.localUnspecified_start[-1]
        else:
            curr_memory = self.mem
            intStart = self.localInt_start[-2]
            floatStart = self.localFloat_start[-2]
            charStart = self.localChar_start[-2]
            strStart = self.localString_start[-2]
            uStart = self.localUnspecified_start[-2]
        
        if type(address) is int:
            if v_type == 'int':
                return curr_memory[intStart + address]
            elif v_type == 'float':
                # print(floatStart + address, " has the value: ", curr_memory[floatStart + address])
                return curr_memory[floatStart + address]
            elif v_type == 'char':
                return curr_memory[charStart + address]
            elif v_type == 'string':
                # print( address, " has the value: ", curr_memory[strStart + address])
                return curr_memory[strStart + address]
            elif v_type == 'Any':
                return curr_memory[uStart + address]
        else:
            if v_type == 'int':
                # print("value =",curr_memory[intStart + self.get_value(address.op_addr, 'int', address.isGlobal)])
                # print(intStart + self.get_value(address.op_addr, 'int', address.isGlobal))
                return curr_memory[intStart + self.get_value(address.op_addr, 'int', address.isGlobal)]
            elif v_type == 'float':
                # print("value =",curr_memory[floatStart + self.get_value(address.op_addr, 'int', address.isGlobal)])
                return curr_memory[floatStart + self.get_value(address.op_addr, 'int', address.isGlobal)]
            elif v_type == 'char':
                return curr_memory[charStart + self.get_value(address.op_addr, 'int', address.isGlobal)]
            elif v_type == 'string':
                return curr_memory[strStart + self.get_value(address.op_addr, 'int', address.isGlobal)]
            elif v_type == 'Any':
                return curr_memory[uStart + self.get_value(address.op_addr, 'int', address.isGlobal)]


    def write(self, operand):
        value = self.get_value(operand.op_addr, operand.op_type, operand.isGlobal) if operand.dimensions == 0 else self.get_value(operand.op_addr, operand.op_type, operand.isGlobal, operand.dimensions)
        print(value, end ="")

    def read(self, operand):
        value = input("Enter value to read: ")
        if operand.op_type != 'string' and operand.op_type != 'char':
            if operand.op_type == 'int':
                try:
                    val = int(value)
                    if operand.dimensions == 0:
                        self.register_value(operand.op_addr, val, operand.op_type, operand.isGlobal) 
                    else: 
                        self.register_value(operand.op_addr, val, operand.op_type, operand.isGlobal, isRef=operand.isRef, memRef=operand.refAmount)
                except ValueError:
                    raise Exception(f"Invalid input to read for variable of type {operand.op_type}")
            elif operand.op_type == 'float':
                try:
                    val = float(value)
                    if operand.dimensions == 0:
                        self.register_value(operand.op_addr, val, operand.op_type, operand.isGlobal) 
                    else: 
                        self.register_value(operand.op_addr, val, operand.op_type, operand.isGlobal, isRef=operand.isRef, memRef=operand.refAmount)
                except ValueError:
                    raise Exception(f"Invalid input to read for variable of type {operand.op_type}")
        else:  
            val = f'{value}'
            if operand.dimensions == 0:
                self.register_value(operand.op_addr, val, operand.op_type, operand.isGlobal) 
            else: 
                self.register_value(operand.op_addr, val, operand.op_type, operand.isGlobal, isRef=operand.isRef, memRef=operand.refAmount)

    def operation(self, left, right, op):
        # CHECK FOR TYPE
        type_left_str = left.op_type == 'string'
        type_right_str = right.op_type == 'string'

        type_left_char = left.op_type == 'char'
        type_right_char = right.op_type == 'char'

        left_v = None
        right_v = None
        # print(left.op_id , ', ', right.op_id)
        if left.op_addr == None and left.op_type == 'int':
            left_v = int(float(left.op_id))
        elif left.dimensions == 0:
            left_v = self.get_value(left.op_addr, left.op_type, left.isGlobal) 
        else:
            left_v = self.get_value(left.op_addr, left.op_type, left.isGlobal, left.dimensions)

        if right.op_addr == None and right.op_type == 'int':
            right_v = int(float(right.op_id))
        elif right.dimensions == 0:
            right_v = self.get_value(right.op_addr, right.op_type, right.isGlobal) 
        else:
            right_v = self.get_value(right.op_addr, right.op_type, right.isGlobal, right.dimensions)
        # print("l: ",left_v, "r: ", right_v)
        if left_v == None:
            raise Exception(f'Unassigned variable: {left.op_id}')
        elif right_v == None:
            raise Exception(f'Unassigned variable: {right.op_id}')
        if op == 'add':
            if type_left_char:
                if right.op_type == 'int':
                    return ord(left_v) + right_v
                elif type_right_char:
                    return ord(left_v) + ord(right_v)
                elif right.op_type == 'float':
                    return ord(left_v) + right_v
            elif type_right_char:
                if left.op_type == 'int':
                    return left_v + ord(right_v)
                elif type_left_char:
                    return ord(left_v) + ord(right_v)
                elif left.op_type == 'float':
                    return left_v + ord(right_v)
            else:
                return left_v + right_v
        elif op == 'sub':
            if type_left_char:
                if right.op_type == 'int':
                    return ord(left_v) - right_v
                elif type_right_char:
                    return ord(left_v) - ord(right_v)
                elif right.op_type == 'float':
                    return ord(left_v) - right_v
            elif type_right_char:
                if left.op_type == 'int':
                    return left_v - ord(right_v)
                elif type_left_char:
                    return ord(left_v) - ord(right_v)
                elif left.op_type == 'float':
                    return left_v - ord(right_v)
            else:
                return left_v - right_v
        elif op == 'mul':
            if type_left_char:
                if right.op_type == 'int':
                    return ord(left_v) * right_v
                elif type_right_char:
                    return ord(left_v) * ord(right_v)
                elif right.op_type == 'float':
                    return ord(left_v) * right_v
            elif type_right_char:
                if left.op_type == 'int':
                    return left_v * ord(right_v)
                elif type_left_char:
                    return ord(left_v) * ord(right_v)
                elif left.op_type == 'float':
                    return left_v * ord(right_v)
            else:
                return left_v * right_v
        elif op == 'div':
            if type_left_char:
                if right.op_type == 'int':
                    return ord(left_v) / right_v
                elif type_right_char:
                    return ord(left_v) / ord(right_v)
                elif right.op_type == 'float':
                    return ord(left_v) / right_v
            elif type_right_char:
                if left.op_type == 'int':
                    return left_v / ord(right_v)
                elif type_left_char:
                    return ord(left_v) / ord(right_v)
                elif left.op_type == 'float':
                    return left_v / ord(right_v)
            else:
                return left_v / right_v
        elif op == 'gt':
            if type_left_char:
                if right.op_type == 'int':
                    return ord(left_v) > right_v
                elif type_right_char:
                    return ord(left_v) > ord(right_v)
                elif right.op_type == 'float':
                    return ord(left_v) > right_v
            elif type_right_char:
                if left.op_type == 'int':
                    return left_v > ord(right_v)
                elif type_left_char:
                    return ord(left_v) > ord(right_v)
                elif left.op_type == 'float':
                    return left_v > ord(right_v)
            else:
                return left_v > right_v
        elif op == 'ge':
            if type_left_char:
                if right.op_type == 'int':
                    return ord(left_v) >= right_v
                elif type_right_char:
                    return ord(left_v) >= ord(right_v)
                elif right.op_type == 'float':
                    return ord(left_v) >= right_v
            elif type_right_char:
                if left.op_type == 'int':
                    return left_v >= ord(right_v)
                elif type_left_char:
                    return ord(left_v) >= ord(right_v)
                elif left.op_type == 'float':
                    return left_v >= ord(right_v)
            else:
                return left_v >= right_v
        elif op == 'lt':
            if type_left_char:
                if right.op_type == 'int':
                    return ord(left_v) < right_v
                elif type_right_char:
                    return ord(left_v) < ord(right_v)
                elif right.op_type == 'float':
                    return ord(left_v) < right_v
            elif type_right_char:
                if left.op_type == 'int':
                    return left_v < ord(right_v)
                elif type_left_char:
                    return ord(left_v) < ord(right_v)
                elif left.op_type == 'float':
                    return left_v < ord(right_v)
            else:
                return left_v < right_v
        elif op == 'le':
            if type_left_char:
                if right.op_type == 'int':
                    return ord(left_v) <= right_v
                elif type_right_char:
                    return ord(left_v) <= ord(right_v)
                elif right.op_type == 'float':
                    return ord(left_v) <= right_v
            elif type_right_char:
                if left.op_type == 'int':
                    return left_v <= ord(right_v)
                elif type_left_char:
                    return ord(left_v) <= ord(right_v)
                elif left.op_type == 'float':
                    return left_v <= ord(right_v)
            else:
                return left_v <= right_v
        elif op == 'eq':
            if type_left_char:
                if right.op_type == 'int':
                    return ord(left_v) == right_v
                elif type_right_char:
                    return ord(left_v) == ord(right_v)
                elif right.op_type == 'float':
                    return ord(left_v) == right_v
            elif type_right_char:
                if left.op_type == 'int':
                    return left_v == ord(right_v)
                elif type_left_char:
                    return ord(left_v) == ord(right_v)
                elif left.op_type == 'float':
                    return left_v == ord(right_v)
            else:
                # print (left_v, " == ", right_v, " = ", left_v == right_v)
                return left_v == right_v
        elif op == 'ne':
            if type_left_char:
                if right.op_type == 'int':
                    return ord(left_v) != right_v
                elif type_right_char:
                    return ord(left_v) != ord(right_v)
                elif right.op_type == 'float':
                    return ord(left_v) != right_v
            elif type_right_char:
                if left.op_type == 'int':
                    return left_v != ord(right_v)
                elif type_left_char:
                    return ord(left_v) != ord(right_v)
                elif left.op_type == 'float':
                    return left_v != ord(right_v)
            else:
                return left_v != right_v
        elif op == 'mod':
            if type_left_char:
                if right.op_type == 'int':
                    return ord(left_v) % right_v
                elif type_right_char:
                    return ord(left_v) % ord(right_v)
                elif right.op_type == 'float':
                    return ord(left_v) % right_v
            elif type_right_char:
                if left.op_type == 'int':
                    return left_v % ord(right_v)
                elif type_left_char:
                    return ord(left_v) % ord(right_v)
                elif left.op_type == 'float':
                    return left_v % ord(right_v)
            else:
                return left_v % right_v

        # Validation was already done on the compiler
    def do_operation(self, op, quad):
        left_op = quad.left_op
        
        right_op = quad.right_op
       
        res_op = quad.ans
        if res_op.op_type == 'int':
            ans = int(self.operation(left_op, right_op, op))
            # print(f'{left_op.op_id}' + ' ' + f'{op}' + ' ' + f'{right_op.op_id}' + ' = ' + f'{ans}')
        elif res_op.op_type == 'float':
            ans = float(self.operation(left_op, right_op, op))
        else:
            ans = self.operation(left_op, right_op, op)
        # print(op, left_op, right_op, " = ", ans)
        if res_op.dimensions == 0:
            self.register_value(res_op.op_addr, ans, res_op.op_type, res_op.isGlobal)
        else: 
            self.register_value(res_op.op_addr, ans, res_op.op_type, res_op.isGlobal, isRef=res_op.isRef, memRef=res_op.refAmount)
    
    def do_logical(self, op, quad):
        left_op = quad.left_op
        res_op = quad.ans
        if op == 'AND':
            right_op = quad.right_op
            ans = int(self.get_value(left_op.op_addr, left_op.op_type, left_op.isGlobal) and self.get_value(right_op.op_addr, right_op.op_type, right_op.isGlobal))
        elif op == 'OR':
            right_op = quad.right_op
            ans = int(self.get_value(left_op.op_addr, left_op.op_type, left_op.isGlobal) or self.get_value(right_op.op_addr, right_op.op_type, right_op.isGlobal))
        elif op == 'NOT':
            ans = int(not self.get_value(left_op.op_addr, left_op.op_type, left_op.isGlobal))
        else:
            raise Exception("Invalid operation type")
        self.register_value(res_op.op_addr, ans, res_op.op_type, res_op.isGlobal, isRef=res_op.isRef, memRef=res_op.refAmount)
    
    def era(self, m_id, cl = None):
        if cl == None:
            localVarTable = self.meth_dir[m_id].m_vars
            tempCounts = self.meth_dir[m_id].m_temps
            method = self.meth_dir[m_id]
        else:
            localVarTable = self.class_dir[cl].methods[m_id].m_vars
            tempCounts = self.class_dir[cl].methods[m_id].m_temps
            method = self.class_dir[cl].methods[m_id]
        intCount = len(localVarTable['int']) + tempCounts['int']
        flCount = len(localVarTable['float']) + tempCounts['float']
        charCount = len(localVarTable['char']) + tempCounts['char']
        strCount = len(localVarTable['string']) + tempCounts['string']
        uCount = len(localVarTable['Any']) + tempCounts['Any']
        if intCount + flCount + charCount + strCount + uCount > 10000:
            raise Exception(f'Stack overflow, memory limit exceeded for method {m_id}')
        self.localInt_start.append(0)
        self.localFloat_start.append(intCount)
        self.localChar_start.append(intCount + flCount)
        self.localString_start.append(intCount + flCount + charCount)
        self.localUnspecified_start.append(intCount + flCount + charCount + strCount)
        # save previous memory in t_mem
        self.t_mem = self.mem
        # Create memory with just the needed addresses
        self.mem = [None]*(intCount + flCount + charCount + strCount + uCount)
        self.messages.append("Created local memory with " + str(intCount + flCount + charCount + strCount + uCount) + " spaces.")
        self.param_addrs = method.m_param_addrs
        self.param_refs = method.m_param_refs
        self.attribute_refs = method.m_member_addrs
    
    def param(self, arg, argNum):
        new_mem = self.mem
        p_local_address = self.param_addrs[argNum]
        self.mem = self.t_mem
        if arg.dimensions == 0:
            p_value = self.get_value(arg.op_addr, arg.op_type, arg.isGlobal, older=True) 
            self.mem = new_mem
            self.register_value(p_local_address, p_value, arg.op_type)
        elif arg.dimensions == 1:
            self.mem = new_mem
            self.register_value(self.param_refs[argNum][0], arg.op_addr, 'int')
            if arg.refAmount:
                self.mem = self.t_mem
                amount = self.get_value(arg.refAmount.op_addr, arg.refAmount.op_type, arg.refAmount.isGlobal)
                # print("Saved ref to:",amount)
                self.mem = new_mem
                self.register_value(self.param_refs[argNum][1], amount, 'int')
            else:
                # print("Saved ref to:",self.mem_stack.index(self.t_mem))
                self.register_value(self.param_refs[argNum][1], self.mem_stack.index(self.t_mem), 'int')
            self.mem = self.t_mem
            for i in range(arg.dims[0].upperLim + 1):
                p_value = self.get_value(arg.op_addr + i, arg.op_type, arg.isGlobal, older=True)
                self.mem = new_mem
                self.register_value(p_local_address[i], p_value, arg.op_type)
                self.mem = self.t_mem
            self.mem = new_mem
        elif arg.dimensions == 2:
            self.mem = new_mem
            self.register_value(self.param_refs[argNum][0], arg.op_addr, 'int')
            if arg.refAmount:
                self.mem = self.t_mem
                amount = self.get_value(arg.refAmount.op_addr, arg.refAmount.op_type, arg.refAmount.isGlobal)
                # print("Saved ref to:",amount)
                self.mem = new_mem
                self.register_value(self.param_refs[argNum][1], amount, 'int')
            else:
                # print("Saved ref to:",self.mem_stack.index(self.t_mem))
                self.register_value(self.param_refs[argNum][1], self.mem_stack.index(self.t_mem), 'int')
            self.mem = self.t_mem
            for i in range((arg.dims[0].upperLim + 1) * (arg.dims[1].upperLim + 1)):
                p_value = self.get_value(arg.op_addr+i, arg.op_type, arg.isGlobal, older=True)
                self.mem = new_mem
                self.register_value(p_local_address[i], p_value, arg.op_type)
                self.mem = self.t_mem
            self.mem = new_mem
    
    def memberVar(self, att, l_address):
        new_mem = self.mem
        # l_address = self.attribute_refs[attrNum]
        self.mem = self.t_mem

        if att.dimensions == 0:
            p_value = self.get_value(att.op_addr, att.op_type, att.isGlobal, older=True)
            # print("value:",p_value)
            self.mem = new_mem
            # print("Registering at address", l_address, "type", att.op_type)
            self.register_value(l_address, p_value, att.op_type)
        elif att.dimensions == 1:
            for i in range(att.dims[0].upperLim + 1):
                p_value = self.get_value(att.op_addr + i, att.op_type, att.isGlobal, older=True)
                self.mem = new_mem
                self.register_value(l_address[i], p_value, att.op_type)
                self.mem = self.t_mem
            self.mem = new_mem
            
        elif att.dimensions == 2:
            for i in range((att.dims[0].upperLim + 1) * (att.dims[1].upperLim + 1)):
                p_value = self.get_value(att.op_addr+i, att.op_type, att.isGlobal, older=True)
                self.mem = new_mem
                self.register_value(l_address[i], p_value, att.op_type)
                self.mem = self.t_mem
            self.mem = new_mem
    
    def rtn_stmt(self, res, m_type):
        val = self.get_value(res.op_addr, res.op_type, res.isGlobal)
        if val is None:
            return
        goSub = self.call_stack[-1] - 1
        r_addr = self.quad_queue[goSub].right_op
        curr_memory = self.mem_stack[-2]
        intStart = self.INT_START if len(self.mem_stack) == 2  else self.localInt_start[-1]
        flStart = self.FLOAT_START if len(self.mem_stack) == 2  else self.localFloat_start[-1]
        charStart = self.CHAR_START if len(self.mem_stack) == 2  else self.localChar_start[-1]
        strStart = self.STRING_START if len(self.mem_stack) == 2  else self.localString_start[-1]
        uStart = self.UNSPECIFIED if len(self.mem_stack) == 2  else self.localUnspecified_start[-1]
        if m_type == 'int':
            curr_memory[intStart + r_addr] = int(val)
        elif m_type == 'float':
            curr_memory[flStart + r_addr] = float(val)
        elif m_type == 'char':
            curr_memory[charStart + r_addr] = val
        elif m_type == 'string':
            curr_memory[strStart + r_addr] = str(val)
        elif m_type == 'any':
            curr_memory[uStart + r_addr] = val
    
    def save_attributes(self):
        expiring_mem = self.mem
        returning_mem = self.t_mem
        # l_address = self.attribute_refs[attrNum]
        # self.mem = self.t_mem
        ownerMethod = self.meth_dir[self.classAttRefStack[-1][1]] if not self.classAttRefStack[-1][0] else self.class_dir[self.classAttRefStack[-1][0]].methods[self.classAttRefStack[-1][1]]
        expiringMethod = self.class_dir[self.classAttRefStack[-1][2]].methods[self.classAttRefStack[-1][3]]
        ownerId = self.classAttRefStack[-1][4]
        # if not self.classAttRefStack[-1][0] and self.classAttRefStack[-1][1] == 'global':
        #     isGlobal = True
        # else:
        #     isGlobal = False
        for key in expiringMethod.m_member_addrs:
            if key == 'this':
                continue
            address = expiringMethod.m_member_addrs[key]
            member_type = expiringMethod.m_member_data[key][0]
            member_dims = expiringMethod.m_member_data[key][1]
            keyWithoutThis = key.replace('this', '')
            if ownerId != 'this':
                toSaveRefs = ownerMethod.m_obj_vars_refs[f'{ownerId}{keyWithoutThis}']
                if member_dims == 0:
                    p_value = self.get_value(address, member_type, False)
                    # print("value for", key, member_type, "at", address, "in meth:",p_value)
                    self.mem = returning_mem
                    # print("Registering at address", toSaveRefs[0], "type", toSaveRefs[1])
                    self.register_value(toSaveRefs[0], p_value, toSaveRefs[1], toSaveRefs[2], older=True)
                    self.mem = expiring_mem
                elif member_dims == 1:
                    for i in range(toSaveRefs[4][0].upperLim + 1):
                        p_value = self.get_value(address[i], member_type, False)
                        self.mem = returning_mem
                        self.register_value(toSaveRefs[0][i], p_value, toSaveRefs[1], toSaveRefs[2], older=True)
                        self.mem = expiring_mem
                elif member_dims == 2:
                    for i in range((toSaveRefs[4][0].upperLim + 1) * (toSaveRefs[4][1].upperLim + 1)):
                        p_value = self.get_value(address[i], member_type, False)
                        self.mem = returning_mem
                        self.register_value(toSaveRefs[0][i], p_value, toSaveRefs[1], toSaveRefs[2], older=True)
                        self.mem = expiring_mem
            else:
                om_address = ownerMethod.m_member_addrs[key]
                om_data = ownerMethod.m_member_data[key]
                if member_dims == 0:
                    p_value = self.get_value(address, member_type, False)
                    self.mem = returning_mem
                    self.register_value(om_address, p_value, om_data[0], False, older=True)
                    self.mem = expiring_mem
                elif member_dims == 1:
                    for i in range(om_data[2][0].upperLim + 1):
                        p_value = self.get_value(address[i], member_type, False)
                        self.mem = returning_mem
                        self.register_value(om_address[i], p_value, om_data[0], False, older=True)
                        self.mem = expiring_mem
                elif member_dims == 2:
                    for i in range((om_data[2][0].upperLim + 1) * (om_data[2][1].upperLim + 1)):
                        p_value = self.get_value(address[i], member_type, False)
                        self.mem = returning_mem
                        self.register_value(om_address[i], p_value, om_data[0], False, older=True)
                        self.mem = expiring_mem
        self.classAttRefStack.pop()

    def run(self):
        q = 0
        # uncomment to print generated quadruples
        # for i, quad in enumerate(self.quad_queue):
        #    print(i, quad)
        
        while q < len(self.quad_queue):
            quad = self.quad_queue[q]
            if quad.operator == 'ASSIGN':
                value_op = quad.left_op
                value = self.get_value(value_op.op_addr, value_op.op_type, value_op.isGlobal) if value_op.dimensions == 0 else self.get_value(value_op.op_addr, value_op.op_type, value_op.isGlobal, value_op.dimensions)
                result = quad.ans
                self.register_value(result.op_addr, value, result.op_type, result.isGlobal) if not result.isRef else self.register_value(result.op_addr, value, result.op_type, result.isGlobal, isRef=result.isRef, memRef=result.refAmount)
            elif quad.operator == 'WRITE':
                self.write(quad.ans)
            elif quad.operator == 'NEWLINE':
                print()
            elif quad.operator == 'READ':
                self.read(quad.ans)
            elif quad.operator == 'GOTO':
                q = quad.ans
                continue
            elif quad.operator == 'GOTOFALSE':
                value_op = quad.left_op
                value = self.get_value(value_op.op_addr, value_op.op_type, value_op.isGlobal) if value_op.dimensions == 0 else self.get_value(value_op.op_addr, value_op.op_type, value_op.isGlobal, value_op.dimensions)
                if value == False:
                    q = quad.ans
                    continue
            elif quad.operator == 'ERA':
                if quad.left_op:
                    self.classAttRefStack.append(quad.left_op)
                self.era(quad.ans) if quad.right_op == None else self.era(quad.ans, quad.right_op.op_id)
            elif quad.operator == 'PARAM':
                self.param(quad.left_op, quad.ans)
            elif quad.operator == 'MEMBERVAR':
                self.memberVar(quad.left_op, quad.ans)
            elif quad.operator == 'GOSUB':
                # add new memory to stack
                self.mem_stack.append(self.mem)
                # clear param refs
                self.param_addrs = []
                self.param_refs = []
                self.attribute_refs = []
                self.call_stack.append(q + 1)
                q = quad.ans
                continue
            elif quad.operator == 'RETURN':
                # Check if method is from a class
                if quad.left_op == None:
                    self.rtn_stmt(quad.ans, self.meth_dir[quad.right_op.op_id].m_type)
                    q = self.meth_dir[quad.right_op.op_id].m_end
                else:
                    self.rtn_stmt(quad.ans, self.class_dir[quad.left_op.op_id].methods[quad.right_op.op_id].m_type)
                    q = self.class_dir[quad.left_op.op_id].methods[quad.right_op.op_id].m_end
                continue
            elif quad.operator == 'ENDMETH':
                # Remove local memory from the top of mem_stack
                # for i in self.mem_stack[-1]:
                #     print(i)
                if quad.ans == 'cl':
                    self.save_attributes()
                self.mem_stack.pop()
                self.localInt_start.pop()
                self.localFloat_start.pop()
                self.localChar_start.pop()
                self.localString_start.pop()
                self.localUnspecified_start.pop()
                q = self.call_stack.pop()
                # Set memory to last memory in stack
                self.mem = self.mem_stack[-1]
                self.messages.append("Removed local memory.")
                continue
            elif quad.operator == 'VERIFY':
                index = self.get_value(quad.left_op.op_addr, quad.left_op.op_type, quad.left_op.isGlobal)
                lower_lim = quad.right_op
                upper_lim = quad.ans
                # print(index)
                if index < lower_lim or index > upper_lim:
                    raise Exception(f'Index {index} out of bounds {lower_lim}, {upper_lim}.')
            elif quad.operator == 'AND':
                self.do_logical('AND', quad)
            elif quad.operator == 'OR':
                self.do_logical('OR', quad)
            elif quad.operator == 'NOT':
                self.do_logical('NOT', quad)
            elif quad.operator == '+':
                self.do_operation('add', quad) 
            elif quad.operator == '-':
                self.do_operation('sub', quad) 
            elif quad.operator == '*':
                self.do_operation('mul', quad) 
            elif quad.operator == '/':
                self.do_operation('div', quad)
            elif quad.operator == '%':
                self.do_operation('mod', quad)
            elif quad.operator == '>':
                self.do_operation('gt', quad) 
            elif quad.operator == '>=':
                self.do_operation('ge', quad) 
            elif quad.operator == '<':
                self.do_operation('lt', quad) 
            elif quad.operator == '<=':
                self.do_operation('le', quad) 
            elif quad.operator == '==':
                self.do_operation('eq', quad) 
            elif quad.operator == '!=':
                self.do_operation('ne', quad)
            elif quad.operator == '+_1':
                value_op = quad.left_op
                value = self.get_value(value_op.op_addr, value_op.op_type, value_op.isGlobal) if value_op.dimensions == 0 else self.get_value(value_op.op_addr, value_op.op_type, value_op.isGlobal, value_op.dimensions)
                value += 1
                ans_op = quad.ans
                self.register_value(ans_op.op_addr, value, ans_op.op_type, ans_op.isGlobal) if not ans_op.isRef else self.register_value(ans_op.op_addr, value, ans_op.op_type, ans_op.isGlobal, isRef=ans_op.isRef, memRef=ans_op.refAmount)
            q += 1
        
        print("\nFinished execution...")
        # if len(self.messages) > 0:
        #     print("Important execution logs:")
        # for i in range(len(self.messages)):
        #     print(self.messages[i])