// Generated from e:\GitProjects\Bloon\src\Bloon.g4 by ANTLR 4.8

    from BloonCompiler import Compiler
    compi = Compiler()

import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class BloonParser extends Parser {
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
	public static final int
		RULE_program = 0, RULE_program_t = 1, RULE_main = 2, RULE_r_class = 3, 
		RULE_class_t = 4, RULE_class_k = 5, RULE_class_j = 6, RULE_class_l = 7, 
		RULE_class_p = 8, RULE_var = 9, RULE_var_t = 10, RULE_var_k = 11, RULE_var_dec = 12, 
		RULE_var_dec_t = 13, RULE_var_dec_l = 14, RULE_arr_idx = 15, RULE_arr_idx_t = 16, 
		RULE_arr = 17, RULE_arr_t = 18, RULE_assign = 19, RULE_assign_t = 20, 
		RULE_var_type = 21, RULE_custom_type = 22, RULE_assign_op = 23, RULE_type_meth = 24, 
		RULE_statement = 25, RULE_func = 26, RULE_func_t = 27, RULE_func_k = 28, 
		RULE_func_p = 29, RULE_param = 30, RULE_param_t = 31, RULE_block = 32, 
		RULE_block_t = 33, RULE_r_return = 34, RULE_call = 35, RULE_call_t = 36, 
		RULE_call_args = 37, RULE_call_args_t = 38, RULE_call_void = 39, RULE_read = 40, 
		RULE_read_t = 41, RULE_read_k = 42, RULE_write = 43, RULE_write_t = 44, 
		RULE_write_k = 45, RULE_cond = 46, RULE_cond_t = 47, RULE_r_while = 48, 
		RULE_floop = 49, RULE_super_exp = 50, RULE_super_exp_t = 51, RULE_expression = 52, 
		RULE_expression_t = 53, RULE_exp = 54, RULE_exp_t = 55, RULE_term = 56, 
		RULE_term_t = 57, RULE_factor = 58, RULE_factor_t = 59, RULE_var_const = 60;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "program_t", "main", "r_class", "class_t", "class_k", "class_j", 
			"class_l", "class_p", "var", "var_t", "var_k", "var_dec", "var_dec_t", 
			"var_dec_l", "arr_idx", "arr_idx_t", "arr", "arr_t", "assign", "assign_t", 
			"var_type", "custom_type", "assign_op", "type_meth", "statement", "func", 
			"func_t", "func_k", "func_p", "param", "param_t", "block", "block_t", 
			"r_return", "call", "call_t", "call_args", "call_args_t", "call_void", 
			"read", "read_t", "read_k", "write", "write_t", "write_k", "cond", "cond_t", 
			"r_while", "floop", "super_exp", "super_exp_t", "expression", "expression_t", 
			"exp", "exp_t", "term", "term_t", "factor", "factor_t", "var_const"
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

	@Override
	public String getGrammarFileName() { return "Bloon.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public BloonParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BloonParser.ID, 0); }
		public Program_tContext program_t() {
			return getRuleContext(Program_tContext.class,0);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(122);
			match(T__0);
			setState(123);
			match(ID);
			setState(124);
			match(T__1);
			setState(125);
			program_t();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Program_tContext extends ParserRuleContext {
		public R_classContext r_class() {
			return getRuleContext(R_classContext.class,0);
		}
		public Program_tContext program_t() {
			return getRuleContext(Program_tContext.class,0);
		}
		public Var_decContext var_dec() {
			return getRuleContext(Var_decContext.class,0);
		}
		public FuncContext func() {
			return getRuleContext(FuncContext.class,0);
		}
		public MainContext main() {
			return getRuleContext(MainContext.class,0);
		}
		public Program_tContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program_t; }
	}

	public final Program_tContext program_t() throws RecognitionException {
		Program_tContext _localctx = new Program_tContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_program_t);
		try {
			setState(137);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__5:
				enterOuterAlt(_localctx, 1);
				{
				setState(127);
				r_class();
				setState(128);
				program_t();
				}
				break;
			case T__14:
				enterOuterAlt(_localctx, 2);
				{
				setState(130);
				var_dec();
				setState(131);
				program_t();
				}
				break;
			case T__20:
			case T__21:
			case T__22:
			case T__23:
			case T__28:
				enterOuterAlt(_localctx, 3);
				{
				setState(133);
				func();
				setState(134);
				program_t();
				}
				break;
			case T__2:
				enterOuterAlt(_localctx, 4);
				{
				setState(136);
				main();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MainContext extends ParserRuleContext {
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public MainContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_main; }
	}

	public final MainContext main() throws RecognitionException {
		MainContext _localctx = new MainContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_main);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(139);
			match(T__2);
			setState(140);
			match(T__3);
			setState(141);
			match(T__4);
			setState(142);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class R_classContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BloonParser.ID, 0); }
		public Class_tContext class_t() {
			return getRuleContext(Class_tContext.class,0);
		}
		public R_classContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_r_class; }
	}

	public final R_classContext r_class() throws RecognitionException {
		R_classContext _localctx = new R_classContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_r_class);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(144);
			match(T__5);
			setState(145);
			match(ID);
			setState(146);
			class_t();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Class_tContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BloonParser.ID, 0); }
		public Class_kContext class_k() {
			return getRuleContext(Class_kContext.class,0);
		}
		public Class_tContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class_t; }
	}

	public final Class_tContext class_t() throws RecognitionException {
		Class_tContext _localctx = new Class_tContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_class_t);
		try {
			setState(154);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__6:
				enterOuterAlt(_localctx, 1);
				{
				setState(148);
				match(T__6);
				setState(149);
				match(T__7);
				setState(150);
				match(ID);
				setState(151);
				match(T__8);
				setState(152);
				class_k();
				}
				break;
			case T__1:
				enterOuterAlt(_localctx, 2);
				{
				setState(153);
				class_k();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Class_kContext extends ParserRuleContext {
		public Class_jContext class_j() {
			return getRuleContext(Class_jContext.class,0);
		}
		public Class_kContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class_k; }
	}

	public final Class_kContext class_k() throws RecognitionException {
		Class_kContext _localctx = new Class_kContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_class_k);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(156);
			match(T__1);
			setState(157);
			match(T__9);
			setState(158);
			class_j();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Class_jContext extends ParserRuleContext {
		public Var_decContext var_dec() {
			return getRuleContext(Var_decContext.class,0);
		}
		public Class_lContext class_l() {
			return getRuleContext(Class_lContext.class,0);
		}
		public Class_jContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class_j; }
	}

	public final Class_jContext class_j() throws RecognitionException {
		Class_jContext _localctx = new Class_jContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_class_j);
		try {
			setState(167);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__10:
				enterOuterAlt(_localctx, 1);
				{
				setState(160);
				match(T__10);
				setState(161);
				match(T__6);
				setState(162);
				var_dec();
				setState(163);
				match(T__8);
				setState(164);
				class_l();
				}
				break;
			case T__11:
			case T__12:
				enterOuterAlt(_localctx, 2);
				{
				setState(166);
				class_l();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Class_lContext extends ParserRuleContext {
		public Class_pContext class_p() {
			return getRuleContext(Class_pContext.class,0);
		}
		public Class_lContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class_l; }
	}

	public final Class_lContext class_l() throws RecognitionException {
		Class_lContext _localctx = new Class_lContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_class_l);
		try {
			setState(174);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__11:
				enterOuterAlt(_localctx, 1);
				{
				setState(169);
				match(T__11);
				setState(170);
				match(T__6);
				setState(171);
				class_p();
				}
				break;
			case T__12:
				enterOuterAlt(_localctx, 2);
				{
				setState(172);
				match(T__12);
				setState(173);
				match(T__1);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Class_pContext extends ParserRuleContext {
		public FuncContext func() {
			return getRuleContext(FuncContext.class,0);
		}
		public Class_pContext class_p() {
			return getRuleContext(Class_pContext.class,0);
		}
		public Class_pContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class_p; }
	}

	public final Class_pContext class_p() throws RecognitionException {
		Class_pContext _localctx = new Class_pContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_class_p);
		try {
			setState(184);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(176);
				func();
				setState(177);
				match(T__8);
				setState(178);
				match(T__12);
				setState(179);
				match(T__1);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(181);
				func();
				setState(182);
				class_p();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VarContext extends ParserRuleContext {
		public Token ID;
		public TerminalNode ID() { return getToken(BloonParser.ID, 0); }
		public Var_tContext var_t() {
			return getRuleContext(Var_tContext.class,0);
		}
		public VarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var; }
	}

	public final VarContext var() throws RecognitionException {
		VarContext _localctx = new VarContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_var);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(186);
			((VarContext)_localctx).ID = match(ID);
			setState(187);
			var_t();
			compi.get_var((((VarContext)_localctx).ID!=null?((VarContext)_localctx).ID.getText():null))
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Var_tContext extends ParserRuleContext {
		public Arr_idxContext arr_idx() {
			return getRuleContext(Arr_idxContext.class,0);
		}
		public Var_kContext var_k() {
			return getRuleContext(Var_kContext.class,0);
		}
		public Var_tContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_t; }
	}

	public final Var_tContext var_t() throws RecognitionException {
		Var_tContext _localctx = new Var_tContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_var_t);
		try {
			setState(194);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__17:
				enterOuterAlt(_localctx, 1);
				{
				setState(190);
				arr_idx();
				setState(191);
				var_k();
				}
				break;
			case T__1:
			case T__3:
			case T__4:
			case T__6:
			case T__8:
			case T__13:
			case T__15:
			case T__18:
			case T__19:
			case T__24:
			case T__25:
			case T__26:
			case T__27:
			case T__37:
			case T__39:
			case T__40:
			case T__41:
			case T__43:
			case T__44:
			case T__45:
			case T__46:
				enterOuterAlt(_localctx, 2);
				{
				setState(193);
				var_k();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Var_kContext extends ParserRuleContext {
		public VarContext var() {
			return getRuleContext(VarContext.class,0);
		}
		public Var_kContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_k; }
	}

	public final Var_kContext var_k() throws RecognitionException {
		Var_kContext _localctx = new Var_kContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_var_k);
		try {
			setState(199);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__13:
				enterOuterAlt(_localctx, 1);
				{
				setState(196);
				match(T__13);
				setState(197);
				var();
				}
				break;
			case T__1:
			case T__3:
			case T__4:
			case T__6:
			case T__8:
			case T__15:
			case T__18:
			case T__19:
			case T__24:
			case T__25:
			case T__26:
			case T__27:
			case T__37:
			case T__39:
			case T__40:
			case T__41:
			case T__43:
			case T__44:
			case T__45:
			case T__46:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Var_decContext extends ParserRuleContext {
		public Var_dec_tContext var_dec_t() {
			return getRuleContext(Var_dec_tContext.class,0);
		}
		public Var_decContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_dec; }
	}

	public final Var_decContext var_dec() throws RecognitionException {
		Var_decContext _localctx = new Var_decContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_var_dec);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(201);
			match(T__14);
			setState(202);
			var_dec_t();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Var_dec_tContext extends ParserRuleContext {
		public Token ID;
		public Var_typeContext var_type;
		public Custom_typeContext custom_type;
		public TerminalNode ID() { return getToken(BloonParser.ID, 0); }
		public Var_dec_tContext var_dec_t() {
			return getRuleContext(Var_dec_tContext.class,0);
		}
		public ArrContext arr() {
			return getRuleContext(ArrContext.class,0);
		}
		public Var_typeContext var_type() {
			return getRuleContext(Var_typeContext.class,0);
		}
		public Var_dec_lContext var_dec_l() {
			return getRuleContext(Var_dec_lContext.class,0);
		}
		public Custom_typeContext custom_type() {
			return getRuleContext(Custom_typeContext.class,0);
		}
		public Var_dec_tContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_dec_t; }
	}

	public final Var_dec_tContext var_dec_t() throws RecognitionException {
		Var_dec_tContext _localctx = new Var_dec_tContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_var_dec_t);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(204);
			((Var_dec_tContext)_localctx).ID = match(ID);
			setState(206);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__17) {
				{
				setState(205);
				arr();
				}
			}

			compi.add_operand((((Var_dec_tContext)_localctx).ID!=null?((Var_dec_tContext)_localctx).ID.getText():null)); compi.increase_varCount()
			setState(224);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__15:
				{
				setState(209);
				match(T__15);
				setState(210);
				var_dec_t();
				}
				break;
			case T__16:
				{
				setState(211);
				match(T__16);
				setState(222);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__20:
				case T__21:
				case T__22:
				case T__23:
					{
					setState(212);
					((Var_dec_tContext)_localctx).var_type = var_type();
					compi.define_var((((Var_dec_tContext)_localctx).var_type!=null?_input.getText(((Var_dec_tContext)_localctx).var_type.start,((Var_dec_tContext)_localctx).var_type.stop):null))
					setState(214);
					match(T__1);
					setState(215);
					var_dec_l();
					}
					break;
				case ID:
					{
					setState(217);
					((Var_dec_tContext)_localctx).custom_type = custom_type();
					compi.define_var((((Var_dec_tContext)_localctx).custom_type!=null?_input.getText(((Var_dec_tContext)_localctx).custom_type.start,((Var_dec_tContext)_localctx).custom_type.stop):null))
					setState(219);
					match(T__1);
					setState(220);
					var_dec_l();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Var_dec_lContext extends ParserRuleContext {
		public Var_dec_tContext var_dec_t() {
			return getRuleContext(Var_dec_tContext.class,0);
		}
		public Var_dec_lContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_dec_l; }
	}

	public final Var_dec_lContext var_dec_l() throws RecognitionException {
		Var_dec_lContext _localctx = new Var_dec_lContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_var_dec_l);
		try {
			setState(228);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(226);
				var_dec_t();
				}
				break;
			case T__2:
			case T__5:
			case T__8:
			case T__9:
			case T__14:
			case T__20:
			case T__21:
			case T__22:
			case T__23:
			case T__28:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Arr_idxContext extends ParserRuleContext {
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public Arr_idx_tContext arr_idx_t() {
			return getRuleContext(Arr_idx_tContext.class,0);
		}
		public Arr_idxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arr_idx; }
	}

	public final Arr_idxContext arr_idx() throws RecognitionException {
		Arr_idxContext _localctx = new Arr_idxContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_arr_idx);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(230);
			match(T__17);
			setState(231);
			exp();
			setState(232);
			arr_idx_t();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Arr_idx_tContext extends ParserRuleContext {
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public Arr_idx_tContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arr_idx_t; }
	}

	public final Arr_idx_tContext arr_idx_t() throws RecognitionException {
		Arr_idx_tContext _localctx = new Arr_idx_tContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_arr_idx_t);
		try {
			setState(239);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__15:
				enterOuterAlt(_localctx, 1);
				{
				setState(234);
				match(T__15);
				setState(235);
				exp();
				setState(236);
				match(T__18);
				}
				break;
			case T__18:
				enterOuterAlt(_localctx, 2);
				{
				setState(238);
				match(T__18);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArrContext extends ParserRuleContext {
		public TerminalNode CONST_INT() { return getToken(BloonParser.CONST_INT, 0); }
		public Arr_tContext arr_t() {
			return getRuleContext(Arr_tContext.class,0);
		}
		public ArrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arr; }
	}

	public final ArrContext arr() throws RecognitionException {
		ArrContext _localctx = new ArrContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_arr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(241);
			match(T__17);
			setState(242);
			match(CONST_INT);
			setState(243);
			arr_t();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Arr_tContext extends ParserRuleContext {
		public TerminalNode CONST_INT() { return getToken(BloonParser.CONST_INT, 0); }
		public Arr_tContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arr_t; }
	}

	public final Arr_tContext arr_t() throws RecognitionException {
		Arr_tContext _localctx = new Arr_tContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_arr_t);
		try {
			setState(249);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__15:
				enterOuterAlt(_localctx, 1);
				{
				setState(245);
				match(T__15);
				setState(246);
				match(CONST_INT);
				setState(247);
				match(T__18);
				}
				break;
			case T__18:
				enterOuterAlt(_localctx, 2);
				{
				setState(248);
				match(T__18);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssignContext extends ParserRuleContext {
		public VarContext var() {
			return getRuleContext(VarContext.class,0);
		}
		public Assign_tContext assign_t() {
			return getRuleContext(Assign_tContext.class,0);
		}
		public AssignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign; }
	}

	public final AssignContext assign() throws RecognitionException {
		AssignContext _localctx = new AssignContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_assign);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(251);
			var();
			setState(252);
			assign_t();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Assign_tContext extends ParserRuleContext {
		public Assign_opContext assign_op;
		public Super_expContext super_exp() {
			return getRuleContext(Super_expContext.class,0);
		}
		public Assign_opContext assign_op() {
			return getRuleContext(Assign_opContext.class,0);
		}
		public Assign_tContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign_t; }
	}

	public final Assign_tContext assign_t() throws RecognitionException {
		Assign_tContext _localctx = new Assign_tContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_assign_t);
		try {
			setState(266);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__19:
				enterOuterAlt(_localctx, 1);
				{
				setState(254);
				match(T__19);
				compi.add_op('=')
				setState(256);
				super_exp();
				compi.assign_var()
				setState(258);
				match(T__1);
				}
				break;
			case T__24:
			case T__25:
			case T__26:
			case T__27:
				enterOuterAlt(_localctx, 2);
				{
				setState(260);
				((Assign_tContext)_localctx).assign_op = assign_op();
				compi.add_op((((Assign_tContext)_localctx).assign_op!=null?_input.getText(((Assign_tContext)_localctx).assign_op.start,((Assign_tContext)_localctx).assign_op.stop):null))
				setState(262);
				super_exp();
				compi.assign_var()
				setState(264);
				match(T__1);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Var_typeContext extends ParserRuleContext {
		public Var_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_type; }
	}

	public final Var_typeContext var_type() throws RecognitionException {
		Var_typeContext _localctx = new Var_typeContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_var_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(268);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__20) | (1L << T__21) | (1L << T__22) | (1L << T__23))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Custom_typeContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BloonParser.ID, 0); }
		public Custom_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_custom_type; }
	}

	public final Custom_typeContext custom_type() throws RecognitionException {
		Custom_typeContext _localctx = new Custom_typeContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_custom_type);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(270);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Assign_opContext extends ParserRuleContext {
		public Assign_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign_op; }
	}

	public final Assign_opContext assign_op() throws RecognitionException {
		Assign_opContext _localctx = new Assign_opContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_assign_op);
		try {
			setState(280);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__24:
				enterOuterAlt(_localctx, 1);
				{
				setState(272);
				match(T__24);
				setState(273);
				match(T__19);
				}
				break;
			case T__25:
				enterOuterAlt(_localctx, 2);
				{
				setState(274);
				match(T__25);
				setState(275);
				match(T__19);
				}
				break;
			case T__26:
				enterOuterAlt(_localctx, 3);
				{
				setState(276);
				match(T__26);
				setState(277);
				match(T__19);
				}
				break;
			case T__27:
				enterOuterAlt(_localctx, 4);
				{
				setState(278);
				match(T__27);
				setState(279);
				match(T__19);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Type_methContext extends ParserRuleContext {
		public Var_typeContext var_type() {
			return getRuleContext(Var_typeContext.class,0);
		}
		public Type_methContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type_meth; }
	}

	public final Type_methContext type_meth() throws RecognitionException {
		Type_methContext _localctx = new Type_methContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_type_meth);
		try {
			setState(284);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__20:
			case T__21:
			case T__22:
			case T__23:
				enterOuterAlt(_localctx, 1);
				{
				setState(282);
				var_type();
				}
				break;
			case T__28:
				enterOuterAlt(_localctx, 2);
				{
				setState(283);
				match(T__28);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public AssignContext assign() {
			return getRuleContext(AssignContext.class,0);
		}
		public CondContext cond() {
			return getRuleContext(CondContext.class,0);
		}
		public R_returnContext r_return() {
			return getRuleContext(R_returnContext.class,0);
		}
		public ReadContext read() {
			return getRuleContext(ReadContext.class,0);
		}
		public WriteContext write() {
			return getRuleContext(WriteContext.class,0);
		}
		public R_whileContext r_while() {
			return getRuleContext(R_whileContext.class,0);
		}
		public FloopContext floop() {
			return getRuleContext(FloopContext.class,0);
		}
		public Call_voidContext call_void() {
			return getRuleContext(Call_voidContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_statement);
		try {
			setState(294);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(286);
				assign();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(287);
				cond();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(288);
				r_return();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(289);
				read();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(290);
				write();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(291);
				r_while();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(292);
				floop();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(293);
				call_void();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FuncContext extends ParserRuleContext {
		public Type_methContext type_meth() {
			return getRuleContext(Type_methContext.class,0);
		}
		public TerminalNode ID() { return getToken(BloonParser.ID, 0); }
		public Func_tContext func_t() {
			return getRuleContext(Func_tContext.class,0);
		}
		public FuncContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func; }
	}

	public final FuncContext func() throws RecognitionException {
		FuncContext _localctx = new FuncContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_func);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(296);
			type_meth();
			setState(297);
			match(T__29);
			setState(298);
			match(ID);
			setState(299);
			match(T__3);
			setState(300);
			func_t();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Func_tContext extends ParserRuleContext {
		public ParamContext param() {
			return getRuleContext(ParamContext.class,0);
		}
		public Func_kContext func_k() {
			return getRuleContext(Func_kContext.class,0);
		}
		public Func_tContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func_t; }
	}

	public final Func_tContext func_t() throws RecognitionException {
		Func_tContext _localctx = new Func_tContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_func_t);
		try {
			setState(306);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__20:
			case T__21:
			case T__22:
			case T__23:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(302);
				param();
				setState(303);
				func_k();
				}
				break;
			case T__4:
				enterOuterAlt(_localctx, 2);
				{
				setState(305);
				func_k();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Func_kContext extends ParserRuleContext {
		public Func_pContext func_p() {
			return getRuleContext(Func_pContext.class,0);
		}
		public Func_kContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func_k; }
	}

	public final Func_kContext func_k() throws RecognitionException {
		Func_kContext _localctx = new Func_kContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_func_k);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(308);
			match(T__4);
			setState(309);
			match(T__1);
			setState(310);
			func_p();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Func_pContext extends ParserRuleContext {
		public Var_decContext var_dec() {
			return getRuleContext(Var_decContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public Func_pContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func_p; }
	}

	public final Func_pContext func_p() throws RecognitionException {
		Func_pContext _localctx = new Func_pContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_func_p);
		try {
			setState(316);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__14:
				enterOuterAlt(_localctx, 1);
				{
				setState(312);
				var_dec();
				setState(313);
				block();
				}
				break;
			case T__9:
				enterOuterAlt(_localctx, 2);
				{
				setState(315);
				block();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParamContext extends ParserRuleContext {
		public Var_typeContext var_type() {
			return getRuleContext(Var_typeContext.class,0);
		}
		public TerminalNode ID() { return getToken(BloonParser.ID, 0); }
		public Param_tContext param_t() {
			return getRuleContext(Param_tContext.class,0);
		}
		public Custom_typeContext custom_type() {
			return getRuleContext(Custom_typeContext.class,0);
		}
		public ParamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param; }
	}

	public final ParamContext param() throws RecognitionException {
		ParamContext _localctx = new ParamContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_param);
		try {
			setState(326);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__20:
			case T__21:
			case T__22:
			case T__23:
				enterOuterAlt(_localctx, 1);
				{
				setState(318);
				var_type();
				setState(319);
				match(ID);
				setState(320);
				param_t();
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(322);
				custom_type();
				setState(323);
				match(ID);
				setState(324);
				param_t();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Param_tContext extends ParserRuleContext {
		public ParamContext param() {
			return getRuleContext(ParamContext.class,0);
		}
		public Param_tContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param_t; }
	}

	public final Param_tContext param_t() throws RecognitionException {
		Param_tContext _localctx = new Param_tContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_param_t);
		try {
			setState(331);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__15:
				enterOuterAlt(_localctx, 1);
				{
				setState(328);
				match(T__15);
				setState(329);
				param();
				}
				break;
			case T__4:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BlockContext extends ParserRuleContext {
		public Block_tContext block_t() {
			return getRuleContext(Block_tContext.class,0);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_block);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(333);
			match(T__9);
			setState(334);
			block_t();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Block_tContext extends ParserRuleContext {
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public Block_tContext block_t() {
			return getRuleContext(Block_tContext.class,0);
		}
		public Block_tContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block_t; }
	}

	public final Block_tContext block_t() throws RecognitionException {
		Block_tContext _localctx = new Block_tContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_block_t);
		try {
			setState(343);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(336);
				statement();
				setState(337);
				block_t();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(339);
				statement();
				setState(340);
				match(T__12);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(342);
				match(T__12);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class R_returnContext extends ParserRuleContext {
		public Super_expContext super_exp() {
			return getRuleContext(Super_expContext.class,0);
		}
		public R_returnContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_r_return; }
	}

	public final R_returnContext r_return() throws RecognitionException {
		R_returnContext _localctx = new R_returnContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_r_return);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(345);
			match(T__30);
			setState(346);
			match(T__3);
			compi.add_op('(')
			setState(348);
			super_exp();
			setState(349);
			match(T__4);
			compi.close_parens()
			setState(351);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CallContext extends ParserRuleContext {
		public VarContext var() {
			return getRuleContext(VarContext.class,0);
		}
		public Call_tContext call_t() {
			return getRuleContext(Call_tContext.class,0);
		}
		public CallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_call; }
	}

	public final CallContext call() throws RecognitionException {
		CallContext _localctx = new CallContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_call);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(353);
			var();
			setState(354);
			match(T__3);
			setState(355);
			call_t();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Call_tContext extends ParserRuleContext {
		public Call_argsContext call_args() {
			return getRuleContext(Call_argsContext.class,0);
		}
		public Call_tContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_call_t; }
	}

	public final Call_tContext call_t() throws RecognitionException {
		Call_tContext _localctx = new Call_tContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_call_t);
		try {
			setState(361);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__3:
			case T__24:
			case T__25:
			case T__42:
			case ID:
			case CONST_INT:
			case CONST_FLOAT:
			case CONST_STR:
				enterOuterAlt(_localctx, 1);
				{
				setState(357);
				call_args();
				setState(358);
				match(T__4);
				}
				break;
			case T__4:
				enterOuterAlt(_localctx, 2);
				{
				setState(360);
				match(T__4);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Call_argsContext extends ParserRuleContext {
		public Super_expContext super_exp() {
			return getRuleContext(Super_expContext.class,0);
		}
		public Call_args_tContext call_args_t() {
			return getRuleContext(Call_args_tContext.class,0);
		}
		public CallContext call() {
			return getRuleContext(CallContext.class,0);
		}
		public Call_argsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_call_args; }
	}

	public final Call_argsContext call_args() throws RecognitionException {
		Call_argsContext _localctx = new Call_argsContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_call_args);
		try {
			setState(369);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,23,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(363);
				super_exp();
				setState(364);
				call_args_t();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(366);
				call();
				setState(367);
				call_args_t();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Call_args_tContext extends ParserRuleContext {
		public Call_argsContext call_args() {
			return getRuleContext(Call_argsContext.class,0);
		}
		public Call_args_tContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_call_args_t; }
	}

	public final Call_args_tContext call_args_t() throws RecognitionException {
		Call_args_tContext _localctx = new Call_args_tContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_call_args_t);
		try {
			setState(374);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__15:
				enterOuterAlt(_localctx, 1);
				{
				setState(371);
				match(T__15);
				setState(372);
				call_args();
				}
				break;
			case T__4:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Call_voidContext extends ParserRuleContext {
		public CallContext call() {
			return getRuleContext(CallContext.class,0);
		}
		public Call_voidContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_call_void; }
	}

	public final Call_voidContext call_void() throws RecognitionException {
		Call_voidContext _localctx = new Call_voidContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_call_void);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(376);
			call();
			setState(377);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ReadContext extends ParserRuleContext {
		public Read_tContext read_t() {
			return getRuleContext(Read_tContext.class,0);
		}
		public ReadContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_read; }
	}

	public final ReadContext read() throws RecognitionException {
		ReadContext _localctx = new ReadContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_read);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(379);
			match(T__31);
			setState(380);
			match(T__3);
			compi.add_op('(')
			setState(382);
			read_t();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Read_tContext extends ParserRuleContext {
		public VarContext var() {
			return getRuleContext(VarContext.class,0);
		}
		public Read_kContext read_k() {
			return getRuleContext(Read_kContext.class,0);
		}
		public Read_tContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_read_t; }
	}

	public final Read_tContext read_t() throws RecognitionException {
		Read_tContext _localctx = new Read_tContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_read_t);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(384);
			var();
			compi.call_method('read')
			setState(386);
			read_k();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Read_kContext extends ParserRuleContext {
		public Read_tContext read_t() {
			return getRuleContext(Read_tContext.class,0);
		}
		public Read_kContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_read_k; }
	}

	public final Read_kContext read_k() throws RecognitionException {
		Read_kContext _localctx = new Read_kContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_read_k);
		try {
			setState(393);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__15:
				enterOuterAlt(_localctx, 1);
				{
				setState(388);
				match(T__15);
				setState(389);
				read_t();
				}
				break;
			case T__4:
				enterOuterAlt(_localctx, 2);
				{
				setState(390);
				match(T__4);
				compi.close_parens()
				setState(392);
				match(T__1);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class WriteContext extends ParserRuleContext {
		public Write_tContext write_t() {
			return getRuleContext(Write_tContext.class,0);
		}
		public WriteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_write; }
	}

	public final WriteContext write() throws RecognitionException {
		WriteContext _localctx = new WriteContext(_ctx, getState());
		enterRule(_localctx, 86, RULE_write);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(395);
			match(T__32);
			setState(396);
			match(T__3);
			compi.add_op('(')
			setState(398);
			write_t();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Write_tContext extends ParserRuleContext {
		public Token CONST_STR;
		public Super_expContext super_exp() {
			return getRuleContext(Super_expContext.class,0);
		}
		public Write_kContext write_k() {
			return getRuleContext(Write_kContext.class,0);
		}
		public TerminalNode CONST_STR() { return getToken(BloonParser.CONST_STR, 0); }
		public CallContext call() {
			return getRuleContext(CallContext.class,0);
		}
		public Write_tContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_write_t; }
	}

	public final Write_tContext write_t() throws RecognitionException {
		Write_tContext _localctx = new Write_tContext(_ctx, getState());
		enterRule(_localctx, 88, RULE_write_t);
		try {
			setState(410);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,26,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(400);
				super_exp();
				compi.call_method('write')
				setState(402);
				write_k();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(404);
				((Write_tContext)_localctx).CONST_STR = match(CONST_STR);
				compi.get_const((((Write_tContext)_localctx).CONST_STR!=null?((Write_tContext)_localctx).CONST_STR.getText():null), "string"); compi.call_method('write')
				setState(406);
				write_k();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(407);
				call();
				setState(408);
				write_k();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Write_kContext extends ParserRuleContext {
		public Write_tContext write_t() {
			return getRuleContext(Write_tContext.class,0);
		}
		public Write_kContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_write_k; }
	}

	public final Write_kContext write_k() throws RecognitionException {
		Write_kContext _localctx = new Write_kContext(_ctx, getState());
		enterRule(_localctx, 90, RULE_write_k);
		try {
			setState(417);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__15:
				enterOuterAlt(_localctx, 1);
				{
				setState(412);
				match(T__15);
				setState(413);
				write_t();
				}
				break;
			case T__4:
				enterOuterAlt(_localctx, 2);
				{
				setState(414);
				match(T__4);
				compi.close_parens()
				setState(416);
				match(T__1);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CondContext extends ParserRuleContext {
		public Super_expContext super_exp() {
			return getRuleContext(Super_expContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public Cond_tContext cond_t() {
			return getRuleContext(Cond_tContext.class,0);
		}
		public CondContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cond; }
	}

	public final CondContext cond() throws RecognitionException {
		CondContext _localctx = new CondContext(_ctx, getState());
		enterRule(_localctx, 92, RULE_cond);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(419);
			match(T__33);
			setState(420);
			match(T__3);
			compi.add_op('(')
			setState(422);
			super_exp();
			setState(423);
			match(T__4);
			compi.close_parens()
			setState(425);
			match(T__34);
			setState(426);
			block();
			setState(427);
			cond_t();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Cond_tContext extends ParserRuleContext {
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public Cond_tContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cond_t; }
	}

	public final Cond_tContext cond_t() throws RecognitionException {
		Cond_tContext _localctx = new Cond_tContext(_ctx, getState());
		enterRule(_localctx, 94, RULE_cond_t);
		try {
			setState(432);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__35:
				enterOuterAlt(_localctx, 1);
				{
				setState(429);
				match(T__35);
				setState(430);
				block();
				}
				break;
			case T__12:
			case T__30:
			case T__31:
			case T__32:
			case T__33:
			case T__36:
			case T__38:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class R_whileContext extends ParserRuleContext {
		public Super_expContext super_exp() {
			return getRuleContext(Super_expContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public R_whileContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_r_while; }
	}

	public final R_whileContext r_while() throws RecognitionException {
		R_whileContext _localctx = new R_whileContext(_ctx, getState());
		enterRule(_localctx, 96, RULE_r_while);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(434);
			match(T__36);
			setState(435);
			match(T__3);
			compi.add_op('(')
			setState(437);
			super_exp();
			setState(438);
			match(T__4);
			compi.close_parens()
			setState(440);
			match(T__37);
			setState(441);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FloopContext extends ParserRuleContext {
		public VarContext var() {
			return getRuleContext(VarContext.class,0);
		}
		public Super_expContext super_exp() {
			return getRuleContext(Super_expContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public FloopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_floop; }
	}

	public final FloopContext floop() throws RecognitionException {
		FloopContext _localctx = new FloopContext(_ctx, getState());
		enterRule(_localctx, 98, RULE_floop);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(443);
			match(T__38);
			setState(444);
			var();
			setState(445);
			match(T__39);
			setState(446);
			super_exp();
			setState(447);
			match(T__37);
			setState(448);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Super_expContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Super_exp_tContext super_exp_t() {
			return getRuleContext(Super_exp_tContext.class,0);
		}
		public Super_expContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_super_exp; }
	}

	public final Super_expContext super_exp() throws RecognitionException {
		Super_expContext _localctx = new Super_expContext(_ctx, getState());
		enterRule(_localctx, 100, RULE_super_exp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(450);
			expression();
			setState(451);
			super_exp_t();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Super_exp_tContext extends ParserRuleContext {
		public Super_expContext super_exp() {
			return getRuleContext(Super_expContext.class,0);
		}
		public Super_exp_tContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_super_exp_t; }
	}

	public final Super_exp_tContext super_exp_t() throws RecognitionException {
		Super_exp_tContext _localctx = new Super_exp_tContext(_ctx, getState());
		enterRule(_localctx, 102, RULE_super_exp_t);
		try {
			setState(458);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__40:
				enterOuterAlt(_localctx, 1);
				{
				setState(453);
				match(T__40);
				setState(454);
				super_exp();
				}
				break;
			case T__41:
				enterOuterAlt(_localctx, 2);
				{
				setState(455);
				match(T__41);
				setState(456);
				super_exp();
				}
				break;
			case T__1:
			case T__4:
			case T__15:
			case T__37:
				enterOuterAlt(_localctx, 3);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public Expression_tContext expression_t() {
			return getRuleContext(Expression_tContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 104, RULE_expression);
		try {
			setState(468);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__42:
				enterOuterAlt(_localctx, 1);
				{
				setState(460);
				match(T__42);
				setState(461);
				exp();
				setState(462);
				expression_t();
				}
				break;
			case T__3:
			case T__24:
			case T__25:
			case ID:
			case CONST_INT:
			case CONST_FLOAT:
			case CONST_STR:
				enterOuterAlt(_localctx, 2);
				{
				setState(464);
				exp();
				setState(465);
				expression_t();
				compi.arithmetic_operation()
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expression_tContext extends ParserRuleContext {
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public Expression_tContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression_t; }
	}

	public final Expression_tContext expression_t() throws RecognitionException {
		Expression_tContext _localctx = new Expression_tContext(_ctx, getState());
		enterRule(_localctx, 106, RULE_expression_t);
		try {
			setState(489);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__8:
				enterOuterAlt(_localctx, 1);
				{
				setState(470);
				match(T__8);
				compi.add_op('>')
				setState(472);
				exp();
				}
				break;
			case T__6:
				enterOuterAlt(_localctx, 2);
				{
				setState(473);
				match(T__6);
				compi.add_op('<')
				setState(475);
				exp();
				}
				break;
			case T__43:
				enterOuterAlt(_localctx, 3);
				{
				setState(476);
				match(T__43);
				compi.add_op('<=')
				setState(478);
				exp();
				}
				break;
			case T__44:
				enterOuterAlt(_localctx, 4);
				{
				setState(479);
				match(T__44);
				compi.add_op('>=')
				setState(481);
				exp();
				}
				break;
			case T__45:
				enterOuterAlt(_localctx, 5);
				{
				setState(482);
				match(T__45);
				compi.add_op('==')
				setState(484);
				exp();
				}
				break;
			case T__46:
				enterOuterAlt(_localctx, 6);
				{
				setState(485);
				match(T__46);
				compi.add_op('!=')
				setState(487);
				exp();
				}
				break;
			case T__1:
			case T__4:
			case T__15:
			case T__37:
			case T__40:
			case T__41:
				enterOuterAlt(_localctx, 7);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpContext extends ParserRuleContext {
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public Exp_tContext exp_t() {
			return getRuleContext(Exp_tContext.class,0);
		}
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
	}

	public final ExpContext exp() throws RecognitionException {
		ExpContext _localctx = new ExpContext(_ctx, getState());
		enterRule(_localctx, 108, RULE_exp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(491);
			term();
			setState(492);
			exp_t();
			compi.arithmetic_operation()
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Exp_tContext extends ParserRuleContext {
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public Exp_tContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp_t; }
	}

	public final Exp_tContext exp_t() throws RecognitionException {
		Exp_tContext _localctx = new Exp_tContext(_ctx, getState());
		enterRule(_localctx, 110, RULE_exp_t);
		try {
			setState(502);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__24:
				enterOuterAlt(_localctx, 1);
				{
				setState(495);
				match(T__24);
				compi.add_op('+')
				setState(497);
				exp();
				}
				break;
			case T__25:
				enterOuterAlt(_localctx, 2);
				{
				setState(498);
				match(T__25);
				compi.add_op('-')
				setState(500);
				exp();
				}
				break;
			case T__1:
			case T__4:
			case T__6:
			case T__8:
			case T__15:
			case T__18:
			case T__37:
			case T__40:
			case T__41:
			case T__43:
			case T__44:
			case T__45:
			case T__46:
				enterOuterAlt(_localctx, 3);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TermContext extends ParserRuleContext {
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public Term_tContext term_t() {
			return getRuleContext(Term_tContext.class,0);
		}
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 112, RULE_term);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(504);
			factor();
			setState(505);
			term_t();
			compi.arithmetic_operation()
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Term_tContext extends ParserRuleContext {
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public Term_tContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term_t; }
	}

	public final Term_tContext term_t() throws RecognitionException {
		Term_tContext _localctx = new Term_tContext(_ctx, getState());
		enterRule(_localctx, 114, RULE_term_t);
		try {
			setState(515);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__26:
				enterOuterAlt(_localctx, 1);
				{
				setState(508);
				match(T__26);
				compi.add_op('*')
				setState(510);
				term();
				}
				break;
			case T__27:
				enterOuterAlt(_localctx, 2);
				{
				setState(511);
				match(T__27);
				compi.add_op('/')
				setState(513);
				term();
				}
				break;
			case T__1:
			case T__4:
			case T__6:
			case T__8:
			case T__15:
			case T__18:
			case T__24:
			case T__25:
			case T__37:
			case T__40:
			case T__41:
			case T__43:
			case T__44:
			case T__45:
			case T__46:
				enterOuterAlt(_localctx, 3);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FactorContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Var_constContext var_const() {
			return getRuleContext(Var_constContext.class,0);
		}
		public CallContext call() {
			return getRuleContext(CallContext.class,0);
		}
		public Factor_tContext factor_t() {
			return getRuleContext(Factor_tContext.class,0);
		}
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 116, RULE_factor);
		try {
			setState(526);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,34,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(517);
				match(T__3);
				compi.add_op('(')
				setState(519);
				expression();
				setState(520);
				match(T__4);
				compi.close_parens()
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(523);
				var_const();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(524);
				call();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(525);
				factor_t();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Factor_tContext extends ParserRuleContext {
		public Var_constContext var_const() {
			return getRuleContext(Var_constContext.class,0);
		}
		public Factor_tContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor_t; }
	}

	public final Factor_tContext factor_t() throws RecognitionException {
		Factor_tContext _localctx = new Factor_tContext(_ctx, getState());
		enterRule(_localctx, 118, RULE_factor_t);
		try {
			setState(532);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__24:
				enterOuterAlt(_localctx, 1);
				{
				setState(528);
				match(T__24);
				setState(529);
				var_const();
				}
				break;
			case T__25:
				enterOuterAlt(_localctx, 2);
				{
				setState(530);
				match(T__25);
				setState(531);
				var_const();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Var_constContext extends ParserRuleContext {
		public Token CONST_INT;
		public Token CONST_FLOAT;
		public Token CONST_STR;
		public VarContext var() {
			return getRuleContext(VarContext.class,0);
		}
		public TerminalNode CONST_INT() { return getToken(BloonParser.CONST_INT, 0); }
		public TerminalNode CONST_FLOAT() { return getToken(BloonParser.CONST_FLOAT, 0); }
		public TerminalNode CONST_STR() { return getToken(BloonParser.CONST_STR, 0); }
		public Var_constContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_const; }
	}

	public final Var_constContext var_const() throws RecognitionException {
		Var_constContext _localctx = new Var_constContext(_ctx, getState());
		enterRule(_localctx, 120, RULE_var_const);
		try {
			setState(541);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(534);
				var();
				}
				break;
			case CONST_INT:
				enterOuterAlt(_localctx, 2);
				{
				setState(535);
				((Var_constContext)_localctx).CONST_INT = match(CONST_INT);
				compi.get_const((((Var_constContext)_localctx).CONST_INT!=null?((Var_constContext)_localctx).CONST_INT.getText():null), "int")
				}
				break;
			case CONST_FLOAT:
				enterOuterAlt(_localctx, 3);
				{
				setState(537);
				((Var_constContext)_localctx).CONST_FLOAT = match(CONST_FLOAT);
				compi.get_const((((Var_constContext)_localctx).CONST_FLOAT!=null?((Var_constContext)_localctx).CONST_FLOAT.getText():null), "float")
				}
				break;
			case CONST_STR:
				enterOuterAlt(_localctx, 4);
				{
				setState(539);
				((Var_constContext)_localctx).CONST_STR = match(CONST_STR);
				compi.get_const((((Var_constContext)_localctx).CONST_STR!=null?((Var_constContext)_localctx).CONST_STR.getText():null), "string")
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\66\u0222\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3"+
		"\u008c\n\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6"+
		"\5\6\u009d\n\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00aa\n"+
		"\b\3\t\3\t\3\t\3\t\3\t\5\t\u00b1\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5"+
		"\n\u00bb\n\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\5\f\u00c5\n\f\3\r\3\r"+
		"\3\r\5\r\u00ca\n\r\3\16\3\16\3\16\3\17\3\17\5\17\u00d1\n\17\3\17\3\17"+
		"\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00e1"+
		"\n\17\5\17\u00e3\n\17\3\20\3\20\5\20\u00e7\n\20\3\21\3\21\3\21\3\21\3"+
		"\22\3\22\3\22\3\22\3\22\5\22\u00f2\n\22\3\23\3\23\3\23\3\23\3\24\3\24"+
		"\3\24\3\24\5\24\u00fc\n\24\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26"+
		"\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u010d\n\26\3\27\3\27\3\30\3\30\3\31"+
		"\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u011b\n\31\3\32\3\32\5\32\u011f"+
		"\n\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u0129\n\33\3\34\3\34"+
		"\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\5\35\u0135\n\35\3\36\3\36\3\36"+
		"\3\36\3\37\3\37\3\37\3\37\5\37\u013f\n\37\3 \3 \3 \3 \3 \3 \3 \3 \5 \u0149"+
		"\n \3!\3!\3!\5!\u014e\n!\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\5#\u015a\n#"+
		"\3$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3&\5&\u016c\n&\3\'\3\'\3"+
		"\'\3\'\3\'\3\'\5\'\u0174\n\'\3(\3(\3(\5(\u0179\n(\3)\3)\3)\3*\3*\3*\3"+
		"*\3*\3+\3+\3+\3+\3,\3,\3,\3,\3,\5,\u018c\n,\3-\3-\3-\3-\3-\3.\3.\3.\3"+
		".\3.\3.\3.\3.\3.\3.\5.\u019d\n.\3/\3/\3/\3/\3/\5/\u01a4\n/\3\60\3\60\3"+
		"\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\5\61\u01b3\n\61"+
		"\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63"+
		"\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\5\65\u01cd\n\65\3\66"+
		"\3\66\3\66\3\66\3\66\3\66\3\66\3\66\5\66\u01d7\n\66\3\67\3\67\3\67\3\67"+
		"\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67"+
		"\3\67\5\67\u01ec\n\67\38\38\38\38\39\39\39\39\39\39\39\59\u01f9\n9\3:"+
		"\3:\3:\3:\3;\3;\3;\3;\3;\3;\3;\5;\u0206\n;\3<\3<\3<\3<\3<\3<\3<\3<\3<"+
		"\5<\u0211\n<\3=\3=\3=\3=\5=\u0217\n=\3>\3>\3>\3>\3>\3>\3>\5>\u0220\n>"+
		"\3>\2\2?\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668"+
		":<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz\2\3\3\2\27\32\2\u0221\2|\3\2\2\2\4"+
		"\u008b\3\2\2\2\6\u008d\3\2\2\2\b\u0092\3\2\2\2\n\u009c\3\2\2\2\f\u009e"+
		"\3\2\2\2\16\u00a9\3\2\2\2\20\u00b0\3\2\2\2\22\u00ba\3\2\2\2\24\u00bc\3"+
		"\2\2\2\26\u00c4\3\2\2\2\30\u00c9\3\2\2\2\32\u00cb\3\2\2\2\34\u00ce\3\2"+
		"\2\2\36\u00e6\3\2\2\2 \u00e8\3\2\2\2\"\u00f1\3\2\2\2$\u00f3\3\2\2\2&\u00fb"+
		"\3\2\2\2(\u00fd\3\2\2\2*\u010c\3\2\2\2,\u010e\3\2\2\2.\u0110\3\2\2\2\60"+
		"\u011a\3\2\2\2\62\u011e\3\2\2\2\64\u0128\3\2\2\2\66\u012a\3\2\2\28\u0134"+
		"\3\2\2\2:\u0136\3\2\2\2<\u013e\3\2\2\2>\u0148\3\2\2\2@\u014d\3\2\2\2B"+
		"\u014f\3\2\2\2D\u0159\3\2\2\2F\u015b\3\2\2\2H\u0163\3\2\2\2J\u016b\3\2"+
		"\2\2L\u0173\3\2\2\2N\u0178\3\2\2\2P\u017a\3\2\2\2R\u017d\3\2\2\2T\u0182"+
		"\3\2\2\2V\u018b\3\2\2\2X\u018d\3\2\2\2Z\u019c\3\2\2\2\\\u01a3\3\2\2\2"+
		"^\u01a5\3\2\2\2`\u01b2\3\2\2\2b\u01b4\3\2\2\2d\u01bd\3\2\2\2f\u01c4\3"+
		"\2\2\2h\u01cc\3\2\2\2j\u01d6\3\2\2\2l\u01eb\3\2\2\2n\u01ed\3\2\2\2p\u01f8"+
		"\3\2\2\2r\u01fa\3\2\2\2t\u0205\3\2\2\2v\u0210\3\2\2\2x\u0216\3\2\2\2z"+
		"\u021f\3\2\2\2|}\7\3\2\2}~\7\62\2\2~\177\7\4\2\2\177\u0080\5\4\3\2\u0080"+
		"\3\3\2\2\2\u0081\u0082\5\b\5\2\u0082\u0083\5\4\3\2\u0083\u008c\3\2\2\2"+
		"\u0084\u0085\5\32\16\2\u0085\u0086\5\4\3\2\u0086\u008c\3\2\2\2\u0087\u0088"+
		"\5\66\34\2\u0088\u0089\5\4\3\2\u0089\u008c\3\2\2\2\u008a\u008c\5\6\4\2"+
		"\u008b\u0081\3\2\2\2\u008b\u0084\3\2\2\2\u008b\u0087\3\2\2\2\u008b\u008a"+
		"\3\2\2\2\u008c\5\3\2\2\2\u008d\u008e\7\5\2\2\u008e\u008f\7\6\2\2\u008f"+
		"\u0090\7\7\2\2\u0090\u0091\5B\"\2\u0091\7\3\2\2\2\u0092\u0093\7\b\2\2"+
		"\u0093\u0094\7\62\2\2\u0094\u0095\5\n\6\2\u0095\t\3\2\2\2\u0096\u0097"+
		"\7\t\2\2\u0097\u0098\7\n\2\2\u0098\u0099\7\62\2\2\u0099\u009a\7\13\2\2"+
		"\u009a\u009d\5\f\7\2\u009b\u009d\5\f\7\2\u009c\u0096\3\2\2\2\u009c\u009b"+
		"\3\2\2\2\u009d\13\3\2\2\2\u009e\u009f\7\4\2\2\u009f\u00a0\7\f\2\2\u00a0"+
		"\u00a1\5\16\b\2\u00a1\r\3\2\2\2\u00a2\u00a3\7\r\2\2\u00a3\u00a4\7\t\2"+
		"\2\u00a4\u00a5\5\32\16\2\u00a5\u00a6\7\13\2\2\u00a6\u00a7\5\20\t\2\u00a7"+
		"\u00aa\3\2\2\2\u00a8\u00aa\5\20\t\2\u00a9\u00a2\3\2\2\2\u00a9\u00a8\3"+
		"\2\2\2\u00aa\17\3\2\2\2\u00ab\u00ac\7\16\2\2\u00ac\u00ad\7\t\2\2\u00ad"+
		"\u00b1\5\22\n\2\u00ae\u00af\7\17\2\2\u00af\u00b1\7\4\2\2\u00b0\u00ab\3"+
		"\2\2\2\u00b0\u00ae\3\2\2\2\u00b1\21\3\2\2\2\u00b2\u00b3\5\66\34\2\u00b3"+
		"\u00b4\7\13\2\2\u00b4\u00b5\7\17\2\2\u00b5\u00b6\7\4\2\2\u00b6\u00bb\3"+
		"\2\2\2\u00b7\u00b8\5\66\34\2\u00b8\u00b9\5\22\n\2\u00b9\u00bb\3\2\2\2"+
		"\u00ba\u00b2\3\2\2\2\u00ba\u00b7\3\2\2\2\u00bb\23\3\2\2\2\u00bc\u00bd"+
		"\7\62\2\2\u00bd\u00be\5\26\f\2\u00be\u00bf\b\13\1\2\u00bf\25\3\2\2\2\u00c0"+
		"\u00c1\5 \21\2\u00c1\u00c2\5\30\r\2\u00c2\u00c5\3\2\2\2\u00c3\u00c5\5"+
		"\30\r\2\u00c4\u00c0\3\2\2\2\u00c4\u00c3\3\2\2\2\u00c5\27\3\2\2\2\u00c6"+
		"\u00c7\7\20\2\2\u00c7\u00ca\5\24\13\2\u00c8\u00ca\3\2\2\2\u00c9\u00c6"+
		"\3\2\2\2\u00c9\u00c8\3\2\2\2\u00ca\31\3\2\2\2\u00cb\u00cc\7\21\2\2\u00cc"+
		"\u00cd\5\34\17\2\u00cd\33\3\2\2\2\u00ce\u00d0\7\62\2\2\u00cf\u00d1\5$"+
		"\23\2\u00d0\u00cf\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2"+
		"\u00e2\b\17\1\2\u00d3\u00d4\7\22\2\2\u00d4\u00e3\5\34\17\2\u00d5\u00e0"+
		"\7\23\2\2\u00d6\u00d7\5,\27\2\u00d7\u00d8\b\17\1\2\u00d8\u00d9\7\4\2\2"+
		"\u00d9\u00da\5\36\20\2\u00da\u00e1\3\2\2\2\u00db\u00dc\5.\30\2\u00dc\u00dd"+
		"\b\17\1\2\u00dd\u00de\7\4\2\2\u00de\u00df\5\36\20\2\u00df\u00e1\3\2\2"+
		"\2\u00e0\u00d6\3\2\2\2\u00e0\u00db\3\2\2\2\u00e1\u00e3\3\2\2\2\u00e2\u00d3"+
		"\3\2\2\2\u00e2\u00d5\3\2\2\2\u00e3\35\3\2\2\2\u00e4\u00e7\5\34\17\2\u00e5"+
		"\u00e7\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e5\3\2\2\2\u00e7\37\3\2\2"+
		"\2\u00e8\u00e9\7\24\2\2\u00e9\u00ea\5n8\2\u00ea\u00eb\5\"\22\2\u00eb!"+
		"\3\2\2\2\u00ec\u00ed\7\22\2\2\u00ed\u00ee\5n8\2\u00ee\u00ef\7\25\2\2\u00ef"+
		"\u00f2\3\2\2\2\u00f0\u00f2\7\25\2\2\u00f1\u00ec\3\2\2\2\u00f1\u00f0\3"+
		"\2\2\2\u00f2#\3\2\2\2\u00f3\u00f4\7\24\2\2\u00f4\u00f5\7\63\2\2\u00f5"+
		"\u00f6\5&\24\2\u00f6%\3\2\2\2\u00f7\u00f8\7\22\2\2\u00f8\u00f9\7\63\2"+
		"\2\u00f9\u00fc\7\25\2\2\u00fa\u00fc\7\25\2\2\u00fb\u00f7\3\2\2\2\u00fb"+
		"\u00fa\3\2\2\2\u00fc\'\3\2\2\2\u00fd\u00fe\5\24\13\2\u00fe\u00ff\5*\26"+
		"\2\u00ff)\3\2\2\2\u0100\u0101\7\26\2\2\u0101\u0102\b\26\1\2\u0102\u0103"+
		"\5f\64\2\u0103\u0104\b\26\1\2\u0104\u0105\7\4\2\2\u0105\u010d\3\2\2\2"+
		"\u0106\u0107\5\60\31\2\u0107\u0108\b\26\1\2\u0108\u0109\5f\64\2\u0109"+
		"\u010a\b\26\1\2\u010a\u010b\7\4\2\2\u010b\u010d\3\2\2\2\u010c\u0100\3"+
		"\2\2\2\u010c\u0106\3\2\2\2\u010d+\3\2\2\2\u010e\u010f\t\2\2\2\u010f-\3"+
		"\2\2\2\u0110\u0111\7\62\2\2\u0111/\3\2\2\2\u0112\u0113\7\33\2\2\u0113"+
		"\u011b\7\26\2\2\u0114\u0115\7\34\2\2\u0115\u011b\7\26\2\2\u0116\u0117"+
		"\7\35\2\2\u0117\u011b\7\26\2\2\u0118\u0119\7\36\2\2\u0119\u011b\7\26\2"+
		"\2\u011a\u0112\3\2\2\2\u011a\u0114\3\2\2\2\u011a\u0116\3\2\2\2\u011a\u0118"+
		"\3\2\2\2\u011b\61\3\2\2\2\u011c\u011f\5,\27\2\u011d\u011f\7\37\2\2\u011e"+
		"\u011c\3\2\2\2\u011e\u011d\3\2\2\2\u011f\63\3\2\2\2\u0120\u0129\5(\25"+
		"\2\u0121\u0129\5^\60\2\u0122\u0129\5F$\2\u0123\u0129\5R*\2\u0124\u0129"+
		"\5X-\2\u0125\u0129\5b\62\2\u0126\u0129\5d\63\2\u0127\u0129\5P)\2\u0128"+
		"\u0120\3\2\2\2\u0128\u0121\3\2\2\2\u0128\u0122\3\2\2\2\u0128\u0123\3\2"+
		"\2\2\u0128\u0124\3\2\2\2\u0128\u0125\3\2\2\2\u0128\u0126\3\2\2\2\u0128"+
		"\u0127\3\2\2\2\u0129\65\3\2\2\2\u012a\u012b\5\62\32\2\u012b\u012c\7 \2"+
		"\2\u012c\u012d\7\62\2\2\u012d\u012e\7\6\2\2\u012e\u012f\58\35\2\u012f"+
		"\67\3\2\2\2\u0130\u0131\5> \2\u0131\u0132\5:\36\2\u0132\u0135\3\2\2\2"+
		"\u0133\u0135\5:\36\2\u0134\u0130\3\2\2\2\u0134\u0133\3\2\2\2\u01359\3"+
		"\2\2\2\u0136\u0137\7\7\2\2\u0137\u0138\7\4\2\2\u0138\u0139\5<\37\2\u0139"+
		";\3\2\2\2\u013a\u013b\5\32\16\2\u013b\u013c\5B\"\2\u013c\u013f\3\2\2\2"+
		"\u013d\u013f\5B\"\2\u013e\u013a\3\2\2\2\u013e\u013d\3\2\2\2\u013f=\3\2"+
		"\2\2\u0140\u0141\5,\27\2\u0141\u0142\7\62\2\2\u0142\u0143\5@!\2\u0143"+
		"\u0149\3\2\2\2\u0144\u0145\5.\30\2\u0145\u0146\7\62\2\2\u0146\u0147\5"+
		"@!\2\u0147\u0149\3\2\2\2\u0148\u0140\3\2\2\2\u0148\u0144\3\2\2\2\u0149"+
		"?\3\2\2\2\u014a\u014b\7\22\2\2\u014b\u014e\5> \2\u014c\u014e\3\2\2\2\u014d"+
		"\u014a\3\2\2\2\u014d\u014c\3\2\2\2\u014eA\3\2\2\2\u014f\u0150\7\f\2\2"+
		"\u0150\u0151\5D#\2\u0151C\3\2\2\2\u0152\u0153\5\64\33\2\u0153\u0154\5"+
		"D#\2\u0154\u015a\3\2\2\2\u0155\u0156\5\64\33\2\u0156\u0157\7\17\2\2\u0157"+
		"\u015a\3\2\2\2\u0158\u015a\7\17\2\2\u0159\u0152\3\2\2\2\u0159\u0155\3"+
		"\2\2\2\u0159\u0158\3\2\2\2\u015aE\3\2\2\2\u015b\u015c\7!\2\2\u015c\u015d"+
		"\7\6\2\2\u015d\u015e\b$\1\2\u015e\u015f\5f\64\2\u015f\u0160\7\7\2\2\u0160"+
		"\u0161\b$\1\2\u0161\u0162\7\4\2\2\u0162G\3\2\2\2\u0163\u0164\5\24\13\2"+
		"\u0164\u0165\7\6\2\2\u0165\u0166\5J&\2\u0166I\3\2\2\2\u0167\u0168\5L\'"+
		"\2\u0168\u0169\7\7\2\2\u0169\u016c\3\2\2\2\u016a\u016c\7\7\2\2\u016b\u0167"+
		"\3\2\2\2\u016b\u016a\3\2\2\2\u016cK\3\2\2\2\u016d\u016e\5f\64\2\u016e"+
		"\u016f\5N(\2\u016f\u0174\3\2\2\2\u0170\u0171\5H%\2\u0171\u0172\5N(\2\u0172"+
		"\u0174\3\2\2\2\u0173\u016d\3\2\2\2\u0173\u0170\3\2\2\2\u0174M\3\2\2\2"+
		"\u0175\u0176\7\22\2\2\u0176\u0179\5L\'\2\u0177\u0179\3\2\2\2\u0178\u0175"+
		"\3\2\2\2\u0178\u0177\3\2\2\2\u0179O\3\2\2\2\u017a\u017b\5H%\2\u017b\u017c"+
		"\7\4\2\2\u017cQ\3\2\2\2\u017d\u017e\7\"\2\2\u017e\u017f\7\6\2\2\u017f"+
		"\u0180\b*\1\2\u0180\u0181\5T+\2\u0181S\3\2\2\2\u0182\u0183\5\24\13\2\u0183"+
		"\u0184\b+\1\2\u0184\u0185\5V,\2\u0185U\3\2\2\2\u0186\u0187\7\22\2\2\u0187"+
		"\u018c\5T+\2\u0188\u0189\7\7\2\2\u0189\u018a\b,\1\2\u018a\u018c\7\4\2"+
		"\2\u018b\u0186\3\2\2\2\u018b\u0188\3\2\2\2\u018cW\3\2\2\2\u018d\u018e"+
		"\7#\2\2\u018e\u018f\7\6\2\2\u018f\u0190\b-\1\2\u0190\u0191\5Z.\2\u0191"+
		"Y\3\2\2\2\u0192\u0193\5f\64\2\u0193\u0194\b.\1\2\u0194\u0195\5\\/\2\u0195"+
		"\u019d\3\2\2\2\u0196\u0197\7\65\2\2\u0197\u0198\b.\1\2\u0198\u019d\5\\"+
		"/\2\u0199\u019a\5H%\2\u019a\u019b\5\\/\2\u019b\u019d\3\2\2\2\u019c\u0192"+
		"\3\2\2\2\u019c\u0196\3\2\2\2\u019c\u0199\3\2\2\2\u019d[\3\2\2\2\u019e"+
		"\u019f\7\22\2\2\u019f\u01a4\5Z.\2\u01a0\u01a1\7\7\2\2\u01a1\u01a2\b/\1"+
		"\2\u01a2\u01a4\7\4\2\2\u01a3\u019e\3\2\2\2\u01a3\u01a0\3\2\2\2\u01a4]"+
		"\3\2\2\2\u01a5\u01a6\7$\2\2\u01a6\u01a7\7\6\2\2\u01a7\u01a8\b\60\1\2\u01a8"+
		"\u01a9\5f\64\2\u01a9\u01aa\7\7\2\2\u01aa\u01ab\b\60\1\2\u01ab\u01ac\7"+
		"%\2\2\u01ac\u01ad\5B\"\2\u01ad\u01ae\5`\61\2\u01ae_\3\2\2\2\u01af\u01b0"+
		"\7&\2\2\u01b0\u01b3\5B\"\2\u01b1\u01b3\3\2\2\2\u01b2\u01af\3\2\2\2\u01b2"+
		"\u01b1\3\2\2\2\u01b3a\3\2\2\2\u01b4\u01b5\7\'\2\2\u01b5\u01b6\7\6\2\2"+
		"\u01b6\u01b7\b\62\1\2\u01b7\u01b8\5f\64\2\u01b8\u01b9\7\7\2\2\u01b9\u01ba"+
		"\b\62\1\2\u01ba\u01bb\7(\2\2\u01bb\u01bc\5B\"\2\u01bcc\3\2\2\2\u01bd\u01be"+
		"\7)\2\2\u01be\u01bf\5\24\13\2\u01bf\u01c0\7*\2\2\u01c0\u01c1\5f\64\2\u01c1"+
		"\u01c2\7(\2\2\u01c2\u01c3\5B\"\2\u01c3e\3\2\2\2\u01c4\u01c5\5j\66\2\u01c5"+
		"\u01c6\5h\65\2\u01c6g\3\2\2\2\u01c7\u01c8\7+\2\2\u01c8\u01cd\5f\64\2\u01c9"+
		"\u01ca\7,\2\2\u01ca\u01cd\5f\64\2\u01cb\u01cd\3\2\2\2\u01cc\u01c7\3\2"+
		"\2\2\u01cc\u01c9\3\2\2\2\u01cc\u01cb\3\2\2\2\u01cdi\3\2\2\2\u01ce\u01cf"+
		"\7-\2\2\u01cf\u01d0\5n8\2\u01d0\u01d1\5l\67\2\u01d1\u01d7\3\2\2\2\u01d2"+
		"\u01d3\5n8\2\u01d3\u01d4\5l\67\2\u01d4\u01d5\b\66\1\2\u01d5\u01d7\3\2"+
		"\2\2\u01d6\u01ce\3\2\2\2\u01d6\u01d2\3\2\2\2\u01d7k\3\2\2\2\u01d8\u01d9"+
		"\7\13\2\2\u01d9\u01da\b\67\1\2\u01da\u01ec\5n8\2\u01db\u01dc\7\t\2\2\u01dc"+
		"\u01dd\b\67\1\2\u01dd\u01ec\5n8\2\u01de\u01df\7.\2\2\u01df\u01e0\b\67"+
		"\1\2\u01e0\u01ec\5n8\2\u01e1\u01e2\7/\2\2\u01e2\u01e3\b\67\1\2\u01e3\u01ec"+
		"\5n8\2\u01e4\u01e5\7\60\2\2\u01e5\u01e6\b\67\1\2\u01e6\u01ec\5n8\2\u01e7"+
		"\u01e8\7\61\2\2\u01e8\u01e9\b\67\1\2\u01e9\u01ec\5n8\2\u01ea\u01ec\3\2"+
		"\2\2\u01eb\u01d8\3\2\2\2\u01eb\u01db\3\2\2\2\u01eb\u01de\3\2\2\2\u01eb"+
		"\u01e1\3\2\2\2\u01eb\u01e4\3\2\2\2\u01eb\u01e7\3\2\2\2\u01eb\u01ea\3\2"+
		"\2\2\u01ecm\3\2\2\2\u01ed\u01ee\5r:\2\u01ee\u01ef\5p9\2\u01ef\u01f0\b"+
		"8\1\2\u01f0o\3\2\2\2\u01f1\u01f2\7\33\2\2\u01f2\u01f3\b9\1\2\u01f3\u01f9"+
		"\5n8\2\u01f4\u01f5\7\34\2\2\u01f5\u01f6\b9\1\2\u01f6\u01f9\5n8\2\u01f7"+
		"\u01f9\3\2\2\2\u01f8\u01f1\3\2\2\2\u01f8\u01f4\3\2\2\2\u01f8\u01f7\3\2"+
		"\2\2\u01f9q\3\2\2\2\u01fa\u01fb\5v<\2\u01fb\u01fc\5t;\2\u01fc\u01fd\b"+
		":\1\2\u01fds\3\2\2\2\u01fe\u01ff\7\35\2\2\u01ff\u0200\b;\1\2\u0200\u0206"+
		"\5r:\2\u0201\u0202\7\36\2\2\u0202\u0203\b;\1\2\u0203\u0206\5r:\2\u0204"+
		"\u0206\3\2\2\2\u0205\u01fe\3\2\2\2\u0205\u0201\3\2\2\2\u0205\u0204\3\2"+
		"\2\2\u0206u\3\2\2\2\u0207\u0208\7\6\2\2\u0208\u0209\b<\1\2\u0209\u020a"+
		"\5j\66\2\u020a\u020b\7\7\2\2\u020b\u020c\b<\1\2\u020c\u0211\3\2\2\2\u020d"+
		"\u0211\5z>\2\u020e\u0211\5H%\2\u020f\u0211\5x=\2\u0210\u0207\3\2\2\2\u0210"+
		"\u020d\3\2\2\2\u0210\u020e\3\2\2\2\u0210\u020f\3\2\2\2\u0211w\3\2\2\2"+
		"\u0212\u0213\7\33\2\2\u0213\u0217\5z>\2\u0214\u0215\7\34\2\2\u0215\u0217"+
		"\5z>\2\u0216\u0212\3\2\2\2\u0216\u0214\3\2\2\2\u0217y\3\2\2\2\u0218\u0220"+
		"\5\24\13\2\u0219\u021a\7\63\2\2\u021a\u0220\b>\1\2\u021b\u021c\7\64\2"+
		"\2\u021c\u0220\b>\1\2\u021d\u021e\7\65\2\2\u021e\u0220\b>\1\2\u021f\u0218"+
		"\3\2\2\2\u021f\u0219\3\2\2\2\u021f\u021b\3\2\2\2\u021f\u021d\3\2\2\2\u0220"+
		"{\3\2\2\2\'\u008b\u009c\u00a9\u00b0\u00ba\u00c4\u00c9\u00d0\u00e0\u00e2"+
		"\u00e6\u00f1\u00fb\u010c\u011a\u011e\u0128\u0134\u013e\u0148\u014d\u0159"+
		"\u016b\u0173\u0178\u018b\u019c\u01a3\u01b2\u01cc\u01d6\u01eb\u01f8\u0205"+
		"\u0210\u0216\u021f";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}