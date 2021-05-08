# Entregable 3: Cubo semántico de operaciones

INT = "int"
FLOAT = "float"
CHAR = "char"
STRING = "string"
ANY = "any"
TYPE_ERROR = "Undefined operator {} for types {} and {}"

semanticCube = {
    INT:{
        INT: {
            '+':INT,
            '-': INT,
            '*': INT,
            '/': INT,
            '>': INT,
            '<': INT,
            '=': INT,
            '<=': INT,
            '>=': INT,
            '==': INT,
            '!=': INT,
            '+=': INT,
            '-=': INT,
            '*=': INT,
            '/=': INT
        },
        FLOAT: {
            '+': FLOAT,
            '-': FLOAT,
            '*': FLOAT,
            '/': FLOAT,
            '>': INT,
            '<': INT,
            '=': INT,
            '<=': INT,
            '>=': INT,
            '==': INT,
            '!=': INT,
            '+=': INT,
            '-=': INT,
            '*=': INT,
            '/=': INT,
        },
        CHAR: {
            '+':INT,
            '-': INT,
            '*': INT,
            '/': INT,
            '>': INT,
            '<': INT,
            '=': INT,
            '<=': INT,
            '>=': INT,
            '==': INT,
            '!=': INT,
            '+=': INT,
            '-=': INT,
            '*=': INT,
            '/=': INT
        },
        STRING: {
            '+':TYPE_ERROR,
            '-': TYPE_ERROR,
            '*': TYPE_ERROR,
            '/': TYPE_ERROR,
            '>': TYPE_ERROR,
            '<': TYPE_ERROR,
            '=': TYPE_ERROR,
            '<=': TYPE_ERROR,
            '>=': TYPE_ERROR,
            '==': TYPE_ERROR,
            '!=': TYPE_ERROR,
            '+=': TYPE_ERROR,
            '-=': TYPE_ERROR,
            '*=': TYPE_ERROR,
            '/=': TYPE_ERROR
        }
    },
    FLOAT: {
        INT: {
            '+':FLOAT,
            '-': FLOAT,
            '*': FLOAT,
            '/': FLOAT,
            '>': INT,
            '<': INT,
            '=': FLOAT,
            '<=': INT,
            '>=': INT,
            '==': INT,
            '!=': INT,
            '+=': FLOAT,
            '-=': FLOAT,
            '*=': FLOAT,
            '/=': FLOAT
        },
        FLOAT: {
            '+':FLOAT,
            '-': FLOAT,
            '*': FLOAT,
            '/': FLOAT,
            '>': INT,
            '<': INT,
            '=': FLOAT,
            '<=': INT,
            '>=': INT,
            '==': INT,
            '!=': INT,
            '+=': FLOAT,
            '-=': FLOAT,
            '*=': FLOAT,
            '/=': FLOAT
        },
        CHAR: {
            '+':FLOAT,
            '-': FLOAT,
            '*': FLOAT,
            '/': FLOAT,
            '>': INT,
            '<': INT,
            '=': FLOAT,
            '<=': INT,
            '>=': INT,
            '==': INT,
            '!=': INT,
            '+=': FLOAT,
            '-=': FLOAT,
            '*=': FLOAT,
            '/=': FLOAT
        },
        STRING: {
            '+':TYPE_ERROR,
            '-': TYPE_ERROR,
            '*': TYPE_ERROR,
            '/': TYPE_ERROR,
            '>': TYPE_ERROR,
            '<': TYPE_ERROR,
            '=': TYPE_ERROR,
            '<=': TYPE_ERROR,
            '>=': TYPE_ERROR,
            '==': TYPE_ERROR,
            '!=': TYPE_ERROR,
            '+=': TYPE_ERROR,
            '-=': TYPE_ERROR,
            '*=': TYPE_ERROR,
            '/=': TYPE_ERROR
        }
    },
    CHAR: {
         INT: {
            '+':INT,
            '-': INT,
            '*': INT,
            '/': INT,
            '>': INT,
            '<': INT,
            '=': CHAR,
            '<=': INT,
            '>=': INT,
            '==': INT,
            '!=': INT,
            '+=': CHAR,
            '-=': CHAR,
            '*=': CHAR,
            '/=': CHAR
        },
        FLOAT: {
            '+':FLOAT,
            '-': FLOAT,
            '*': FLOAT,
            '/': FLOAT,
            '>': INT,
            '<': INT,
            '=': CHAR,
            '<=': INT,
            '>=': INT,
            '==': INT,
            '!=': INT,
            '+=': CHAR,
            '-=': CHAR,
            '*=': CHAR,
            '/=': CHAR
        },
        CHAR: {
            '+':INT,
            '-': INT,
            '*': INT,
            '/': INT,
            '>': INT,
            '<': INT,
            '=': CHAR,
            '<=': INT,
            '>=': INT,
            '==': INT,
            '!=': INT,
            '+=': CHAR,
            '-=': CHAR,
            '*=': CHAR,
            '/=': CHAR
        },
        STRING: {
            '+': STRING,
            '-': TYPE_ERROR,
            '*': TYPE_ERROR,
            '/': TYPE_ERROR,
            '>': TYPE_ERROR,
            '<': TYPE_ERROR,
            '=': TYPE_ERROR,
            '<=': TYPE_ERROR,
            '>=': TYPE_ERROR,
            '==': TYPE_ERROR,
            '!=': TYPE_ERROR,
            '+=': TYPE_ERROR,
            '-=': TYPE_ERROR,
            '*=': TYPE_ERROR,
            '/=': TYPE_ERROR
        }
    },
    STRING: {
        INT: {
            '+': TYPE_ERROR,
            '-': TYPE_ERROR,
            '*': TYPE_ERROR,
            '/': TYPE_ERROR,
            '>': TYPE_ERROR,
            '<': TYPE_ERROR,
            '=': TYPE_ERROR,
            '<=': TYPE_ERROR,
            '>=': TYPE_ERROR,
            '==': TYPE_ERROR,
            '!=': TYPE_ERROR,
            '+=': TYPE_ERROR,
            '-=': TYPE_ERROR,
            '*=': TYPE_ERROR,
            '/=': TYPE_ERROR
        },
         FLOAT: {
            '+': TYPE_ERROR,
            '-': TYPE_ERROR,
            '*': TYPE_ERROR,
            '/': TYPE_ERROR,
            '>': TYPE_ERROR,
            '<': TYPE_ERROR,
            '=': TYPE_ERROR,
            '<=': TYPE_ERROR,
            '>=': TYPE_ERROR,
            '==': TYPE_ERROR,
            '!=': TYPE_ERROR,
            '+=': TYPE_ERROR,
            '-=': TYPE_ERROR,
            '*=': TYPE_ERROR,
            '/=': TYPE_ERROR
        },
         CHAR: {
            '+': STRING,
            '-': TYPE_ERROR,
            '*': TYPE_ERROR,
            '/': TYPE_ERROR,
            '>': TYPE_ERROR,
            '<': TYPE_ERROR,
            '=': STRING,
            '<=': TYPE_ERROR,
            '>=': TYPE_ERROR,
            '==': TYPE_ERROR,
            '!=': TYPE_ERROR,
            '+=': STRING,
            '-=': TYPE_ERROR,
            '*=': TYPE_ERROR,
            '/=': TYPE_ERROR
        },
         STRING: {
            '+': STRING,
            '-': TYPE_ERROR,
            '*': TYPE_ERROR,
            '/': TYPE_ERROR,
            '>': INT,
            '<': INT,
            '=': STRING,
            '<=': INT,
            '>=': INT,
            '==': INT,
            '!=': INT,
            '+=': STRING,
            '-=': TYPE_ERROR,
            '*=': TYPE_ERROR,
            '/=': TYPE_ERROR
        }
    }

}

def operation_result_type(left_type, right_type, oper):
    if not left_type in semanticCube or not right_type in semanticCube[left_type] or not oper in semanticCube[left_type][right_type]:
        raise ValueError("{} does not exist".format(oper))
    elif semanticCube[left_type][right_type][oper] == TYPE_ERROR:
        raise TypeError(TYPE_ERROR.format(oper, left_type, right_type))
    return(semanticCube[left_type][right_type][oper])
