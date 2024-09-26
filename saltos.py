from sys import argv

def recur(n):
    if n < 0: return 0
    if n == 0: return 1
    if str[n] == '0': return 0
    return recur(n-1) + recur(n-2) + (1 if n-3 == 0 else 0) + ((recur(n-4) + recur(n-5)) if n-3 > 0 and str[n-3] == '1' else 0)

# def recurMem(str):


# def noRecur(str):



str = argv[1]
print("Recursao simples:", recur(len(str)-1))
# print("Recursao memorizada:", recurMem(str))
# print("Sem recursao:", noRecur(str))