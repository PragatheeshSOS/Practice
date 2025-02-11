#Chessboard Cell Color....................
given = input()
alpha,number = given[0],int(given[1])
print("White") if ((ord(alpha)-ord('a')+1)+int(number))%2 else print("Black")
# print(ord(alpha)-ord('a')+1)
# print(number)
# print(number+(ord(alpha)-ord('a'))+1)
'''
INPUT:
a1
OUTPUT:
Black

INPUT:
b2
OUTPUT:
Black

INPUT:
a8
OUTPUT:
White
'''
