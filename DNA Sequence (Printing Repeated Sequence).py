# DNA Sequence (Printing Repeated Sequence)..................
gene = input()
dic = {}
for i in range(len(gene)-9):
    sub = gene[i:i+10]
    if sub not in dic:
        dic[sub] = 1
    else:
        dic[sub]+=1
[print(i) for i,j in dic.items() if j>1]
'''
INPUT:
ACGAATTCCGACGAATTCCG
OUTPUT:
ACGAATTCCG

INPUT:
AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT
OUTPUT:
AAAAACCCCC
CCCCCAAAAA
'''
