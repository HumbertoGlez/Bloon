# Entregable 3: Cubo aritmetico de operaciones

INT = "int"
FLOAT = "float"
CHAR = "char"
STRING = "string"
ANY = "any"
TYPE_ERROR = "Undefined operator {} for types {} and {}"

def operation_result_type(oper, left_type, right_type):
    if oper == "+":
        if left_type == INT:
            if right_type == INT:
                return INT
            if right_type == FLOAT:
                return FLOAT
            if right_type == CHAR:
                return INT
        if left_type == FLOAT:
            if right_type == INT:
                return FLOAT
            if right_type == FLOAT:
                return FLOAT
            if right_type == CHAR:
                return FLOAT
        if left_type == CHAR:
            if right_type == INT:
                return INT
            if right_type == FLOAT:
                return FLOAT
            if right_type == CHAR:
                return INT
            if right_type == STRING:
                return STRING
        if left_type == STRING:
            if right_type == CHAR:
                return STRING
            if right_type == STRING:
                return STRING
        raise TypeError(TYPE_ERROR.format(oper, left_type, right_type))
    elif oper == "-":
        if left_type == INT:
            if right_type == INT:
                return INT
            if right_type == FLOAT:
                return FLOAT
            if right_type == CHAR:
                return INT
        if left_type == FLOAT:
            if right_type == INT:
                return FLOAT
            if right_type == FLOAT:
                return FLOAT
            if right_type == CHAR:
                return FLOAT
        if left_type == CHAR:
            if right_type == INT:
                return INT
            if right_type == FLOAT:
                return FLOAT
            if right_type == CHAR:
                return INT 
        raise TypeError(TYPE_ERROR.format(oper, left_type, right_type))
    elif oper == "*":
        if left_type == INT:
            if right_type == INT:
                return INT
            if right_type == FLOAT:
                return FLOAT
            if right_type == CHAR:
                return INT
        if left_type == FLOAT:
            if right_type == INT:
                return FLOAT
            if right_type == FLOAT:
                return FLOAT
            if right_type == CHAR:
                return FLOAT
        if left_type == CHAR:
            if right_type == INT:
                return INT
            if right_type == FLOAT:
                return FLOAT
            if right_type == CHAR:
                return INT 
        raise TypeError(TYPE_ERROR.format(oper, left_type, right_type))
    elif oper == "/":
        if left_type == INT:
            if right_type == INT:
                return INT
            if right_type == FLOAT:
                return FLOAT
            if right_type == CHAR:
                return INT
        if left_type == FLOAT:
            if right_type == INT:
                return FLOAT
            if right_type == FLOAT:
                return FLOAT
            if right_type == CHAR:
                return FLOAT
        if left_type == CHAR:
            if right_type == INT:
                return INT
            if right_type == FLOAT:
                return FLOAT
            if right_type == CHAR:
                return INT 
        raise TypeError(TYPE_ERROR.format(oper, left_type, right_type))
    elif oper == ">":
        if left_type == INT:
            if right_type == INT:
                return INT
            if right_type == FLOAT:
                return INT
            if right_type == CHAR:
                return INT
        if left_type == FLOAT:
            if right_type == INT:
                return INT
            if right_type == FLOAT:
                return INT
            if right_type == CHAR:
                return INT
        if left_type == CHAR:
            if right_type == INT:
                return INT
            if right_type == FLOAT:
                return INT
            if right_type == CHAR:
                return INT
        if left_type == STRING:
            if right_type == STRING:
                return INT
        raise TypeError(TYPE_ERROR.format(oper, left_type, right_type))
    elif oper == "<":
        if left_type == INT:
            if right_type == INT:
                return INT
            if right_type == FLOAT:
                return INT
            if right_type == CHAR:
                return INT
        if left_type == FLOAT:
            if right_type == INT:
                return INT
            if right_type == FLOAT:
                return INT
            if right_type == CHAR:
                return INT
        if left_type == CHAR:
            if right_type == INT:
                return INT
            if right_type == FLOAT:
                return INT
            if right_type == CHAR:
                return INT
        if left_type == STRING:
            if right_type == STRING:
                return INT
        raise TypeError(TYPE_ERROR.format(oper, left_type, right_type))
    elif oper == "=":
        if left_type == INT:
            if right_type == INT:
                return INT
            if right_type == FLOAT:
                return INT
            if right_type == CHAR:
                return INT
        if left_type == FLOAT:
            if right_type == INT:
                return FLOAT
            if right_type == FLOAT:
                return FLOAT
            if right_type == CHAR:
                return FLOAT
        if left_type == CHAR:
            if right_type == INT:
                return CHAR
            if right_type == FLOAT:
                return CHAR
            if right_type == CHAR:
                return CHAR
        if left_type == STRING:
            if right_type == CHAR:
                return STRING
            if right_type == STRING:
                return STRING
        raise TypeError(TYPE_ERROR.format(oper, left_type, right_type))
    elif oper == ">=":
        if left_type == INT:
            if right_type == INT:
                return INT
            if right_type == FLOAT:
                return INT
            if right_type == CHAR:
                return INT
        if left_type == FLOAT:
            if right_type == INT:
                return INT
            if right_type == FLOAT:
                return INT
            if right_type == CHAR:
                return INT
        if left_type == CHAR:
            if right_type == INT:
                return INT
            if right_type == FLOAT:
                return INT
            if right_type == CHAR:
                return INT
        if left_type == STRING:
            if right_type == STRING:
                return INT
        raise TypeError(TYPE_ERROR.format(oper, left_type, right_type))
    elif oper == "<=":
        if left_type == INT:
            if right_type == INT:
                return INT
            if right_type == FLOAT:
                return INT
            if right_type == CHAR:
                return INT
        if left_type == FLOAT:
            if right_type == INT:
                return INT
            if right_type == FLOAT:
                return INT
            if right_type == CHAR:
                return INT
        if left_type == CHAR:
            if right_type == INT:
                return INT
            if right_type == FLOAT:
                return INT
            if right_type == CHAR:
                return INT
        if left_type == STRING:
            if right_type == STRING:
                return INT
        raise TypeError(TYPE_ERROR.format(oper, left_type, right_type))
    elif oper == "==":
        if left_type == INT:
            if right_type == INT:
                return INT
            if right_type == FLOAT:
                return INT
            if right_type == CHAR:
                return INT
        if left_type == FLOAT:
            if right_type == INT:
                return INT
            if right_type == FLOAT:
                return INT
            if right_type == CHAR:
                return INT
        if left_type == CHAR:
            if right_type == INT:
                return INT
            if right_type == FLOAT:
                return INT
            if right_type == CHAR:
                return INT
        if left_type == STRING:
            if right_type == STRING:
                return INT
        raise TypeError(TYPE_ERROR.format(oper, left_type, right_type))
    elif oper == "!=":
        if left_type == INT:
            if right_type == INT:
                return INT
            if right_type == FLOAT:
                return INT
            if right_type == CHAR:
                return INT
        if left_type == FLOAT:
            if right_type == INT:
                return INT
            if right_type == FLOAT:
                return INT
            if right_type == CHAR:
                return INT
        if left_type == CHAR:
            if right_type == INT:
                return INT
            if right_type == FLOAT:
                return INT
            if right_type == CHAR:
                return INT
        if left_type == STRING:
            if right_type == STRING:
                return INT
        raise TypeError(TYPE_ERROR.format(oper, left_type, right_type))
    elif oper == "+=":
        if left_type == INT:
            if right_type == INT:
                return INT
            if right_type == FLOAT:
                return INT
            if right_type == CHAR:
                return INT
        if left_type == FLOAT:
            if right_type == INT:
                return FLOAT
            if right_type == FLOAT:
                return FLOAT
            if right_type == CHAR:
                return FLOAT
        if left_type == CHAR:
            if right_type == INT:
                return CHAR
            if right_type == FLOAT:
                return CHAR
            if right_type == CHAR:
                return CHAR
        if left_type == STRING:
            if right_type == CHAR:
                return STRING
            if right_type == STRING:
                return STRING
        raise TypeError(TYPE_ERROR.format(oper, left_type, right_type))
    elif oper == "-=":
        if left_type == INT:
            if right_type == INT:
                return INT
            if right_type == FLOAT:
                return INT
            if right_type == CHAR:
                return INT
        if left_type == FLOAT:
            if right_type == INT:
                return FLOAT
            if right_type == FLOAT:
                return FLOAT
            if right_type == CHAR:
                return FLOAT
        if left_type == CHAR:
            if right_type == INT:
                return CHAR
            if right_type == FLOAT:
                return CHAR
            if right_type == CHAR:
                return CHAR
        raise TypeError(TYPE_ERROR.format(oper, left_type, right_type))
    elif oper == "*=":
        if left_type == INT:
            if right_type == INT:
                return INT
            if right_type == FLOAT:
                return INT
            if right_type == CHAR:
                return INT
        if left_type == FLOAT:
            if right_type == INT:
                return FLOAT
            if right_type == FLOAT:
                return FLOAT
            if right_type == CHAR:
                return FLOAT
        if left_type == CHAR:
            if right_type == INT:
                return CHAR
            if right_type == FLOAT:
                return CHAR
            if right_type == CHAR:
                return CHAR
        raise TypeError(TYPE_ERROR.format(oper, left_type, right_type))
    elif oper == "/=":
        if left_type == INT:
            if right_type == INT:
                return INT
            if right_type == FLOAT:
                return INT
            if right_type == CHAR:
                return INT
        if left_type == FLOAT:
            if right_type == INT:
                return FLOAT
            if right_type == FLOAT:
                return FLOAT
            if right_type == CHAR:
                return FLOAT
        if left_type == CHAR:
            if right_type == INT:
                return CHAR
            if right_type == FLOAT:
                return CHAR
            if right_type == CHAR:
                return CHAR
        raise TypeError(TYPE_ERROR.format(oper, left_type, right_type))
    else:
        raise ValueError("{} does not exist".format(oper))