import re

n = int(input())

for i in range(n):
    s = input()
    # check if it matches the pattern
    if re.match(r'^[6789]\d{9}$', s):
        print("YES")
    else:
        print("NO")
