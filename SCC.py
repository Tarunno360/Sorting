x1=open('input3.txt','r')
x2=open('output3.txt','w')
x3=x1.readline()
N=int(x3[0])
M=int(x3[2])
graph={}
for i in range(1,N+1):
    graph[i]=[]
for j in range(M):
    A,B=x1.readline().split()
    A=int(A)
    B=int(B)
    graph[A].append(B)
print(graph)
def defth_first_search(N,V,occ,ord):
    occ[V]=True
    for i in N[V]:
        if not occ[i]:
            defth_first_search(N,i,occ,ord)
    ord.append(V)
    print(ord)
    return ord
def transpose(N):
    new_graph={}
    for i in N:
        new_graph[i]=[]
    for i in N:
        for j in N[i]:
            new_graph[j].append(i)
    return new_graph
def SCC(graph,ord,ulta):
    occured={}
    for i in graph:
        occured[i]=False
    result_list=[]
    while ord==True:
        N=ord.pop()
        if occured[N]==False:
            new=[]
            defth_first_search(ulta,N,occured,new)
            result_list.append(new)
    for i in graph:
        if occured[i]==False:
            new=[]
            defth_first_search(ulta,i,occured,new)
            result_list.append(new)
    return result_list
trans=transpose(graph)
stack=[]
occured={}
for i in graph:
    occured[i]=False
dfs=defth_first_search(graph,1,occured,stack)
strong=SCC(graph,dfs,trans)
for i in range(len(strong)):
    for j in range(len(strong[i])):
        x2.write(f'{strong[i][j]} ')
    x2.write('\n')