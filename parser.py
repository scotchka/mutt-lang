from lark import Lark

grammar = r"""

?block: "{" (stmt ";") * "}"

stmt: "global" WORD expr -> assign_global
    | "local" WORD expr -> assign_local
    | "fn" WORD "(" WORD * ")" block -> declare_function
    | "return" expr -> return
    | "if" expr block ("elif" expr block)* ("else" block)? -> conditional
    | "while" expr block -> while
    | "print" expr -> print
    | expr





?expr: term "==" expr -> eq
    | term "<" expr -> lt
    | term ">" expr -> gt
    | term "<=" expr -> le
    | term ">=" expr -> ge
    | term "!=" expr -> ne
    | "!" expr -> neg
    | expr "+" term -> add
    | expr "-" term -> sub
    | term

?term: term "*" factor -> mul
    | term "/" factor -> sub
    | factor

?factor: "+" factor
    | "-" factor -> neg
    | NUMBER
    | WORD
    | ESCAPED_STRING
    | WORD "(" expr* ")" -> call
    | "True"
    | "False"
    | "None"
    | "(" expr ")"

COMMENT: /\(#[\s\S]*#\)/

%import common.NUMBER
%import common.ESCAPED_STRING
%import common.WORD
%import common.WS
%ignore WS
%ignore COMMENT

"""


parser = Lark(grammar, start='block', parser='lalr')
