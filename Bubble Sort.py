x1=open('input2.txt','r')
x2=open('output2.txt','w')
x3=int(x1.readline())
x4=str(x1.readline())
arr=x4.split(" ")
def bubbleSort():
    hum=False
    for i in range(x3-1):
        if int(arr[i])>int(arr[i+1]):
            hum=True
            break
    if hum==True:
        for i in range(x3-1):
            for j in range(x3-i-1):
                if int(arr[j]) > int(arr[j+1]):
                    arr[j], arr[j+1] = int(arr[j+1]), int(arr[j])
    for k in arr:
        x2.write(str(k)+' ')
bubbleSort()