# Generated from CSVFilter.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("J\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\5\7\64\n\7\3\b\3")
        buf.write("\b\7\b8\n\b\f\b\16\b;\13\b\3\b\3\b\3\t\6\t@\n\t\r\t\16")
        buf.write("\tA\3\n\6\nE\n\n\r\n\16\nF\3\n\3\n\2\2\13\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\3\2\6\4\2>>@@\5\2\f\f\17")
        buf.write("\17$$\3\2\62;\5\2\13\f\17\17\"\"\2M\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\3\25\3\2\2\2")
        buf.write("\5\32\3\2\2\2\7\34\3\2\2\2\t#\3\2\2\2\13*\3\2\2\2\r\63")
        buf.write("\3\2\2\2\17\65\3\2\2\2\21?\3\2\2\2\23D\3\2\2\2\25\26\7")
        buf.write("n\2\2\26\27\7q\2\2\27\30\7c\2\2\30\31\7f\2\2\31\4\3\2")
        buf.write("\2\2\32\33\7=\2\2\33\6\3\2\2\2\34\35\7h\2\2\35\36\7k\2")
        buf.write("\2\36\37\7n\2\2\37 \7v\2\2 !\7g\2\2!\"\7t\2\2\"\b\3\2")
        buf.write("\2\2#$\7e\2\2$%\7q\2\2%&\7n\2\2&\'\7w\2\2\'(\7o\2\2()")
        buf.write("\7p\2\2)\n\3\2\2\2*+\7r\2\2+,\7t\2\2,-\7k\2\2-.\7p\2\2")
        buf.write("./\7v\2\2/\f\3\2\2\2\60\64\t\2\2\2\61\62\7?\2\2\62\64")
        buf.write("\7?\2\2\63\60\3\2\2\2\63\61\3\2\2\2\64\16\3\2\2\2\659")
        buf.write("\7$\2\2\668\n\3\2\2\67\66\3\2\2\28;\3\2\2\29\67\3\2\2")
        buf.write("\29:\3\2\2\2:<\3\2\2\2;9\3\2\2\2<=\7$\2\2=\20\3\2\2\2")
        buf.write(">@\t\4\2\2?>\3\2\2\2@A\3\2\2\2A?\3\2\2\2AB\3\2\2\2B\22")
        buf.write("\3\2\2\2CE\t\5\2\2DC\3\2\2\2EF\3\2\2\2FD\3\2\2\2FG\3\2")
        buf.write("\2\2GH\3\2\2\2HI\b\n\2\2I\24\3\2\2\2\7\2\639AF\3\b\2\2")
        return buf.getvalue()


class CSVFilterLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    OPERATOR = 6
    STRING = 7
    INT = 8
    WS = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'load'", "';'", "'filter'", "'column'", "'print'" ]

    symbolicNames = [ "<INVALID>",
            "OPERATOR", "STRING", "INT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "OPERATOR", "STRING", 
                  "INT", "WS" ]

    grammarFileName = "CSVFilter.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


