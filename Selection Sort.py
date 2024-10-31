x1=open('input3.txt','r')
x2=open('output3.txt', 'w')
x3=int(x1.readline())
x4=str(x1.readline()).strip()
arr_std=x4.split(' ')
mrk=str(x1.readline()).strip()
arr_mrk=mrk.split(' ')
dic={}
for i in range(x3):
    dic[arr_std[i]]=arr_mrk[i]
l1=list(dic.items())
def selection_sort(l1):
    for i in range(x3):
        max_idx=i
        for j in range(i+1,x3):
            if int(l1[j][1])>int(l1[max_idx][1]):
                l1[max_idx],l1[j]=l1[j],l1[max_idx]
            elif int(l1[j][1])== int(l1[max_idx][1]):
                if int(l1[j][0])<int(l1[max_idx][0]):
                    l1[j], l1[max_idx] = l1[max_idx], l1[j]
selection_sort(l1)
for k in range(x3):
    x2.write(f"ID:{l1[k][0]} Mark:{l1[k][1]}\n")