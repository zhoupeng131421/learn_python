#~/user/bin/python3

import sys
import xml.sax
from docx import Document
# maybe need to install the python-docx lib use command: pip3 install python-docx

ROWs = []


class testcaseHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.id = ""
        self.tracefrom = ""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "testcase":
            self.id = attributes["id"]

    def endElement(self, tag):
        self.CurrentData = ""
    
    def characters(self, content):
        global ROWs
        ROW = []
        isExist = False
        if self.CurrentData == "tracefrom":
            self.tracefrom = content
            for row in ROWs:
                if row[0] == self.tracefrom:
                    s1 = ""
                    seq = (row[2], '\n', self.id)
                    row[2] = s1.join(seq)
                    isExist = True
            if not isExist:
                ROW.append(self.tracefrom)
                ROW.append('test')
                ROW.append(self.id)
                ROWs.append(ROW)


def main():
    global ROWs
    document = Document()
    len_rows = 0

    ROWs.append(['Requirement', 'Proof', 'Analyses/Test cases'])

    if len(sys.argv) != 2:
        print("Usage : python3 parse_reqs_from_xml.py xml_file_path")
    else:
        xml_path = sys.argv[1]

    parse = xml.sax.make_parser()
    parse.setFeature(xml.sax.handler.feature_namespaces, 0)

    Handler = testcaseHandler()
    parse.setContentHandler(Handler)
    parse.parse(xml_path)

    len_rows = len(ROWs)
    table = document.add_table(rows = len_rows, cols = 3)
    table.style = 'TableGrid'
    index_row = 0
    for row in ROWs:
        index_cell = 0
        for cell in row:
            table.rows[index_row].cells[index_cell].text = cell
            index_cell += 1
        index_row += 1
    document.save(xml_path + '.docx')


if (__name__ == "__main__"):
    main()