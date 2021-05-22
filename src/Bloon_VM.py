from collections import deque

from tools import operation_result_type

class VirtualMachine():
    quad_queue = []
    meth_dir = {}
    type_dir = {}
    mem = [None]*10000
    mem_stack = [mem]
    call_stack = []
    arguments = []
    param_refs = []
    INT_START = 0
    FLOAT_START = 250
    CHAR_START = 500
    STRING_START = 750
    UNSPECIFIED = 1000

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
        if isglobal:
            curr_memory = self.mem_stack[0]
        else:
            curr_memory = self.mem
        
        if v_type == 'int':
            return curr_memory[self.INT_START + address]
        elif v_type == 'float':
            return curr_memory[self.FLOAT_START + address]
        elif v_type == 'char':
            return curr_memory[self.CHAR_START + address]
        elif v_type == 'string':
            return curr_memory[self.STRING_START + address]
        elif v_type == 'custom':
            return curr_memory[self.UNSPECIFIED + address]
    
    def era(self, m_id):
        new_mem = [None]*10000
        t_mem = []
        self.param_refs = self.meth_dir[m_id].m_param_addrs
        for i, arg in enumerate(self.arguments):
            p_local_address = self.param_refs[i]
            p_value = self.get_value(arg.op_addr, arg.op_type)
            t_mem = self.mem
            self.mem = new_mem
            self.register_value(p_local_address, p_value, arg.op_type)
            self.mem = t_mem
        self.mem_stack.append(new_mem)
        self.mem = new_mem
        self.arguments = []
        self.param_refs = []

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

    def rtn_stmt(self, res):
        val = self.get_value(res.op_addr, res.op_type, res.isGlobal)
        if val is None:
            return
        goSub = self.call_stack[-1] - 1
        r_addr = self.quad_queue[goSub].right_op
        curr_memory = self.mem_stack[-2]
        if res.op_type == 'int':
            curr_memory[self.INT_START + r_addr] = int(val)
        elif res.op_type == 'float':
            curr_memory[self.FLOAT_START + r_addr] = float(val)
        elif res.op_type == 'char':
            curr_memory[self.CHAR_START + r_addr] = val
        elif res.op_type == 'string':
            curr_memory[self.STRING_START + r_addr] = val
        elif res.op_type == 'any':
            curr_memory[self.UNSPECIFIED + r_addr] = val

    def operation(self, op, left, right):
        # Validation was already done on the compiler
        # CHAR OPERATIONS NEED TO BE REVISED, MODULUS NEED IMPLEMENTATION
        if op == 'add':
            return left + right
        elif op == 'sub':
            return left - right
        elif op == 'mul':
            return left * right
        elif op == 'div':
            return left / right
        elif op == 'mod':
            return left % right
        elif op == 'gt':
            return left > right
        elif op == 'ge':
            return left >= right
        elif op == 'lt':
            return left < right
        elif op == 'le':
            return left <= right
        elif op == 'eq':
            return left == right
        elif op == 'ne':
            return left != right

    def do_operation(self, op, quad):
        left_op = quad.left_op
        l_value = self.get_value(left_op.op_addr, left_op.op_type, left_op.isGlobal)
        right_op = quad.right_op
        r_value = self.get_value(right_op.op_addr, right_op.op_type, right_op.isGlobal)
        res_op = quad.ans

        ans = self.operation(op, l_value, r_value)
        self.register_value(res_op.op_addr, ans, res_op.op_type, res_op.isGlobal)

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
                self.arguments.insert(0, quad.ans)
            elif quad.operator == 'ERA':
                self.era(quad.ans)
            elif quad.operator == 'GOSUB':
                self.call_stack.append(q + 1)
                q = quad.ans
                continue
            elif quad.operator == 'RETURN':
                self.rtn_stmt(quad.ans)
            elif quad.operator == 'ENDMETH':
                self.mem_stack.pop()
                self.mem = self.mem_stack[-1]
                q = self.call_stack.pop()
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