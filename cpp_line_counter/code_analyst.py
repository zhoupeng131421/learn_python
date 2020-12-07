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
cpp_lines = 0
sub_folder_lines = 0
# max traverse depth
max_depth = 1
cur_depth = 0


def count_lines(file_path):
    """
    calc file 'file_path' lines num, and count to global variable according to file type
    """
    global CPP_SUFFIX_SET
    global cpp_lines, sub_folder_lines

    # calc file line num
    suffix = os.path.splitext(file_path)[-1]
    if suffix in CPP_SUFFIX_SET:
        with open(file_path, 'rb') as file:
            cnt = 0
            for line in file:
                cnt += 1
            # print("file: %s, count is %4d" % (file_path, cnt))
        cpp_lines += cnt
        sub_folder_lines += cnt
    else:
        pass


def list_files(path):
    """
    Recursively traverse all files of the project path, calc every file line number.
    """
    file_names = os.listdir(path)
    global sub_folder_lines, cur_depth, max_depth
    # print("current path [%s] depth is %d." % (path, cur_depth))
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
        table.add_row([path, sub_folder_lines])
    sub_folder_lines = 0
    cur_depth -= 1


if __name__ == '__main__':
    table.field_names = ['PATH', 'LINES']
    if len(sys.argv) != 2:
        print("Usage : python3 code_analyst.py project_path")
    else:
        project_path = sys.argv[1]
        print("project path: %s" % project_path)
        list_files(project_path)
        table.add_row([project_path, cpp_lines])
        print(table)

