#Palindrome.....
def ispal(number):
    return number == number[::-1]
print("Palindrome") if ispal(input()) == True else print("Not a Palindrome")
'''
INPUT - 12321
OUTPUT - Palindrome
INPUT - 12345
OUTPUT - Not a Palindrome
'''
