%{
#include <stdio.h>
%}

%option noyywrap

COMMENT "//.*"
FLOATDCL "f"
INTDCL "i"
PRINT "p"
ID [a-zA-Z]
ASSIGN "="
PLUS "+"
MINUS "-"
MULTIPLY "*"
DIVIDE "/"
INUM [0-9]+
FNUM [0-9]+\.[0-9]+

%%
{COMMENT}   { /* Ignorar comentarios */ }
{FLOATDCL}  { printf("floatdcl id\n"); }
{INTDCL}    { printf("intdcl id\n"); }
{PRINT}     { printf("print id\n"); }
{ID}        { printf("id\n"); }
{ASSIGN}    { printf("assign\n"); }
{PLUS}      { printf("plus\n"); }
{MINUS}     { printf("minus\n"); }
{MULTIPLY}  { printf("multiply\n"); }
{DIVIDE}    { printf("divide\n"); }
{INUM}      { printf("inum\n"); }
{FNUM}      { printf("fnum\n"); }
\n          { /* Ignorar saltos de línea */ }
[ \t]       { /* Ignorar espacios */ }
.           { printf("unknown character: %s\n", yytext); }
%%
int main() {
    yylex();
    return 0;
}
