x1=open('input5.txt','r')
x2=open('output5.txt','w')
x3=x1.readline()
x4=x1.readline().split(' ')
l1=[0]*int(x3)
for k in range(int(x3)):
    l1[k]=int(x4[k])
def quick_sort_algo(A,p,r):
    if p<r:
        q=Partition(A,p,r)
        quick_sort_algo(A,p,q-1)
        quick_sort_algo(A,q+1,r)
def Partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1
quick_sort_algo(l1,0,len(l1)-1)
for k in range(int(x3)):
    x2.write(f'{str(l1[k])} ')
