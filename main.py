# coding=utf-8
from passwd_dict import Generate_pwd_dict
import sys

if __name__ == '__main__':
    if len(sys.argv) == 2:
        pwd_dict = Generate_pwd_dict(sys.argv[1])
        pwd_dict.generate()
    else:
        print("只能输入一个参数!")
        sys.exit(-1)
