#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void parse(char* token) {
    if (strcmp(token, "floatdcl") == 0 || strcmp(token, "intdcl") == 0) {
        printf("Parsed declaration\n");
    } else if (strcmp(token, "id") == 0) {
        printf("Parsed identifier\n");
    } else if (strcmp(token, "assign") == 0) {
        printf("Parsed assignment\n");
    } else if (strcmp(token, "plus") == 0 || strcmp(token, "minus") == 0 || 
               strcmp(token, "multiply") == 0 || strcmp(token, "divide") == 0) {
        printf("Parsed operator\n");
    } else if (strcmp(token, "inum") == 0 || strcmp(token, "fnum") == 0) {
        printf("Parsed number\n");
    } else if (strcmp(token, "print") == 0) {
        printf("Parsed print statement\n");
    } else {
        printf("Syntax error: Unknown token '%s'\n", token);
        exit(1);
    }
}

int main(int argc, char** argv) {
    if (argc < 2) {
        printf("Usage: %s <tokens.out>\n", argv[0]);
        return 1;
    }

    FILE* file = fopen(argv[1], "r");
    if (!file) {
        perror("Error opening file");
        return 1;
    }

    char token[100];
    while (fscanf(file, "%s", token) != EOF) {
        parse(token);
    }

    fclose(file);
    return 0;
}
