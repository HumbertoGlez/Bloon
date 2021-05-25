from collections import deque

from tools import operation_result_type

class VirtualMachine():
    quad_queue = []
    meth_dir = {}
    type_dir = {}
    mem = [None]*10000
    mem_stack = [mem]
    t_mem = []
    call_stack = []
    arguments = []
    param_refs = []
    INT_START = 0
    FLOAT_START = 250
    CHAR_START = 500
    STRING_START = 750
    UNSPECIFIED = 1000
    localInt_start = 0
    localFloat_start = 0
    localChar_start = 0
    localString_start = 0
    localUnspecified_start = 0
    messages = []

    def __init__(self, parser, **kwargs):
        self.quad_queue = parser.quad_queue
        self.meth_dir = parser.meth_dir
        self.type_dir = parser.type_dir
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
    
    def register_value(self, address, value, v_type, isglobal=False):
        if isglobal:
            curr_memory = self.mem_stack[0]
        else:
            curr_memory = self.mem
        
        if v_type == 'int':
            curr_memory[self.INT_START + address] = value
        elif v_type == 'float':
            curr_memory[self.FLOAT_START + address] = value
        elif v_type == 'char':
            curr_memory[self.CHAR_START + address] = value
        elif v_type == 'string':
            curr_memory[self.STRING_START + address] = value
        elif v_type == 'custom':
            curr_memory[self.UNSPECIFIED + address] = address
    
    def get_value(self, address, v_type, isglobal=False):
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
            intStart = self.localInt_start
            floatStart = self.localFloat_start
            charStart = self.localChar_start
            strStart = self.localString_start
            uStart = self.localUnspecified_start
        if v_type == 'int':
            return curr_memory[intStart + address]
        elif v_type == 'float':
            return curr_memory[floatStart + address]
        elif v_type == 'char':
            return curr_memory[charStart + address]
        elif v_type == 'string':
            return curr_memory[strStart + address]
        elif v_type == 'custom':
            return curr_memory[uStart + address]

    def write(self, operand):
        value = self.get_value(operand.op_addr, operand.op_type, operand.isGlobal)
        print(value, end ="")

    def read(self, operand):
        value = input("Enter value to read: ")
        if operand.op_type != 'string' or operand.op_type != 'char':
            if operand.op_type == 'int':
                try:
                    val = int(value)
                    self.register_value(operand.op_addr, val, operand.op_type, operand.isGlobal)
                except ValueError:
                    raise Exception(f"Invalid input to read for variable of type {operand.op_type}")
            elif operand.op_type == 'float':
                try:
                    val = float(value)
                    self.register_value(operand.op_addr, val, operand.op_type, operand.isGlobal)
                except ValueError:
                    raise Exception(f"Invalid input to read for variable of type {operand.op_type}")
        else:
            self.register_value(operand.op_addr, value, operand.op_type, operand.isGlobal)

    def operation(self, left, right, op):
        # CHECK FOR TYPE
        type_left_str = left.op_type == 'string'
        type_right_str = right.op_type == 'string'

        type_left_char = left.op_type == 'char'
        type_right_char = right.op_type == 'char'

        left_v = self.get_value(left.op_addr, left.op_type, left.isGlobal)
        right_v = self.get_value(right.op_addr, right.op_type, right.isGlobal)

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

        ans = self.operation(left_op, right_op, op)
        self.register_value(res_op.op_addr, ans, res_op.op_type, res_op.isGlobal)
    
    def era(self, m_id):
        localVarTable = self.meth_dir[m_id].m_vars
        intCount = len(localVarTable['int']) + self.meth_dir[m_id].m_temps['int']
        flCount = len(localVarTable['float']) + self.meth_dir[m_id].m_temps['float']
        charCount = len(localVarTable['char']) + self.meth_dir[m_id].m_temps['char']
        strCount = len(localVarTable['string']) + self.meth_dir[m_id].m_temps['string']
        uCount = 1000 if len(localVarTable['custom']) + self.meth_dir[m_id].m_temps['custom'] > 0 else 0
        self.localInt_start = 0
        self.localFloat_start = intCount
        self.localChar_start = intCount + flCount
        self.localString_start = intCount + flCount + charCount
        self.localUnspecified_start = intCount + flCount + charCount + strCount
        # save previous memory in t_mem
        self.t_mem = self.mem
        # Create memory with just the needed addresses
        self.mem = [None]*(intCount + flCount + charCount + strCount + uCount)
        self.messages.append("Created local memory with " + str(intCount + flCount + charCount + strCount + uCount) + " spaces.")
        self.param_refs = self.meth_dir[m_id].m_param_addrs
    
    def param(self, arg, argNum):
        new_mem = self.mem
        p_local_address = self.param_refs[argNum]
        self.mem = self.t_mem
        p_value = self.get_value(arg.op_addr, arg.op_type)
        self.mem = new_mem
        self.register_value(p_local_address, p_value, arg.op_type)
    
    def rtn_stmt(self, res):
        val = self.get_value(res.op_addr, res.op_type, res.isGlobal)
        if val is None:
            return
        goSub = self.call_stack[-1] - 1
        r_addr = self.quad_queue[goSub].right_op
        curr_memory = self.mem_stack[-2]
        intStart = self.INT_START if len(self.mem_stack) == 2  else self.localInt_start
        flStart = self.FLOAT_START if len(self.mem_stack) == 2  else self.localFloat_start
        charStart = self.CHAR_START if len(self.mem_stack) == 2  else self.localChar_start
        strStart = self.STRING_START if len(self.mem_stack) == 2  else self.localString_start
        uStart = self.UNSPECIFIED if len(self.mem_stack) == 2  else self.localUnspecified_start
        if res.op_type == 'int':
            curr_memory[intStart + r_addr] = int(val)
        elif res.op_type == 'float':
            curr_memory[flStart + r_addr] = float(val)
        elif res.op_type == 'char':
            curr_memory[charStart + r_addr] = val
        elif res.op_type == 'string':
            curr_memory[strStart + r_addr] = val
        elif res.op_type == 'any':
            curr_memory[uStart + r_addr] = val

    def run(self):
        q = 0
        for i, quad in enumerate(self.quad_queue):
            print(i, quad)
        
        while q < len(self.quad_queue):
            quad = self.quad_queue[q]
            if quad.operator == 'ASSIGN':
                value_op = quad.left_op
                value = self.get_value(value_op.op_addr, value_op.op_type, value_op.isGlobal)
                result = quad.ans
                self.register_value(result.op_addr, value, result.op_type, result.isGlobal)
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
                value = self.get_value(value_op.op_addr, value_op.op_type, value_op.isGlobal)
                if value == False:
                    q = quad.ans
                    continue
            elif quad.operator == 'PARAM':
                self.param(quad.left_op, quad.ans)
            elif quad.operator == 'ERA':
                self.era(quad.ans)
            elif quad.operator == 'GOSUB':
                self.mem_stack.append(self.mem)
                self.param_refs = []
                self.call_stack.append(q + 1)
                q = quad.ans
                continue
            elif quad.operator == 'RETURN':
                self.rtn_stmt(quad.ans)
            elif quad.operator == 'ENDMETH':
                # Remove local memory from the top of mem_stack
                self.mem_stack.pop()
                # Set memory to last memory in stack
                self.mem = self.mem_stack[-1]
                q = self.call_stack.pop()
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
                value = self.get_value(value_op.op_addr, value_op.op_type, value_op.isGlobal)
                value += 1
                ans_op = quad.ans
                self.register_value(ans_op.op_addr, value, ans_op.op_type, ans_op.isGlobal)
            q += 1
        
        print("\nFinished execution...")
        print("Important execution logs:")
        for i in range(len(self.messages)):
            print(self.messages[i])