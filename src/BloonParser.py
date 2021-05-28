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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3<")
        buf.write("\u0294\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("\n\b\5\b\u00bf\n\b\3\t\3\t\3\t\3\t\3\t\5\t\u00c6\n\t\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00d0\n\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\5\f\u00de")
        buf.write("\n\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\5\16\u00eb\n\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00fb\n\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u0106\n")
        buf.write("\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\5\23\u0116\n\23\3\23\3\23\3\23\5")
        buf.write("\23\u011b\n\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\5\23\u012a\n\23\5\23\u012c\n")
        buf.write("\23\3\24\3\24\5\24\u0130\n\24\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u013f\n")
        buf.write("\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\5\32\u0149")
        buf.write("\n\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u0153")
        buf.write("\n\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\5\35\u0161\n\35\3\36\3\36\3\36\3\36\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\5\37\u016e\n\37\3 \3 \3 ")
        buf.write("\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \5 \u0183")
        buf.write("\n \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \5 \u019a\n \3 \3 \5 \u019e\n \3!\3!\3!\5")
        buf.write("!\u01a3\n!\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\5#\u01af\n")
        buf.write("#\3$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\5%\u01be\n%\3")
        buf.write("%\3%\7%\u01c2\n%\f%\16%\u01c5\13%\3%\3%\3%\5%\u01ca\n")
        buf.write("%\3&\3&\3&\3&\3&\3&\3&\3&\5&\u01d4\n&\3&\3&\7&\u01d8\n")
        buf.write("&\f&\16&\u01db\13&\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3(\3")
        buf.write("(\3)\3)\3)\3)\3*\3*\3*\3*\3*\5*\u01f1\n*\3+\3+\3+\3+\3")
        buf.write("+\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\5,\u0202\n,\3-\3-\3-\3")
        buf.write("-\3-\5-\u0209\n-\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3/\3")
        buf.write("/\3/\3/\5/\u021a\n/\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\62\5\62")
        buf.write("\u0238\n\62\3\63\3\63\3\63\3\63\3\63\5\63\u023f\n\63\3")
        buf.write("\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\5\64\u024e\n\64\3\64\3\64\3\64\7\64\u0253\n")
        buf.write("\64\f\64\16\64\u0256\13\64\3\65\3\65\3\65\3\65\3\65\5")
        buf.write("\65\u025d\n\65\3\65\3\65\3\65\7\65\u0262\n\65\f\65\16")
        buf.write("\65\u0265\13\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66\5\66")
        buf.write("\u026e\n\66\3\66\3\66\3\66\7\66\u0273\n\66\f\66\16\66")
        buf.write("\u0276\13\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3")
        buf.write("\67\5\67\u0281\n\67\38\38\38\38\58\u0287\n8\39\39\39\3")
        buf.write("9\39\39\39\39\39\59\u0292\n9\39\2\2:\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJL")
        buf.write("NPRTVXZ\\^`bdfhjlnp\2\4\3\2\30\33\3\2\34\37\2\u02a4\2")
        buf.write("r\3\2\2\2\4\u0083\3\2\2\2\6\u0085\3\2\2\2\b\u008c\3\2")
        buf.write("\2\2\n\u0099\3\2\2\2\f\u009b\3\2\2\2\16\u00b2\3\2\2\2")
        buf.write("\20\u00c5\3\2\2\2\22\u00cf\3\2\2\2\24\u00d1\3\2\2\2\26")
        buf.write("\u00dd\3\2\2\2\30\u00df\3\2\2\2\32\u00ea\3\2\2\2\34\u00ec")
        buf.write("\3\2\2\2\36\u00fa\3\2\2\2 \u00fc\3\2\2\2\"\u0107\3\2\2")
        buf.write("\2$\u011a\3\2\2\2&\u012f\3\2\2\2(\u0131\3\2\2\2*\u013e")
        buf.write("\3\2\2\2,\u0140\3\2\2\2.\u0142\3\2\2\2\60\u0144\3\2\2")
        buf.write("\2\62\u0148\3\2\2\2\64\u0152\3\2\2\2\66\u0154\3\2\2\2")
        buf.write("8\u0160\3\2\2\2:\u0162\3\2\2\2<\u016d\3\2\2\2>\u019d\3")
        buf.write("\2\2\2@\u01a2\3\2\2\2B\u01a4\3\2\2\2D\u01ae\3\2\2\2F\u01b0")
        buf.write("\3\2\2\2H\u01c9\3\2\2\2J\u01cb\3\2\2\2L\u01df\3\2\2\2")
        buf.write("N\u01e2\3\2\2\2P\u01e7\3\2\2\2R\u01f0\3\2\2\2T\u01f2\3")
        buf.write("\2\2\2V\u0201\3\2\2\2X\u0208\3\2\2\2Z\u020a\3\2\2\2\\")
        buf.write("\u0219\3\2\2\2^\u021b\3\2\2\2`\u0226\3\2\2\2b\u0237\3")
        buf.write("\2\2\2d\u023e\3\2\2\2f\u0240\3\2\2\2h\u0257\3\2\2\2j\u0266")
        buf.write("\3\2\2\2l\u0280\3\2\2\2n\u0286\3\2\2\2p\u0291\3\2\2\2")
        buf.write("rs\7\3\2\2st\7\67\2\2tu\7\4\2\2uv\5\4\3\2vw\b\2\1\2wx")
        buf.write("\7\2\2\3x\3\3\2\2\2yz\5\b\5\2z{\5\4\3\2{\u0084\3\2\2\2")
        buf.write("|}\5\"\22\2}~\5\4\3\2~\u0084\3\2\2\2\177\u0080\5\66\34")
        buf.write("\2\u0080\u0081\5\4\3\2\u0081\u0084\3\2\2\2\u0082\u0084")
        buf.write("\5\6\4\2\u0083y\3\2\2\2\u0083|\3\2\2\2\u0083\177\3\2\2")
        buf.write("\2\u0083\u0082\3\2\2\2\u0084\5\3\2\2\2\u0085\u0086\7\5")
        buf.write("\2\2\u0086\u0087\7\6\2\2\u0087\u0088\b\4\1\2\u0088\u0089")
        buf.write("\7\7\2\2\u0089\u008a\b\4\1\2\u008a\u008b\5B\"\2\u008b")
        buf.write("\7\3\2\2\2\u008c\u008d\7\b\2\2\u008d\u008e\7\67\2\2\u008e")
        buf.write("\u008f\b\5\1\2\u008f\u0090\5\n\6\2\u0090\t\3\2\2\2\u0091")
        buf.write("\u0092\7\t\2\2\u0092\u0093\7\n\2\2\u0093\u0094\7\67\2")
        buf.write("\2\u0094\u0095\7\13\2\2\u0095\u0096\b\6\1\2\u0096\u009a")
        buf.write("\5\f\7\2\u0097\u0098\b\6\1\2\u0098\u009a\5\f\7\2\u0099")
        buf.write("\u0091\3\2\2\2\u0099\u0097\3\2\2\2\u009a\13\3\2\2\2\u009b")
        buf.write("\u00a0\7\f\2\2\u009c\u009d\7\r\2\2\u009d\u009e\7\16\2")
        buf.write("\2\u009e\u00a1\5\16\b\2\u009f\u00a1\5\20\t\2\u00a0\u009c")
        buf.write("\3\2\2\2\u00a0\u009f\3\2\2\2\u00a1\r\3\2\2\2\u00a2\u00a3")
        buf.write("\7\67\2\2\u00a3\u00b3\b\b\1\2\u00a4\u00a5\7\67\2\2\u00a5")
        buf.write("\u00a6\7\17\2\2\u00a6\u00a7\78\2\2\u00a7\u00af\b\b\1\2")
        buf.write("\u00a8\u00a9\7\20\2\2\u00a9\u00aa\78\2\2\u00aa\u00ab\b")
        buf.write("\b\1\2\u00ab\u00ac\7\21\2\2\u00ac\u00b0\b\b\1\2\u00ad")
        buf.write("\u00ae\7\21\2\2\u00ae\u00b0\b\b\1\2\u00af\u00a8\3\2\2")
        buf.write("\2\u00af\u00ad\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b3")
        buf.write("\b\b\1\2\u00b2\u00a2\3\2\2\2\u00b2\u00a4\3\2\2\2\u00b3")
        buf.write("\u00be\3\2\2\2\u00b4\u00b5\7\20\2\2\u00b5\u00bf\5\16\b")
        buf.write("\2\u00b6\u00b7\7\16\2\2\u00b7\u00b8\5,\27\2\u00b8\u00b9")
        buf.write("\b\b\1\2\u00b9\u00bc\7\4\2\2\u00ba\u00bd\5\16\b\2\u00bb")
        buf.write("\u00bd\5\20\t\2\u00bc\u00ba\3\2\2\2\u00bc\u00bb\3\2\2")
        buf.write("\2\u00bd\u00bf\3\2\2\2\u00be\u00b4\3\2\2\2\u00be\u00b6")
        buf.write("\3\2\2\2\u00bf\17\3\2\2\2\u00c0\u00c1\7\22\2\2\u00c1\u00c2")
        buf.write("\7\16\2\2\u00c2\u00c6\5\22\n\2\u00c3\u00c4\7\23\2\2\u00c4")
        buf.write("\u00c6\7\4\2\2\u00c5\u00c0\3\2\2\2\u00c5\u00c3\3\2\2\2")
        buf.write("\u00c6\21\3\2\2\2\u00c7\u00c8\5\24\13\2\u00c8\u00c9\7")
        buf.write("\23\2\2\u00c9\u00ca\7\4\2\2\u00ca\u00cb\b\n\1\2\u00cb")
        buf.write("\u00d0\3\2\2\2\u00cc\u00cd\5\24\13\2\u00cd\u00ce\5\22")
        buf.write("\n\2\u00ce\u00d0\3\2\2\2\u00cf\u00c7\3\2\2\2\u00cf\u00cc")
        buf.write("\3\2\2\2\u00d0\23\3\2\2\2\u00d1\u00d2\5\62\32\2\u00d2")
        buf.write("\u00d3\7\24\2\2\u00d3\u00d4\7\67\2\2\u00d4\u00d5\b\13")
        buf.write("\1\2\u00d5\u00d6\7\6\2\2\u00d6\u00d7\b\13\1\2\u00d7\u00d8")
        buf.write("\5\26\f\2\u00d8\25\3\2\2\2\u00d9\u00da\5> \2\u00da\u00db")
        buf.write("\5\30\r\2\u00db\u00de\3\2\2\2\u00dc\u00de\5\30\r\2\u00dd")
        buf.write("\u00d9\3\2\2\2\u00dd\u00dc\3\2\2\2\u00de\27\3\2\2\2\u00df")
        buf.write("\u00e0\7\7\2\2\u00e0\u00e1\b\r\1\2\u00e1\u00e2\5\32\16")
        buf.write("\2\u00e2\31\3\2\2\2\u00e3\u00e4\5\"\22\2\u00e4\u00e5\5")
        buf.write("B\"\2\u00e5\u00e6\b\16\1\2\u00e6\u00eb\3\2\2\2\u00e7\u00e8")
        buf.write("\5B\"\2\u00e8\u00e9\b\16\1\2\u00e9\u00eb\3\2\2\2\u00ea")
        buf.write("\u00e3\3\2\2\2\u00ea\u00e7\3\2\2\2\u00eb\33\3\2\2\2\u00ec")
        buf.write("\u00ed\7\67\2\2\u00ed\u00ee\b\17\1\2\u00ee\u00ef\5\36")
        buf.write("\20\2\u00ef\35\3\2\2\2\u00f0\u00fb\5 \21\2\u00f1\u00f2")
        buf.write("\5 \21\2\u00f2\u00f3\7\25\2\2\u00f3\u00f4\5\34\17\2\u00f4")
        buf.write("\u00f5\b\20\1\2\u00f5\u00fb\3\2\2\2\u00f6\u00f7\7\25\2")
        buf.write("\2\u00f7\u00f8\7\67\2\2\u00f8\u00fb\b\20\1\2\u00f9\u00fb")
        buf.write("\b\20\1\2\u00fa\u00f0\3\2\2\2\u00fa\u00f1\3\2\2\2\u00fa")
        buf.write("\u00f6\3\2\2\2\u00fa\u00f9\3\2\2\2\u00fb\37\3\2\2\2\u00fc")
        buf.write("\u00fd\7\17\2\2\u00fd\u0105\5h\65\2\u00fe\u00ff\7\20\2")
        buf.write("\2\u00ff\u0100\5h\65\2\u0100\u0101\7\21\2\2\u0101\u0102")
        buf.write("\b\21\1\2\u0102\u0106\3\2\2\2\u0103\u0104\7\21\2\2\u0104")
        buf.write("\u0106\b\21\1\2\u0105\u00fe\3\2\2\2\u0105\u0103\3\2\2")
        buf.write("\2\u0106!\3\2\2\2\u0107\u0108\7\26\2\2\u0108\u0109\5$")
        buf.write("\23\2\u0109#\3\2\2\2\u010a\u010b\7\67\2\2\u010b\u010c")
        buf.write("\7\17\2\2\u010c\u010d\78\2\2\u010d\u0115\b\23\1\2\u010e")
        buf.write("\u010f\7\20\2\2\u010f\u0110\78\2\2\u0110\u0111\b\23\1")
        buf.write("\2\u0111\u0112\7\21\2\2\u0112\u0116\b\23\1\2\u0113\u0114")
        buf.write("\7\21\2\2\u0114\u0116\b\23\1\2\u0115\u010e\3\2\2\2\u0115")
        buf.write("\u0113\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u011b\b\23\1")
        buf.write("\2\u0118\u0119\7\67\2\2\u0119\u011b\b\23\1\2\u011a\u010a")
        buf.write("\3\2\2\2\u011a\u0118\3\2\2\2\u011b\u012b\3\2\2\2\u011c")
        buf.write("\u011d\7\20\2\2\u011d\u012c\5$\23\2\u011e\u0129\7\16\2")
        buf.write("\2\u011f\u0120\5,\27\2\u0120\u0121\b\23\1\2\u0121\u0122")
        buf.write("\7\4\2\2\u0122\u0123\5&\24\2\u0123\u012a\3\2\2\2\u0124")
        buf.write("\u0125\5.\30\2\u0125\u0126\b\23\1\2\u0126\u0127\7\4\2")
        buf.write("\2\u0127\u0128\5&\24\2\u0128\u012a\3\2\2\2\u0129\u011f")
        buf.write("\3\2\2\2\u0129\u0124\3\2\2\2\u012a\u012c\3\2\2\2\u012b")
        buf.write("\u011c\3\2\2\2\u012b\u011e\3\2\2\2\u012c%\3\2\2\2\u012d")
        buf.write("\u0130\5$\23\2\u012e\u0130\3\2\2\2\u012f\u012d\3\2\2\2")
        buf.write("\u012f\u012e\3\2\2\2\u0130\'\3\2\2\2\u0131\u0132\5\34")
        buf.write("\17\2\u0132\u0133\5*\26\2\u0133)\3\2\2\2\u0134\u0135\7")
        buf.write("\27\2\2\u0135\u0136\5b\62\2\u0136\u0137\b\26\1\2\u0137")
        buf.write("\u0138\7\4\2\2\u0138\u013f\3\2\2\2\u0139\u013a\5\60\31")
        buf.write("\2\u013a\u013b\5b\62\2\u013b\u013c\b\26\1\2\u013c\u013d")
        buf.write("\7\4\2\2\u013d\u013f\3\2\2\2\u013e\u0134\3\2\2\2\u013e")
        buf.write("\u0139\3\2\2\2\u013f+\3\2\2\2\u0140\u0141\t\2\2\2\u0141")
        buf.write("-\3\2\2\2\u0142\u0143\7\67\2\2\u0143/\3\2\2\2\u0144\u0145")
        buf.write("\t\3\2\2\u0145\61\3\2\2\2\u0146\u0149\5,\27\2\u0147\u0149")
        buf.write("\7 \2\2\u0148\u0146\3\2\2\2\u0148\u0147\3\2\2\2\u0149")
        buf.write("\63\3\2\2\2\u014a\u0153\5(\25\2\u014b\u0153\5Z.\2\u014c")
        buf.write("\u0153\5F$\2\u014d\u0153\5N(\2\u014e\u0153\5T+\2\u014f")
        buf.write("\u0153\5^\60\2\u0150\u0153\5`\61\2\u0151\u0153\5L\'\2")
        buf.write("\u0152\u014a\3\2\2\2\u0152\u014b\3\2\2\2\u0152\u014c\3")
        buf.write("\2\2\2\u0152\u014d\3\2\2\2\u0152\u014e\3\2\2\2\u0152\u014f")
        buf.write("\3\2\2\2\u0152\u0150\3\2\2\2\u0152\u0151\3\2\2\2\u0153")
        buf.write("\65\3\2\2\2\u0154\u0155\5\62\32\2\u0155\u0156\7\24\2\2")
        buf.write("\u0156\u0157\7\67\2\2\u0157\u0158\b\34\1\2\u0158\u0159")
        buf.write("\7\6\2\2\u0159\u015a\b\34\1\2\u015a\u015b\58\35\2\u015b")
        buf.write("\67\3\2\2\2\u015c\u015d\5> \2\u015d\u015e\5:\36\2\u015e")
        buf.write("\u0161\3\2\2\2\u015f\u0161\5:\36\2\u0160\u015c\3\2\2\2")
        buf.write("\u0160\u015f\3\2\2\2\u01619\3\2\2\2\u0162\u0163\7\7\2")
        buf.write("\2\u0163\u0164\b\36\1\2\u0164\u0165\5<\37\2\u0165;\3\2")
        buf.write("\2\2\u0166\u0167\5\"\22\2\u0167\u0168\5B\"\2\u0168\u0169")
        buf.write("\b\37\1\2\u0169\u016e\3\2\2\2\u016a\u016b\5B\"\2\u016b")
        buf.write("\u016c\b\37\1\2\u016c\u016e\3\2\2\2\u016d\u0166\3\2\2")
        buf.write("\2\u016d\u016a\3\2\2\2\u016e=\3\2\2\2\u016f\u0170\5,\27")
        buf.write("\2\u0170\u0171\7\67\2\2\u0171\u0172\b \1\2\u0172\u0173")
        buf.write("\5@!\2\u0173\u019e\3\2\2\2\u0174\u0175\5,\27\2\u0175\u0182")
        buf.write("\7\67\2\2\u0176\u0177\7\17\2\2\u0177\u0178\78\2\2\u0178")
        buf.write("\u0179\7\21\2\2\u0179\u0183\b \1\2\u017a\u017b\7\17\2")
        buf.write("\2\u017b\u017c\78\2\2\u017c\u017d\b \1\2\u017d\u017e\7")
        buf.write("\20\2\2\u017e\u017f\78\2\2\u017f\u0180\b \1\2\u0180\u0181")
        buf.write("\7\21\2\2\u0181\u0183\b \1\2\u0182\u0176\3\2\2\2\u0182")
        buf.write("\u017a\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0185\5@!\2\u0185")
        buf.write("\u019e\3\2\2\2\u0186\u0187\5.\30\2\u0187\u0188\7\67\2")
        buf.write("\2\u0188\u0189\b \1\2\u0189\u018a\5@!\2\u018a\u019e\3")
        buf.write("\2\2\2\u018b\u018c\5.\30\2\u018c\u0199\7\67\2\2\u018d")
        buf.write("\u018e\7\17\2\2\u018e\u018f\78\2\2\u018f\u0190\7\21\2")
        buf.write("\2\u0190\u019a\b \1\2\u0191\u0192\7\17\2\2\u0192\u0193")
        buf.write("\78\2\2\u0193\u0194\b \1\2\u0194\u0195\7\20\2\2\u0195")
        buf.write("\u0196\78\2\2\u0196\u0197\b \1\2\u0197\u0198\7\21\2\2")
        buf.write("\u0198\u019a\b \1\2\u0199\u018d\3\2\2\2\u0199\u0191\3")
        buf.write("\2\2\2\u019a\u019b\3\2\2\2\u019b\u019c\5@!\2\u019c\u019e")
        buf.write("\3\2\2\2\u019d\u016f\3\2\2\2\u019d\u0174\3\2\2\2\u019d")
        buf.write("\u0186\3\2\2\2\u019d\u018b\3\2\2\2\u019e?\3\2\2\2\u019f")
        buf.write("\u01a0\7\20\2\2\u01a0\u01a3\5> \2\u01a1\u01a3\3\2\2\2")
        buf.write("\u01a2\u019f\3\2\2\2\u01a2\u01a1\3\2\2\2\u01a3A\3\2\2")
        buf.write("\2\u01a4\u01a5\7\f\2\2\u01a5\u01a6\5D#\2\u01a6C\3\2\2")
        buf.write("\2\u01a7\u01a8\5\64\33\2\u01a8\u01a9\5D#\2\u01a9\u01af")
        buf.write("\3\2\2\2\u01aa\u01ab\5\64\33\2\u01ab\u01ac\7\23\2\2\u01ac")
        buf.write("\u01af\3\2\2\2\u01ad\u01af\7\23\2\2\u01ae\u01a7\3\2\2")
        buf.write("\2\u01ae\u01aa\3\2\2\2\u01ae\u01ad\3\2\2\2\u01afE\3\2")
        buf.write("\2\2\u01b0\u01b1\7!\2\2\u01b1\u01b2\7\6\2\2\u01b2\u01b3")
        buf.write("\b$\1\2\u01b3\u01b4\5b\62\2\u01b4\u01b5\7\7\2\2\u01b5")
        buf.write("\u01b6\b$\1\2\u01b6\u01b7\7\4\2\2\u01b7G\3\2\2\2\u01b8")
        buf.write("\u01b9\7\67\2\2\u01b9\u01ba\b%\1\2\u01ba\u01bb\7\6\2\2")
        buf.write("\u01bb\u01bd\b%\1\2\u01bc\u01be\5b\62\2\u01bd\u01bc\3")
        buf.write("\2\2\2\u01bd\u01be\3\2\2\2\u01be\u01c3\3\2\2\2\u01bf\u01c0")
        buf.write("\7\20\2\2\u01c0\u01c2\5b\62\2\u01c1\u01bf\3\2\2\2\u01c2")
        buf.write("\u01c5\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c3\u01c4\3\2\2\2")
        buf.write("\u01c4\u01c6\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c6\u01c7\7")
        buf.write("\7\2\2\u01c7\u01ca\b%\1\2\u01c8\u01ca\5J&\2\u01c9\u01b8")
        buf.write("\3\2\2\2\u01c9\u01c8\3\2\2\2\u01caI\3\2\2\2\u01cb\u01cc")
        buf.write("\7\67\2\2\u01cc\u01cd\b&\1\2\u01cd\u01ce\7\25\2\2\u01ce")
        buf.write("\u01cf\7\67\2\2\u01cf\u01d0\b&\1\2\u01d0\u01d1\7\6\2\2")
        buf.write("\u01d1\u01d3\b&\1\2\u01d2\u01d4\5b\62\2\u01d3\u01d2\3")
        buf.write("\2\2\2\u01d3\u01d4\3\2\2\2\u01d4\u01d9\3\2\2\2\u01d5\u01d6")
        buf.write("\7\20\2\2\u01d6\u01d8\5b\62\2\u01d7\u01d5\3\2\2\2\u01d8")
        buf.write("\u01db\3\2\2\2\u01d9\u01d7\3\2\2\2\u01d9\u01da\3\2\2\2")
        buf.write("\u01da\u01dc\3\2\2\2\u01db\u01d9\3\2\2\2\u01dc\u01dd\7")
        buf.write("\7\2\2\u01dd\u01de\b&\1\2\u01deK\3\2\2\2\u01df\u01e0\5")
        buf.write("H%\2\u01e0\u01e1\7\4\2\2\u01e1M\3\2\2\2\u01e2\u01e3\7")
        buf.write("\"\2\2\u01e3\u01e4\7\6\2\2\u01e4\u01e5\b(\1\2\u01e5\u01e6")
        buf.write("\5P)\2\u01e6O\3\2\2\2\u01e7\u01e8\5\34\17\2\u01e8\u01e9")
        buf.write("\b)\1\2\u01e9\u01ea\5R*\2\u01eaQ\3\2\2\2\u01eb\u01ec\7")
        buf.write("\20\2\2\u01ec\u01f1\5P)\2\u01ed\u01ee\7\7\2\2\u01ee\u01ef")
        buf.write("\b*\1\2\u01ef\u01f1\7\4\2\2\u01f0\u01eb\3\2\2\2\u01f0")
        buf.write("\u01ed\3\2\2\2\u01f1S\3\2\2\2\u01f2\u01f3\7#\2\2\u01f3")
        buf.write("\u01f4\7\6\2\2\u01f4\u01f5\b+\1\2\u01f5\u01f6\5V,\2\u01f6")
        buf.write("U\3\2\2\2\u01f7\u01f8\5b\62\2\u01f8\u01f9\b,\1\2\u01f9")
        buf.write("\u01fa\5X-\2\u01fa\u0202\3\2\2\2\u01fb\u01fc\7:\2\2\u01fc")
        buf.write("\u01fd\b,\1\2\u01fd\u0202\5X-\2\u01fe\u01ff\5H%\2\u01ff")
        buf.write("\u0200\5X-\2\u0200\u0202\3\2\2\2\u0201\u01f7\3\2\2\2\u0201")
        buf.write("\u01fb\3\2\2\2\u0201\u01fe\3\2\2\2\u0202W\3\2\2\2\u0203")
        buf.write("\u0204\7\20\2\2\u0204\u0209\5V,\2\u0205\u0206\7\7\2\2")
        buf.write("\u0206\u0207\b-\1\2\u0207\u0209\7\4\2\2\u0208\u0203\3")
        buf.write("\2\2\2\u0208\u0205\3\2\2\2\u0209Y\3\2\2\2\u020a\u020b")
        buf.write("\7$\2\2\u020b\u020c\7\6\2\2\u020c\u020d\b.\1\2\u020d\u020e")
        buf.write("\5b\62\2\u020e\u020f\7\7\2\2\u020f\u0210\b.\1\2\u0210")
        buf.write("\u0211\7%\2\2\u0211\u0212\5B\"\2\u0212\u0213\5\\/\2\u0213")
        buf.write("\u0214\b.\1\2\u0214[\3\2\2\2\u0215\u0216\7&\2\2\u0216")
        buf.write("\u0217\b/\1\2\u0217\u021a\5B\"\2\u0218\u021a\3\2\2\2\u0219")
        buf.write("\u0215\3\2\2\2\u0219\u0218\3\2\2\2\u021a]\3\2\2\2\u021b")
        buf.write("\u021c\7\'\2\2\u021c\u021d\b\60\1\2\u021d\u021e\7\6\2")
        buf.write("\2\u021e\u021f\b\60\1\2\u021f\u0220\5b\62\2\u0220\u0221")
        buf.write("\7\7\2\2\u0221\u0222\b\60\1\2\u0222\u0223\7(\2\2\u0223")
        buf.write("\u0224\5B\"\2\u0224\u0225\b\60\1\2\u0225_\3\2\2\2\u0226")
        buf.write("\u0227\7)\2\2\u0227\u0228\5\34\17\2\u0228\u0229\7*\2\2")
        buf.write("\u0229\u022a\5b\62\2\u022a\u022b\b\61\1\2\u022b\u022c")
        buf.write("\7(\2\2\u022c\u022d\b\61\1\2\u022d\u022e\5B\"\2\u022e")
        buf.write("\u022f\b\61\1\2\u022fa\3\2\2\2\u0230\u0231\7+\2\2\u0231")
        buf.write("\u0232\5f\64\2\u0232\u0233\5d\63\2\u0233\u0238\3\2\2\2")
        buf.write("\u0234\u0235\5f\64\2\u0235\u0236\5d\63\2\u0236\u0238\3")
        buf.write("\2\2\2\u0237\u0230\3\2\2\2\u0237\u0234\3\2\2\2\u0238c")
        buf.write("\3\2\2\2\u0239\u023a\7,\2\2\u023a\u023f\5b\62\2\u023b")
        buf.write("\u023c\7-\2\2\u023c\u023f\5b\62\2\u023d\u023f\3\2\2\2")
        buf.write("\u023e\u0239\3\2\2\2\u023e\u023b\3\2\2\2\u023e\u023d\3")
        buf.write("\2\2\2\u023fe\3\2\2\2\u0240\u0254\5h\65\2\u0241\u0242")
        buf.write("\7\13\2\2\u0242\u024e\b\64\1\2\u0243\u0244\7\t\2\2\u0244")
        buf.write("\u024e\b\64\1\2\u0245\u0246\7.\2\2\u0246\u024e\b\64\1")
        buf.write("\2\u0247\u0248\7/\2\2\u0248\u024e\b\64\1\2\u0249\u024a")
        buf.write("\7\60\2\2\u024a\u024e\b\64\1\2\u024b\u024c\7\61\2\2\u024c")
        buf.write("\u024e\b\64\1\2\u024d\u0241\3\2\2\2\u024d\u0243\3\2\2")
        buf.write("\2\u024d\u0245\3\2\2\2\u024d\u0247\3\2\2\2\u024d\u0249")
        buf.write("\3\2\2\2\u024d\u024b\3\2\2\2\u024e\u024f\3\2\2\2\u024f")
        buf.write("\u0250\5h\65\2\u0250\u0251\b\64\1\2\u0251\u0253\3\2\2")
        buf.write("\2\u0252\u024d\3\2\2\2\u0253\u0256\3\2\2\2\u0254\u0252")
        buf.write("\3\2\2\2\u0254\u0255\3\2\2\2\u0255g\3\2\2\2\u0256\u0254")
        buf.write("\3\2\2\2\u0257\u0263\5j\66\2\u0258\u0259\7\62\2\2\u0259")
        buf.write("\u025d\b\65\1\2\u025a\u025b\7\63\2\2\u025b\u025d\b\65")
        buf.write("\1\2\u025c\u0258\3\2\2\2\u025c\u025a\3\2\2\2\u025d\u025e")
        buf.write("\3\2\2\2\u025e\u025f\5j\66\2\u025f\u0260\b\65\1\2\u0260")
        buf.write("\u0262\3\2\2\2\u0261\u025c\3\2\2\2\u0262\u0265\3\2\2\2")
        buf.write("\u0263\u0261\3\2\2\2\u0263\u0264\3\2\2\2\u0264i\3\2\2")
        buf.write("\2\u0265\u0263\3\2\2\2\u0266\u0274\5l\67\2\u0267\u0268")
        buf.write("\7\64\2\2\u0268\u026e\b\66\1\2\u0269\u026a\7\65\2\2\u026a")
        buf.write("\u026e\b\66\1\2\u026b\u026c\7\66\2\2\u026c\u026e\b\66")
        buf.write("\1\2\u026d\u0267\3\2\2\2\u026d\u0269\3\2\2\2\u026d\u026b")
        buf.write("\3\2\2\2\u026e\u026f\3\2\2\2\u026f\u0270\5l\67\2\u0270")
        buf.write("\u0271\b\66\1\2\u0271\u0273\3\2\2\2\u0272\u026d\3\2\2")
        buf.write("\2\u0273\u0276\3\2\2\2\u0274\u0272\3\2\2\2\u0274\u0275")
        buf.write("\3\2\2\2\u0275k\3\2\2\2\u0276\u0274\3\2\2\2\u0277\u0278")
        buf.write("\7\6\2\2\u0278\u0279\b\67\1\2\u0279\u027a\5f\64\2\u027a")
        buf.write("\u027b\7\7\2\2\u027b\u027c\b\67\1\2\u027c\u0281\3\2\2")
        buf.write("\2\u027d\u0281\5p9\2\u027e\u0281\5H%\2\u027f\u0281\5n")
        buf.write("8\2\u0280\u0277\3\2\2\2\u0280\u027d\3\2\2\2\u0280\u027e")
        buf.write("\3\2\2\2\u0280\u027f\3\2\2\2\u0281m\3\2\2\2\u0282\u0287")
        buf.write("\5p9\2\u0283\u0284\7\63\2\2\u0284\u0285\b8\1\2\u0285\u0287")
        buf.write("\5p9\2\u0286\u0282\3\2\2\2\u0286\u0283\3\2\2\2\u0287o")
        buf.write("\3\2\2\2\u0288\u0292\5\34\17\2\u0289\u028a\78\2\2\u028a")
        buf.write("\u0292\b9\1\2\u028b\u028c\79\2\2\u028c\u0292\b9\1\2\u028d")
        buf.write("\u028e\7:\2\2\u028e\u0292\b9\1\2\u028f\u0290\7;\2\2\u0290")
        buf.write("\u0292\b9\1\2\u0291\u0288\3\2\2\2\u0291\u0289\3\2\2\2")
        buf.write("\u0291\u028b\3\2\2\2\u0291\u028d\3\2\2\2\u0291\u028f\3")
        buf.write("\2\2\2\u0292q\3\2\2\2\62\u0083\u0099\u00a0\u00af\u00b2")
        buf.write("\u00bc\u00be\u00c5\u00cf\u00dd\u00ea\u00fa\u0105\u0115")
        buf.write("\u011a\u0129\u012b\u012f\u013e\u0148\u0152\u0160\u016d")
        buf.write("\u0182\u0199\u019d\u01a2\u01ae\u01bd\u01c3\u01c9\u01d3")
        buf.write("\u01d9\u01f0\u0201\u0208\u0219\u0237\u023e\u024d\u0254")
        buf.write("\u025c\u0263\u026d\u0274\u0280\u0286\u0291")
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
                     "'-'", "'*'", "'/'", "'%'" ]

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
                      "CONST_CHAR", "WHITESPACE" ]

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
            self.state = 195
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.match(BloonParser.T__15)
                self.state = 191
                self.match(BloonParser.T__11)
                self.state = 192
                self.class_p()
                pass
            elif token in [BloonParser.T__16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.match(BloonParser.T__16)
                self.state = 194
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
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.class_func()
                self.state = 198
                self.match(BloonParser.T__16)
                self.state = 199
                self.match(BloonParser.T__1)
                compi.end_class()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.class_func()
                self.state = 203
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
            self.state = 207
            localctx._type_meth = self.type_meth()
            self.state = 208
            self.match(BloonParser.T__17)
            self.state = 209
            localctx._ID = self.match(BloonParser.ID)
            compi.define_method((None if localctx._type_meth is None else self._input.getText(localctx._type_meth.start,localctx._type_meth.stop)), (None if localctx._ID is None else localctx._ID.text), True)
            self.state = 211
            self.match(BloonParser.T__3)
            compi.open_parens()
            self.state = 213
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
            self.state = 219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__21, BloonParser.T__22, BloonParser.T__23, BloonParser.T__24, BloonParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.param()
                self.state = 216
                self.c_func_k()
                pass
            elif token in [BloonParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
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
            self.state = 221
            self.match(BloonParser.T__4)
            compi.close_parens()
            self.state = 223
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
            self.state = 232
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.var_dec()
                self.state = 226
                self.block()
                compi.process_method()
                pass
            elif token in [BloonParser.T__9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
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
            self.state = 234
            localctx._ID = self.match(BloonParser.ID)
            compi.add_operand((None if localctx._ID is None else localctx._ID.text))
            self.state = 236
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
            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.arr_idx()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.arr_idx()
                self.state = 240
                self.match(BloonParser.T__18)
                self.state = 241
                self.var()
                compi.get_var(True)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 244
                self.match(BloonParser.T__18)
                self.state = 245
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
            self.state = 250
            self.match(BloonParser.T__12)
            self.state = 251
            self.exp()
            self.state = 259
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__13]:
                self.state = 252
                self.match(BloonParser.T__13)
                self.state = 253
                self.exp()
                self.state = 254
                self.match(BloonParser.T__14)
                compi.get_array_item(2)
                pass
            elif token in [BloonParser.T__14]:
                self.state = 257
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
            self.state = 261
            self.match(BloonParser.T__19)
            self.state = 262
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
            self.state = 280
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 264
                localctx._ID = self.match(BloonParser.ID)
                self.state = 265
                self.match(BloonParser.T__12)
                self.state = 266
                localctx._CONST_INT = self.match(BloonParser.CONST_INT)
                compi.add_limit((None if localctx._CONST_INT is None else localctx._CONST_INT.text))
                self.state = 275
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BloonParser.T__13]:
                    self.state = 268
                    self.match(BloonParser.T__13)
                    self.state = 269
                    localctx._CONST_INT = self.match(BloonParser.CONST_INT)
                    compi.add_limit((None if localctx._CONST_INT is None else localctx._CONST_INT.text))
                    self.state = 271
                    self.match(BloonParser.T__14)
                    compi.add_operand((None if localctx._ID is None else localctx._ID.text), 2);
                    pass
                elif token in [BloonParser.T__14]:
                    self.state = 273
                    self.match(BloonParser.T__14)
                    compi.add_operand((None if localctx._ID is None else localctx._ID.text), 1)
                    pass
                else:
                    raise NoViableAltException(self)

                compi.increase_varCount()
                pass

            elif la_ == 2:
                self.state = 278
                localctx._ID = self.match(BloonParser.ID)
                compi.add_operand((None if localctx._ID is None else localctx._ID.text)); compi.increase_varCount()
                pass


            self.state = 297
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__13]:
                self.state = 282
                self.match(BloonParser.T__13)
                self.state = 283
                self.var_dec_t()
                pass
            elif token in [BloonParser.T__11]:
                self.state = 284
                self.match(BloonParser.T__11)
                self.state = 295
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BloonParser.T__21, BloonParser.T__22, BloonParser.T__23, BloonParser.T__24]:
                    self.state = 285
                    localctx._var_type = self.var_type()
                    compi.define_var((None if localctx._var_type is None else self._input.getText(localctx._var_type.start,localctx._var_type.stop)))
                    self.state = 287
                    self.match(BloonParser.T__1)
                    self.state = 288
                    self.var_dec_l()
                    pass
                elif token in [BloonParser.ID]:
                    self.state = 290
                    localctx._custom_type = self.custom_type()
                    compi.define_var((None if localctx._custom_type is None else self._input.getText(localctx._custom_type.start,localctx._custom_type.stop)))
                    self.state = 292
                    self.match(BloonParser.T__1)
                    self.state = 293
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
            self.state = 301
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
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
            self.state = 303
            self.var()
            self.state = 304
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
            self.state = 316
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 306
                self.match(BloonParser.T__20)
                self.state = 307
                self.super_exp()
                compi.assign_var()
                self.state = 309
                self.match(BloonParser.T__1)
                pass
            elif token in [BloonParser.T__25, BloonParser.T__26, BloonParser.T__27, BloonParser.T__28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 311
                localctx._assign_op = self.assign_op()
                self.state = 312
                self.super_exp()
                compi.arithmetic_assign((None if localctx._assign_op is None else self._input.getText(localctx._assign_op.start,localctx._assign_op.stop)))
                self.state = 314
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
            self.state = 318
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
            self.state = 320
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
            self.state = 322
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
            self.state = 326
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__21, BloonParser.T__22, BloonParser.T__23, BloonParser.T__24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 324
                self.var_type()
                pass
            elif token in [BloonParser.T__29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
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
            self.state = 336
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
                self.assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 329
                self.cond()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 330
                self.r_return()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 331
                self.read()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 332
                self.write()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 333
                self.r_while()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 334
                self.floop()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 335
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
            self.state = 338
            localctx._type_meth = self.type_meth()
            self.state = 339
            self.match(BloonParser.T__17)
            self.state = 340
            localctx._ID = self.match(BloonParser.ID)
            compi.define_method((None if localctx._type_meth is None else self._input.getText(localctx._type_meth.start,localctx._type_meth.stop)), (None if localctx._ID is None else localctx._ID.text))
            self.state = 342
            self.match(BloonParser.T__3)
            compi.open_parens()
            self.state = 344
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
            self.state = 350
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__21, BloonParser.T__22, BloonParser.T__23, BloonParser.T__24, BloonParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.param()
                self.state = 347
                self.func_k()
                pass
            elif token in [BloonParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 349
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
            self.state = 352
            self.match(BloonParser.T__4)
            compi.close_parens()
            self.state = 354
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
            self.state = 363
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.var_dec()
                self.state = 357
                self.block()
                compi.process_method()
                pass
            elif token in [BloonParser.T__9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 360
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
            self.state = 411
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 365
                localctx._var_type = self.var_type()
                self.state = 366
                localctx._ID = self.match(BloonParser.ID)
                compi.define_param((None if localctx._var_type is None else self._input.getText(localctx._var_type.start,localctx._var_type.stop)), (None if localctx._ID is None else localctx._ID.text))
                self.state = 368
                self.param_t()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
                localctx._var_type = self.var_type()
                self.state = 371
                localctx._ID = self.match(BloonParser.ID)
                self.state = 384
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                if la_ == 1:
                    self.state = 372
                    self.match(BloonParser.T__12)
                    self.state = 373
                    localctx._CONST_INT = self.match(BloonParser.CONST_INT)
                    self.state = 374
                    self.match(BloonParser.T__14)
                    compi.add_limit((None if localctx._CONST_INT is None else localctx._CONST_INT.text)); compi.define_param((None if localctx._var_type is None else self._input.getText(localctx._var_type.start,localctx._var_type.stop)), (None if localctx._ID is None else localctx._ID.text), 1)
                    pass

                elif la_ == 2:
                    self.state = 376
                    self.match(BloonParser.T__12)
                    self.state = 377
                    localctx._CONST_INT = self.match(BloonParser.CONST_INT)
                    compi.add_limit((None if localctx._CONST_INT is None else localctx._CONST_INT.text))
                    self.state = 379
                    self.match(BloonParser.T__13)
                    self.state = 380
                    localctx._CONST_INT = self.match(BloonParser.CONST_INT)
                    compi.add_limit((None if localctx._CONST_INT is None else localctx._CONST_INT.text))
                    self.state = 382
                    self.match(BloonParser.T__14)
                    compi.define_param((None if localctx._var_type is None else self._input.getText(localctx._var_type.start,localctx._var_type.stop)), (None if localctx._ID is None else localctx._ID.text), 2)
                    pass


                self.state = 386
                self.param_t()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 388
                localctx._custom_type = self.custom_type()
                self.state = 389
                localctx._ID = self.match(BloonParser.ID)
                compi.define_param((None if localctx._custom_type is None else self._input.getText(localctx._custom_type.start,localctx._custom_type.stop)), (None if localctx._ID is None else localctx._ID.text))
                self.state = 391
                self.param_t()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 393
                localctx._custom_type = self.custom_type()
                self.state = 394
                localctx._ID = self.match(BloonParser.ID)
                self.state = 407
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 395
                    self.match(BloonParser.T__12)
                    self.state = 396
                    localctx._CONST_INT = self.match(BloonParser.CONST_INT)
                    self.state = 397
                    self.match(BloonParser.T__14)
                    compi.add_limit((None if localctx._CONST_INT is None else localctx._CONST_INT.text)); compi.define_param((None if localctx._custom_type is None else self._input.getText(localctx._custom_type.start,localctx._custom_type.stop)), (None if localctx._ID is None else localctx._ID.text), 1)
                    pass

                elif la_ == 2:
                    self.state = 399
                    self.match(BloonParser.T__12)
                    self.state = 400
                    localctx._CONST_INT = self.match(BloonParser.CONST_INT)
                    compi.add_limit((None if localctx._CONST_INT is None else localctx._CONST_INT.text))
                    self.state = 402
                    self.match(BloonParser.T__13)
                    self.state = 403
                    localctx._CONST_INT = self.match(BloonParser.CONST_INT)
                    compi.add_limit((None if localctx._CONST_INT is None else localctx._CONST_INT.text))
                    self.state = 405
                    self.match(BloonParser.T__14)
                    compi.define_param((None if localctx._custom_type is None else self._input.getText(localctx._custom_type.start,localctx._custom_type.stop)), (None if localctx._ID is None else localctx._ID.text), 2)
                    pass


                self.state = 409
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
            self.state = 416
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 413
                self.match(BloonParser.T__13)
                self.state = 414
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
            self.state = 418
            self.match(BloonParser.T__9)
            self.state = 419
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
            self.state = 428
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 421
                self.statement()
                self.state = 422
                self.block_t()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 424
                self.statement()
                self.state = 425
                self.match(BloonParser.T__16)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 427
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
            self.state = 430
            self.match(BloonParser.T__30)
            self.state = 431
            self.match(BloonParser.T__3)
            compi.open_parens()
            self.state = 433
            self.super_exp()
            self.state = 434
            self.match(BloonParser.T__4)
            compi.close_parens(); compi.rtn_stmt()
            self.state = 436
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
            self.state = 455
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 438
                localctx._ID = self.match(BloonParser.ID)
                compi.verify_method((None if localctx._ID is None else localctx._ID.text))
                self.state = 440
                self.match(BloonParser.T__3)
                compi.open_parens()
                self.state = 443
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BloonParser.T__3) | (1 << BloonParser.T__40) | (1 << BloonParser.T__48) | (1 << BloonParser.ID) | (1 << BloonParser.CONST_INT) | (1 << BloonParser.CONST_FLOAT) | (1 << BloonParser.CONST_STR) | (1 << BloonParser.CONST_CHAR))) != 0):
                    self.state = 442
                    self.super_exp()


                self.state = 449
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BloonParser.T__13:
                    self.state = 445
                    self.match(BloonParser.T__13)
                    self.state = 446
                    self.super_exp()
                    self.state = 451
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 452
                self.match(BloonParser.T__4)
                compi.close_parens(); compi.call_method((None if localctx._ID is None else localctx._ID.text))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 454
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
            self.state = 457
            localctx._ID = self.match(BloonParser.ID)
            compi.add_operand((None if localctx._ID is None else localctx._ID.text))
            self.state = 459
            self.match(BloonParser.T__18)
            self.state = 460
            localctx._ID = self.match(BloonParser.ID)
            compi.verify_method((None if localctx._ID is None else localctx._ID.text), True)
            self.state = 462
            self.match(BloonParser.T__3)
            compi.open_parens()
            self.state = 465
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BloonParser.T__3) | (1 << BloonParser.T__40) | (1 << BloonParser.T__48) | (1 << BloonParser.ID) | (1 << BloonParser.CONST_INT) | (1 << BloonParser.CONST_FLOAT) | (1 << BloonParser.CONST_STR) | (1 << BloonParser.CONST_CHAR))) != 0):
                self.state = 464
                self.super_exp()


            self.state = 471
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BloonParser.T__13:
                self.state = 467
                self.match(BloonParser.T__13)
                self.state = 468
                self.super_exp()
                self.state = 473
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 474
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
            self.state = 477
            self.call()
            self.state = 478
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
            self.state = 480
            self.match(BloonParser.T__31)
            self.state = 481
            self.match(BloonParser.T__3)
            compi.open_parens()
            self.state = 483
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
            self.state = 485
            self.var()
            compi.call_method('read')
            self.state = 487
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
            self.state = 494
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 489
                self.match(BloonParser.T__13)
                self.state = 490
                self.read_t()
                pass
            elif token in [BloonParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 491
                self.match(BloonParser.T__4)
                compi.close_parens()
                self.state = 493
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
            self.state = 496
            self.match(BloonParser.T__32)
            self.state = 497
            self.match(BloonParser.T__3)
            compi.open_parens()
            self.state = 499
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
            self.state = 511
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 501
                self.super_exp()
                compi.call_method('write')
                self.state = 503
                self.write_k()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 505
                localctx._CONST_STR = self.match(BloonParser.CONST_STR)
                compi.get_const((None if localctx._CONST_STR is None else localctx._CONST_STR.text), "string"); compi.call_method('write')
                self.state = 507
                self.write_k()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 508
                self.call()
                self.state = 509
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
            self.state = 518
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 513
                self.match(BloonParser.T__13)
                self.state = 514
                self.write_t()
                pass
            elif token in [BloonParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 515
                self.match(BloonParser.T__4)
                compi.close_parens(); compi.new_write()
                self.state = 517
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
            self.state = 520
            self.match(BloonParser.T__33)
            self.state = 521
            self.match(BloonParser.T__3)
            compi.open_parens()
            self.state = 523
            self.super_exp()
            self.state = 524
            self.match(BloonParser.T__4)
            compi.close_parens(); compi.condition()
            self.state = 526
            self.match(BloonParser.T__34)
            self.state = 527
            self.block()
            self.state = 528
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
            self.state = 535
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 531
                self.match(BloonParser.T__35)
                compi.else_condition()
                self.state = 533
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
            self.state = 537
            self.match(BloonParser.T__36)
            compi.while_condition()
            self.state = 539
            self.match(BloonParser.T__3)
            compi.open_parens()
            self.state = 541
            self.super_exp()
            self.state = 542
            self.match(BloonParser.T__4)
            compi.close_parens(); compi.while_expression()
            self.state = 544
            self.match(BloonParser.T__37)
            self.state = 545
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
            self.state = 548
            self.match(BloonParser.T__38)
            self.state = 549
            self.var()
            self.state = 550
            self.match(BloonParser.T__39)
            self.state = 551
            self.super_exp()
            compi.floop()
            self.state = 553
            self.match(BloonParser.T__37)
            compi.floop_check()
            self.state = 555
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
            self.state = 565
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 558
                self.match(BloonParser.T__40)
                self.state = 559
                self.expression()
                self.state = 560
                self.super_exp_t()
                pass
            elif token in [BloonParser.T__3, BloonParser.T__48, BloonParser.ID, BloonParser.CONST_INT, BloonParser.CONST_FLOAT, BloonParser.CONST_STR, BloonParser.CONST_CHAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 562
                self.expression()
                self.state = 563
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

        def super_exp(self):
            return self.getTypedRuleContext(BloonParser.Super_expContext,0)


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
            self.state = 572
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 567
                self.match(BloonParser.T__41)
                self.state = 568
                self.super_exp()
                pass
            elif token in [BloonParser.T__42]:
                self.enterOuterAlt(localctx, 2)
                self.state = 569
                self.match(BloonParser.T__42)
                self.state = 570
                self.super_exp()
                pass
            elif token in [BloonParser.T__1, BloonParser.T__4, BloonParser.T__13, BloonParser.T__37]:
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
            self.state = 574
            self.exp()
            self.state = 594
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BloonParser.T__6) | (1 << BloonParser.T__8) | (1 << BloonParser.T__43) | (1 << BloonParser.T__44) | (1 << BloonParser.T__45) | (1 << BloonParser.T__46))) != 0):
                self.state = 587
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BloonParser.T__8]:
                    self.state = 575
                    self.match(BloonParser.T__8)
                    compi.add_op('>')
                    pass
                elif token in [BloonParser.T__6]:
                    self.state = 577
                    self.match(BloonParser.T__6)
                    compi.add_op('<')
                    pass
                elif token in [BloonParser.T__43]:
                    self.state = 579
                    self.match(BloonParser.T__43)
                    compi.add_op('>=')
                    pass
                elif token in [BloonParser.T__44]:
                    self.state = 581
                    self.match(BloonParser.T__44)
                    compi.add_op('<=')
                    pass
                elif token in [BloonParser.T__45]:
                    self.state = 583
                    self.match(BloonParser.T__45)
                    compi.add_op('==')
                    pass
                elif token in [BloonParser.T__46]:
                    self.state = 585
                    self.match(BloonParser.T__46)
                    compi.add_op('!=')
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 589
                self.exp()
                compi.arithmetic_operation('>', '<', '>=', '<=', '==', '!=')
                self.state = 596
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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 597
            self.term()
            self.state = 609
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BloonParser.T__47 or _la==BloonParser.T__48:
                self.state = 602
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BloonParser.T__47]:
                    self.state = 598
                    self.match(BloonParser.T__47)
                    compi.add_op('+')
                    pass
                elif token in [BloonParser.T__48]:
                    self.state = 600
                    self.match(BloonParser.T__48)
                    compi.add_op('-')
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 604
                self.term()
                compi.arithmetic_operation('+', '-')
                self.state = 611
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.state = 612
            self.factor()
            self.state = 626
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BloonParser.T__49) | (1 << BloonParser.T__50) | (1 << BloonParser.T__51))) != 0):
                self.state = 619
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BloonParser.T__49]:
                    self.state = 613
                    self.match(BloonParser.T__49)
                    compi.add_op('*')
                    pass
                elif token in [BloonParser.T__50]:
                    self.state = 615
                    self.match(BloonParser.T__50)
                    compi.add_op('/')
                    pass
                elif token in [BloonParser.T__51]:
                    self.state = 617
                    self.match(BloonParser.T__51)
                    compi.add_op('%')
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 621
                self.factor()
                compi.arithmetic_operation('*', '/', '%')
                self.state = 628
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
            self.state = 638
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 629
                self.match(BloonParser.T__3)
                compi.open_parens()
                self.state = 631
                self.expression()
                self.state = 632
                self.match(BloonParser.T__4)
                compi.close_parens()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 635
                self.var_const()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 636
                self.call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 637
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
            self.state = 644
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.ID, BloonParser.CONST_INT, BloonParser.CONST_FLOAT, BloonParser.CONST_STR, BloonParser.CONST_CHAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 640
                self.var_const()
                pass
            elif token in [BloonParser.T__48]:
                self.enterOuterAlt(localctx, 2)
                self.state = 641
                self.match(BloonParser.T__48)
                compi.set_negative()
                self.state = 643
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
            self.state = 655
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 646
                self.var()
                pass
            elif token in [BloonParser.CONST_INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 647
                localctx._CONST_INT = self.match(BloonParser.CONST_INT)
                compi.get_const((None if localctx._CONST_INT is None else localctx._CONST_INT.text), "int")
                pass
            elif token in [BloonParser.CONST_FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 649
                localctx._CONST_FLOAT = self.match(BloonParser.CONST_FLOAT)
                compi.get_const((None if localctx._CONST_FLOAT is None else localctx._CONST_FLOAT.text), "float")
                pass
            elif token in [BloonParser.CONST_STR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 651
                localctx._CONST_STR = self.match(BloonParser.CONST_STR)
                compi.get_const((None if localctx._CONST_STR is None else localctx._CONST_STR.text), "string")
                pass
            elif token in [BloonParser.CONST_CHAR]:
                self.enterOuterAlt(localctx, 5)
                self.state = 653
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





