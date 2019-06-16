a= input()
for J in a:
    if ord(J) > 64  and ord(J) < 88 or ord(J) > 96 and ord(J) < 120:
        print(chr(ord(J)+3),end='')
    else:
        print(chr(ord(J)+3-26),end='')
        
