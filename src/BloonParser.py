# Generated from Bloon.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


from BloonCompiler import Compiler
compi = Compiler()
quad_queue = None
meth_dir = None
class_dir = None
constants = None


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3=")
        buf.write("\u02a5\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\5\3\u0084\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u009a\n")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\5\7\u00a1\n\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00b0\n\b\3\b\5")
        buf.write("\b\u00b3\n\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00bd")
        buf.write("\n\b\5\b\u00bf\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00c8")
        buf.write("\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00d2\n\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\5")
        buf.write("\f\u00e0\n\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\5\16\u00ed\n\16\3\17\3\17\3\17\3\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00fd")
        buf.write("\n\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21")
        buf.write("\u0108\n\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\5\23\u0118\n\23\3\23\3\23")
        buf.write("\3\23\5\23\u011d\n\23\3\23\3\23\3\23\3\23\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u012c\n\23\5\23")
        buf.write("\u012e\n\23\3\24\3\24\5\24\u0132\n\24\3\25\3\25\3\25\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26")
        buf.write("\u0141\n\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\5")
        buf.write("\32\u014b\n\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\5\33\u0155\n\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\35\3\35\3\35\3\35\5\35\u0163\n\35\3\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u0170\n")
        buf.write("\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(" \3 \3 \5 \u0185\n \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \3 \3 \3 \3 \5 \u019c\n \3 \3 \5 \u01a0")
        buf.write("\n \3!\3!\3!\5!\u01a5\n!\3\"\3\"\3\"\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\5#\u01b1\n#\3$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3")
        buf.write("%\5%\u01c0\n%\3%\3%\7%\u01c4\n%\f%\16%\u01c7\13%\3%\3")
        buf.write("%\3%\5%\u01cc\n%\3&\3&\3&\3&\3&\3&\3&\3&\5&\u01d6\n&\3")
        buf.write("&\3&\7&\u01da\n&\f&\16&\u01dd\13&\3&\3&\3&\3\'\3\'\3\'")
        buf.write("\3(\3(\3(\3(\3(\3)\3)\3)\3)\3*\3*\3*\3*\3*\5*\u01f3\n")
        buf.write("*\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\5,\u0204")
        buf.write("\n,\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u020f\n-\3.\3.\3.\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\5/\u0220\n/\3\60\3")
        buf.write("\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\5\62\u023f\n\62\3\63\3")
        buf.write("\63\3\63\3\63\3\63\5\63\u0246\n\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\5\63\u024d\n\63\3\63\5\63\u0250\n\63\3\64\3\64\3")
        buf.write("\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\5\64\u025f\n\64\3\64\3\64\3\64\7\64\u0264\n\64\f\64\16")
        buf.write("\64\u0267\13\64\3\65\3\65\3\65\3\65\3\65\5\65\u026e\n")
        buf.write("\65\3\65\3\65\3\65\7\65\u0273\n\65\f\65\16\65\u0276\13")
        buf.write("\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66\5\66\u027f\n\66")
        buf.write("\3\66\3\66\3\66\7\66\u0284\n\66\f\66\16\66\u0287\13\66")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\5\67\u0292")
        buf.write("\n\67\38\38\38\38\58\u0298\n8\39\39\39\39\39\39\39\39")
        buf.write("\39\59\u02a3\n9\39\2\2:\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`b")
        buf.write("dfhjlnp\2\4\3\2\30\33\3\2\34\37\2\u02b8\2r\3\2\2\2\4\u0083")
        buf.write("\3\2\2\2\6\u0085\3\2\2\2\b\u008c\3\2\2\2\n\u0099\3\2\2")
        buf.write("\2\f\u009b\3\2\2\2\16\u00b2\3\2\2\2\20\u00c0\3\2\2\2\22")
        buf.write("\u00d1\3\2\2\2\24\u00d3\3\2\2\2\26\u00df\3\2\2\2\30\u00e1")
        buf.write("\3\2\2\2\32\u00ec\3\2\2\2\34\u00ee\3\2\2\2\36\u00fc\3")
        buf.write("\2\2\2 \u00fe\3\2\2\2\"\u0109\3\2\2\2$\u011c\3\2\2\2&")
        buf.write("\u0131\3\2\2\2(\u0133\3\2\2\2*\u0140\3\2\2\2,\u0142\3")
        buf.write("\2\2\2.\u0144\3\2\2\2\60\u0146\3\2\2\2\62\u014a\3\2\2")
        buf.write("\2\64\u0154\3\2\2\2\66\u0156\3\2\2\28\u0162\3\2\2\2:\u0164")
        buf.write("\3\2\2\2<\u016f\3\2\2\2>\u019f\3\2\2\2@\u01a4\3\2\2\2")
        buf.write("B\u01a6\3\2\2\2D\u01b0\3\2\2\2F\u01b2\3\2\2\2H\u01cb\3")
        buf.write("\2\2\2J\u01cd\3\2\2\2L\u01e1\3\2\2\2N\u01e4\3\2\2\2P\u01e9")
        buf.write("\3\2\2\2R\u01f2\3\2\2\2T\u01f4\3\2\2\2V\u0203\3\2\2\2")
        buf.write("X\u020e\3\2\2\2Z\u0210\3\2\2\2\\\u021f\3\2\2\2^\u0221")
        buf.write("\3\2\2\2`\u022c\3\2\2\2b\u023e\3\2\2\2d\u024f\3\2\2\2")
        buf.write("f\u0251\3\2\2\2h\u0268\3\2\2\2j\u0277\3\2\2\2l\u0291\3")
        buf.write("\2\2\2n\u0297\3\2\2\2p\u02a2\3\2\2\2rs\7\3\2\2st\7\67")
        buf.write("\2\2tu\7\4\2\2uv\5\4\3\2vw\b\2\1\2wx\7\2\2\3x\3\3\2\2")
        buf.write("\2yz\5\b\5\2z{\5\4\3\2{\u0084\3\2\2\2|}\5\"\22\2}~\5\4")
        buf.write("\3\2~\u0084\3\2\2\2\177\u0080\5\66\34\2\u0080\u0081\5")
        buf.write("\4\3\2\u0081\u0084\3\2\2\2\u0082\u0084\5\6\4\2\u0083y")
        buf.write("\3\2\2\2\u0083|\3\2\2\2\u0083\177\3\2\2\2\u0083\u0082")
        buf.write("\3\2\2\2\u0084\5\3\2\2\2\u0085\u0086\7\5\2\2\u0086\u0087")
        buf.write("\7\6\2\2\u0087\u0088\b\4\1\2\u0088\u0089\7\7\2\2\u0089")
        buf.write("\u008a\b\4\1\2\u008a\u008b\5B\"\2\u008b\7\3\2\2\2\u008c")
        buf.write("\u008d\7\b\2\2\u008d\u008e\7\67\2\2\u008e\u008f\b\5\1")
        buf.write("\2\u008f\u0090\5\n\6\2\u0090\t\3\2\2\2\u0091\u0092\7\t")
        buf.write("\2\2\u0092\u0093\7\n\2\2\u0093\u0094\7\67\2\2\u0094\u0095")
        buf.write("\7\13\2\2\u0095\u0096\b\6\1\2\u0096\u009a\5\f\7\2\u0097")
        buf.write("\u0098\b\6\1\2\u0098\u009a\5\f\7\2\u0099\u0091\3\2\2\2")
        buf.write("\u0099\u0097\3\2\2\2\u009a\13\3\2\2\2\u009b\u00a0\7\f")
        buf.write("\2\2\u009c\u009d\7\r\2\2\u009d\u009e\7\16\2\2\u009e\u00a1")
        buf.write("\5\16\b\2\u009f\u00a1\5\20\t\2\u00a0\u009c\3\2\2\2\u00a0")
        buf.write("\u009f\3\2\2\2\u00a1\r\3\2\2\2\u00a2\u00a3\7\67\2\2\u00a3")
        buf.write("\u00b3\b\b\1\2\u00a4\u00a5\7\67\2\2\u00a5\u00a6\7\17\2")
        buf.write("\2\u00a6\u00a7\78\2\2\u00a7\u00af\b\b\1\2\u00a8\u00a9")
        buf.write("\7\20\2\2\u00a9\u00aa\78\2\2\u00aa\u00ab\b\b\1\2\u00ab")
        buf.write("\u00ac\7\21\2\2\u00ac\u00b0\b\b\1\2\u00ad\u00ae\7\21\2")
        buf.write("\2\u00ae\u00b0\b\b\1\2\u00af\u00a8\3\2\2\2\u00af\u00ad")
        buf.write("\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b3\b\b\1\2\u00b2")
        buf.write("\u00a2\3\2\2\2\u00b2\u00a4\3\2\2\2\u00b3\u00be\3\2\2\2")
        buf.write("\u00b4\u00b5\7\20\2\2\u00b5\u00bf\5\16\b\2\u00b6\u00b7")
        buf.write("\7\16\2\2\u00b7\u00b8\5,\27\2\u00b8\u00b9\b\b\1\2\u00b9")
        buf.write("\u00bc\7\4\2\2\u00ba\u00bd\5\16\b\2\u00bb\u00bd\5\20\t")
        buf.write("\2\u00bc\u00ba\3\2\2\2\u00bc\u00bb\3\2\2\2\u00bd\u00bf")
        buf.write("\3\2\2\2\u00be\u00b4\3\2\2\2\u00be\u00b6\3\2\2\2\u00bf")
        buf.write("\17\3\2\2\2\u00c0\u00c7\b\t\1\2\u00c1\u00c2\7\22\2\2\u00c2")
        buf.write("\u00c3\7\16\2\2\u00c3\u00c8\5\22\n\2\u00c4\u00c5\7\23")
        buf.write("\2\2\u00c5\u00c6\7\4\2\2\u00c6\u00c8\b\t\1\2\u00c7\u00c1")
        buf.write("\3\2\2\2\u00c7\u00c4\3\2\2\2\u00c8\21\3\2\2\2\u00c9\u00ca")
        buf.write("\5\24\13\2\u00ca\u00cb\7\23\2\2\u00cb\u00cc\7\4\2\2\u00cc")
        buf.write("\u00cd\b\n\1\2\u00cd\u00d2\3\2\2\2\u00ce\u00cf\5\24\13")
        buf.write("\2\u00cf\u00d0\5\22\n\2\u00d0\u00d2\3\2\2\2\u00d1\u00c9")
        buf.write("\3\2\2\2\u00d1\u00ce\3\2\2\2\u00d2\23\3\2\2\2\u00d3\u00d4")
        buf.write("\5\62\32\2\u00d4\u00d5\7\24\2\2\u00d5\u00d6\7\67\2\2\u00d6")
        buf.write("\u00d7\b\13\1\2\u00d7\u00d8\7\6\2\2\u00d8\u00d9\b\13\1")
        buf.write("\2\u00d9\u00da\5\26\f\2\u00da\25\3\2\2\2\u00db\u00dc\5")
        buf.write("> \2\u00dc\u00dd\5\30\r\2\u00dd\u00e0\3\2\2\2\u00de\u00e0")
        buf.write("\5\30\r\2\u00df\u00db\3\2\2\2\u00df\u00de\3\2\2\2\u00e0")
        buf.write("\27\3\2\2\2\u00e1\u00e2\7\7\2\2\u00e2\u00e3\b\r\1\2\u00e3")
        buf.write("\u00e4\5\32\16\2\u00e4\31\3\2\2\2\u00e5\u00e6\5\"\22\2")
        buf.write("\u00e6\u00e7\5B\"\2\u00e7\u00e8\b\16\1\2\u00e8\u00ed\3")
        buf.write("\2\2\2\u00e9\u00ea\5B\"\2\u00ea\u00eb\b\16\1\2\u00eb\u00ed")
        buf.write("\3\2\2\2\u00ec\u00e5\3\2\2\2\u00ec\u00e9\3\2\2\2\u00ed")
        buf.write("\33\3\2\2\2\u00ee\u00ef\7\67\2\2\u00ef\u00f0\b\17\1\2")
        buf.write("\u00f0\u00f1\5\36\20\2\u00f1\35\3\2\2\2\u00f2\u00fd\5")
        buf.write(" \21\2\u00f3\u00f4\5 \21\2\u00f4\u00f5\7\25\2\2\u00f5")
        buf.write("\u00f6\5\34\17\2\u00f6\u00f7\b\20\1\2\u00f7\u00fd\3\2")
        buf.write("\2\2\u00f8\u00f9\7\25\2\2\u00f9\u00fa\7\67\2\2\u00fa\u00fd")
        buf.write("\b\20\1\2\u00fb\u00fd\b\20\1\2\u00fc\u00f2\3\2\2\2\u00fc")
        buf.write("\u00f3\3\2\2\2\u00fc\u00f8\3\2\2\2\u00fc\u00fb\3\2\2\2")
        buf.write("\u00fd\37\3\2\2\2\u00fe\u00ff\7\17\2\2\u00ff\u0107\5h")
        buf.write("\65\2\u0100\u0101\7\20\2\2\u0101\u0102\5h\65\2\u0102\u0103")
        buf.write("\7\21\2\2\u0103\u0104\b\21\1\2\u0104\u0108\3\2\2\2\u0105")
        buf.write("\u0106\7\21\2\2\u0106\u0108\b\21\1\2\u0107\u0100\3\2\2")
        buf.write("\2\u0107\u0105\3\2\2\2\u0108!\3\2\2\2\u0109\u010a\7\26")
        buf.write("\2\2\u010a\u010b\5$\23\2\u010b#\3\2\2\2\u010c\u010d\7")
        buf.write("\67\2\2\u010d\u010e\7\17\2\2\u010e\u010f\78\2\2\u010f")
        buf.write("\u0117\b\23\1\2\u0110\u0111\7\20\2\2\u0111\u0112\78\2")
        buf.write("\2\u0112\u0113\b\23\1\2\u0113\u0114\7\21\2\2\u0114\u0118")
        buf.write("\b\23\1\2\u0115\u0116\7\21\2\2\u0116\u0118\b\23\1\2\u0117")
        buf.write("\u0110\3\2\2\2\u0117\u0115\3\2\2\2\u0118\u0119\3\2\2\2")
        buf.write("\u0119\u011d\b\23\1\2\u011a\u011b\7\67\2\2\u011b\u011d")
        buf.write("\b\23\1\2\u011c\u010c\3\2\2\2\u011c\u011a\3\2\2\2\u011d")
        buf.write("\u012d\3\2\2\2\u011e\u011f\7\20\2\2\u011f\u012e\5$\23")
        buf.write("\2\u0120\u012b\7\16\2\2\u0121\u0122\5,\27\2\u0122\u0123")
        buf.write("\b\23\1\2\u0123\u0124\7\4\2\2\u0124\u0125\5&\24\2\u0125")
        buf.write("\u012c\3\2\2\2\u0126\u0127\5.\30\2\u0127\u0128\b\23\1")
        buf.write("\2\u0128\u0129\7\4\2\2\u0129\u012a\5&\24\2\u012a\u012c")
        buf.write("\3\2\2\2\u012b\u0121\3\2\2\2\u012b\u0126\3\2\2\2\u012c")
        buf.write("\u012e\3\2\2\2\u012d\u011e\3\2\2\2\u012d\u0120\3\2\2\2")
        buf.write("\u012e%\3\2\2\2\u012f\u0132\5$\23\2\u0130\u0132\3\2\2")
        buf.write("\2\u0131\u012f\3\2\2\2\u0131\u0130\3\2\2\2\u0132\'\3\2")
        buf.write("\2\2\u0133\u0134\5\34\17\2\u0134\u0135\5*\26\2\u0135)")
        buf.write("\3\2\2\2\u0136\u0137\7\27\2\2\u0137\u0138\5b\62\2\u0138")
        buf.write("\u0139\b\26\1\2\u0139\u013a\7\4\2\2\u013a\u0141\3\2\2")
        buf.write("\2\u013b\u013c\5\60\31\2\u013c\u013d\5b\62\2\u013d\u013e")
        buf.write("\b\26\1\2\u013e\u013f\7\4\2\2\u013f\u0141\3\2\2\2\u0140")
        buf.write("\u0136\3\2\2\2\u0140\u013b\3\2\2\2\u0141+\3\2\2\2\u0142")
        buf.write("\u0143\t\2\2\2\u0143-\3\2\2\2\u0144\u0145\7\67\2\2\u0145")
        buf.write("/\3\2\2\2\u0146\u0147\t\3\2\2\u0147\61\3\2\2\2\u0148\u014b")
        buf.write("\5,\27\2\u0149\u014b\7 \2\2\u014a\u0148\3\2\2\2\u014a")
        buf.write("\u0149\3\2\2\2\u014b\63\3\2\2\2\u014c\u0155\5(\25\2\u014d")
        buf.write("\u0155\5Z.\2\u014e\u0155\5F$\2\u014f\u0155\5N(\2\u0150")
        buf.write("\u0155\5T+\2\u0151\u0155\5^\60\2\u0152\u0155\5`\61\2\u0153")
        buf.write("\u0155\5L\'\2\u0154\u014c\3\2\2\2\u0154\u014d\3\2\2\2")
        buf.write("\u0154\u014e\3\2\2\2\u0154\u014f\3\2\2\2\u0154\u0150\3")
        buf.write("\2\2\2\u0154\u0151\3\2\2\2\u0154\u0152\3\2\2\2\u0154\u0153")
        buf.write("\3\2\2\2\u0155\65\3\2\2\2\u0156\u0157\5\62\32\2\u0157")
        buf.write("\u0158\7\24\2\2\u0158\u0159\7\67\2\2\u0159\u015a\b\34")
        buf.write("\1\2\u015a\u015b\7\6\2\2\u015b\u015c\b\34\1\2\u015c\u015d")
        buf.write("\58\35\2\u015d\67\3\2\2\2\u015e\u015f\5> \2\u015f\u0160")
        buf.write("\5:\36\2\u0160\u0163\3\2\2\2\u0161\u0163\5:\36\2\u0162")
        buf.write("\u015e\3\2\2\2\u0162\u0161\3\2\2\2\u01639\3\2\2\2\u0164")
        buf.write("\u0165\7\7\2\2\u0165\u0166\b\36\1\2\u0166\u0167\5<\37")
        buf.write("\2\u0167;\3\2\2\2\u0168\u0169\5\"\22\2\u0169\u016a\5B")
        buf.write("\"\2\u016a\u016b\b\37\1\2\u016b\u0170\3\2\2\2\u016c\u016d")
        buf.write("\5B\"\2\u016d\u016e\b\37\1\2\u016e\u0170\3\2\2\2\u016f")
        buf.write("\u0168\3\2\2\2\u016f\u016c\3\2\2\2\u0170=\3\2\2\2\u0171")
        buf.write("\u0172\5,\27\2\u0172\u0173\7\67\2\2\u0173\u0174\b \1\2")
        buf.write("\u0174\u0175\5@!\2\u0175\u01a0\3\2\2\2\u0176\u0177\5,")
        buf.write("\27\2\u0177\u0184\7\67\2\2\u0178\u0179\7\17\2\2\u0179")
        buf.write("\u017a\78\2\2\u017a\u017b\7\21\2\2\u017b\u0185\b \1\2")
        buf.write("\u017c\u017d\7\17\2\2\u017d\u017e\78\2\2\u017e\u017f\b")
        buf.write(" \1\2\u017f\u0180\7\20\2\2\u0180\u0181\78\2\2\u0181\u0182")
        buf.write("\b \1\2\u0182\u0183\7\21\2\2\u0183\u0185\b \1\2\u0184")
        buf.write("\u0178\3\2\2\2\u0184\u017c\3\2\2\2\u0185\u0186\3\2\2\2")
        buf.write("\u0186\u0187\5@!\2\u0187\u01a0\3\2\2\2\u0188\u0189\5.")
        buf.write("\30\2\u0189\u018a\7\67\2\2\u018a\u018b\b \1\2\u018b\u018c")
        buf.write("\5@!\2\u018c\u01a0\3\2\2\2\u018d\u018e\5.\30\2\u018e\u019b")
        buf.write("\7\67\2\2\u018f\u0190\7\17\2\2\u0190\u0191\78\2\2\u0191")
        buf.write("\u0192\7\21\2\2\u0192\u019c\b \1\2\u0193\u0194\7\17\2")
        buf.write("\2\u0194\u0195\78\2\2\u0195\u0196\b \1\2\u0196\u0197\7")
        buf.write("\20\2\2\u0197\u0198\78\2\2\u0198\u0199\b \1\2\u0199\u019a")
        buf.write("\7\21\2\2\u019a\u019c\b \1\2\u019b\u018f\3\2\2\2\u019b")
        buf.write("\u0193\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u019e\5@!\2\u019e")
        buf.write("\u01a0\3\2\2\2\u019f\u0171\3\2\2\2\u019f\u0176\3\2\2\2")
        buf.write("\u019f\u0188\3\2\2\2\u019f\u018d\3\2\2\2\u01a0?\3\2\2")
        buf.write("\2\u01a1\u01a2\7\20\2\2\u01a2\u01a5\5> \2\u01a3\u01a5")
        buf.write("\3\2\2\2\u01a4\u01a1\3\2\2\2\u01a4\u01a3\3\2\2\2\u01a5")
        buf.write("A\3\2\2\2\u01a6\u01a7\7\f\2\2\u01a7\u01a8\5D#\2\u01a8")
        buf.write("C\3\2\2\2\u01a9\u01aa\5\64\33\2\u01aa\u01ab\5D#\2\u01ab")
        buf.write("\u01b1\3\2\2\2\u01ac\u01ad\5\64\33\2\u01ad\u01ae\7\23")
        buf.write("\2\2\u01ae\u01b1\3\2\2\2\u01af\u01b1\7\23\2\2\u01b0\u01a9")
        buf.write("\3\2\2\2\u01b0\u01ac\3\2\2\2\u01b0\u01af\3\2\2\2\u01b1")
        buf.write("E\3\2\2\2\u01b2\u01b3\7!\2\2\u01b3\u01b4\7\6\2\2\u01b4")
        buf.write("\u01b5\b$\1\2\u01b5\u01b6\5b\62\2\u01b6\u01b7\7\7\2\2")
        buf.write("\u01b7\u01b8\b$\1\2\u01b8\u01b9\7\4\2\2\u01b9G\3\2\2\2")
        buf.write("\u01ba\u01bb\7\67\2\2\u01bb\u01bc\b%\1\2\u01bc\u01bd\7")
        buf.write("\6\2\2\u01bd\u01bf\b%\1\2\u01be\u01c0\5b\62\2\u01bf\u01be")
        buf.write("\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c5\3\2\2\2\u01c1")
        buf.write("\u01c2\7\20\2\2\u01c2\u01c4\5b\62\2\u01c3\u01c1\3\2\2")
        buf.write("\2\u01c4\u01c7\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c5\u01c6")
        buf.write("\3\2\2\2\u01c6\u01c8\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c8")
        buf.write("\u01c9\7\7\2\2\u01c9\u01cc\b%\1\2\u01ca\u01cc\5J&\2\u01cb")
        buf.write("\u01ba\3\2\2\2\u01cb\u01ca\3\2\2\2\u01ccI\3\2\2\2\u01cd")
        buf.write("\u01ce\7\67\2\2\u01ce\u01cf\b&\1\2\u01cf\u01d0\7\25\2")
        buf.write("\2\u01d0\u01d1\7\67\2\2\u01d1\u01d2\b&\1\2\u01d2\u01d3")
        buf.write("\7\6\2\2\u01d3\u01d5\b&\1\2\u01d4\u01d6\5b\62\2\u01d5")
        buf.write("\u01d4\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01db\3\2\2\2")
        buf.write("\u01d7\u01d8\7\20\2\2\u01d8\u01da\5b\62\2\u01d9\u01d7")
        buf.write("\3\2\2\2\u01da\u01dd\3\2\2\2\u01db\u01d9\3\2\2\2\u01db")
        buf.write("\u01dc\3\2\2\2\u01dc\u01de\3\2\2\2\u01dd\u01db\3\2\2\2")
        buf.write("\u01de\u01df\7\7\2\2\u01df\u01e0\b&\1\2\u01e0K\3\2\2\2")
        buf.write("\u01e1\u01e2\5H%\2\u01e2\u01e3\7\4\2\2\u01e3M\3\2\2\2")
        buf.write("\u01e4\u01e5\7\"\2\2\u01e5\u01e6\7\6\2\2\u01e6\u01e7\b")
        buf.write("(\1\2\u01e7\u01e8\5P)\2\u01e8O\3\2\2\2\u01e9\u01ea\5\34")
        buf.write("\17\2\u01ea\u01eb\b)\1\2\u01eb\u01ec\5R*\2\u01ecQ\3\2")
        buf.write("\2\2\u01ed\u01ee\7\20\2\2\u01ee\u01f3\5P)\2\u01ef\u01f0")
        buf.write("\7\7\2\2\u01f0\u01f1\b*\1\2\u01f1\u01f3\7\4\2\2\u01f2")
        buf.write("\u01ed\3\2\2\2\u01f2\u01ef\3\2\2\2\u01f3S\3\2\2\2\u01f4")
        buf.write("\u01f5\7#\2\2\u01f5\u01f6\7\6\2\2\u01f6\u01f7\b+\1\2\u01f7")
        buf.write("\u01f8\5V,\2\u01f8U\3\2\2\2\u01f9\u01fa\5b\62\2\u01fa")
        buf.write("\u01fb\b,\1\2\u01fb\u01fc\5X-\2\u01fc\u0204\3\2\2\2\u01fd")
        buf.write("\u01fe\7:\2\2\u01fe\u01ff\b,\1\2\u01ff\u0204\5X-\2\u0200")
        buf.write("\u0201\5H%\2\u0201\u0202\5X-\2\u0202\u0204\3\2\2\2\u0203")
        buf.write("\u01f9\3\2\2\2\u0203\u01fd\3\2\2\2\u0203\u0200\3\2\2\2")
        buf.write("\u0204W\3\2\2\2\u0205\u0206\7\20\2\2\u0206\u020f\5V,\2")
        buf.write("\u0207\u0208\7=\2\2\u0208\u0209\7\7\2\2\u0209\u020a\b")
        buf.write("-\1\2\u020a\u020f\7\4\2\2\u020b\u020c\7\7\2\2\u020c\u020d")
        buf.write("\b-\1\2\u020d\u020f\7\4\2\2\u020e\u0205\3\2\2\2\u020e")
        buf.write("\u0207\3\2\2\2\u020e\u020b\3\2\2\2\u020fY\3\2\2\2\u0210")
        buf.write("\u0211\7$\2\2\u0211\u0212\7\6\2\2\u0212\u0213\b.\1\2\u0213")
        buf.write("\u0214\5b\62\2\u0214\u0215\7\7\2\2\u0215\u0216\b.\1\2")
        buf.write("\u0216\u0217\7%\2\2\u0217\u0218\5B\"\2\u0218\u0219\5\\")
        buf.write("/\2\u0219\u021a\b.\1\2\u021a[\3\2\2\2\u021b\u021c\7&\2")
        buf.write("\2\u021c\u021d\b/\1\2\u021d\u0220\5B\"\2\u021e\u0220\3")
        buf.write("\2\2\2\u021f\u021b\3\2\2\2\u021f\u021e\3\2\2\2\u0220]")
        buf.write("\3\2\2\2\u0221\u0222\7\'\2\2\u0222\u0223\b\60\1\2\u0223")
        buf.write("\u0224\7\6\2\2\u0224\u0225\b\60\1\2\u0225\u0226\5b\62")
        buf.write("\2\u0226\u0227\7\7\2\2\u0227\u0228\b\60\1\2\u0228\u0229")
        buf.write("\7(\2\2\u0229\u022a\5B\"\2\u022a\u022b\b\60\1\2\u022b")
        buf.write("_\3\2\2\2\u022c\u022d\7)\2\2\u022d\u022e\5\34\17\2\u022e")
        buf.write("\u022f\7*\2\2\u022f\u0230\5b\62\2\u0230\u0231\b\61\1\2")
        buf.write("\u0231\u0232\7(\2\2\u0232\u0233\b\61\1\2\u0233\u0234\5")
        buf.write("B\"\2\u0234\u0235\b\61\1\2\u0235a\3\2\2\2\u0236\u0237")
        buf.write("\7+\2\2\u0237\u0238\5f\64\2\u0238\u0239\b\62\1\2\u0239")
        buf.write("\u023a\5d\63\2\u023a\u023f\3\2\2\2\u023b\u023c\5f\64\2")
        buf.write("\u023c\u023d\5d\63\2\u023d\u023f\3\2\2\2\u023e\u0236\3")
        buf.write("\2\2\2\u023e\u023b\3\2\2\2\u023fc\3\2\2\2\u0240\u0241")
        buf.write("\7,\2\2\u0241\u0242\5b\62\2\u0242\u0245\b\63\1\2\u0243")
        buf.write("\u0246\5b\62\2\u0244\u0246\3\2\2\2\u0245\u0243\3\2\2\2")
        buf.write("\u0245\u0244\3\2\2\2\u0246\u0250\3\2\2\2\u0247\u0248\7")
        buf.write("-\2\2\u0248\u0249\5b\62\2\u0249\u024c\b\63\1\2\u024a\u024d")
        buf.write("\5b\62\2\u024b\u024d\3\2\2\2\u024c\u024a\3\2\2\2\u024c")
        buf.write("\u024b\3\2\2\2\u024d\u0250\3\2\2\2\u024e\u0250\3\2\2\2")
        buf.write("\u024f\u0240\3\2\2\2\u024f\u0247\3\2\2\2\u024f\u024e\3")
        buf.write("\2\2\2\u0250e\3\2\2\2\u0251\u0265\5h\65\2\u0252\u0253")
        buf.write("\7\13\2\2\u0253\u025f\b\64\1\2\u0254\u0255\7\t\2\2\u0255")
        buf.write("\u025f\b\64\1\2\u0256\u0257\7.\2\2\u0257\u025f\b\64\1")
        buf.write("\2\u0258\u0259\7/\2\2\u0259\u025f\b\64\1\2\u025a\u025b")
        buf.write("\7\60\2\2\u025b\u025f\b\64\1\2\u025c\u025d\7\61\2\2\u025d")
        buf.write("\u025f\b\64\1\2\u025e\u0252\3\2\2\2\u025e\u0254\3\2\2")
        buf.write("\2\u025e\u0256\3\2\2\2\u025e\u0258\3\2\2\2\u025e\u025a")
        buf.write("\3\2\2\2\u025e\u025c\3\2\2\2\u025f\u0260\3\2\2\2\u0260")
        buf.write("\u0261\5h\65\2\u0261\u0262\b\64\1\2\u0262\u0264\3\2\2")
        buf.write("\2\u0263\u025e\3\2\2\2\u0264\u0267\3\2\2\2\u0265\u0263")
        buf.write("\3\2\2\2\u0265\u0266\3\2\2\2\u0266g\3\2\2\2\u0267\u0265")
        buf.write("\3\2\2\2\u0268\u0274\5j\66\2\u0269\u026a\7\62\2\2\u026a")
        buf.write("\u026e\b\65\1\2\u026b\u026c\7\63\2\2\u026c\u026e\b\65")
        buf.write("\1\2\u026d\u0269\3\2\2\2\u026d\u026b\3\2\2\2\u026e\u026f")
        buf.write("\3\2\2\2\u026f\u0270\5j\66\2\u0270\u0271\b\65\1\2\u0271")
        buf.write("\u0273\3\2\2\2\u0272\u026d\3\2\2\2\u0273\u0276\3\2\2\2")
        buf.write("\u0274\u0272\3\2\2\2\u0274\u0275\3\2\2\2\u0275i\3\2\2")
        buf.write("\2\u0276\u0274\3\2\2\2\u0277\u0285\5l\67\2\u0278\u0279")
        buf.write("\7\64\2\2\u0279\u027f\b\66\1\2\u027a\u027b\7\65\2\2\u027b")
        buf.write("\u027f\b\66\1\2\u027c\u027d\7\66\2\2\u027d\u027f\b\66")
        buf.write("\1\2\u027e\u0278\3\2\2\2\u027e\u027a\3\2\2\2\u027e\u027c")
        buf.write("\3\2\2\2\u027f\u0280\3\2\2\2\u0280\u0281\5l\67\2\u0281")
        buf.write("\u0282\b\66\1\2\u0282\u0284\3\2\2\2\u0283\u027e\3\2\2")
        buf.write("\2\u0284\u0287\3\2\2\2\u0285\u0283\3\2\2\2\u0285\u0286")
        buf.write("\3\2\2\2\u0286k\3\2\2\2\u0287\u0285\3\2\2\2\u0288\u0289")
        buf.write("\7\6\2\2\u0289\u028a\b\67\1\2\u028a\u028b\5f\64\2\u028b")
        buf.write("\u028c\7\7\2\2\u028c\u028d\b\67\1\2\u028d\u0292\3\2\2")
        buf.write("\2\u028e\u0292\5p9\2\u028f\u0292\5H%\2\u0290\u0292\5n")
        buf.write("8\2\u0291\u0288\3\2\2\2\u0291\u028e\3\2\2\2\u0291\u028f")
        buf.write("\3\2\2\2\u0291\u0290\3\2\2\2\u0292m\3\2\2\2\u0293\u0298")
        buf.write("\5p9\2\u0294\u0295\7\63\2\2\u0295\u0296\b8\1\2\u0296\u0298")
        buf.write("\5p9\2\u0297\u0293\3\2\2\2\u0297\u0294\3\2\2\2\u0298o")
        buf.write("\3\2\2\2\u0299\u02a3\5\34\17\2\u029a\u029b\78\2\2\u029b")
        buf.write("\u02a3\b9\1\2\u029c\u029d\79\2\2\u029d\u02a3\b9\1\2\u029e")
        buf.write("\u029f\7:\2\2\u029f\u02a3\b9\1\2\u02a0\u02a1\7;\2\2\u02a1")
        buf.write("\u02a3\b9\1\2\u02a2\u0299\3\2\2\2\u02a2\u029a\3\2\2\2")
        buf.write("\u02a2\u029c\3\2\2\2\u02a2\u029e\3\2\2\2\u02a2\u02a0\3")
        buf.write("\2\2\2\u02a3q\3\2\2\2\64\u0083\u0099\u00a0\u00af\u00b2")
        buf.write("\u00bc\u00be\u00c7\u00d1\u00df\u00ec\u00fc\u0107\u0117")
        buf.write("\u011c\u012b\u012d\u0131\u0140\u014a\u0154\u0162\u016f")
        buf.write("\u0184\u019b\u019f\u01a4\u01b0\u01bf\u01c5\u01cb\u01d5")
        buf.write("\u01db\u01f2\u0203\u020e\u021f\u023e\u0245\u024c\u024f")
        buf.write("\u025e\u0265\u026d\u0274\u027e\u0285\u0291\u0297\u02a2")
        return buf.getvalue()


class BloonParser ( Parser ):

    grammarFileName = "Bloon.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "';'", "'main'", "'('", "')'", 
                     "'class'", "'<'", "'inherits'", "'>'", "'{'", "'attributes'", 
                     "':'", "'['", "','", "']'", "'methods'", "'}'", "'meth'", 
                     "'.'", "'vars'", "'='", "'int'", "'float'", "'char'", 
                     "'string'", "'+='", "'-='", "'*='", "'/='", "'void'", 
                     "'return'", "'read'", "'write'", "'cond'", "'then'", 
                     "'else'", "'while'", "'do'", "'floop'", "'to'", "'!'", 
                     "'and'", "'or'", "'>='", "'<='", "'=='", "'!='", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'\\c'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "CONST_INT", "CONST_FLOAT", "CONST_STR", 
                      "CONST_CHAR", "WHITESPACE", "CONTINUE" ]

    RULE_program = 0
    RULE_program_t = 1
    RULE_main = 2
    RULE_r_class = 3
    RULE_class_t = 4
    RULE_class_k = 5
    RULE_class_att = 6
    RULE_class_l = 7
    RULE_class_p = 8
    RULE_class_func = 9
    RULE_c_func_t = 10
    RULE_c_func_k = 11
    RULE_c_func_p = 12
    RULE_var = 13
    RULE_var_t = 14
    RULE_arr_idx = 15
    RULE_var_dec = 16
    RULE_var_dec_t = 17
    RULE_var_dec_l = 18
    RULE_assign = 19
    RULE_assign_t = 20
    RULE_var_type = 21
    RULE_custom_type = 22
    RULE_assign_op = 23
    RULE_type_meth = 24
    RULE_statement = 25
    RULE_func = 26
    RULE_func_t = 27
    RULE_func_k = 28
    RULE_func_p = 29
    RULE_param = 30
    RULE_param_t = 31
    RULE_block = 32
    RULE_block_t = 33
    RULE_r_return = 34
    RULE_call = 35
    RULE_call_class_meth = 36
    RULE_call_void = 37
    RULE_read = 38
    RULE_read_t = 39
    RULE_read_k = 40
    RULE_write = 41
    RULE_write_t = 42
    RULE_write_k = 43
    RULE_cond = 44
    RULE_cond_t = 45
    RULE_r_while = 46
    RULE_floop = 47
    RULE_super_exp = 48
    RULE_super_exp_t = 49
    RULE_expression = 50
    RULE_exp = 51
    RULE_term = 52
    RULE_factor = 53
    RULE_factor_t = 54
    RULE_var_const = 55

    ruleNames =  [ "program", "program_t", "main", "r_class", "class_t", 
                   "class_k", "class_att", "class_l", "class_p", "class_func", 
                   "c_func_t", "c_func_k", "c_func_p", "var", "var_t", "arr_idx", 
                   "var_dec", "var_dec_t", "var_dec_l", "assign", "assign_t", 
                   "var_type", "custom_type", "assign_op", "type_meth", 
                   "statement", "func", "func_t", "func_k", "func_p", "param", 
                   "param_t", "block", "block_t", "r_return", "call", "call_class_meth", 
                   "call_void", "read", "read_t", "read_k", "write", "write_t", 
                   "write_k", "cond", "cond_t", "r_while", "floop", "super_exp", 
                   "super_exp_t", "expression", "exp", "term", "factor", 
                   "factor_t", "var_const" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    T__47=48
    T__48=49
    T__49=50
    T__50=51
    T__51=52
    ID=53
    CONST_INT=54
    CONST_FLOAT=55
    CONST_STR=56
    CONST_CHAR=57
    WHITESPACE=58
    CONTINUE=59

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BloonParser.ID, 0)

        def program_t(self):
            return self.getTypedRuleContext(BloonParser.Program_tContext,0)


        def EOF(self):
            return self.getToken(BloonParser.EOF, 0)

        def getRuleIndex(self):
            return BloonParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = BloonParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(BloonParser.T__0)
            self.state = 113
            self.match(BloonParser.ID)
            self.state = 114
            self.match(BloonParser.T__1)
            self.state = 115
            self.program_t()
            compi.save_state(self)
            self.state = 117
            self.match(BloonParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Program_tContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def r_class(self):
            return self.getTypedRuleContext(BloonParser.R_classContext,0)


        def program_t(self):
            return self.getTypedRuleContext(BloonParser.Program_tContext,0)


        def var_dec(self):
            return self.getTypedRuleContext(BloonParser.Var_decContext,0)


        def func(self):
            return self.getTypedRuleContext(BloonParser.FuncContext,0)


        def main(self):
            return self.getTypedRuleContext(BloonParser.MainContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_program_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram_t" ):
                listener.enterProgram_t(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram_t" ):
                listener.exitProgram_t(self)




    def program_t(self):

        localctx = BloonParser.Program_tContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_program_t)
        try:
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.r_class()
                self.state = 120
                self.program_t()
                pass
            elif token in [BloonParser.T__19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 122
                self.var_dec()
                self.state = 123
                self.program_t()
                pass
            elif token in [BloonParser.T__21, BloonParser.T__22, BloonParser.T__23, BloonParser.T__24, BloonParser.T__29]:
                self.enterOuterAlt(localctx, 3)
                self.state = 125
                self.func()
                self.state = 126
                self.program_t()
                pass
            elif token in [BloonParser.T__2]:
                self.enterOuterAlt(localctx, 4)
                self.state = 128
                self.main()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(BloonParser.BlockContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain" ):
                listener.enterMain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain" ):
                listener.exitMain(self)




    def main(self):

        localctx = BloonParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_main)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(BloonParser.T__2)
            self.state = 132
            self.match(BloonParser.T__3)
            compi.open_parens()
            self.state = 134
            self.match(BloonParser.T__4)
            compi.close_parens(); compi.main_method()
            self.state = 136
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class R_classContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self):
            return self.getToken(BloonParser.ID, 0)

        def class_t(self):
            return self.getTypedRuleContext(BloonParser.Class_tContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_r_class

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterR_class" ):
                listener.enterR_class(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitR_class" ):
                listener.exitR_class(self)




    def r_class(self):

        localctx = BloonParser.R_classContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_r_class)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(BloonParser.T__5)
            self.state = 139
            localctx._ID = self.match(BloonParser.ID)
            compi.add_operand((None if localctx._ID is None else localctx._ID.text))
            self.state = 141
            self.class_t()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_tContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self):
            return self.getToken(BloonParser.ID, 0)

        def class_k(self):
            return self.getTypedRuleContext(BloonParser.Class_kContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_class_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_t" ):
                listener.enterClass_t(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_t" ):
                listener.exitClass_t(self)




    def class_t(self):

        localctx = BloonParser.Class_tContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_class_t)
        try:
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.match(BloonParser.T__6)
                self.state = 144
                self.match(BloonParser.T__7)
                self.state = 145
                localctx._ID = self.match(BloonParser.ID)
                self.state = 146
                self.match(BloonParser.T__8)
                compi.add_operand((None if localctx._ID is None else localctx._ID.text)); compi.define_class(True)
                self.state = 148
                self.class_k()
                pass
            elif token in [BloonParser.T__9]:
                self.enterOuterAlt(localctx, 2)
                compi.define_class()
                self.state = 150
                self.class_k()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_kContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_att(self):
            return self.getTypedRuleContext(BloonParser.Class_attContext,0)


        def class_l(self):
            return self.getTypedRuleContext(BloonParser.Class_lContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_class_k

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_k" ):
                listener.enterClass_k(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_k" ):
                listener.exitClass_k(self)




    def class_k(self):

        localctx = BloonParser.Class_kContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_class_k)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(BloonParser.T__9)
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__10]:
                self.state = 154
                self.match(BloonParser.T__10)
                self.state = 155
                self.match(BloonParser.T__11)
                self.state = 156
                self.class_att()
                pass
            elif token in [BloonParser.T__15, BloonParser.T__16]:
                self.state = 157
                self.class_l()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_attContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token
            self._CONST_INT = None # Token
            self._var_type = None # Var_typeContext

        def ID(self):
            return self.getToken(BloonParser.ID, 0)

        def CONST_INT(self, i:int=None):
            if i is None:
                return self.getTokens(BloonParser.CONST_INT)
            else:
                return self.getToken(BloonParser.CONST_INT, i)

        def class_att(self):
            return self.getTypedRuleContext(BloonParser.Class_attContext,0)


        def var_type(self):
            return self.getTypedRuleContext(BloonParser.Var_typeContext,0)


        def class_l(self):
            return self.getTypedRuleContext(BloonParser.Class_lContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_class_att

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_att" ):
                listener.enterClass_att(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_att" ):
                listener.exitClass_att(self)




    def class_att(self):

        localctx = BloonParser.Class_attContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_class_att)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 160
                localctx._ID = self.match(BloonParser.ID)
                compi.add_operand((None if localctx._ID is None else localctx._ID.text)); compi.increase_varCount()
                pass

            elif la_ == 2:
                self.state = 162
                localctx._ID = self.match(BloonParser.ID)
                self.state = 163
                self.match(BloonParser.T__12)
                self.state = 164
                localctx._CONST_INT = self.match(BloonParser.CONST_INT)
                compi.add_limit((None if localctx._CONST_INT is None else localctx._CONST_INT.text))
                self.state = 173
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BloonParser.T__13]:
                    self.state = 166
                    self.match(BloonParser.T__13)
                    self.state = 167
                    localctx._CONST_INT = self.match(BloonParser.CONST_INT)
                    compi.add_limit((None if localctx._CONST_INT is None else localctx._CONST_INT.text))
                    self.state = 169
                    self.match(BloonParser.T__14)
                    compi.add_operand((None if localctx._ID is None else localctx._ID.text), 2);
                    pass
                elif token in [BloonParser.T__14]:
                    self.state = 171
                    self.match(BloonParser.T__14)
                    compi.add_operand((None if localctx._ID is None else localctx._ID.text), 1)
                    pass
                else:
                    raise NoViableAltException(self)

                compi.increase_varCount()
                pass


            self.state = 188
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__13]:
                self.state = 178
                self.match(BloonParser.T__13)
                self.state = 179
                self.class_att()
                pass
            elif token in [BloonParser.T__11]:
                self.state = 180
                self.match(BloonParser.T__11)
                self.state = 181
                localctx._var_type = self.var_type()
                compi.define_attr((None if localctx._var_type is None else self._input.getText(localctx._var_type.start,localctx._var_type.stop)))
                self.state = 183
                self.match(BloonParser.T__1)
                self.state = 186
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BloonParser.ID]:
                    self.state = 184
                    self.class_att()
                    pass
                elif token in [BloonParser.T__15, BloonParser.T__16]:
                    self.state = 185
                    self.class_l()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_lContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_p(self):
            return self.getTypedRuleContext(BloonParser.Class_pContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_class_l

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_l" ):
                listener.enterClass_l(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_l" ):
                listener.exitClass_l(self)




    def class_l(self):

        localctx = BloonParser.Class_lContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_class_l)
        try:
            self.enterOuterAlt(localctx, 1)
            compi.add_att_to_parent_meths()
            self.state = 197
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__15]:
                self.state = 191
                self.match(BloonParser.T__15)
                self.state = 192
                self.match(BloonParser.T__11)
                self.state = 193
                self.class_p()
                pass
            elif token in [BloonParser.T__16]:
                self.state = 194
                self.match(BloonParser.T__16)
                self.state = 195
                self.match(BloonParser.T__1)
                compi.end_class()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_pContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_func(self):
            return self.getTypedRuleContext(BloonParser.Class_funcContext,0)


        def class_p(self):
            return self.getTypedRuleContext(BloonParser.Class_pContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_class_p

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_p" ):
                listener.enterClass_p(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_p" ):
                listener.exitClass_p(self)




    def class_p(self):

        localctx = BloonParser.Class_pContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_class_p)
        try:
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self.class_func()
                self.state = 200
                self.match(BloonParser.T__16)
                self.state = 201
                self.match(BloonParser.T__1)
                compi.end_class()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.class_func()
                self.state = 205
                self.class_p()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._type_meth = None # Type_methContext
            self._ID = None # Token

        def type_meth(self):
            return self.getTypedRuleContext(BloonParser.Type_methContext,0)


        def ID(self):
            return self.getToken(BloonParser.ID, 0)

        def c_func_t(self):
            return self.getTypedRuleContext(BloonParser.C_func_tContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_class_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_func" ):
                listener.enterClass_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_func" ):
                listener.exitClass_func(self)




    def class_func(self):

        localctx = BloonParser.Class_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_class_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            localctx._type_meth = self.type_meth()
            self.state = 210
            self.match(BloonParser.T__17)
            self.state = 211
            localctx._ID = self.match(BloonParser.ID)
            compi.define_method((None if localctx._type_meth is None else self._input.getText(localctx._type_meth.start,localctx._type_meth.stop)), (None if localctx._ID is None else localctx._ID.text), True)
            self.state = 213
            self.match(BloonParser.T__3)
            compi.open_parens()
            self.state = 215
            self.c_func_t()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class C_func_tContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(BloonParser.ParamContext,0)


        def c_func_k(self):
            return self.getTypedRuleContext(BloonParser.C_func_kContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_c_func_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterC_func_t" ):
                listener.enterC_func_t(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitC_func_t" ):
                listener.exitC_func_t(self)




    def c_func_t(self):

        localctx = BloonParser.C_func_tContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_c_func_t)
        try:
            self.state = 221
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__21, BloonParser.T__22, BloonParser.T__23, BloonParser.T__24, BloonParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.param()
                self.state = 218
                self.c_func_k()
                pass
            elif token in [BloonParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.c_func_k()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class C_func_kContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def c_func_p(self):
            return self.getTypedRuleContext(BloonParser.C_func_pContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_c_func_k

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterC_func_k" ):
                listener.enterC_func_k(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitC_func_k" ):
                listener.exitC_func_k(self)




    def c_func_k(self):

        localctx = BloonParser.C_func_kContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_c_func_k)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(BloonParser.T__4)
            compi.close_parens()
            self.state = 225
            self.c_func_p()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class C_func_pContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_dec(self):
            return self.getTypedRuleContext(BloonParser.Var_decContext,0)


        def block(self):
            return self.getTypedRuleContext(BloonParser.BlockContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_c_func_p

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterC_func_p" ):
                listener.enterC_func_p(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitC_func_p" ):
                listener.exitC_func_p(self)




    def c_func_p(self):

        localctx = BloonParser.C_func_pContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_c_func_p)
        try:
            self.state = 234
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.var_dec()
                self.state = 228
                self.block()
                compi.process_method()
                pass
            elif token in [BloonParser.T__9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 231
                self.block()
                compi.process_method()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self):
            return self.getToken(BloonParser.ID, 0)

        def var_t(self):
            return self.getTypedRuleContext(BloonParser.Var_tContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)




    def var(self):

        localctx = BloonParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            localctx._ID = self.match(BloonParser.ID)
            compi.add_operand((None if localctx._ID is None else localctx._ID.text))
            self.state = 238
            self.var_t()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_tContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def arr_idx(self):
            return self.getTypedRuleContext(BloonParser.Arr_idxContext,0)


        def var(self):
            return self.getTypedRuleContext(BloonParser.VarContext,0)


        def ID(self):
            return self.getToken(BloonParser.ID, 0)

        def getRuleIndex(self):
            return BloonParser.RULE_var_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_t" ):
                listener.enterVar_t(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_t" ):
                listener.exitVar_t(self)




    def var_t(self):

        localctx = BloonParser.Var_tContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_var_t)
        try:
            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.arr_idx()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.arr_idx()
                self.state = 242
                self.match(BloonParser.T__18)
                self.state = 243
                self.var()
                compi.get_var(True)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 246
                self.match(BloonParser.T__18)
                self.state = 247
                localctx._ID = self.match(BloonParser.ID)
                compi.add_operand((None if localctx._ID is None else localctx._ID.text)); compi.get_var(True)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                compi.get_var()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_idxContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BloonParser.ExpContext)
            else:
                return self.getTypedRuleContext(BloonParser.ExpContext,i)


        def getRuleIndex(self):
            return BloonParser.RULE_arr_idx

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArr_idx" ):
                listener.enterArr_idx(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArr_idx" ):
                listener.exitArr_idx(self)




    def arr_idx(self):

        localctx = BloonParser.Arr_idxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_arr_idx)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(BloonParser.T__12)
            self.state = 253
            self.exp()
            self.state = 261
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__13]:
                self.state = 254
                self.match(BloonParser.T__13)
                self.state = 255
                self.exp()
                self.state = 256
                self.match(BloonParser.T__14)
                compi.get_array_item(2)
                pass
            elif token in [BloonParser.T__14]:
                self.state = 259
                self.match(BloonParser.T__14)
                compi.get_array_item(1)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_dec_t(self):
            return self.getTypedRuleContext(BloonParser.Var_dec_tContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_var_dec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_dec" ):
                listener.enterVar_dec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_dec" ):
                listener.exitVar_dec(self)




    def var_dec(self):

        localctx = BloonParser.Var_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_var_dec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(BloonParser.T__19)
            self.state = 264
            self.var_dec_t()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_dec_tContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token
            self._CONST_INT = None # Token
            self._var_type = None # Var_typeContext
            self._custom_type = None # Custom_typeContext

        def ID(self):
            return self.getToken(BloonParser.ID, 0)

        def CONST_INT(self, i:int=None):
            if i is None:
                return self.getTokens(BloonParser.CONST_INT)
            else:
                return self.getToken(BloonParser.CONST_INT, i)

        def var_dec_t(self):
            return self.getTypedRuleContext(BloonParser.Var_dec_tContext,0)


        def var_type(self):
            return self.getTypedRuleContext(BloonParser.Var_typeContext,0)


        def var_dec_l(self):
            return self.getTypedRuleContext(BloonParser.Var_dec_lContext,0)


        def custom_type(self):
            return self.getTypedRuleContext(BloonParser.Custom_typeContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_var_dec_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_dec_t" ):
                listener.enterVar_dec_t(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_dec_t" ):
                listener.exitVar_dec_t(self)




    def var_dec_t(self):

        localctx = BloonParser.Var_dec_tContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_var_dec_t)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 266
                localctx._ID = self.match(BloonParser.ID)
                self.state = 267
                self.match(BloonParser.T__12)
                self.state = 268
                localctx._CONST_INT = self.match(BloonParser.CONST_INT)
                compi.add_limit((None if localctx._CONST_INT is None else localctx._CONST_INT.text))
                self.state = 277
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BloonParser.T__13]:
                    self.state = 270
                    self.match(BloonParser.T__13)
                    self.state = 271
                    localctx._CONST_INT = self.match(BloonParser.CONST_INT)
                    compi.add_limit((None if localctx._CONST_INT is None else localctx._CONST_INT.text))
                    self.state = 273
                    self.match(BloonParser.T__14)
                    compi.add_operand((None if localctx._ID is None else localctx._ID.text), 2);
                    pass
                elif token in [BloonParser.T__14]:
                    self.state = 275
                    self.match(BloonParser.T__14)
                    compi.add_operand((None if localctx._ID is None else localctx._ID.text), 1)
                    pass
                else:
                    raise NoViableAltException(self)

                compi.increase_varCount()
                pass

            elif la_ == 2:
                self.state = 280
                localctx._ID = self.match(BloonParser.ID)
                compi.add_operand((None if localctx._ID is None else localctx._ID.text)); compi.increase_varCount()
                pass


            self.state = 299
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__13]:
                self.state = 284
                self.match(BloonParser.T__13)
                self.state = 285
                self.var_dec_t()
                pass
            elif token in [BloonParser.T__11]:
                self.state = 286
                self.match(BloonParser.T__11)
                self.state = 297
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BloonParser.T__21, BloonParser.T__22, BloonParser.T__23, BloonParser.T__24]:
                    self.state = 287
                    localctx._var_type = self.var_type()
                    compi.define_var((None if localctx._var_type is None else self._input.getText(localctx._var_type.start,localctx._var_type.stop)))
                    self.state = 289
                    self.match(BloonParser.T__1)
                    self.state = 290
                    self.var_dec_l()
                    pass
                elif token in [BloonParser.ID]:
                    self.state = 292
                    localctx._custom_type = self.custom_type()
                    compi.define_var((None if localctx._custom_type is None else self._input.getText(localctx._custom_type.start,localctx._custom_type.stop)))
                    self.state = 294
                    self.match(BloonParser.T__1)
                    self.state = 295
                    self.var_dec_l()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_dec_lContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_dec_t(self):
            return self.getTypedRuleContext(BloonParser.Var_dec_tContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_var_dec_l

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_dec_l" ):
                listener.enterVar_dec_l(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_dec_l" ):
                listener.exitVar_dec_l(self)




    def var_dec_l(self):

        localctx = BloonParser.Var_dec_lContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_var_dec_l)
        try:
            self.state = 303
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 301
                self.var_dec_t()
                pass
            elif token in [BloonParser.T__2, BloonParser.T__5, BloonParser.T__9, BloonParser.T__19, BloonParser.T__21, BloonParser.T__22, BloonParser.T__23, BloonParser.T__24, BloonParser.T__29]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(BloonParser.VarContext,0)


        def assign_t(self):
            return self.getTypedRuleContext(BloonParser.Assign_tContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)




    def assign(self):

        localctx = BloonParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.var()
            self.state = 306
            self.assign_t()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_tContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._assign_op = None # Assign_opContext

        def super_exp(self):
            return self.getTypedRuleContext(BloonParser.Super_expContext,0)


        def assign_op(self):
            return self.getTypedRuleContext(BloonParser.Assign_opContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_assign_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_t" ):
                listener.enterAssign_t(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_t" ):
                listener.exitAssign_t(self)




    def assign_t(self):

        localctx = BloonParser.Assign_tContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_assign_t)
        try:
            self.state = 318
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 308
                self.match(BloonParser.T__20)
                self.state = 309
                self.super_exp()
                compi.assign_var()
                self.state = 311
                self.match(BloonParser.T__1)
                pass
            elif token in [BloonParser.T__25, BloonParser.T__26, BloonParser.T__27, BloonParser.T__28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                localctx._assign_op = self.assign_op()
                self.state = 314
                self.super_exp()
                compi.arithmetic_assign((None if localctx._assign_op is None else self._input.getText(localctx._assign_op.start,localctx._assign_op.stop)))
                self.state = 316
                self.match(BloonParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BloonParser.RULE_var_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_type" ):
                listener.enterVar_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_type" ):
                listener.exitVar_type(self)




    def var_type(self):

        localctx = BloonParser.Var_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_var_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BloonParser.T__21) | (1 << BloonParser.T__22) | (1 << BloonParser.T__23) | (1 << BloonParser.T__24))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Custom_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BloonParser.ID, 0)

        def getRuleIndex(self):
            return BloonParser.RULE_custom_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCustom_type" ):
                listener.enterCustom_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCustom_type" ):
                listener.exitCustom_type(self)




    def custom_type(self):

        localctx = BloonParser.Custom_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_custom_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.match(BloonParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BloonParser.RULE_assign_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_op" ):
                listener.enterAssign_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_op" ):
                listener.exitAssign_op(self)




    def assign_op(self):

        localctx = BloonParser.Assign_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_assign_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BloonParser.T__25) | (1 << BloonParser.T__26) | (1 << BloonParser.T__27) | (1 << BloonParser.T__28))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_methContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_type(self):
            return self.getTypedRuleContext(BloonParser.Var_typeContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_type_meth

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_meth" ):
                listener.enterType_meth(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_meth" ):
                listener.exitType_meth(self)




    def type_meth(self):

        localctx = BloonParser.Type_methContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_type_meth)
        try:
            self.state = 328
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__21, BloonParser.T__22, BloonParser.T__23, BloonParser.T__24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.var_type()
                pass
            elif token in [BloonParser.T__29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 327
                self.match(BloonParser.T__29)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(BloonParser.AssignContext,0)


        def cond(self):
            return self.getTypedRuleContext(BloonParser.CondContext,0)


        def r_return(self):
            return self.getTypedRuleContext(BloonParser.R_returnContext,0)


        def read(self):
            return self.getTypedRuleContext(BloonParser.ReadContext,0)


        def write(self):
            return self.getTypedRuleContext(BloonParser.WriteContext,0)


        def r_while(self):
            return self.getTypedRuleContext(BloonParser.R_whileContext,0)


        def floop(self):
            return self.getTypedRuleContext(BloonParser.FloopContext,0)


        def call_void(self):
            return self.getTypedRuleContext(BloonParser.Call_voidContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = BloonParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_statement)
        try:
            self.state = 338
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self.assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 331
                self.cond()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 332
                self.r_return()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 333
                self.read()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 334
                self.write()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 335
                self.r_while()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 336
                self.floop()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 337
                self.call_void()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._type_meth = None # Type_methContext
            self._ID = None # Token

        def type_meth(self):
            return self.getTypedRuleContext(BloonParser.Type_methContext,0)


        def ID(self):
            return self.getToken(BloonParser.ID, 0)

        def func_t(self):
            return self.getTypedRuleContext(BloonParser.Func_tContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc" ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc" ):
                listener.exitFunc(self)




    def func(self):

        localctx = BloonParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            localctx._type_meth = self.type_meth()
            self.state = 341
            self.match(BloonParser.T__17)
            self.state = 342
            localctx._ID = self.match(BloonParser.ID)
            compi.define_method((None if localctx._type_meth is None else self._input.getText(localctx._type_meth.start,localctx._type_meth.stop)), (None if localctx._ID is None else localctx._ID.text))
            self.state = 344
            self.match(BloonParser.T__3)
            compi.open_parens()
            self.state = 346
            self.func_t()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_tContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(BloonParser.ParamContext,0)


        def func_k(self):
            return self.getTypedRuleContext(BloonParser.Func_kContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_func_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_t" ):
                listener.enterFunc_t(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_t" ):
                listener.exitFunc_t(self)




    def func_t(self):

        localctx = BloonParser.Func_tContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_func_t)
        try:
            self.state = 352
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__21, BloonParser.T__22, BloonParser.T__23, BloonParser.T__24, BloonParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.param()
                self.state = 349
                self.func_k()
                pass
            elif token in [BloonParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 351
                self.func_k()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_kContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_p(self):
            return self.getTypedRuleContext(BloonParser.Func_pContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_func_k

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_k" ):
                listener.enterFunc_k(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_k" ):
                listener.exitFunc_k(self)




    def func_k(self):

        localctx = BloonParser.Func_kContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_func_k)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.match(BloonParser.T__4)
            compi.close_parens()
            self.state = 356
            self.func_p()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_pContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_dec(self):
            return self.getTypedRuleContext(BloonParser.Var_decContext,0)


        def block(self):
            return self.getTypedRuleContext(BloonParser.BlockContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_func_p

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_p" ):
                listener.enterFunc_p(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_p" ):
                listener.exitFunc_p(self)




    def func_p(self):

        localctx = BloonParser.Func_pContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_func_p)
        try:
            self.state = 365
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                self.var_dec()
                self.state = 359
                self.block()
                compi.process_method()
                pass
            elif token in [BloonParser.T__9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
                self.block()
                compi.process_method()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._var_type = None # Var_typeContext
            self._ID = None # Token
            self._CONST_INT = None # Token
            self._custom_type = None # Custom_typeContext

        def var_type(self):
            return self.getTypedRuleContext(BloonParser.Var_typeContext,0)


        def ID(self):
            return self.getToken(BloonParser.ID, 0)

        def param_t(self):
            return self.getTypedRuleContext(BloonParser.Param_tContext,0)


        def CONST_INT(self, i:int=None):
            if i is None:
                return self.getTokens(BloonParser.CONST_INT)
            else:
                return self.getToken(BloonParser.CONST_INT, i)

        def custom_type(self):
            return self.getTypedRuleContext(BloonParser.Custom_typeContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)




    def param(self):

        localctx = BloonParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_param)
        try:
            self.state = 413
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 367
                localctx._var_type = self.var_type()
                self.state = 368
                localctx._ID = self.match(BloonParser.ID)
                compi.define_param((None if localctx._var_type is None else self._input.getText(localctx._var_type.start,localctx._var_type.stop)), (None if localctx._ID is None else localctx._ID.text))
                self.state = 370
                self.param_t()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 372
                localctx._var_type = self.var_type()
                self.state = 373
                localctx._ID = self.match(BloonParser.ID)
                self.state = 386
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                if la_ == 1:
                    self.state = 374
                    self.match(BloonParser.T__12)
                    self.state = 375
                    localctx._CONST_INT = self.match(BloonParser.CONST_INT)
                    self.state = 376
                    self.match(BloonParser.T__14)
                    compi.add_limit((None if localctx._CONST_INT is None else localctx._CONST_INT.text)); compi.define_param((None if localctx._var_type is None else self._input.getText(localctx._var_type.start,localctx._var_type.stop)), (None if localctx._ID is None else localctx._ID.text), 1)
                    pass

                elif la_ == 2:
                    self.state = 378
                    self.match(BloonParser.T__12)
                    self.state = 379
                    localctx._CONST_INT = self.match(BloonParser.CONST_INT)
                    compi.add_limit((None if localctx._CONST_INT is None else localctx._CONST_INT.text))
                    self.state = 381
                    self.match(BloonParser.T__13)
                    self.state = 382
                    localctx._CONST_INT = self.match(BloonParser.CONST_INT)
                    compi.add_limit((None if localctx._CONST_INT is None else localctx._CONST_INT.text))
                    self.state = 384
                    self.match(BloonParser.T__14)
                    compi.define_param((None if localctx._var_type is None else self._input.getText(localctx._var_type.start,localctx._var_type.stop)), (None if localctx._ID is None else localctx._ID.text), 2)
                    pass


                self.state = 388
                self.param_t()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 390
                localctx._custom_type = self.custom_type()
                self.state = 391
                localctx._ID = self.match(BloonParser.ID)
                compi.define_param((None if localctx._custom_type is None else self._input.getText(localctx._custom_type.start,localctx._custom_type.stop)), (None if localctx._ID is None else localctx._ID.text))
                self.state = 393
                self.param_t()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 395
                localctx._custom_type = self.custom_type()
                self.state = 396
                localctx._ID = self.match(BloonParser.ID)
                self.state = 409
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 397
                    self.match(BloonParser.T__12)
                    self.state = 398
                    localctx._CONST_INT = self.match(BloonParser.CONST_INT)
                    self.state = 399
                    self.match(BloonParser.T__14)
                    compi.add_limit((None if localctx._CONST_INT is None else localctx._CONST_INT.text)); compi.define_param((None if localctx._custom_type is None else self._input.getText(localctx._custom_type.start,localctx._custom_type.stop)), (None if localctx._ID is None else localctx._ID.text), 1)
                    pass

                elif la_ == 2:
                    self.state = 401
                    self.match(BloonParser.T__12)
                    self.state = 402
                    localctx._CONST_INT = self.match(BloonParser.CONST_INT)
                    compi.add_limit((None if localctx._CONST_INT is None else localctx._CONST_INT.text))
                    self.state = 404
                    self.match(BloonParser.T__13)
                    self.state = 405
                    localctx._CONST_INT = self.match(BloonParser.CONST_INT)
                    compi.add_limit((None if localctx._CONST_INT is None else localctx._CONST_INT.text))
                    self.state = 407
                    self.match(BloonParser.T__14)
                    compi.define_param((None if localctx._custom_type is None else self._input.getText(localctx._custom_type.start,localctx._custom_type.stop)), (None if localctx._ID is None else localctx._ID.text), 2)
                    pass


                self.state = 411
                self.param_t()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_tContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(BloonParser.ParamContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_param_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam_t" ):
                listener.enterParam_t(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam_t" ):
                listener.exitParam_t(self)




    def param_t(self):

        localctx = BloonParser.Param_tContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_param_t)
        try:
            self.state = 418
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 415
                self.match(BloonParser.T__13)
                self.state = 416
                self.param()
                pass
            elif token in [BloonParser.T__4]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_t(self):
            return self.getTypedRuleContext(BloonParser.Block_tContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = BloonParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.match(BloonParser.T__9)
            self.state = 421
            self.block_t()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_tContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(BloonParser.StatementContext,0)


        def block_t(self):
            return self.getTypedRuleContext(BloonParser.Block_tContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_block_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_t" ):
                listener.enterBlock_t(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_t" ):
                listener.exitBlock_t(self)




    def block_t(self):

        localctx = BloonParser.Block_tContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_block_t)
        try:
            self.state = 430
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 423
                self.statement()
                self.state = 424
                self.block_t()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 426
                self.statement()
                self.state = 427
                self.match(BloonParser.T__16)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 429
                self.match(BloonParser.T__16)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class R_returnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def super_exp(self):
            return self.getTypedRuleContext(BloonParser.Super_expContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_r_return

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterR_return" ):
                listener.enterR_return(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitR_return" ):
                listener.exitR_return(self)




    def r_return(self):

        localctx = BloonParser.R_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_r_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.match(BloonParser.T__30)
            self.state = 433
            self.match(BloonParser.T__3)
            compi.open_parens()
            self.state = 435
            self.super_exp()
            self.state = 436
            self.match(BloonParser.T__4)
            compi.close_parens(); compi.rtn_stmt()
            self.state = 438
            self.match(BloonParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self):
            return self.getToken(BloonParser.ID, 0)

        def super_exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BloonParser.Super_expContext)
            else:
                return self.getTypedRuleContext(BloonParser.Super_expContext,i)


        def call_class_meth(self):
            return self.getTypedRuleContext(BloonParser.Call_class_methContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)




    def call(self):

        localctx = BloonParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.state = 457
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 440
                localctx._ID = self.match(BloonParser.ID)
                compi.verify_method((None if localctx._ID is None else localctx._ID.text))
                self.state = 442
                self.match(BloonParser.T__3)
                compi.open_parens()
                self.state = 445
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BloonParser.T__3) | (1 << BloonParser.T__40) | (1 << BloonParser.T__48) | (1 << BloonParser.ID) | (1 << BloonParser.CONST_INT) | (1 << BloonParser.CONST_FLOAT) | (1 << BloonParser.CONST_STR) | (1 << BloonParser.CONST_CHAR))) != 0):
                    self.state = 444
                    self.super_exp()


                self.state = 451
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BloonParser.T__13:
                    self.state = 447
                    self.match(BloonParser.T__13)
                    self.state = 448
                    self.super_exp()
                    self.state = 453
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 454
                self.match(BloonParser.T__4)
                compi.close_parens(); compi.call_method((None if localctx._ID is None else localctx._ID.text))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 456
                self.call_class_meth()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_class_methContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BloonParser.ID)
            else:
                return self.getToken(BloonParser.ID, i)

        def super_exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BloonParser.Super_expContext)
            else:
                return self.getTypedRuleContext(BloonParser.Super_expContext,i)


        def getRuleIndex(self):
            return BloonParser.RULE_call_class_meth

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall_class_meth" ):
                listener.enterCall_class_meth(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall_class_meth" ):
                listener.exitCall_class_meth(self)




    def call_class_meth(self):

        localctx = BloonParser.Call_class_methContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_call_class_meth)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            localctx._ID = self.match(BloonParser.ID)
            compi.add_operand((None if localctx._ID is None else localctx._ID.text))
            self.state = 461
            self.match(BloonParser.T__18)
            self.state = 462
            localctx._ID = self.match(BloonParser.ID)
            compi.verify_method((None if localctx._ID is None else localctx._ID.text), True)
            self.state = 464
            self.match(BloonParser.T__3)
            compi.open_parens()
            self.state = 467
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BloonParser.T__3) | (1 << BloonParser.T__40) | (1 << BloonParser.T__48) | (1 << BloonParser.ID) | (1 << BloonParser.CONST_INT) | (1 << BloonParser.CONST_FLOAT) | (1 << BloonParser.CONST_STR) | (1 << BloonParser.CONST_CHAR))) != 0):
                self.state = 466
                self.super_exp()


            self.state = 473
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BloonParser.T__13:
                self.state = 469
                self.match(BloonParser.T__13)
                self.state = 470
                self.super_exp()
                self.state = 475
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 476
            self.match(BloonParser.T__4)
            compi.close_parens(); compi.call_method((None if localctx._ID is None else localctx._ID.text), True)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_voidContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call(self):
            return self.getTypedRuleContext(BloonParser.CallContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_call_void

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall_void" ):
                listener.enterCall_void(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall_void" ):
                listener.exitCall_void(self)




    def call_void(self):

        localctx = BloonParser.Call_voidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_call_void)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
            self.call()
            self.state = 480
            self.match(BloonParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def read_t(self):
            return self.getTypedRuleContext(BloonParser.Read_tContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_read

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead" ):
                listener.enterRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead" ):
                listener.exitRead(self)




    def read(self):

        localctx = BloonParser.ReadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_read)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            self.match(BloonParser.T__31)
            self.state = 483
            self.match(BloonParser.T__3)
            compi.open_parens()
            self.state = 485
            self.read_t()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Read_tContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(BloonParser.VarContext,0)


        def read_k(self):
            return self.getTypedRuleContext(BloonParser.Read_kContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_read_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead_t" ):
                listener.enterRead_t(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead_t" ):
                listener.exitRead_t(self)




    def read_t(self):

        localctx = BloonParser.Read_tContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_read_t)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            self.var()
            compi.call_method('read')
            self.state = 489
            self.read_k()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Read_kContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def read_t(self):
            return self.getTypedRuleContext(BloonParser.Read_tContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_read_k

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead_k" ):
                listener.enterRead_k(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead_k" ):
                listener.exitRead_k(self)




    def read_k(self):

        localctx = BloonParser.Read_kContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_read_k)
        try:
            self.state = 496
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 491
                self.match(BloonParser.T__13)
                self.state = 492
                self.read_t()
                pass
            elif token in [BloonParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 493
                self.match(BloonParser.T__4)
                compi.close_parens()
                self.state = 495
                self.match(BloonParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def write_t(self):
            return self.getTypedRuleContext(BloonParser.Write_tContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_write

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrite" ):
                listener.enterWrite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrite" ):
                listener.exitWrite(self)




    def write(self):

        localctx = BloonParser.WriteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_write)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self.match(BloonParser.T__32)
            self.state = 499
            self.match(BloonParser.T__3)
            compi.open_parens()
            self.state = 501
            self.write_t()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Write_tContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._CONST_STR = None # Token

        def super_exp(self):
            return self.getTypedRuleContext(BloonParser.Super_expContext,0)


        def write_k(self):
            return self.getTypedRuleContext(BloonParser.Write_kContext,0)


        def CONST_STR(self):
            return self.getToken(BloonParser.CONST_STR, 0)

        def call(self):
            return self.getTypedRuleContext(BloonParser.CallContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_write_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrite_t" ):
                listener.enterWrite_t(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrite_t" ):
                listener.exitWrite_t(self)




    def write_t(self):

        localctx = BloonParser.Write_tContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_write_t)
        try:
            self.state = 513
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 503
                self.super_exp()
                compi.call_method('write')
                self.state = 505
                self.write_k()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 507
                localctx._CONST_STR = self.match(BloonParser.CONST_STR)
                compi.get_const((None if localctx._CONST_STR is None else localctx._CONST_STR.text), "string"); compi.call_method('write')
                self.state = 509
                self.write_k()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 510
                self.call()
                self.state = 511
                self.write_k()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Write_kContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def write_t(self):
            return self.getTypedRuleContext(BloonParser.Write_tContext,0)


        def CONTINUE(self):
            return self.getToken(BloonParser.CONTINUE, 0)

        def getRuleIndex(self):
            return BloonParser.RULE_write_k

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrite_k" ):
                listener.enterWrite_k(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrite_k" ):
                listener.exitWrite_k(self)




    def write_k(self):

        localctx = BloonParser.Write_kContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_write_k)
        try:
            self.state = 524
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 515
                self.match(BloonParser.T__13)
                self.state = 516
                self.write_t()
                pass
            elif token in [BloonParser.CONTINUE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 517
                self.match(BloonParser.CONTINUE)
                self.state = 518
                self.match(BloonParser.T__4)
                compi.close_parens()
                self.state = 520
                self.match(BloonParser.T__1)
                pass
            elif token in [BloonParser.T__4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 521
                self.match(BloonParser.T__4)
                compi.close_parens(); compi.new_write()
                self.state = 523
                self.match(BloonParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def super_exp(self):
            return self.getTypedRuleContext(BloonParser.Super_expContext,0)


        def block(self):
            return self.getTypedRuleContext(BloonParser.BlockContext,0)


        def cond_t(self):
            return self.getTypedRuleContext(BloonParser.Cond_tContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_cond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond" ):
                listener.enterCond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond" ):
                listener.exitCond(self)




    def cond(self):

        localctx = BloonParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_cond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
            self.match(BloonParser.T__33)
            self.state = 527
            self.match(BloonParser.T__3)
            compi.open_parens()
            self.state = 529
            self.super_exp()
            self.state = 530
            self.match(BloonParser.T__4)
            compi.close_parens(); compi.condition()
            self.state = 532
            self.match(BloonParser.T__34)
            self.state = 533
            self.block()
            self.state = 534
            self.cond_t()
            compi.end_condition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cond_tContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(BloonParser.BlockContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_cond_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond_t" ):
                listener.enterCond_t(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond_t" ):
                listener.exitCond_t(self)




    def cond_t(self):

        localctx = BloonParser.Cond_tContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_cond_t)
        try:
            self.state = 541
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 537
                self.match(BloonParser.T__35)
                compi.else_condition()
                self.state = 539
                self.block()
                pass
            elif token in [BloonParser.T__16, BloonParser.T__30, BloonParser.T__31, BloonParser.T__32, BloonParser.T__33, BloonParser.T__36, BloonParser.T__38, BloonParser.ID]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class R_whileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def super_exp(self):
            return self.getTypedRuleContext(BloonParser.Super_expContext,0)


        def block(self):
            return self.getTypedRuleContext(BloonParser.BlockContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_r_while

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterR_while" ):
                listener.enterR_while(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitR_while" ):
                listener.exitR_while(self)




    def r_while(self):

        localctx = BloonParser.R_whileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_r_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 543
            self.match(BloonParser.T__36)
            compi.while_condition()
            self.state = 545
            self.match(BloonParser.T__3)
            compi.open_parens()
            self.state = 547
            self.super_exp()
            self.state = 548
            self.match(BloonParser.T__4)
            compi.close_parens(); compi.while_expression()
            self.state = 550
            self.match(BloonParser.T__37)
            self.state = 551
            self.block()
            compi.while_end()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FloopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(BloonParser.VarContext,0)


        def super_exp(self):
            return self.getTypedRuleContext(BloonParser.Super_expContext,0)


        def block(self):
            return self.getTypedRuleContext(BloonParser.BlockContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_floop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloop" ):
                listener.enterFloop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloop" ):
                listener.exitFloop(self)




    def floop(self):

        localctx = BloonParser.FloopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_floop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 554
            self.match(BloonParser.T__38)
            self.state = 555
            self.var()
            self.state = 556
            self.match(BloonParser.T__39)
            self.state = 557
            self.super_exp()
            compi.floop()
            self.state = 559
            self.match(BloonParser.T__37)
            compi.floop_check()
            self.state = 561
            self.block()
            compi.floop_end()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Super_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(BloonParser.ExpressionContext,0)


        def super_exp_t(self):
            return self.getTypedRuleContext(BloonParser.Super_exp_tContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_super_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuper_exp" ):
                listener.enterSuper_exp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuper_exp" ):
                listener.exitSuper_exp(self)




    def super_exp(self):

        localctx = BloonParser.Super_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_super_exp)
        try:
            self.state = 572
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 564
                self.match(BloonParser.T__40)
                self.state = 565
                self.expression()
                compi.logic_operation('NOT')
                self.state = 567
                self.super_exp_t()
                pass
            elif token in [BloonParser.T__3, BloonParser.T__48, BloonParser.ID, BloonParser.CONST_INT, BloonParser.CONST_FLOAT, BloonParser.CONST_STR, BloonParser.CONST_CHAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 569
                self.expression()
                self.state = 570
                self.super_exp_t()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Super_exp_tContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def super_exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BloonParser.Super_expContext)
            else:
                return self.getTypedRuleContext(BloonParser.Super_expContext,i)


        def getRuleIndex(self):
            return BloonParser.RULE_super_exp_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuper_exp_t" ):
                listener.enterSuper_exp_t(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuper_exp_t" ):
                listener.exitSuper_exp_t(self)




    def super_exp_t(self):

        localctx = BloonParser.Super_exp_tContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_super_exp_t)
        try:
            self.state = 589
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 574
                self.match(BloonParser.T__41)
                self.state = 575
                self.super_exp()
                compi.logic_operation('AND')
                self.state = 579
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                if la_ == 1:
                    self.state = 577
                    self.super_exp()
                    pass

                elif la_ == 2:
                    pass


                pass
            elif token in [BloonParser.T__42]:
                self.enterOuterAlt(localctx, 2)
                self.state = 581
                self.match(BloonParser.T__42)
                self.state = 582
                self.super_exp()
                compi.logic_operation('OR')
                self.state = 586
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                if la_ == 1:
                    self.state = 584
                    self.super_exp()
                    pass

                elif la_ == 2:
                    pass


                pass
            elif token in [BloonParser.T__1, BloonParser.T__3, BloonParser.T__4, BloonParser.T__13, BloonParser.T__37, BloonParser.T__40, BloonParser.T__48, BloonParser.ID, BloonParser.CONST_INT, BloonParser.CONST_FLOAT, BloonParser.CONST_STR, BloonParser.CONST_CHAR, BloonParser.CONTINUE]:
                self.enterOuterAlt(localctx, 3)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BloonParser.ExpContext)
            else:
                return self.getTypedRuleContext(BloonParser.ExpContext,i)


        def getRuleIndex(self):
            return BloonParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = BloonParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 591
            self.exp()
            self.state = 611
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BloonParser.T__6) | (1 << BloonParser.T__8) | (1 << BloonParser.T__43) | (1 << BloonParser.T__44) | (1 << BloonParser.T__45) | (1 << BloonParser.T__46))) != 0):
                self.state = 604
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BloonParser.T__8]:
                    self.state = 592
                    self.match(BloonParser.T__8)
                    compi.add_op('>')
                    pass
                elif token in [BloonParser.T__6]:
                    self.state = 594
                    self.match(BloonParser.T__6)
                    compi.add_op('<')
                    pass
                elif token in [BloonParser.T__43]:
                    self.state = 596
                    self.match(BloonParser.T__43)
                    compi.add_op('>=')
                    pass
                elif token in [BloonParser.T__44]:
                    self.state = 598
                    self.match(BloonParser.T__44)
                    compi.add_op('<=')
                    pass
                elif token in [BloonParser.T__45]:
                    self.state = 600
                    self.match(BloonParser.T__45)
                    compi.add_op('==')
                    pass
                elif token in [BloonParser.T__46]:
                    self.state = 602
                    self.match(BloonParser.T__46)
                    compi.add_op('!=')
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 606
                self.exp()
                compi.arithmetic_operation('>', '<', '>=', '<=', '==', '!=')
                self.state = 613
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BloonParser.TermContext)
            else:
                return self.getTypedRuleContext(BloonParser.TermContext,i)


        def getRuleIndex(self):
            return BloonParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)




    def exp(self):

        localctx = BloonParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 614
            self.term()
            self.state = 626
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 619
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [BloonParser.T__47]:
                        self.state = 615
                        self.match(BloonParser.T__47)
                        compi.add_op('+')
                        pass
                    elif token in [BloonParser.T__48]:
                        self.state = 617
                        self.match(BloonParser.T__48)
                        compi.add_op('-')
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 621
                    self.term()
                    compi.arithmetic_operation('+', '-') 
                self.state = 628
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BloonParser.FactorContext)
            else:
                return self.getTypedRuleContext(BloonParser.FactorContext,i)


        def getRuleIndex(self):
            return BloonParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = BloonParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 629
            self.factor()
            self.state = 643
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BloonParser.T__49) | (1 << BloonParser.T__50) | (1 << BloonParser.T__51))) != 0):
                self.state = 636
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BloonParser.T__49]:
                    self.state = 630
                    self.match(BloonParser.T__49)
                    compi.add_op('*')
                    pass
                elif token in [BloonParser.T__50]:
                    self.state = 632
                    self.match(BloonParser.T__50)
                    compi.add_op('/')
                    pass
                elif token in [BloonParser.T__51]:
                    self.state = 634
                    self.match(BloonParser.T__51)
                    compi.add_op('%')
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 638
                self.factor()
                compi.arithmetic_operation('*', '/', '%')
                self.state = 645
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(BloonParser.ExpressionContext,0)


        def var_const(self):
            return self.getTypedRuleContext(BloonParser.Var_constContext,0)


        def call(self):
            return self.getTypedRuleContext(BloonParser.CallContext,0)


        def factor_t(self):
            return self.getTypedRuleContext(BloonParser.Factor_tContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = BloonParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_factor)
        try:
            self.state = 655
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 646
                self.match(BloonParser.T__3)
                compi.open_parens()
                self.state = 648
                self.expression()
                self.state = 649
                self.match(BloonParser.T__4)
                compi.close_parens()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 652
                self.var_const()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 653
                self.call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 654
                self.factor_t()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Factor_tContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_const(self):
            return self.getTypedRuleContext(BloonParser.Var_constContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_factor_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor_t" ):
                listener.enterFactor_t(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor_t" ):
                listener.exitFactor_t(self)




    def factor_t(self):

        localctx = BloonParser.Factor_tContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_factor_t)
        try:
            self.state = 661
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.ID, BloonParser.CONST_INT, BloonParser.CONST_FLOAT, BloonParser.CONST_STR, BloonParser.CONST_CHAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 657
                self.var_const()
                pass
            elif token in [BloonParser.T__48]:
                self.enterOuterAlt(localctx, 2)
                self.state = 658
                self.match(BloonParser.T__48)
                compi.set_negative()
                self.state = 660
                self.var_const()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_constContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._CONST_INT = None # Token
            self._CONST_FLOAT = None # Token
            self._CONST_STR = None # Token
            self._CONST_CHAR = None # Token

        def var(self):
            return self.getTypedRuleContext(BloonParser.VarContext,0)


        def CONST_INT(self):
            return self.getToken(BloonParser.CONST_INT, 0)

        def CONST_FLOAT(self):
            return self.getToken(BloonParser.CONST_FLOAT, 0)

        def CONST_STR(self):
            return self.getToken(BloonParser.CONST_STR, 0)

        def CONST_CHAR(self):
            return self.getToken(BloonParser.CONST_CHAR, 0)

        def getRuleIndex(self):
            return BloonParser.RULE_var_const

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_const" ):
                listener.enterVar_const(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_const" ):
                listener.exitVar_const(self)




    def var_const(self):

        localctx = BloonParser.Var_constContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_var_const)
        try:
            self.state = 672
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 663
                self.var()
                pass
            elif token in [BloonParser.CONST_INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 664
                localctx._CONST_INT = self.match(BloonParser.CONST_INT)
                compi.get_const((None if localctx._CONST_INT is None else localctx._CONST_INT.text), "int")
                pass
            elif token in [BloonParser.CONST_FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 666
                localctx._CONST_FLOAT = self.match(BloonParser.CONST_FLOAT)
                compi.get_const((None if localctx._CONST_FLOAT is None else localctx._CONST_FLOAT.text), "float")
                pass
            elif token in [BloonParser.CONST_STR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 668
                localctx._CONST_STR = self.match(BloonParser.CONST_STR)
                compi.get_const((None if localctx._CONST_STR is None else localctx._CONST_STR.text), "string")
                pass
            elif token in [BloonParser.CONST_CHAR]:
                self.enterOuterAlt(localctx, 5)
                self.state = 670
                localctx._CONST_CHAR = self.match(BloonParser.CONST_CHAR)
                compi.get_const((None if localctx._CONST_CHAR is None else localctx._CONST_CHAR.text), "char")
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





