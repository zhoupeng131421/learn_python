import sys
import os
import time


# rawCountInfo store file lines, code lines, comments lines, block lines.
rawCountInfo = [0, 0, 0, 0, 0]
# detailCountInfo store current file info: lines, file name, all files lines.
detailCountInfo = []
# process file numbers
gProcFileNum = 0

# calculate c/c++ line type
def CalcLinesCh(line, isBlockComment):
    lineType, lineLen = 0, len(line)
    if not lineLen:
        return lineType

    line = line + '\n'  # 添加一个字符防止iChar+1时越界
    iChar, isLineComment = 0, False
    while iChar < lineLen:
        if line[iChar] == ' ' or line[iChar] == '\t':   # 空白字符
            iChar += 1; continue
        elif line[iChar] == '/' and line[iChar+1] == '/':  # 行注释
            isLineComment = True
            lineType |= 2; iChar += 1  # 跳过'/'
        elif line[iChar] == '/' and line[iChar+1] == '*':  # 块注释开始符
            isBlockComment[0] = True
            lineType |= 2; iChar += 1
        elif line[iChar] == '*' and line[iChar+1] == '/':  # 块注释结束符
            isBlockComment[0] = False
            lineType |= 2; iChar += 1
        else:
            if isLineComment or isBlockComment[0]:
                lineType |= 2
            else:
                lineType |= 1
        iChar += 1

    return lineType   # Bitmap：0空行，1代码，2注释，3代码和注释


def CalcLines(fileType, line, isBlockComment):
    try:
        if fileType is 'ch':  # is(同一性运算符)判断对象标识(id)是否相同，较==更快
            lineType = CalcLinesCh(line, bCmmtArr)
        else:
            pass



def SafeDiv(dividend, divisor):
    if divisor: return float(dividend)/divisor
    elif dividend: return -1
    else: return 0


def CountFileLines(filePath, isRawReport=True, isShortName=False):
    fileExt = os.path.splitext(filePath)
    if fileExt[1] == '.c' or fileExt[1] == '.h' or fileExt[1] == '.cpp':
        fileType = 'ch'
    else:
        return

    global gProcFileNum; gProcFileNum += 1
    sys.stderr.write('%d files processed...\r' % gProcFileNum)

    isBlockComment = [False]*2  #或定义为全局变量，以保存上次值
    lineCountInfo = [0]*5       #[代码总行数, 代码行数, 注释行数, 空白行数, 注释率]
    with open(filePath, 'r') as file:
        for line in file:
            lineType = CalcLines(fileType, line.strip(), isBlockComment)
            lineCountInfo[0] += 1
            if   lineType == 0:  lineCountInfo[3] += 1
            elif lineType == 1:  lineCountInfo[1] += 1
            elif lineType == 2:  lineCountInfo[2] += 1
            elif lineType == 3:  lineCountInfo[1] += 1; lineCountInfo[2] += 1
            else:
                assert False, 'Unexpected lineType: %d(0~3)!' %lineType

    if isRawReport:
        global rawCountInfo
        rawCountInfo[:-1] = [x+y for x, y in zip(rawCountInfo[:-1], lineCountInfo[:-1])]
        rawCountInfo[-1] += 1
    elif isShortName:
        lineCountInfo[4] = SafeDiv(lineCountInfo[2], lineCountInfo[2]+lineCountInfo[1])
        detailCountInfo.append([os.path.basename(filePath), lineCountInfo])
    else:
        lineCountInfo[4] = SafeDiv(lineCountInfo[2], lineCountInfo[2]+lineCountInfo[1])
        detailCountInfo.append([filePath, lineCountInfo])



def main():
    print("test")


if __name__ == '__main__':
    startTime = time.perf_counter()
    main()
    time.sleep(1)
    endTime = time.perf_counter()
    print('Time Elapsed: %.2f sec.' % (endTime - startTime))

