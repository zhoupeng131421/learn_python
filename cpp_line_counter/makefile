#######################
# Makefile
#######################

# SOURCE
SOURCE		:= calc_lines.c

# compile and lib parameter
CC			:= gcc
LD			:= ld
LIBS		:=
LDFLAGS		:=
DEFINES		:=
INCLUDE		:= -I.
CFLAGS		:=
CXXFLAGS	:=

TARGET_LIB_DLL 		:= calc_lines.dll
TARGET_LIB_SO		:= calc_lines.so

all:
	$(CC) -shared -o $(TARGET_LIB_DLL) $(SOURCE)
	$(CC) $(SOURCE) -fPIC -shared -o $(TARGET_LIB_SO)

# clean
clean:
	rm -fr *.o
	rm -rf *.dll
	rm -rf *.so
