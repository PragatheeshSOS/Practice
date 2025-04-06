# String Reverse And Capitalize It. Except Number Both Complete And Incomplete String.....................
string = input().split()
for i in string:
    if i.isnumeric():
        print(i,end=" ")
    else:
        word = list(i)
        left,right = 0,len(word)-1
        while left<=right:
            if word[left].isalpha() and word[right].isalpha():
                word[left],word[right] = word[right],word[left]
                left+=1
                right-=1
            elif not word[left].isalpha():
                left+=1
            elif not word[right].isalpha():
                right-=1
        print("".join(word).capitalize(),end=" ")
'''
INPUT:
there are 26 alphabets in english
OUTPUT:
Ereht Era 26 Stebahpla Ni Hsilgne
INPUT:
I26t is not a digit 1234
OUTPUT:
T26i Si Ton A Tigid 1234
'''
