// calc_lines.h

#ifndef __CALC_LINES_H
#define __CALC_LINES_H

#include <stdio.h>
#include <string.h>

#define LINE_TYPE_BLANK				0x00
#define LINE_TYPE_CODE				0x01
#define LINE_TYPE_COMMENT			0x10
#define LINE_TYPE_CODE_AND_COMMENT	0x11

unsigned int calc_lines_cpp(char *line, unsigned char is_block_comment[2]);


#endif
