import re
import sys

lines = sys.stdin.read().splitlines()  
t=int(lines[0])  
p=lines[1:t+1]  

for i in p:
    try:
        re.compile(i)
        print("True")
    except re.error:
        print("False")