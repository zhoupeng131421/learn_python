import os
import sys


def rename(old_name, new_name, now_dir):
    files = os.listdir(now_dir)
    for filename in files:
        portion = os.path.splitext(filename)
        # 分离文件名字和后缀
        print(portion)

        if os.path.isdir(now_dir+'/'+portion[0]):
            print("cd son dir", now_dir+'/'+portion[0])
            rename(old_name, new_name, now_dir+'/'+portion[0])
        else:
            if portion[1] == old_name:  # 根据后缀来修改,如无后缀则空
                newname = portion[0] + new_name
                # 要改的新后缀
                os.rename(now_dir+'/'+filename, now_dir+'/'+newname)


def main():
    # get target dir path
    argc = len(sys.argv)
    if argc >= 2:
        target_dir = os.path.abspath(sys.argv[1])
        print("target document is: ", target_dir)
        rename(".rts", ".cpp", target_dir)
    else:
        print("There no have parameter about target document, please check your input.")

if __name__ == '__main__':
    main()
