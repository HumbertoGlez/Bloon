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
type_dir = None
constants = None


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3<")
        buf.write("\u023d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\5\3z\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u008d\n\6\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u009a\n")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\5\t\u00a1\n\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\5\n\u00ab\n\n\3\13\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00b9\n\f\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\5\r\u00c4\n\r\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\5\17\u00d4\n\17\3\17\3\17\3\17\5\17\u00d9\n\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\5\17\u00e8\n\17\5\17\u00ea\n\17\3\20\3\20\5\20\u00ee")
        buf.write("\n\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\5\22\u00fd\n\22\3\23\3\23\3\24\3\24\3")
        buf.write("\25\3\25\3\26\3\26\5\26\u0107\n\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\5\27\u0111\n\27\3\30\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\5\31\u011f")
        buf.write("\n\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\5\33\u012d\n\33\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\5\34\u0142\n\34\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u0159\n\34\3\34\3")
        buf.write("\34\5\34\u015d\n\34\3\35\3\35\3\35\5\35\u0162\n\35\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u016e")
        buf.write("\n\37\3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\5!\u017d")
        buf.write("\n!\3!\3!\7!\u0181\n!\f!\16!\u0184\13!\3!\3!\3!\3\"\3")
        buf.write("\"\3\"\3#\3#\3#\3#\3#\3$\3$\3$\3$\3%\3%\3%\3%\3%\5%\u019a")
        buf.write("\n%\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3\'\5\'\u01ab\n\'\3(\3(\3(\3(\3(\5(\u01b2\n(\3)\3)\3")
        buf.write(")\3)\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\5*\u01c3\n*\3+\3")
        buf.write("+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3,\3")
        buf.write(",\3,\3-\3-\3-\3-\3-\3-\3-\5-\u01e1\n-\3.\3.\3.\3.\3.\5")
        buf.write(".\u01e8\n.\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\5/\u01f7")
        buf.write("\n/\3/\3/\3/\7/\u01fc\n/\f/\16/\u01ff\13/\3\60\3\60\3")
        buf.write("\60\3\60\3\60\5\60\u0206\n\60\3\60\3\60\3\60\7\60\u020b")
        buf.write("\n\60\f\60\16\60\u020e\13\60\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\5\61\u0217\n\61\3\61\3\61\3\61\7\61\u021c\n")
        buf.write("\61\f\61\16\61\u021f\13\61\3\62\3\62\3\62\3\62\3\62\3")
        buf.write("\62\3\62\3\62\3\62\5\62\u022a\n\62\3\63\3\63\3\63\3\63")
        buf.write("\5\63\u0230\n\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3")
        buf.write("\64\3\64\5\64\u023b\n\64\3\64\2\2\65\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJL")
        buf.write("NPRTVXZ\\^`bdf\2\4\3\2\27\32\3\2\33\36\2\u0249\2h\3\2")
        buf.write("\2\2\4y\3\2\2\2\6{\3\2\2\2\b\u0082\3\2\2\2\n\u008c\3\2")
        buf.write("\2\2\f\u008e\3\2\2\2\16\u0099\3\2\2\2\20\u00a0\3\2\2\2")
        buf.write("\22\u00aa\3\2\2\2\24\u00ac\3\2\2\2\26\u00b8\3\2\2\2\30")
        buf.write("\u00ba\3\2\2\2\32\u00c5\3\2\2\2\34\u00d8\3\2\2\2\36\u00ed")
        buf.write("\3\2\2\2 \u00ef\3\2\2\2\"\u00fc\3\2\2\2$\u00fe\3\2\2\2")
        buf.write("&\u0100\3\2\2\2(\u0102\3\2\2\2*\u0106\3\2\2\2,\u0110\3")
        buf.write("\2\2\2.\u0112\3\2\2\2\60\u011e\3\2\2\2\62\u0120\3\2\2")
        buf.write("\2\64\u012c\3\2\2\2\66\u015c\3\2\2\28\u0161\3\2\2\2:\u0163")
        buf.write("\3\2\2\2<\u016d\3\2\2\2>\u016f\3\2\2\2@\u0177\3\2\2\2")
        buf.write("B\u0188\3\2\2\2D\u018b\3\2\2\2F\u0190\3\2\2\2H\u0199\3")
        buf.write("\2\2\2J\u019b\3\2\2\2L\u01aa\3\2\2\2N\u01b1\3\2\2\2P\u01b3")
        buf.write("\3\2\2\2R\u01c2\3\2\2\2T\u01c4\3\2\2\2V\u01cf\3\2\2\2")
        buf.write("X\u01e0\3\2\2\2Z\u01e7\3\2\2\2\\\u01e9\3\2\2\2^\u0200")
        buf.write("\3\2\2\2`\u020f\3\2\2\2b\u0229\3\2\2\2d\u022f\3\2\2\2")
        buf.write("f\u023a\3\2\2\2hi\7\3\2\2ij\7\67\2\2jk\7\4\2\2kl\5\4\3")
        buf.write("\2lm\b\2\1\2mn\7\2\2\3n\3\3\2\2\2op\5\b\5\2pq\5\4\3\2")
        buf.write("qz\3\2\2\2rs\5\32\16\2st\5\4\3\2tz\3\2\2\2uv\5.\30\2v")
        buf.write("w\5\4\3\2wz\3\2\2\2xz\5\6\4\2yo\3\2\2\2yr\3\2\2\2yu\3")
        buf.write("\2\2\2yx\3\2\2\2z\5\3\2\2\2{|\7\5\2\2|}\7\6\2\2}~\b\4")
        buf.write("\1\2~\177\7\7\2\2\177\u0080\b\4\1\2\u0080\u0081\5:\36")
        buf.write("\2\u0081\7\3\2\2\2\u0082\u0083\7\b\2\2\u0083\u0084\7\67")
        buf.write("\2\2\u0084\u0085\5\n\6\2\u0085\t\3\2\2\2\u0086\u0087\7")
        buf.write("\t\2\2\u0087\u0088\7\n\2\2\u0088\u0089\7\67\2\2\u0089")
        buf.write("\u008a\7\13\2\2\u008a\u008d\5\f\7\2\u008b\u008d\5\f\7")
        buf.write("\2\u008c\u0086\3\2\2\2\u008c\u008b\3\2\2\2\u008d\13\3")
        buf.write("\2\2\2\u008e\u008f\7\4\2\2\u008f\u0090\7\f\2\2\u0090\u0091")
        buf.write("\5\16\b\2\u0091\r\3\2\2\2\u0092\u0093\7\r\2\2\u0093\u0094")
        buf.write("\7\t\2\2\u0094\u0095\5\32\16\2\u0095\u0096\7\13\2\2\u0096")
        buf.write("\u0097\5\20\t\2\u0097\u009a\3\2\2\2\u0098\u009a\5\20\t")
        buf.write("\2\u0099\u0092\3\2\2\2\u0099\u0098\3\2\2\2\u009a\17\3")
        buf.write("\2\2\2\u009b\u009c\7\16\2\2\u009c\u009d\7\t\2\2\u009d")
        buf.write("\u00a1\5\22\n\2\u009e\u009f\7\17\2\2\u009f\u00a1\7\4\2")
        buf.write("\2\u00a0\u009b\3\2\2\2\u00a0\u009e\3\2\2\2\u00a1\21\3")
        buf.write("\2\2\2\u00a2\u00a3\5.\30\2\u00a3\u00a4\7\13\2\2\u00a4")
        buf.write("\u00a5\7\17\2\2\u00a5\u00a6\7\4\2\2\u00a6\u00ab\3\2\2")
        buf.write("\2\u00a7\u00a8\5.\30\2\u00a8\u00a9\5\22\n\2\u00a9\u00ab")
        buf.write("\3\2\2\2\u00aa\u00a2\3\2\2\2\u00aa\u00a7\3\2\2\2\u00ab")
        buf.write("\23\3\2\2\2\u00ac\u00ad\7\67\2\2\u00ad\u00ae\b\13\1\2")
        buf.write("\u00ae\u00af\5\26\f\2\u00af\25\3\2\2\2\u00b0\u00b9\5\30")
        buf.write("\r\2\u00b1\u00b2\5\30\r\2\u00b2\u00b3\7\20\2\2\u00b3\u00b4")
        buf.write("\5\24\13\2\u00b4\u00b9\3\2\2\2\u00b5\u00b6\7\20\2\2\u00b6")
        buf.write("\u00b9\5\24\13\2\u00b7\u00b9\b\f\1\2\u00b8\u00b0\3\2\2")
        buf.write("\2\u00b8\u00b1\3\2\2\2\u00b8\u00b5\3\2\2\2\u00b8\u00b7")
        buf.write("\3\2\2\2\u00b9\27\3\2\2\2\u00ba\u00bb\7\21\2\2\u00bb\u00c3")
        buf.write("\5^\60\2\u00bc\u00bd\7\22\2\2\u00bd\u00be\5^\60\2\u00be")
        buf.write("\u00bf\7\23\2\2\u00bf\u00c0\b\r\1\2\u00c0\u00c4\3\2\2")
        buf.write("\2\u00c1\u00c2\7\23\2\2\u00c2\u00c4\b\r\1\2\u00c3\u00bc")
        buf.write("\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c4\31\3\2\2\2\u00c5\u00c6")
        buf.write("\7\24\2\2\u00c6\u00c7\5\34\17\2\u00c7\33\3\2\2\2\u00c8")
        buf.write("\u00c9\7\67\2\2\u00c9\u00ca\7\21\2\2\u00ca\u00cb\78\2")
        buf.write("\2\u00cb\u00d3\b\17\1\2\u00cc\u00cd\7\22\2\2\u00cd\u00ce")
        buf.write("\78\2\2\u00ce\u00cf\b\17\1\2\u00cf\u00d0\7\23\2\2\u00d0")
        buf.write("\u00d4\b\17\1\2\u00d1\u00d2\7\23\2\2\u00d2\u00d4\b\17")
        buf.write("\1\2\u00d3\u00cc\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d4\u00d5")
        buf.write("\3\2\2\2\u00d5\u00d9\b\17\1\2\u00d6\u00d7\7\67\2\2\u00d7")
        buf.write("\u00d9\b\17\1\2\u00d8\u00c8\3\2\2\2\u00d8\u00d6\3\2\2")
        buf.write("\2\u00d9\u00e9\3\2\2\2\u00da\u00db\7\22\2\2\u00db\u00ea")
        buf.write("\5\34\17\2\u00dc\u00e7\7\25\2\2\u00dd\u00de\5$\23\2\u00de")
        buf.write("\u00df\b\17\1\2\u00df\u00e0\7\4\2\2\u00e0\u00e1\5\36\20")
        buf.write("\2\u00e1\u00e8\3\2\2\2\u00e2\u00e3\5&\24\2\u00e3\u00e4")
        buf.write("\b\17\1\2\u00e4\u00e5\7\4\2\2\u00e5\u00e6\5\36\20\2\u00e6")
        buf.write("\u00e8\3\2\2\2\u00e7\u00dd\3\2\2\2\u00e7\u00e2\3\2\2\2")
        buf.write("\u00e8\u00ea\3\2\2\2\u00e9\u00da\3\2\2\2\u00e9\u00dc\3")
        buf.write("\2\2\2\u00ea\35\3\2\2\2\u00eb\u00ee\5\34\17\2\u00ec\u00ee")
        buf.write("\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed\u00ec\3\2\2\2\u00ee")
        buf.write("\37\3\2\2\2\u00ef\u00f0\5\24\13\2\u00f0\u00f1\5\"\22\2")
        buf.write("\u00f1!\3\2\2\2\u00f2\u00f3\7\26\2\2\u00f3\u00f4\5X-\2")
        buf.write("\u00f4\u00f5\b\22\1\2\u00f5\u00f6\7\4\2\2\u00f6\u00fd")
        buf.write("\3\2\2\2\u00f7\u00f8\5(\25\2\u00f8\u00f9\5X-\2\u00f9\u00fa")
        buf.write("\b\22\1\2\u00fa\u00fb\7\4\2\2\u00fb\u00fd\3\2\2\2\u00fc")
        buf.write("\u00f2\3\2\2\2\u00fc\u00f7\3\2\2\2\u00fd#\3\2\2\2\u00fe")
        buf.write("\u00ff\t\2\2\2\u00ff%\3\2\2\2\u0100\u0101\7\67\2\2\u0101")
        buf.write("\'\3\2\2\2\u0102\u0103\t\3\2\2\u0103)\3\2\2\2\u0104\u0107")
        buf.write("\5$\23\2\u0105\u0107\7\37\2\2\u0106\u0104\3\2\2\2\u0106")
        buf.write("\u0105\3\2\2\2\u0107+\3\2\2\2\u0108\u0111\5 \21\2\u0109")
        buf.write("\u0111\5P)\2\u010a\u0111\5> \2\u010b\u0111\5D#\2\u010c")
        buf.write("\u0111\5J&\2\u010d\u0111\5T+\2\u010e\u0111\5V,\2\u010f")
        buf.write("\u0111\5B\"\2\u0110\u0108\3\2\2\2\u0110\u0109\3\2\2\2")
        buf.write("\u0110\u010a\3\2\2\2\u0110\u010b\3\2\2\2\u0110\u010c\3")
        buf.write("\2\2\2\u0110\u010d\3\2\2\2\u0110\u010e\3\2\2\2\u0110\u010f")
        buf.write("\3\2\2\2\u0111-\3\2\2\2\u0112\u0113\5*\26\2\u0113\u0114")
        buf.write("\7 \2\2\u0114\u0115\7\67\2\2\u0115\u0116\b\30\1\2\u0116")
        buf.write("\u0117\7\6\2\2\u0117\u0118\b\30\1\2\u0118\u0119\5\60\31")
        buf.write("\2\u0119/\3\2\2\2\u011a\u011b\5\66\34\2\u011b\u011c\5")
        buf.write("\62\32\2\u011c\u011f\3\2\2\2\u011d\u011f\5\62\32\2\u011e")
        buf.write("\u011a\3\2\2\2\u011e\u011d\3\2\2\2\u011f\61\3\2\2\2\u0120")
        buf.write("\u0121\7\7\2\2\u0121\u0122\b\32\1\2\u0122\u0123\7\4\2")
        buf.write("\2\u0123\u0124\5\64\33\2\u0124\63\3\2\2\2\u0125\u0126")
        buf.write("\5\32\16\2\u0126\u0127\5:\36\2\u0127\u0128\b\33\1\2\u0128")
        buf.write("\u012d\3\2\2\2\u0129\u012a\5:\36\2\u012a\u012b\b\33\1")
        buf.write("\2\u012b\u012d\3\2\2\2\u012c\u0125\3\2\2\2\u012c\u0129")
        buf.write("\3\2\2\2\u012d\65\3\2\2\2\u012e\u012f\5$\23\2\u012f\u0130")
        buf.write("\7\67\2\2\u0130\u0131\b\34\1\2\u0131\u0132\58\35\2\u0132")
        buf.write("\u015d\3\2\2\2\u0133\u0134\5$\23\2\u0134\u0141\7\67\2")
        buf.write("\2\u0135\u0136\7\21\2\2\u0136\u0137\78\2\2\u0137\u0138")
        buf.write("\7\23\2\2\u0138\u0142\b\34\1\2\u0139\u013a\7\21\2\2\u013a")
        buf.write("\u013b\78\2\2\u013b\u013c\b\34\1\2\u013c\u013d\7\22\2")
        buf.write("\2\u013d\u013e\78\2\2\u013e\u013f\b\34\1\2\u013f\u0140")
        buf.write("\7\23\2\2\u0140\u0142\b\34\1\2\u0141\u0135\3\2\2\2\u0141")
        buf.write("\u0139\3\2\2\2\u0142\u0143\3\2\2\2\u0143\u0144\58\35\2")
        buf.write("\u0144\u015d\3\2\2\2\u0145\u0146\5&\24\2\u0146\u0147\7")
        buf.write("\67\2\2\u0147\u0148\b\34\1\2\u0148\u0149\58\35\2\u0149")
        buf.write("\u015d\3\2\2\2\u014a\u014b\5&\24\2\u014b\u0158\7\67\2")
        buf.write("\2\u014c\u014d\7\21\2\2\u014d\u014e\78\2\2\u014e\u014f")
        buf.write("\7\23\2\2\u014f\u0159\b\34\1\2\u0150\u0151\7\21\2\2\u0151")
        buf.write("\u0152\78\2\2\u0152\u0153\b\34\1\2\u0153\u0154\7\22\2")
        buf.write("\2\u0154\u0155\78\2\2\u0155\u0156\b\34\1\2\u0156\u0157")
        buf.write("\7\23\2\2\u0157\u0159\b\34\1\2\u0158\u014c\3\2\2\2\u0158")
        buf.write("\u0150\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u015b\58\35\2")
        buf.write("\u015b\u015d\3\2\2\2\u015c\u012e\3\2\2\2\u015c\u0133\3")
        buf.write("\2\2\2\u015c\u0145\3\2\2\2\u015c\u014a\3\2\2\2\u015d\67")
        buf.write("\3\2\2\2\u015e\u015f\7\22\2\2\u015f\u0162\5\66\34\2\u0160")
        buf.write("\u0162\3\2\2\2\u0161\u015e\3\2\2\2\u0161\u0160\3\2\2\2")
        buf.write("\u01629\3\2\2\2\u0163\u0164\7\f\2\2\u0164\u0165\5<\37")
        buf.write("\2\u0165;\3\2\2\2\u0166\u0167\5,\27\2\u0167\u0168\5<\37")
        buf.write("\2\u0168\u016e\3\2\2\2\u0169\u016a\5,\27\2\u016a\u016b")
        buf.write("\7\17\2\2\u016b\u016e\3\2\2\2\u016c\u016e\7\17\2\2\u016d")
        buf.write("\u0166\3\2\2\2\u016d\u0169\3\2\2\2\u016d\u016c\3\2\2\2")
        buf.write("\u016e=\3\2\2\2\u016f\u0170\7!\2\2\u0170\u0171\7\6\2\2")
        buf.write("\u0171\u0172\b \1\2\u0172\u0173\5X-\2\u0173\u0174\7\7")
        buf.write("\2\2\u0174\u0175\b \1\2\u0175\u0176\7\4\2\2\u0176?\3\2")
        buf.write("\2\2\u0177\u0178\7\67\2\2\u0178\u0179\b!\1\2\u0179\u017a")
        buf.write("\7\6\2\2\u017a\u017c\b!\1\2\u017b\u017d\5X-\2\u017c\u017b")
        buf.write("\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u0182\3\2\2\2\u017e")
        buf.write("\u017f\7\22\2\2\u017f\u0181\5X-\2\u0180\u017e\3\2\2\2")
        buf.write("\u0181\u0184\3\2\2\2\u0182\u0180\3\2\2\2\u0182\u0183\3")
        buf.write("\2\2\2\u0183\u0185\3\2\2\2\u0184\u0182\3\2\2\2\u0185\u0186")
        buf.write("\7\7\2\2\u0186\u0187\b!\1\2\u0187A\3\2\2\2\u0188\u0189")
        buf.write("\5@!\2\u0189\u018a\7\4\2\2\u018aC\3\2\2\2\u018b\u018c")
        buf.write("\7\"\2\2\u018c\u018d\7\6\2\2\u018d\u018e\b#\1\2\u018e")
        buf.write("\u018f\5F$\2\u018fE\3\2\2\2\u0190\u0191\5\24\13\2\u0191")
        buf.write("\u0192\b$\1\2\u0192\u0193\5H%\2\u0193G\3\2\2\2\u0194\u0195")
        buf.write("\7\22\2\2\u0195\u019a\5F$\2\u0196\u0197\7\7\2\2\u0197")
        buf.write("\u0198\b%\1\2\u0198\u019a\7\4\2\2\u0199\u0194\3\2\2\2")
        buf.write("\u0199\u0196\3\2\2\2\u019aI\3\2\2\2\u019b\u019c\7#\2\2")
        buf.write("\u019c\u019d\7\6\2\2\u019d\u019e\b&\1\2\u019e\u019f\5")
        buf.write("L\'\2\u019fK\3\2\2\2\u01a0\u01a1\5X-\2\u01a1\u01a2\b\'")
        buf.write("\1\2\u01a2\u01a3\5N(\2\u01a3\u01ab\3\2\2\2\u01a4\u01a5")
        buf.write("\7:\2\2\u01a5\u01a6\b\'\1\2\u01a6\u01ab\5N(\2\u01a7\u01a8")
        buf.write("\5@!\2\u01a8\u01a9\5N(\2\u01a9\u01ab\3\2\2\2\u01aa\u01a0")
        buf.write("\3\2\2\2\u01aa\u01a4\3\2\2\2\u01aa\u01a7\3\2\2\2\u01ab")
        buf.write("M\3\2\2\2\u01ac\u01ad\7\22\2\2\u01ad\u01b2\5L\'\2\u01ae")
        buf.write("\u01af\7\7\2\2\u01af\u01b0\b(\1\2\u01b0\u01b2\7\4\2\2")
        buf.write("\u01b1\u01ac\3\2\2\2\u01b1\u01ae\3\2\2\2\u01b2O\3\2\2")
        buf.write("\2\u01b3\u01b4\7$\2\2\u01b4\u01b5\7\6\2\2\u01b5\u01b6")
        buf.write("\b)\1\2\u01b6\u01b7\5X-\2\u01b7\u01b8\7\7\2\2\u01b8\u01b9")
        buf.write("\b)\1\2\u01b9\u01ba\7%\2\2\u01ba\u01bb\5:\36\2\u01bb\u01bc")
        buf.write("\5R*\2\u01bc\u01bd\b)\1\2\u01bdQ\3\2\2\2\u01be\u01bf\7")
        buf.write("&\2\2\u01bf\u01c0\b*\1\2\u01c0\u01c3\5:\36\2\u01c1\u01c3")
        buf.write("\3\2\2\2\u01c2\u01be\3\2\2\2\u01c2\u01c1\3\2\2\2\u01c3")
        buf.write("S\3\2\2\2\u01c4\u01c5\7\'\2\2\u01c5\u01c6\b+\1\2\u01c6")
        buf.write("\u01c7\7\6\2\2\u01c7\u01c8\b+\1\2\u01c8\u01c9\5X-\2\u01c9")
        buf.write("\u01ca\7\7\2\2\u01ca\u01cb\b+\1\2\u01cb\u01cc\7(\2\2\u01cc")
        buf.write("\u01cd\5:\36\2\u01cd\u01ce\b+\1\2\u01ceU\3\2\2\2\u01cf")
        buf.write("\u01d0\7)\2\2\u01d0\u01d1\5\24\13\2\u01d1\u01d2\7*\2\2")
        buf.write("\u01d2\u01d3\5X-\2\u01d3\u01d4\b,\1\2\u01d4\u01d5\7(\2")
        buf.write("\2\u01d5\u01d6\b,\1\2\u01d6\u01d7\5:\36\2\u01d7\u01d8")
        buf.write("\b,\1\2\u01d8W\3\2\2\2\u01d9\u01da\7+\2\2\u01da\u01db")
        buf.write("\5\\/\2\u01db\u01dc\5Z.\2\u01dc\u01e1\3\2\2\2\u01dd\u01de")
        buf.write("\5\\/\2\u01de\u01df\5Z.\2\u01df\u01e1\3\2\2\2\u01e0\u01d9")
        buf.write("\3\2\2\2\u01e0\u01dd\3\2\2\2\u01e1Y\3\2\2\2\u01e2\u01e3")
        buf.write("\7,\2\2\u01e3\u01e8\5X-\2\u01e4\u01e5\7-\2\2\u01e5\u01e8")
        buf.write("\5X-\2\u01e6\u01e8\3\2\2\2\u01e7\u01e2\3\2\2\2\u01e7\u01e4")
        buf.write("\3\2\2\2\u01e7\u01e6\3\2\2\2\u01e8[\3\2\2\2\u01e9\u01fd")
        buf.write("\5^\60\2\u01ea\u01eb\7\13\2\2\u01eb\u01f7\b/\1\2\u01ec")
        buf.write("\u01ed\7\t\2\2\u01ed\u01f7\b/\1\2\u01ee\u01ef\7.\2\2\u01ef")
        buf.write("\u01f7\b/\1\2\u01f0\u01f1\7/\2\2\u01f1\u01f7\b/\1\2\u01f2")
        buf.write("\u01f3\7\60\2\2\u01f3\u01f7\b/\1\2\u01f4\u01f5\7\61\2")
        buf.write("\2\u01f5\u01f7\b/\1\2\u01f6\u01ea\3\2\2\2\u01f6\u01ec")
        buf.write("\3\2\2\2\u01f6\u01ee\3\2\2\2\u01f6\u01f0\3\2\2\2\u01f6")
        buf.write("\u01f2\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f7\u01f8\3\2\2\2")
        buf.write("\u01f8\u01f9\5^\60\2\u01f9\u01fa\b/\1\2\u01fa\u01fc\3")
        buf.write("\2\2\2\u01fb\u01f6\3\2\2\2\u01fc\u01ff\3\2\2\2\u01fd\u01fb")
        buf.write("\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe]\3\2\2\2\u01ff\u01fd")
        buf.write("\3\2\2\2\u0200\u020c\5`\61\2\u0201\u0202\7\62\2\2\u0202")
        buf.write("\u0206\b\60\1\2\u0203\u0204\7\63\2\2\u0204\u0206\b\60")
        buf.write("\1\2\u0205\u0201\3\2\2\2\u0205\u0203\3\2\2\2\u0206\u0207")
        buf.write("\3\2\2\2\u0207\u0208\5`\61\2\u0208\u0209\b\60\1\2\u0209")
        buf.write("\u020b\3\2\2\2\u020a\u0205\3\2\2\2\u020b\u020e\3\2\2\2")
        buf.write("\u020c\u020a\3\2\2\2\u020c\u020d\3\2\2\2\u020d_\3\2\2")
        buf.write("\2\u020e\u020c\3\2\2\2\u020f\u021d\5b\62\2\u0210\u0211")
        buf.write("\7\64\2\2\u0211\u0217\b\61\1\2\u0212\u0213\7\65\2\2\u0213")
        buf.write("\u0217\b\61\1\2\u0214\u0215\7\66\2\2\u0215\u0217\b\61")
        buf.write("\1\2\u0216\u0210\3\2\2\2\u0216\u0212\3\2\2\2\u0216\u0214")
        buf.write("\3\2\2\2\u0217\u0218\3\2\2\2\u0218\u0219\5b\62\2\u0219")
        buf.write("\u021a\b\61\1\2\u021a\u021c\3\2\2\2\u021b\u0216\3\2\2")
        buf.write("\2\u021c\u021f\3\2\2\2\u021d\u021b\3\2\2\2\u021d\u021e")
        buf.write("\3\2\2\2\u021ea\3\2\2\2\u021f\u021d\3\2\2\2\u0220\u0221")
        buf.write("\7\6\2\2\u0221\u0222\b\62\1\2\u0222\u0223\5\\/\2\u0223")
        buf.write("\u0224\7\7\2\2\u0224\u0225\b\62\1\2\u0225\u022a\3\2\2")
        buf.write("\2\u0226\u022a\5f\64\2\u0227\u022a\5@!\2\u0228\u022a\5")
        buf.write("d\63\2\u0229\u0220\3\2\2\2\u0229\u0226\3\2\2\2\u0229\u0227")
        buf.write("\3\2\2\2\u0229\u0228\3\2\2\2\u022ac\3\2\2\2\u022b\u0230")
        buf.write("\5f\64\2\u022c\u022d\7\63\2\2\u022d\u022e\b\63\1\2\u022e")
        buf.write("\u0230\5f\64\2\u022f\u022b\3\2\2\2\u022f\u022c\3\2\2\2")
        buf.write("\u0230e\3\2\2\2\u0231\u023b\5\24\13\2\u0232\u0233\78\2")
        buf.write("\2\u0233\u023b\b\64\1\2\u0234\u0235\79\2\2\u0235\u023b")
        buf.write("\b\64\1\2\u0236\u0237\7:\2\2\u0237\u023b\b\64\1\2\u0238")
        buf.write("\u0239\7;\2\2\u0239\u023b\b\64\1\2\u023a\u0231\3\2\2\2")
        buf.write("\u023a\u0232\3\2\2\2\u023a\u0234\3\2\2\2\u023a\u0236\3")
        buf.write("\2\2\2\u023a\u0238\3\2\2\2\u023bg\3\2\2\2)y\u008c\u0099")
        buf.write("\u00a0\u00aa\u00b8\u00c3\u00d3\u00d8\u00e7\u00e9\u00ed")
        buf.write("\u00fc\u0106\u0110\u011e\u012c\u0141\u0158\u015c\u0161")
        buf.write("\u016d\u017c\u0182\u0199\u01aa\u01b1\u01c2\u01e0\u01e7")
        buf.write("\u01f6\u01fd\u0205\u020c\u0216\u021d\u0229\u022f\u023a")
        return buf.getvalue()


