x1=open('input4.txt','r')
x2=open('output4.txt','w')
x3=int(x1.readline())
l1=[0]*x3
for i in range(x3):
    x4=x1.readline().strip()
    x5=x4.split(' ')
    x6=((x5[0],x5[-1],x5[-3]))
    l1[i]=x6
def selection_sort(l1):
    for i in range(x3):
        idx=i
        for j in range(i+1,x3):
            if l1[j][0]<l1[idx][0]:
                l1[idx],l1[j]=l1[j],l1[idx]
            if l1[j][0]==l1[idx][0]:
                if l1[j][1]>l1[idx][1]:
                    l1[idx], l1[j] = l1[j], l1[idx]
selection_sort(l1)
for k in range (x3):
    x2.write(f'{l1[k][0]} will departure for {l1[k][2]} at {l1[k][1]}\n')