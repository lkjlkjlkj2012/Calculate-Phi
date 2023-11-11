list=[1,1]
n=int(input())
print('1\n1')
phi=list[-1]/list[-2]
print('phi:',phi)
for i in range(n-2):
    list.append(list[-1]+list[-2])
    print(list[-1])
    phi=list[-1]/list[-2]
    print('phi:',phi)
n=input()