class BloonParser ( Parser ):

    grammarFileName = "Bloon.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "';'", "'main'", "'('", "')'", 
                     "'class'", "'<'", "'inherits'", "'>'", "'{'", "'attributes'", 
                     "'methods'", "'}'", "'.'", "'['", "','", "']'", "'vars'", 
                     "':'", "'='", "'int'", "'float'", "'char'", "'string'", 
                     "'+='", "'-='", "'*='", "'/='", "'void'", "'meth'", 
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
    RULE_class_j = 6
    RULE_class_l = 7
    RULE_class_p = 8
    RULE_var = 9
    RULE_var_t = 10
    RULE_arr_idx = 11
    RULE_var_dec = 12
    RULE_var_dec_t = 13
    RULE_var_dec_l = 14
    RULE_assign = 15
    RULE_assign_t = 16
    RULE_var_type = 17
    RULE_custom_type = 18
    RULE_assign_op = 19
    RULE_type_meth = 20
    RULE_statement = 21
    RULE_func = 22
    RULE_func_t = 23
    RULE_func_k = 24
    RULE_func_p = 25
    RULE_param = 26
    RULE_param_t = 27
    RULE_block = 28
    RULE_block_t = 29
    RULE_r_return = 30
    RULE_call = 31
    RULE_call_void = 32
    RULE_read = 33
    RULE_read_t = 34
    RULE_read_k = 35
    RULE_write = 36
    RULE_write_t = 37
    RULE_write_k = 38
    RULE_cond = 39
    RULE_cond_t = 40
    RULE_r_while = 41
    RULE_floop = 42
    RULE_super_exp = 43
    RULE_super_exp_t = 44
    RULE_expression = 45
    RULE_exp = 46
    RULE_term = 47
    RULE_factor = 48
    RULE_factor_t = 49
    RULE_var_const = 50

    ruleNames =  [ "program", "program_t", "main", "r_class", "class_t", 
                   "class_k", "class_j", "class_l", "class_p", "var", "var_t", 
                   "arr_idx", "var_dec", "var_dec_t", "var_dec_l", "assign", 
                   "assign_t", "var_type", "custom_type", "assign_op", "type_meth", 
                   "statement", "func", "func_t", "func_k", "func_p", "param", 
                   "param_t", "block", "block_t", "r_return", "call", "call_void", 
                   "read", "read_t", "read_k", "write", "write_t", "write_k", 
                   "cond", "cond_t", "r_while", "floop", "super_exp", "super_exp_t", 
                   "expression", "exp", "term", "factor", "factor_t", "var_const" ]

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
            self.state = 102
            self.match(BloonParser.T__0)
            self.state = 103
            self.match(BloonParser.ID)
            self.state = 104
            self.match(BloonParser.T__1)
            self.state = 105
            self.program_t()
            compi.save_state(self)
            self.state = 107
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
            self.state = 119
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.r_class()
                self.state = 110
                self.program_t()
                pass
            elif token in [BloonParser.T__17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.var_dec()
                self.state = 113
                self.program_t()
                pass
            elif token in [BloonParser.T__20, BloonParser.T__21, BloonParser.T__22, BloonParser.T__23, BloonParser.T__28]:
                self.enterOuterAlt(localctx, 3)
                self.state = 115
                self.func()
                self.state = 116
                self.program_t()
                pass
            elif token in [BloonParser.T__2]:
                self.enterOuterAlt(localctx, 4)
                self.state = 118
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
            self.state = 121
            self.match(BloonParser.T__2)
            self.state = 122
            self.match(BloonParser.T__3)
            compi.open_parens()
            self.state = 124
            self.match(BloonParser.T__4)
            compi.close_parens(); compi.main_method()
            self.state = 126
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
            self.state = 128
            self.match(BloonParser.T__5)
            self.state = 129
            self.match(BloonParser.ID)
            self.state = 130
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
            self.state = 138
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.match(BloonParser.T__6)
                self.state = 133
                self.match(BloonParser.T__7)
                self.state = 134
                self.match(BloonParser.ID)
                self.state = 135
                self.match(BloonParser.T__8)
                self.state = 136
                self.class_k()
                pass
            elif token in [BloonParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
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

        def class_j(self):
            return self.getTypedRuleContext(BloonParser.Class_jContext,0)


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
            self.state = 140
            self.match(BloonParser.T__1)
            self.state = 141
            self.match(BloonParser.T__9)
            self.state = 142
            self.class_j()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_jContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_dec(self):
            return self.getTypedRuleContext(BloonParser.Var_decContext,0)


        def class_l(self):
            return self.getTypedRuleContext(BloonParser.Class_lContext,0)


        def getRuleIndex(self):
            return BloonParser.RULE_class_j

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_j" ):
                listener.enterClass_j(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_j" ):
                listener.exitClass_j(self)




    def class_j(self):

        localctx = BloonParser.Class_jContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_class_j)
        try:
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.match(BloonParser.T__10)
                self.state = 145
                self.match(BloonParser.T__6)
                self.state = 146
                self.var_dec()
                self.state = 147
                self.match(BloonParser.T__8)
                self.state = 148
                self.class_l()
                pass
            elif token in [BloonParser.T__11, BloonParser.T__12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
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
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.match(BloonParser.T__11)
                self.state = 154
                self.match(BloonParser.T__6)
                self.state = 155
                self.class_p()
                pass
            elif token in [BloonParser.T__12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.match(BloonParser.T__12)
                self.state = 157
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

        def func(self):
            return self.getTypedRuleContext(BloonParser.FuncContext,0)


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
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.func()
                self.state = 161
                self.match(BloonParser.T__8)
                self.state = 162
                self.match(BloonParser.T__12)
                self.state = 163
                self.match(BloonParser.T__1)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                self.func()
                self.state = 166
                self.class_p()
                pass


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
        self.enterRule(localctx, 18, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            localctx._ID = self.match(BloonParser.ID)
            compi.add_operand((None if localctx._ID is None else localctx._ID.text))
            self.state = 172
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

        def arr_idx(self):
            return self.getTypedRuleContext(BloonParser.Arr_idxContext,0)


        def var(self):
            return self.getTypedRuleContext(BloonParser.VarContext,0)


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
        self.enterRule(localctx, 20, self.RULE_var_t)
        try:
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.arr_idx()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.arr_idx()
                self.state = 176
                self.match(BloonParser.T__13)
                self.state = 177
                self.var()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 179
                self.match(BloonParser.T__13)
                self.state = 180
                self.var()
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
        self.enterRule(localctx, 22, self.RULE_arr_idx)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(BloonParser.T__14)
            self.state = 185
            self.exp()
            self.state = 193
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__15]:
                self.state = 186
                self.match(BloonParser.T__15)
                self.state = 187
                self.exp()
                self.state = 188
                self.match(BloonParser.T__16)
                compi.get_array_item(2)
                pass
            elif token in [BloonParser.T__16]:
                self.state = 191
                self.match(BloonParser.T__16)
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
        self.enterRule(localctx, 24, self.RULE_var_dec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(BloonParser.T__17)
            self.state = 196
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
        self.enterRule(localctx, 26, self.RULE_var_dec_t)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 198
                localctx._ID = self.match(BloonParser.ID)
                self.state = 199
                self.match(BloonParser.T__14)
                self.state = 200
                localctx._CONST_INT = self.match(BloonParser.CONST_INT)
                compi.add_limit((None if localctx._CONST_INT is None else localctx._CONST_INT.text))
                self.state = 209
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BloonParser.T__15]:
                    self.state = 202
                    self.match(BloonParser.T__15)
                    self.state = 203
                    localctx._CONST_INT = self.match(BloonParser.CONST_INT)
                    compi.add_limit((None if localctx._CONST_INT is None else localctx._CONST_INT.text))
                    self.state = 205
                    self.match(BloonParser.T__16)
                    compi.add_operand((None if localctx._ID is None else localctx._ID.text), 2);
                    pass
                elif token in [BloonParser.T__16]:
                    self.state = 207
                    self.match(BloonParser.T__16)
                    compi.add_operand((None if localctx._ID is None else localctx._ID.text), 1)
                    pass
                else:
                    raise NoViableAltException(self)

                compi.increase_varCount()
                pass

            elif la_ == 2:
                self.state = 212
                localctx._ID = self.match(BloonParser.ID)
                compi.add_operand((None if localctx._ID is None else localctx._ID.text)); compi.increase_varCount()
                pass


            self.state = 231
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__15]:
                self.state = 216
                self.match(BloonParser.T__15)
                self.state = 217
                self.var_dec_t()
                pass
            elif token in [BloonParser.T__18]:
                self.state = 218
                self.match(BloonParser.T__18)
                self.state = 229
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BloonParser.T__20, BloonParser.T__21, BloonParser.T__22, BloonParser.T__23]:
                    self.state = 219
                    localctx._var_type = self.var_type()
                    compi.define_var((None if localctx._var_type is None else self._input.getText(localctx._var_type.start,localctx._var_type.stop)))
                    self.state = 221
                    self.match(BloonParser.T__1)
                    self.state = 222
                    self.var_dec_l()
                    pass
                elif token in [BloonParser.ID]:
                    self.state = 224
                    localctx._custom_type = self.custom_type()
                    compi.define_var((None if localctx._custom_type is None else self._input.getText(localctx._custom_type.start,localctx._custom_type.stop)))
                    self.state = 226
                    self.match(BloonParser.T__1)
                    self.state = 227
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
        self.enterRule(localctx, 28, self.RULE_var_dec_l)
        try:
            self.state = 235
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.var_dec_t()
                pass
            elif token in [BloonParser.T__2, BloonParser.T__5, BloonParser.T__8, BloonParser.T__9, BloonParser.T__17, BloonParser.T__20, BloonParser.T__21, BloonParser.T__22, BloonParser.T__23, BloonParser.T__28]:
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
        self.enterRule(localctx, 30, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.var()
            self.state = 238
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
        self.enterRule(localctx, 32, self.RULE_assign_t)
        try:
            self.state = 250
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.match(BloonParser.T__19)
                self.state = 241
                self.super_exp()
                compi.assign_var()
                self.state = 243
                self.match(BloonParser.T__1)
                pass
            elif token in [BloonParser.T__24, BloonParser.T__25, BloonParser.T__26, BloonParser.T__27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
                localctx._assign_op = self.assign_op()
                self.state = 246
                self.super_exp()
                compi.arithmetic_assign((None if localctx._assign_op is None else self._input.getText(localctx._assign_op.start,localctx._assign_op.stop)))
                self.state = 248
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
        self.enterRule(localctx, 34, self.RULE_var_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BloonParser.T__20) | (1 << BloonParser.T__21) | (1 << BloonParser.T__22) | (1 << BloonParser.T__23))) != 0)):
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
        self.enterRule(localctx, 36, self.RULE_custom_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
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
        self.enterRule(localctx, 38, self.RULE_assign_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BloonParser.T__24) | (1 << BloonParser.T__25) | (1 << BloonParser.T__26) | (1 << BloonParser.T__27))) != 0)):
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
        self.enterRule(localctx, 40, self.RULE_type_meth)
        try:
            self.state = 260
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__20, BloonParser.T__21, BloonParser.T__22, BloonParser.T__23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.var_type()
                pass
            elif token in [BloonParser.T__28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.match(BloonParser.T__28)
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
        self.enterRule(localctx, 42, self.RULE_statement)
        try:
            self.state = 270
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 263
                self.cond()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 264
                self.r_return()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 265
                self.read()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 266
                self.write()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 267
                self.r_while()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 268
                self.floop()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 269
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
        self.enterRule(localctx, 44, self.RULE_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            localctx._type_meth = self.type_meth()
            self.state = 273
            self.match(BloonParser.T__29)
            self.state = 274
            localctx._ID = self.match(BloonParser.ID)
            compi.define_method((None if localctx._type_meth is None else self._input.getText(localctx._type_meth.start,localctx._type_meth.stop)), (None if localctx._ID is None else localctx._ID.text))
            self.state = 276
            self.match(BloonParser.T__3)
            compi.open_parens()
            self.state = 278
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
        self.enterRule(localctx, 46, self.RULE_func_t)
        try:
            self.state = 284
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__20, BloonParser.T__21, BloonParser.T__22, BloonParser.T__23, BloonParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.param()
                self.state = 281
                self.func_k()
                pass
            elif token in [BloonParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
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
        self.enterRule(localctx, 48, self.RULE_func_k)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(BloonParser.T__4)
            compi.close_parens()
            self.state = 288
            self.match(BloonParser.T__1)
            self.state = 289
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
        self.enterRule(localctx, 50, self.RULE_func_p)
        try:
            self.state = 298
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.var_dec()
                self.state = 292
                self.block()
                compi.process_method()
                pass
            elif token in [BloonParser.T__9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
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
        self.enterRule(localctx, 52, self.RULE_param)
        try:
            self.state = 346
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                localctx._var_type = self.var_type()
                self.state = 301
                localctx._ID = self.match(BloonParser.ID)
                compi.define_param((None if localctx._var_type is None else self._input.getText(localctx._var_type.start,localctx._var_type.stop)), (None if localctx._ID is None else localctx._ID.text))
                self.state = 303
                self.param_t()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 305
                localctx._var_type = self.var_type()
                self.state = 306
                localctx._ID = self.match(BloonParser.ID)
                self.state = 319
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                if la_ == 1:
                    self.state = 307
                    self.match(BloonParser.T__14)
                    self.state = 308
                    localctx._CONST_INT = self.match(BloonParser.CONST_INT)
                    self.state = 309
                    self.match(BloonParser.T__16)
                    compi.add_limit((None if localctx._CONST_INT is None else localctx._CONST_INT.text)); compi.define_param((None if localctx._var_type is None else self._input.getText(localctx._var_type.start,localctx._var_type.stop)), (None if localctx._ID is None else localctx._ID.text), 1)
                    pass

                elif la_ == 2:
                    self.state = 311
                    self.match(BloonParser.T__14)
                    self.state = 312
                    localctx._CONST_INT = self.match(BloonParser.CONST_INT)
                    compi.add_limit((None if localctx._CONST_INT is None else localctx._CONST_INT.text))
                    self.state = 314
                    self.match(BloonParser.T__15)
                    self.state = 315
                    localctx._CONST_INT = self.match(BloonParser.CONST_INT)
                    compi.add_limit((None if localctx._CONST_INT is None else localctx._CONST_INT.text))
                    self.state = 317
                    self.match(BloonParser.T__16)
                    compi.define_param((None if localctx._var_type is None else self._input.getText(localctx._var_type.start,localctx._var_type.stop)), (None if localctx._ID is None else localctx._ID.text), 2)
                    pass


                self.state = 321
                self.param_t()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 323
                localctx._custom_type = self.custom_type()
                self.state = 324
                localctx._ID = self.match(BloonParser.ID)
                compi.define_param((None if localctx._custom_type is None else self._input.getText(localctx._custom_type.start,localctx._custom_type.stop)), (None if localctx._ID is None else localctx._ID.text))
                self.state = 326
                self.param_t()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 328
                localctx._custom_type = self.custom_type()
                self.state = 329
                localctx._ID = self.match(BloonParser.ID)
                self.state = 342
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 330
                    self.match(BloonParser.T__14)
                    self.state = 331
                    localctx._CONST_INT = self.match(BloonParser.CONST_INT)
                    self.state = 332
                    self.match(BloonParser.T__16)
                    compi.add_limit((None if localctx._CONST_INT is None else localctx._CONST_INT.text)); compi.define_param((None if localctx._custom_type is None else self._input.getText(localctx._custom_type.start,localctx._custom_type.stop)), (None if localctx._ID is None else localctx._ID.text), 1)
                    pass

                elif la_ == 2:
                    self.state = 334
                    self.match(BloonParser.T__14)
                    self.state = 335
                    localctx._CONST_INT = self.match(BloonParser.CONST_INT)
                    compi.add_limit((None if localctx._CONST_INT is None else localctx._CONST_INT.text))
                    self.state = 337
                    self.match(BloonParser.T__15)
                    self.state = 338
                    localctx._CONST_INT = self.match(BloonParser.CONST_INT)
                    compi.add_limit((None if localctx._CONST_INT is None else localctx._CONST_INT.text))
                    self.state = 340
                    self.match(BloonParser.T__16)
                    compi.define_param((None if localctx._custom_type is None else self._input.getText(localctx._custom_type.start,localctx._custom_type.stop)), (None if localctx._ID is None else localctx._ID.text), 2)
                    pass


                self.state = 344
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
        self.enterRule(localctx, 54, self.RULE_param_t)
        try:
            self.state = 351
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.match(BloonParser.T__15)
                self.state = 349
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
        self.enterRule(localctx, 56, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.match(BloonParser.T__9)
            self.state = 354
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
        self.enterRule(localctx, 58, self.RULE_block_t)
        try:
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.statement()
                self.state = 357
                self.block_t()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 359
                self.statement()
                self.state = 360
                self.match(BloonParser.T__12)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 362
                self.match(BloonParser.T__12)
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
        self.enterRule(localctx, 60, self.RULE_r_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(BloonParser.T__30)
            self.state = 366
            self.match(BloonParser.T__3)
            compi.open_parens()
            self.state = 368
            self.super_exp()
            self.state = 369
            self.match(BloonParser.T__4)
            compi.close_parens(); compi.rtn_stmt()
            self.state = 371
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
        self.enterRule(localctx, 62, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            localctx._ID = self.match(BloonParser.ID)
            compi.verify_method((None if localctx._ID is None else localctx._ID.text))
            self.state = 375
            self.match(BloonParser.T__3)
            compi.open_parens()
            self.state = 378
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BloonParser.T__3) | (1 << BloonParser.T__40) | (1 << BloonParser.T__48) | (1 << BloonParser.ID) | (1 << BloonParser.CONST_INT) | (1 << BloonParser.CONST_FLOAT) | (1 << BloonParser.CONST_STR) | (1 << BloonParser.CONST_CHAR))) != 0):
                self.state = 377
                self.super_exp()


            self.state = 384
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BloonParser.T__15:
                self.state = 380
                self.match(BloonParser.T__15)
                self.state = 381
                self.super_exp()
                self.state = 386
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 387
            self.match(BloonParser.T__4)
            compi.close_parens(); compi.call_method((None if localctx._ID is None else localctx._ID.text))
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
        self.enterRule(localctx, 64, self.RULE_call_void)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.call()
            self.state = 391
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
        self.enterRule(localctx, 66, self.RULE_read)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(BloonParser.T__31)
            self.state = 394
            self.match(BloonParser.T__3)
            compi.open_parens()
            self.state = 396
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
        self.enterRule(localctx, 68, self.RULE_read_t)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.var()
            compi.call_method('read')
            self.state = 400
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
        self.enterRule(localctx, 70, self.RULE_read_k)
        try:
            self.state = 407
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 402
                self.match(BloonParser.T__15)
                self.state = 403
                self.read_t()
                pass
            elif token in [BloonParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 404
                self.match(BloonParser.T__4)
                compi.close_parens()
                self.state = 406
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
        self.enterRule(localctx, 72, self.RULE_write)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.match(BloonParser.T__32)
            self.state = 410
            self.match(BloonParser.T__3)
            compi.open_parens()
            self.state = 412
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
        self.enterRule(localctx, 74, self.RULE_write_t)
        try:
            self.state = 424
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 414
                self.super_exp()
                compi.call_method('write')
                self.state = 416
                self.write_k()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 418
                localctx._CONST_STR = self.match(BloonParser.CONST_STR)
                compi.get_const((None if localctx._CONST_STR is None else localctx._CONST_STR.text), "string"); compi.call_method('write')
                self.state = 420
                self.write_k()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 421
                self.call()
                self.state = 422
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
        self.enterRule(localctx, 76, self.RULE_write_k)
        try:
            self.state = 431
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                self.match(BloonParser.T__15)
                self.state = 427
                self.write_t()
                pass
            elif token in [BloonParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 428
                self.match(BloonParser.T__4)
                compi.close_parens(); compi.new_write()
                self.state = 430
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
        self.enterRule(localctx, 78, self.RULE_cond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            self.match(BloonParser.T__33)
            self.state = 434
            self.match(BloonParser.T__3)
            compi.open_parens()
            self.state = 436
            self.super_exp()
            self.state = 437
            self.match(BloonParser.T__4)
            compi.close_parens(); compi.condition()
            self.state = 439
            self.match(BloonParser.T__34)
            self.state = 440
            self.block()
            self.state = 441
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
        self.enterRule(localctx, 80, self.RULE_cond_t)
        try:
            self.state = 448
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 444
                self.match(BloonParser.T__35)
                compi.else_condition()
                self.state = 446
                self.block()
                pass
            elif token in [BloonParser.T__12, BloonParser.T__30, BloonParser.T__31, BloonParser.T__32, BloonParser.T__33, BloonParser.T__36, BloonParser.T__38, BloonParser.ID]:
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
        self.enterRule(localctx, 82, self.RULE_r_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            self.match(BloonParser.T__36)
            compi.while_condition()
            self.state = 452
            self.match(BloonParser.T__3)
            compi.open_parens()
            self.state = 454
            self.super_exp()
            self.state = 455
            self.match(BloonParser.T__4)
            compi.close_parens(); compi.while_expression()
            self.state = 457
            self.match(BloonParser.T__37)
            self.state = 458
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
        self.enterRule(localctx, 84, self.RULE_floop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self.match(BloonParser.T__38)
            self.state = 462
            self.var()
            self.state = 463
            self.match(BloonParser.T__39)
            self.state = 464
            self.super_exp()
            compi.floop()
            self.state = 466
            self.match(BloonParser.T__37)
            compi.floop_check()
            self.state = 468
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
        self.enterRule(localctx, 86, self.RULE_super_exp)
        try:
            self.state = 478
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 471
                self.match(BloonParser.T__40)
                self.state = 472
                self.expression()
                self.state = 473
                self.super_exp_t()
                pass
            elif token in [BloonParser.T__3, BloonParser.T__48, BloonParser.ID, BloonParser.CONST_INT, BloonParser.CONST_FLOAT, BloonParser.CONST_STR, BloonParser.CONST_CHAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 475
                self.expression()
                self.state = 476
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
        self.enterRule(localctx, 88, self.RULE_super_exp_t)
        try:
            self.state = 485
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.T__41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 480
                self.match(BloonParser.T__41)
                self.state = 481
                self.super_exp()
                pass
            elif token in [BloonParser.T__42]:
                self.enterOuterAlt(localctx, 2)
                self.state = 482
                self.match(BloonParser.T__42)
                self.state = 483
                self.super_exp()
                pass
            elif token in [BloonParser.T__1, BloonParser.T__4, BloonParser.T__15, BloonParser.T__37]:
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
        self.enterRule(localctx, 90, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            self.exp()
            self.state = 507
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BloonParser.T__6) | (1 << BloonParser.T__8) | (1 << BloonParser.T__43) | (1 << BloonParser.T__44) | (1 << BloonParser.T__45) | (1 << BloonParser.T__46))) != 0):
                self.state = 500
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BloonParser.T__8]:
                    self.state = 488
                    self.match(BloonParser.T__8)
                    compi.add_op('>')
                    pass
                elif token in [BloonParser.T__6]:
                    self.state = 490
                    self.match(BloonParser.T__6)
                    compi.add_op('<')
                    pass
                elif token in [BloonParser.T__43]:
                    self.state = 492
                    self.match(BloonParser.T__43)
                    compi.add_op('>=')
                    pass
                elif token in [BloonParser.T__44]:
                    self.state = 494
                    self.match(BloonParser.T__44)
                    compi.add_op('<=')
                    pass
                elif token in [BloonParser.T__45]:
                    self.state = 496
                    self.match(BloonParser.T__45)
                    compi.add_op('==')
                    pass
                elif token in [BloonParser.T__46]:
                    self.state = 498
                    self.match(BloonParser.T__46)
                    compi.add_op('!=')
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 502
                self.exp()
                compi.arithmetic_operation('>', '<', '>=', '<=', '==', '!=')
                self.state = 509
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
        self.enterRule(localctx, 92, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 510
            self.term()
            self.state = 522
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BloonParser.T__47 or _la==BloonParser.T__48:
                self.state = 515
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BloonParser.T__47]:
                    self.state = 511
                    self.match(BloonParser.T__47)
                    compi.add_op('+')
                    pass
                elif token in [BloonParser.T__48]:
                    self.state = 513
                    self.match(BloonParser.T__48)
                    compi.add_op('-')
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 517
                self.term()
                compi.arithmetic_operation('+', '-')
                self.state = 524
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
        self.enterRule(localctx, 94, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 525
            self.factor()
            self.state = 539
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BloonParser.T__49) | (1 << BloonParser.T__50) | (1 << BloonParser.T__51))) != 0):
                self.state = 532
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BloonParser.T__49]:
                    self.state = 526
                    self.match(BloonParser.T__49)
                    compi.add_op('*')
                    pass
                elif token in [BloonParser.T__50]:
                    self.state = 528
                    self.match(BloonParser.T__50)
                    compi.add_op('/')
                    pass
                elif token in [BloonParser.T__51]:
                    self.state = 530
                    self.match(BloonParser.T__51)
                    compi.add_op('%')
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 534
                self.factor()
                compi.arithmetic_operation('*', '/', '%')
                self.state = 541
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
        self.enterRule(localctx, 96, self.RULE_factor)
        try:
            self.state = 551
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 542
                self.match(BloonParser.T__3)
                compi.open_parens()
                self.state = 544
                self.expression()
                self.state = 545
                self.match(BloonParser.T__4)
                compi.close_parens()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 548
                self.var_const()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 549
                self.call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 550
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
        self.enterRule(localctx, 98, self.RULE_factor_t)
        try:
            self.state = 557
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.ID, BloonParser.CONST_INT, BloonParser.CONST_FLOAT, BloonParser.CONST_STR, BloonParser.CONST_CHAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 553
                self.var_const()
                pass
            elif token in [BloonParser.T__48]:
                self.enterOuterAlt(localctx, 2)
                self.state = 554
                self.match(BloonParser.T__48)
                compi.set_negative()
                self.state = 556
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
        self.enterRule(localctx, 100, self.RULE_var_const)
        try:
            self.state = 568
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BloonParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 559
                self.var()
                pass
            elif token in [BloonParser.CONST_INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 560
                localctx._CONST_INT = self.match(BloonParser.CONST_INT)
                compi.get_const((None if localctx._CONST_INT is None else localctx._CONST_INT.text), "int")
                pass
            elif token in [BloonParser.CONST_FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 562
                localctx._CONST_FLOAT = self.match(BloonParser.CONST_FLOAT)
                compi.get_const((None if localctx._CONST_FLOAT is None else localctx._CONST_FLOAT.text), "float")
                pass
            elif token in [BloonParser.CONST_STR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 564
                localctx._CONST_STR = self.match(BloonParser.CONST_STR)
                compi.get_const((None if localctx._CONST_STR is None else localctx._CONST_STR.text), "string")
                pass
            elif token in [BloonParser.CONST_CHAR]:
                self.enterOuterAlt(localctx, 5)
                self.state = 566
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





