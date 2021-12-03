print(ord('s') << 8)

with open('./enc') as f:
    contents = f.read()
    f.close()
str = []
for i in range(0, contents.__len__()):
    agg = ord(contents[i])
    first = agg >> 8
    str.append(chr(first))
    str.append(chr(agg-(first << 8)))

print(''.join(str))
