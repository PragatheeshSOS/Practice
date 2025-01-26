#Password Is Strong Or Not.......
given = input()
print("Your Password is Strong" if len(given)>= 8 and any(i.islower() for i in given) and any(i.isupper() for i in given) and any(i.isdigit() for i in given) and any(not i.isalnum() for i in given) else "Your Password is Not Strong")
'''
INPUT:
rakesh@1995kumar
OUTPUT:
Your Password is Not Strong

INPUT:
%ba7RNFm
OUTPUT:
Your Password is Strong
'''
