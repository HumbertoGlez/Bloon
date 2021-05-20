from collections import deque

from tools import operation_result_type

class VirtualMachine():
    quad_queue = []
    meth_dir = {}
    type_dir = {}
    mem = [None]*10000
    mem_stack = [mem]
    call_stack = []
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
    
    def write(self, operand):
        value = self.get_value(operand.op_addr, operand.op_type, operand.isGlobal)
        print("WRITE:", value)

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

    def operation(self, op, left, right):
        # Validation was already done on the compiler
        if op == 'add':
            return left + right
        elif op == 'sub':
            return left - right
        elif op == 'mul':
            return left * right
        elif op == 'div':
            return left / right
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
            elif quad.operator == 'READ':
                self.read(quad.ans)
            elif quad.operator == '+':
                self.do_operation('add', quad) 
            elif quad.operator == '-':
                self.do_operation('sub', quad) 
            elif quad.operator == '*':
                self.do_operation('mul', quad) 
            elif quad.operator == '/':
                self.do_operation('div', quad) 
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