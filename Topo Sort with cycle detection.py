x1=open('input2.txt','r')
x2=open('output2.txt','w')
x3=x1.readline()
N=int(x3[0])
M=int(x3[2])
x11=x1.readlines()
L1=[]
graph={}
for i in range(len(x11)):
    A,B=int(x11[i][0]),int(x11[i][2])
    L1.append((A,B))
def cycle_detection():
    for i in range(len(L1)):
        if L1[i][0] not in graph:
            graph[L1[i][0]]=[L1[i][1]]
        else:
            graph[L1[i][0]].append(L1[i][1])
        if L1[i][1] in graph:
            return True
already=[False]*(N+1)
queue=[]
def topo_sort(graph):
    for i in graph:
        topo_fun(i)
    return queue
def topo_fun(elem):
    already[elem]=True
    if elem not in queue:
        queue.append(elem)
    j=sorted(graph[elem])
    for j in graph[elem]:
        if already[j]==False:
            already[j]=True
            queue.append(j)
if cycle_detection()==True:
    x2.write('IMPOSSIBLE')
else:
    new=topo_sort(graph)
    for i in range(len(new)):
        rmv_elem=new.pop(0)
        x2.write(f'{rmv_elem} ')
