#!/usr/bin/python3
if __name__ == "__main__":
   import sys
   sum_Arg = 0
   for i in range(len(sys.argv) - 1):
       sum_Arg += int(sys.argv[i + 1])
   print(sum_Arg)
