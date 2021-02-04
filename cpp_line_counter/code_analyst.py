# coding=utf-8
# code_analyst.py

# !/usr/bin/env python3
# _*_ coding: utf-8 _*_


import os
import sys
import prettytable as pt


# set of file types
CPP_SUFFIX_SET = {'.h', '.hpp', '.hxx', '.c', '.cpp', '.cc', '.cxx'}

"""
this function depends package PrettyTable，
please use command "sudo pip3 install PrettyTable" to install.
"""
table = pt.PrettyTable()

# global variable
# code, blank, comment, total_lines
total_lines = [0, 0, 0, 0]
sub_folder_lines = [0, 0, 0, 0]
# max traverse depth
max_depth = 1
cur_depth = 0


def count_lines(file_path):
    """
    calc file 'file_path' lines num, and count to global variable according to file type
    """
    global CPP_SUFFIX_SET
    global total_lines, sub_folder_lines
    is_block_comment = False
    # code, blank, comment, total_lines
    temp_count = [0, 0, 0, 0]

    # calc file line num
    suffix = os.path.splitext(file_path)[-1]
    if suffix in CPP_SUFFIX_SET:
        #print("file: %s" % file_path)
        with open(file_path, 'rb') as file:
            for line in file.readlines():
                line = line.strip()

                if line == b'' and not is_block_comment:
                    temp_count[1] += 1
                elif line.startswith(b'//') or \
                     (line.startswith(b'/*') and line.endswith(b'*/')) or \
                     (is_block_comment and not line.endswith(b'*/')):
                    temp_count[2] += 1
                elif line.startswith(b'/*') or line.endswith(b'*/'):
                    is_block_comment = not is_block_comment
                    temp_count[2] += 1
                else:
                    temp_count[0] += 1
                temp_count[3] += 1

            #print("file %s: code %4d, blank %4d, comment %4d, total lines %4d" % (file_path, temp_count[0], temp_count[1], temp_count[2], temp_count[3]))
            # print("file: %s, count is %4d" % (file_path, temp_count[3]))
        total_lines[0] += temp_count[0]
        total_lines[1] += temp_count[1]
        total_lines[2] += temp_count[2]
        total_lines[3] += temp_count[3]
        sub_folder_lines[0] += temp_count[0]
        sub_folder_lines[1] += temp_count[1]
        sub_folder_lines[2] += temp_count[2]
        sub_folder_lines[3] += temp_count[3]
    else:
        pass


def list_files(path):
    """
    Recursively traverse all files of the project path, calc every file line number.
    """
    file_names = os.listdir(path)
    global sub_folder_lines, cur_depth, max_depth
    # print("current path [%s] depth is %d." % (path, cur_depth))
    sub_folder_lines = [0, 0, 0, 0]
    if cur_depth == 0:
        print("root: %s\n" % path)

    for f in file_names:
        file_path = os.path.join(path, f)
        if os.path.isfile(file_path):
            count_lines(file_path)
        if os.path.isdir(file_path) & (cur_depth < max_depth):
            cur_depth += 1
            list_files(file_path)
    if cur_depth:
        table.add_row([path, sub_folder_lines[0], sub_folder_lines[1], sub_folder_lines[2], sub_folder_lines[3]])
    cur_depth -= 1


if __name__ == '__main__':
    table.field_names = ['PATH', 'CODES', 'BLANKS', 'COMMENTS', 'LINES']
    if len(sys.argv) != 2:
        print("Usage : python3 code_analyst.py project_path")
    else:
        project_path = sys.argv[1]
        print("project path: %s" % project_path)
        list_files(project_path)
        table.add_row([project_path, total_lines[0], total_lines[1], total_lines[2], total_lines[3]])
        print(table)

