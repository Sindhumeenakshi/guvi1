i = input()
for a in i:
    if ord(b) > 64  and ord(a) < 88 or ord(a) > 96 and ord(a) < 120:
        print(chr(ord(a)+3),end='')
    else:
        print(chr(ord(a)+3-26),end='')
