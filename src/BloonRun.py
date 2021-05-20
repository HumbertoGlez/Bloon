import sys
from antlr4 import *
from BloonLexer import BloonLexer
from BloonParser import BloonParser
from Bloon_VM import VirtualMachine

def main(argv):
    file = FileStream(argv[1])
    lexer = BloonLexer(file)
    stream = CommonTokenStream(lexer)
    parser = BloonParser(stream)
    tree = parser.program()
    v_machine = VirtualMachine(parser)
    v_machine.run()

if __name__ == '__main__':
    main(sys.argv)