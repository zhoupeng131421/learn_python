#!/usr/bin/python
# _*_ coding: UTF-8 _*_

import sys
import os
import docx
import prettytable as pt


# conf file name
CONF_INI = "get_title.ini"

# rules at every element
titles = []

TABLE = pt.PrettyTable()

def get_tab_title():
    global titles
    script_path = os.path.dirname(os.path.abspath(__file__))
    conf_file = os.path.join(script_path, CONF_INI)
    if os.path.exists(conf_file):
        fd = open(conf_file, 'r')
        for line in fd.readlines():
            titles.append(line)
    else:
        print("There no have config file for rules, please check!")

    for title in titles:
        print(title)


def compare_title_for_table(table):
    global TABLE
    ROW = []
    for row in table.rows:
        for title in titles:
            #print("title: ", title.strip(), ", row: ", row.cells[0].text.strip())
            if title.strip() == row.cells[0].text.strip():
                ROW.append(row.cells[1].text.strip())

    if (3 == len(ROW)):
        TABLE.add_row(ROW)


def match_doc(target_doc):
    document = docx.Document(target_doc)
    tables = document.tables
    print("table num: ", len(tables))
    for table in tables:
        #print(len(table.rows))
        compare_title_for_table(table)


def main():
    global TABLE
    TABLE.field_name = ['Test case identifier', 'Title', 'Description']

    # get target document path
    argc = len(sys.argv)
    if argc >= 2:
        target_doc = os.path.abspath(sys.argv[1])
        print("target document is: ", target_doc)
    else:
        print("There no have parameter about target document, please check your input.")

    # get rule config
    get_tab_title()

    # process the doc file
#    match_doc(target_doc)
    match_doc(sys.argv[1])

    TABLE.align = 'l'
    TABLE.padding_width = 0
    print(TABLE)

if __name__ == '__main__':
    main()
