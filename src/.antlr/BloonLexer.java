// Generated from e:\GitProjects\Bloon\src\Bloon.g4 by ANTLR 4.8

    from BloonCompiler import Compiler
    compi = Compiler()

import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class BloonLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, T__34=35, T__35=36, T__36=37, T__37=38, 
		T__38=39, T__39=40, T__40=41, T__41=42, T__42=43, T__43=44, T__44=45, 
		T__45=46, T__46=47, ID=48, CONST_INT=49, CONST_FLOAT=50, CONST_STR=51, 
		WHITESPACE=52;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"T__9", "T__10", "T__11", "T__12", "T__13", "T__14", "T__15", "T__16", 
			"T__17", "T__18", "T__19", "T__20", "T__21", "T__22", "T__23", "T__24", 
			"T__25", "T__26", "T__27", "T__28", "T__29", "T__30", "T__31", "T__32", 
			"T__33", "T__34", "T__35", "T__36", "T__37", "T__38", "T__39", "T__40", 
			"T__41", "T__42", "T__43", "T__44", "T__45", "T__46", "ID", "CONST_INT", 
			"CONST_FLOAT", "CONST_STR", "WHITESPACE"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'program'", "';'", "'main'", "'('", "')'", "'class'", "'<'", "'inherits'", 
			"'>'", "'{'", "'attributes'", "'methods'", "'}'", "'.'", "'vars'", "','", 
			"':'", "'['", "']'", "'='", "'int'", "'float'", "'char'", "'string'", 
			"'+'", "'-'", "'*'", "'/'", "'void'", "'meth'", "'return'", "'read'", 
			"'write'", "'cond'", "'then'", "'else'", "'while'", "'do'", "'floop'", 
			"'to'", "'and'", "'or'", "'!'", "'<='", "'>='", "'=='", "'!='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			"ID", "CONST_INT", "CONST_FLOAT", "CONST_STR", "WHITESPACE"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public BloonLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Bloon.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\66\u015b\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t"+
		" \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t"+
		"+\4,\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64"+
		"\t\64\4\65\t\65\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3"+
		"\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t"+
		"\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f"+
		"\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\20"+
		"\3\20\3\20\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25"+
		"\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30"+
		"\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34"+
		"\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3 \3 \3 "+
		"\3 \3 \3 \3 \3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$"+
		"\3$\3$\3$\3$\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3("+
		"\3(\3(\3)\3)\3)\3*\3*\3*\3*\3+\3+\3+\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/\3/"+
		"\3\60\3\60\3\60\3\61\3\61\7\61\u012c\n\61\f\61\16\61\u012f\13\61\3\62"+
		"\3\62\7\62\u0133\n\62\f\62\16\62\u0136\13\62\3\62\5\62\u0139\n\62\3\63"+
		"\3\63\7\63\u013d\n\63\f\63\16\63\u0140\13\63\3\63\5\63\u0143\n\63\3\63"+
		"\3\63\3\63\6\63\u0148\n\63\r\63\16\63\u0149\3\64\3\64\7\64\u014e\n\64"+
		"\f\64\16\64\u0151\13\64\3\64\3\64\3\65\6\65\u0156\n\65\r\65\16\65\u0157"+
		"\3\65\3\65\3\u014f\2\66\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f"+
		"\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63"+
		"\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62"+
		"c\63e\64g\65i\66\3\2\n\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3\2\62;\3\2\62"+
		"\62\3\2\60\60\3\2$$\5\2\13\f\17\17\"\"\2\u0162\2\3\3\2\2\2\2\5\3\2\2\2"+
		"\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3"+
		"\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2"+
		"\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2"+
		"\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2"+
		"\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2"+
		"\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2"+
		"\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y"+
		"\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2"+
		"\2\2\2g\3\2\2\2\2i\3\2\2\2\3k\3\2\2\2\5s\3\2\2\2\7u\3\2\2\2\tz\3\2\2\2"+
		"\13|\3\2\2\2\r~\3\2\2\2\17\u0084\3\2\2\2\21\u0086\3\2\2\2\23\u008f\3\2"+
		"\2\2\25\u0091\3\2\2\2\27\u0093\3\2\2\2\31\u009e\3\2\2\2\33\u00a6\3\2\2"+
		"\2\35\u00a8\3\2\2\2\37\u00aa\3\2\2\2!\u00af\3\2\2\2#\u00b1\3\2\2\2%\u00b3"+
		"\3\2\2\2\'\u00b5\3\2\2\2)\u00b7\3\2\2\2+\u00b9\3\2\2\2-\u00bd\3\2\2\2"+
		"/\u00c3\3\2\2\2\61\u00c8\3\2\2\2\63\u00cf\3\2\2\2\65\u00d1\3\2\2\2\67"+
		"\u00d3\3\2\2\29\u00d5\3\2\2\2;\u00d7\3\2\2\2=\u00dc\3\2\2\2?\u00e1\3\2"+
		"\2\2A\u00e8\3\2\2\2C\u00ed\3\2\2\2E\u00f3\3\2\2\2G\u00f8\3\2\2\2I\u00fd"+
		"\3\2\2\2K\u0102\3\2\2\2M\u0108\3\2\2\2O\u010b\3\2\2\2Q\u0111\3\2\2\2S"+
		"\u0114\3\2\2\2U\u0118\3\2\2\2W\u011b\3\2\2\2Y\u011d\3\2\2\2[\u0120\3\2"+
		"\2\2]\u0123\3\2\2\2_\u0126\3\2\2\2a\u0129\3\2\2\2c\u0138\3\2\2\2e\u0142"+
		"\3\2\2\2g\u014b\3\2\2\2i\u0155\3\2\2\2kl\7r\2\2lm\7t\2\2mn\7q\2\2no\7"+
		"i\2\2op\7t\2\2pq\7c\2\2qr\7o\2\2r\4\3\2\2\2st\7=\2\2t\6\3\2\2\2uv\7o\2"+
		"\2vw\7c\2\2wx\7k\2\2xy\7p\2\2y\b\3\2\2\2z{\7*\2\2{\n\3\2\2\2|}\7+\2\2"+
		"}\f\3\2\2\2~\177\7e\2\2\177\u0080\7n\2\2\u0080\u0081\7c\2\2\u0081\u0082"+
		"\7u\2\2\u0082\u0083\7u\2\2\u0083\16\3\2\2\2\u0084\u0085\7>\2\2\u0085\20"+
		"\3\2\2\2\u0086\u0087\7k\2\2\u0087\u0088\7p\2\2\u0088\u0089\7j\2\2\u0089"+
		"\u008a\7g\2\2\u008a\u008b\7t\2\2\u008b\u008c\7k\2\2\u008c\u008d\7v\2\2"+
		"\u008d\u008e\7u\2\2\u008e\22\3\2\2\2\u008f\u0090\7@\2\2\u0090\24\3\2\2"+
		"\2\u0091\u0092\7}\2\2\u0092\26\3\2\2\2\u0093\u0094\7c\2\2\u0094\u0095"+
		"\7v\2\2\u0095\u0096\7v\2\2\u0096\u0097\7t\2\2\u0097\u0098\7k\2\2\u0098"+
		"\u0099\7d\2\2\u0099\u009a\7w\2\2\u009a\u009b\7v\2\2\u009b\u009c\7g\2\2"+
		"\u009c\u009d\7u\2\2\u009d\30\3\2\2\2\u009e\u009f\7o\2\2\u009f\u00a0\7"+
		"g\2\2\u00a0\u00a1\7v\2\2\u00a1\u00a2\7j\2\2\u00a2\u00a3\7q\2\2\u00a3\u00a4"+
		"\7f\2\2\u00a4\u00a5\7u\2\2\u00a5\32\3\2\2\2\u00a6\u00a7\7\177\2\2\u00a7"+
		"\34\3\2\2\2\u00a8\u00a9\7\60\2\2\u00a9\36\3\2\2\2\u00aa\u00ab\7x\2\2\u00ab"+
		"\u00ac\7c\2\2\u00ac\u00ad\7t\2\2\u00ad\u00ae\7u\2\2\u00ae \3\2\2\2\u00af"+
		"\u00b0\7.\2\2\u00b0\"\3\2\2\2\u00b1\u00b2\7<\2\2\u00b2$\3\2\2\2\u00b3"+
		"\u00b4\7]\2\2\u00b4&\3\2\2\2\u00b5\u00b6\7_\2\2\u00b6(\3\2\2\2\u00b7\u00b8"+
		"\7?\2\2\u00b8*\3\2\2\2\u00b9\u00ba\7k\2\2\u00ba\u00bb\7p\2\2\u00bb\u00bc"+
		"\7v\2\2\u00bc,\3\2\2\2\u00bd\u00be\7h\2\2\u00be\u00bf\7n\2\2\u00bf\u00c0"+
		"\7q\2\2\u00c0\u00c1\7c\2\2\u00c1\u00c2\7v\2\2\u00c2.\3\2\2\2\u00c3\u00c4"+
		"\7e\2\2\u00c4\u00c5\7j\2\2\u00c5\u00c6\7c\2\2\u00c6\u00c7\7t\2\2\u00c7"+
		"\60\3\2\2\2\u00c8\u00c9\7u\2\2\u00c9\u00ca\7v\2\2\u00ca\u00cb\7t\2\2\u00cb"+
		"\u00cc\7k\2\2\u00cc\u00cd\7p\2\2\u00cd\u00ce\7i\2\2\u00ce\62\3\2\2\2\u00cf"+
		"\u00d0\7-\2\2\u00d0\64\3\2\2\2\u00d1\u00d2\7/\2\2\u00d2\66\3\2\2\2\u00d3"+
		"\u00d4\7,\2\2\u00d48\3\2\2\2\u00d5\u00d6\7\61\2\2\u00d6:\3\2\2\2\u00d7"+
		"\u00d8\7x\2\2\u00d8\u00d9\7q\2\2\u00d9\u00da\7k\2\2\u00da\u00db\7f\2\2"+
		"\u00db<\3\2\2\2\u00dc\u00dd\7o\2\2\u00dd\u00de\7g\2\2\u00de\u00df\7v\2"+
		"\2\u00df\u00e0\7j\2\2\u00e0>\3\2\2\2\u00e1\u00e2\7t\2\2\u00e2\u00e3\7"+
		"g\2\2\u00e3\u00e4\7v\2\2\u00e4\u00e5\7w\2\2\u00e5\u00e6\7t\2\2\u00e6\u00e7"+
		"\7p\2\2\u00e7@\3\2\2\2\u00e8\u00e9\7t\2\2\u00e9\u00ea\7g\2\2\u00ea\u00eb"+
		"\7c\2\2\u00eb\u00ec\7f\2\2\u00ecB\3\2\2\2\u00ed\u00ee\7y\2\2\u00ee\u00ef"+
		"\7t\2\2\u00ef\u00f0\7k\2\2\u00f0\u00f1\7v\2\2\u00f1\u00f2\7g\2\2\u00f2"+
		"D\3\2\2\2\u00f3\u00f4\7e\2\2\u00f4\u00f5\7q\2\2\u00f5\u00f6\7p\2\2\u00f6"+
		"\u00f7\7f\2\2\u00f7F\3\2\2\2\u00f8\u00f9\7v\2\2\u00f9\u00fa\7j\2\2\u00fa"+
		"\u00fb\7g\2\2\u00fb\u00fc\7p\2\2\u00fcH\3\2\2\2\u00fd\u00fe\7g\2\2\u00fe"+
		"\u00ff\7n\2\2\u00ff\u0100\7u\2\2\u0100\u0101\7g\2\2\u0101J\3\2\2\2\u0102"+
		"\u0103\7y\2\2\u0103\u0104\7j\2\2\u0104\u0105\7k\2\2\u0105\u0106\7n\2\2"+
		"\u0106\u0107\7g\2\2\u0107L\3\2\2\2\u0108\u0109\7f\2\2\u0109\u010a\7q\2"+
		"\2\u010aN\3\2\2\2\u010b\u010c\7h\2\2\u010c\u010d\7n\2\2\u010d\u010e\7"+
		"q\2\2\u010e\u010f\7q\2\2\u010f\u0110\7r\2\2\u0110P\3\2\2\2\u0111\u0112"+
		"\7v\2\2\u0112\u0113\7q\2\2\u0113R\3\2\2\2\u0114\u0115\7c\2\2\u0115\u0116"+
		"\7p\2\2\u0116\u0117\7f\2\2\u0117T\3\2\2\2\u0118\u0119\7q\2\2\u0119\u011a"+
		"\7t\2\2\u011aV\3\2\2\2\u011b\u011c\7#\2\2\u011cX\3\2\2\2\u011d\u011e\7"+
		">\2\2\u011e\u011f\7?\2\2\u011fZ\3\2\2\2\u0120\u0121\7@\2\2\u0121\u0122"+
		"\7?\2\2\u0122\\\3\2\2\2\u0123\u0124\7?\2\2\u0124\u0125\7?\2\2\u0125^\3"+
		"\2\2\2\u0126\u0127\7#\2\2\u0127\u0128\7?\2\2\u0128`\3\2\2\2\u0129\u012d"+
		"\t\2\2\2\u012a\u012c\t\3\2\2\u012b\u012a\3\2\2\2\u012c\u012f\3\2\2\2\u012d"+
		"\u012b\3\2\2\2\u012d\u012e\3\2\2\2\u012eb\3\2\2\2\u012f\u012d\3\2\2\2"+
		"\u0130\u0134\t\4\2\2\u0131\u0133\t\5\2\2\u0132\u0131\3\2\2\2\u0133\u0136"+
		"\3\2\2\2\u0134\u0132\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0139\3\2\2\2\u0136"+
		"\u0134\3\2\2\2\u0137\u0139\t\6\2\2\u0138\u0130\3\2\2\2\u0138\u0137\3\2"+
		"\2\2\u0139d\3\2\2\2\u013a\u013e\t\4\2\2\u013b\u013d\t\5\2\2\u013c\u013b"+
		"\3\2\2\2\u013d\u0140\3\2\2\2\u013e\u013c\3\2\2\2\u013e\u013f\3\2\2\2\u013f"+
		"\u0143\3\2\2\2\u0140\u013e\3\2\2\2\u0141\u0143\t\6\2\2\u0142\u013a\3\2"+
		"\2\2\u0142\u0141\3\2\2\2\u0143\u0144\3\2\2\2\u0144\u0145\t\7\2\2\u0145"+
		"\u0147\3\2\2\2\u0146\u0148\t\5\2\2\u0147\u0146\3\2\2\2\u0148\u0149\3\2"+
		"\2\2\u0149\u0147\3\2\2\2\u0149\u014a\3\2\2\2\u014af\3\2\2\2\u014b\u014f"+
		"\t\b\2\2\u014c\u014e\13\2\2\2\u014d\u014c\3\2\2\2\u014e\u0151\3\2\2\2"+
		"\u014f\u0150\3\2\2\2\u014f\u014d\3\2\2\2\u0150\u0152\3\2\2\2\u0151\u014f"+
		"\3\2\2\2\u0152\u0153\t\b\2\2\u0153h\3\2\2\2\u0154\u0156\t\t\2\2\u0155"+
		"\u0154\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0155\3\2\2\2\u0157\u0158\3\2"+
		"\2\2\u0158\u0159\3\2\2\2\u0159\u015a\b\65\2\2\u015aj\3\2\2\2\f\2\u012b"+
		"\u012d\u0134\u0138\u013e\u0142\u0149\u014f\u0157\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}