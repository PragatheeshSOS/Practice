# Highest Frequency Word In Sentence Without Using In-build Funcation............................................
string = input()
clear = ""
for i in string:
    if i.isalpha():
        clear+=i
    elif i == " ":
        clear+=" "
clear = clear.split()
stack = []
for i in clear:
    if i not in stack:
        stack.append(i)
    else:
        print(i)
        exit()
print(None)
'''
| Input                         | Result |
| ----------------------------- | ------ |
| Way to Way. I said Way to go! | Way    |
| What is this?                 | None   |
'''
