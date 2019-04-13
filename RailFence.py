pt = "Steal like an artist"
key = pt.count(" ") + 1
a,i,z = 0,0,""
k = [[0]*len(pt) for _ in range(key)]
##print(k)

while(i < len(pt)):
    if (a==0):
        while (a<key-1 and i<len(pt)):
            k[a][i] = pt[i]
            a = a + 1
            i = i + 1
    elif (a==key-1):
        while (a>0 and i<len(pt)):
            k[a][i] = pt[i]
            a = a - 1
            i = i + 1

for q in k:
    print(q)

for j in k:
    for l in j:
        if l != 0:
            z += l
print(z)



def decrypt(z):
    d = [[0]*len(z) for _ in range(key)]
    i,index,space = -1,0,((2*key) - 2)
    while(index < key):
        start = index
        i = i + 1
        d[index][index] = z[i]
        if(index == 0 or index == key-1):
            while start < len(z):
                start = start + space
                if start < len(z):
                    i = i + 1
                    d[index][start] = z[i]
        else:
            while start < len(z):
                start = start + (space - (2*index))
                if start < len(z):
                    i = i + 1
                    d[index][start] = z[i]
                else:
                    break
                start = start + (2*index)
                if start < len(z):
                    i = i + 1
                    d[index][start] = z[i]
                else:
                    break
        index = index + 1

    for j in d:
        print(j)
    return d


decrypt(z)
