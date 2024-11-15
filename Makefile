lex_analyzer: lex_analyzer.l
	flex lex_analyzer.l
	gcc lex.yy.c -o lex_analyzer -ll
