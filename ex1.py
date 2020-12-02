a=int(input())
b=int(input())
c=int(input())
d=int(input())
def min_doub(a,b,c,d):
    m=min(a,b)
    k=min(c,d)
    return(min(m,k))
print(min_doub(a,b,c,d))