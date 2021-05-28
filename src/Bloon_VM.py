from collections import deque

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
    param_refs = []
    attribute_refs = []
    INT_START = 0
    FLOAT_START = 250
    CHAR_START = 500
    STRING_START = 750
    UNSPECIFIED = 1000
    localInt_start = []
    localFloat_start = []
    localChar_start = []
    localString_start = []
    localUnspecified_start = []
    messages = []

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
    
    def register_value(self, address, value, v_type, isglobal=False, dims=False):
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
        else:
            curr_memory = self.mem
            intStart = self.localInt_start[-1]
            floatStart = self.localFloat_start[-1]
            charStart = self.localChar_start[-1]
            strStart = self.localString_start[-1]
            uStart = self.localUnspecified_start[-1]
        
        if v_type == 'int':
            curr_memory[intStart + address] = value
        elif v_type == 'float':
            curr_memory[floatStart + address] = value
        elif v_type == 'char':
            curr_memory[charStart + address] = value
        elif v_type == 'string':
            curr_memory[strStart + address] = value
        elif v_type == 'Any':
            curr_memory[uStart + address] = address
    
    def get_value(self, address, v_type, isglobal=False, dims=False):
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
        else:
            curr_memory = self.mem
            intStart = self.localInt_start[-1]
            floatStart = self.localFloat_start[-1]
            charStart = self.localChar_start[-1]
            strStart = self.localString_start[-1]
            uStart = self.localUnspecified_start[-1]
        
        if v_type == 'int':
            return curr_memory[intStart + address]
        elif v_type == 'float':
            return curr_memory[floatStart + address]
        elif v_type == 'char':
            return curr_memory[charStart + address]
        elif v_type == 'string':
            return curr_memory[strStart + address]
        elif v_type == 'Any':
            return curr_memory[uStart + address]

    def write(self, operand):
        value = self.get_value(operand.op_addr, operand.op_type, operand.isGlobal) if operand.dimensions == 0 else self.get_value(operand.op_addr, operand.op_type, operand.isGlobal, operand.dimensions)
        print(value, end ="")

    def read(self, operand):
        value = input("Enter value to read: ")
        if operand.op_type != 'string' or operand.op_type != 'char':
            if operand.op_type == 'int':
                try:
                    val = int(value)
                    if operand.dimensions == 0:
                        self.register_value(operand.op_addr, val, operand.op_type, operand.isGlobal) 
                    else: 
                        self.register_value(operand.op_addr, val, operand.op_type, operand.isGlobal, operand.dimensions)
                except ValueError:
                    raise Exception(f"Invalid input to read for variable of type {operand.op_type}")
            elif operand.op_type == 'float':
                try:
                    val = float(value)
                    self.register_value(operand.op_addr, val, operand.op_type, operand.isGlobal) if operand.dimensions == 0 else self.register_value(operand.op_addr, val, operand.op_type, operand.isGlobal, operand.dimensions)
                except ValueError:
                    raise Exception(f"Invalid input to read for variable of type {operand.op_type}")
        else:
            self.register_value(operand.op_addr, value, operand.op_type, operand.isGlobal) if operand.dimensions == 0 else self.register_value(operand.op_addr, value, operand.op_type, operand.isGlobal, operand.dimensions)

    def operation(self, left, right, op):
        # CHECK FOR TYPE
        type_left_str = left.op_type == 'string'
        type_right_str = right.op_type == 'string'

        type_left_char = left.op_type == 'char'
        type_right_char = right.op_type == 'char'

        left_v = None
        right_v = None
        # print(left.op_id + ', ' + right.op_id)
        if left.op_addr == None and left.op_type == 'int':
            left_v = int(float(right.op_id))
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

        if left_v == None:
            raise Exception(f'Undefined variable: {left.op_id}')
        elif right_v == None:
            raise Exception(f'Undefined variable: {right.op_id}')

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
        if res_op.dimensions == 0:
            self.register_value(res_op.op_addr, ans, res_op.op_type, res_op.isGlobal)
        else: 
            self.register_value(res_op.op_addr, ans, res_op.op_type, res_op.isGlobal, res_op.dimensions)
    
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
        self.param_refs = method.m_param_addrs
        self.attribute_refs = method.m_member_addrs
    
    def param(self, arg, argNum):
        new_mem = self.mem
        p_local_address = self.param_refs[argNum]
        self.mem = self.t_mem
        if arg.dimensions == 0:
            p_value = self.get_value(arg.op_addr, arg.op_type, arg.isGlobal) 
            self.mem = new_mem
            self.register_value(p_local_address, p_value, arg.op_type)
        elif arg.dimensions == 1: 
            for i in range(arg.dims[0].upperLim + 1):
                p_value = self.get_value(arg.op_addr + i, arg.op_type, arg.isGlobal)
                self.mem = new_mem
                self.register_value(p_local_address + i, p_value, arg.op_type)
                self.mem = self.t_mem
            self.mem = new_mem
            
        elif arg.dimensions == 2:
            for i in range((arg.dims[0].upperLim + 1) * (arg.dims[1].upperLim + 1)):
                p_value = self.get_value(arg.op_addr+i, arg.op_type, arg.isGlobal)
                self.mem = new_mem
                self.register_value(p_local_address + i, p_value, arg.op_type)
                self.mem = self.t_mem
            self.mem = new_mem
    
    def memberVar(self, att, attrNum):
        new_mem = self.mem
        l_address = self.attribute_refs[attrNum]
        self.mem = self.t_mem
        if att.dimensions == 0:
            p_value = self.get_value(att.op_addr, att.op_type, att.isGlobal)
            self.mem = new_mem
            self.register_value(l_address, p_value, att.op_type)
        elif att.dimensions == 1: 
            for i in range(att.dims[0].upperLim + 1):
                p_value = self.get_value(att.op_addr + i, att.op_type, att.isGlobal)
                self.mem = new_mem
                self.register_value(l_address + i, p_value, att.op_type)
                self.mem = self.t_mem
            self.mem = new_mem
            
        elif att.dimensions == 2:
            for i in range((att.dims[0].upperLim + 1) * (att.dims[1].upperLim + 1)):
                p_value = self.get_value(att.op_addr+i, att.op_type, att.isGlobal)
                self.mem = new_mem
                self.register_value(l_address + i, p_value, att.op_type)
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

    def run(self):
        q = 0
        for i, quad in enumerate(self.quad_queue):
            print(i, quad)
        
        while q < len(self.quad_queue):
            quad = self.quad_queue[q]
            if quad.operator == 'ASSIGN':
                value_op = quad.left_op
                value = self.get_value(value_op.op_addr, value_op.op_type, value_op.isGlobal) if value_op.dimensions == 0 else self.get_value(value_op.op_addr, value_op.op_type, value_op.isGlobal, value_op.dimensions)
                result = quad.ans
                self.register_value(result.op_addr, value, result.op_type, result.isGlobal) if result.dimensions == 0 else self.register_value(result.op_addr, value, result.op_type, result.isGlobal, result.dimensions)
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
                self.era(quad.ans) if quad.right_op == None else self.era(quad.ans, quad.right_op.op_id)
            elif quad.operator == 'PARAM':
                self.param(quad.left_op, quad.ans)
            elif quad.operator == 'MEMBERVAR':
                self.memberVar(quad.left_op, quad.ans)
            elif quad.operator == 'GOSUB':
                # add new memory to stack
                self.mem_stack.append(self.mem)
                # clear param refs
                self.param_refs = []
                self.call_stack.append(q + 1)
                q = quad.ans
                continue
            elif quad.operator == 'RETURN':
                if quad.left_op == None:
                    self.rtn_stmt(quad.ans, self.meth_dir[quad.right_op.op_id].m_type)
                    q = self.meth_dir[quad.right_op.op_id].m_end
                else:
                    self.rtn_stmt(quad.ans, self.class_dir[quad.left_op.op_id].methods[quad.right_op.op_id].m_type)
                    q = self.class_dir[quad.left_op.op_id].methods[quad.right_op.op_id].m_end
                continue
            elif quad.operator == 'ENDMETH':
                # Remove local memory from the top of mem_stack
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
                self.register_value(ans_op.op_addr, value, ans_op.op_type, ans_op.isGlobal) if ans_op.dimensions == 0 else self.register_value(ans_op.op_addr, value, ans_op.op_type, ans_op.isGlobal, ans_op.dimensions)
            q += 1
        
        print("\nFinished execution...")
        # if len(self.messages) > 0:
        #     print("Important execution logs:")
        # for i in range(len(self.messages)):
        #     print(self.messages[i])