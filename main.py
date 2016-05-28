import sys
from antlr4 import *
from YailLexer import YailLexer
from YailParser import YailParser
from listener import Listener

def main(argv):
    input = FileStream(argv[1])
    lexer = YailLexer(input)
    stream = CommonTokenStream(lexer)
    parser = YailParser(stream)
    tree = parser.prog()
    listener = Listener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main(sys.argv)
