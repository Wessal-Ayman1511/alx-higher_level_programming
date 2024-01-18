#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_num = len(sys.argv) - 1
    sm = 0
    for i in range(arg_num):
        sm += int(sys.argv[i + 1])
    print("{}".format(sm))
