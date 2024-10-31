x1=open('input1.txt','r')
x2=open('output1.txt','w')
x3=x1.readline()
x4=x1.readline().split(' ')
l1=[0]*int(x3)
for k in range(int(x3)):
    l1[k]=int(x4[k])
def merge_fun1(arr1, arr2):
  merged = []
  i, j = 0, 0
  while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
      merged.append(arr1[i])
      i += 1
    else:
      merged.append(arr2[j])
      j += 1
  merged.extend(arr1[i:])
  merged.extend(arr2[j:])
  return merged
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[:mid])
        a2 = mergeSort(arr[mid:])
        return merge_fun1(a1, a2)
x12=mergeSort(l1)
for i in range(int(x3)):
    x2.write(str(x12[i])+' ')


