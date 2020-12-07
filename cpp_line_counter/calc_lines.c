#include "calc_lines.h"

#define TRUE    1
#define FALSE   0

/*
 * parameter:
 *     line: calc target;
 *     isBlockComment: whether the line is in the block comment.
 * return line_type: reference macro definition
 */
unsigned int calc_lines_cpp(char *line, unsigned char is_block_comment[2]) {
    unsigned int line_type = LINE_TYPE_BLANK;

    unsigned int index = 0;
    unsigned char is_line_comment = FALSE;
    while(line[index] != '\0') {
        if(line[index] == ' ' || line[index] == '\t') {  //blank symbol
            index += 1; continue;
        }
        else if(line[index] == '/' && line[index+1] == '/') { //line comment
            is_line_comment = TRUE;
            line_type |= LINE_TYPE_COMMENT; index += 1; //skip'/'
        }
        else if(line[index] == '/' && line[index+1] == '*') { //begin symbol of block comments
            is_block_comment[0] = TRUE;
            line_type |= LINE_TYPE_COMMENT; index += 1;
        }
        else if(line[index] == '*' && line[index+1] == '/') { //end symbol of block comments
            is_block_comment[0] = FALSE;
            line_type |= LINE_TYPE_COMMENT; index += 1;
        }
        else {
            if(is_line_comment || is_block_comment[0])
                line_type |= LINE_TYPE_COMMENT;
            else
                line_type |= LINE_TYPE_CODE;
        }
        index += 1;
    }

    return line_type;   //Bitmap：00 blank，01 code，10 comment，11 code and comment
}

