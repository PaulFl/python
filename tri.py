def selection(t):
    for i in range(1, len(t)):
        iMax = 0
        max = t[0]
        for j in range(len(t)-i+1):
            if t[j]>max:
                max = t[j]
                iMax = j
        t[iMax], t[-i] = t[-i], t[iMax]
        
def insertion(t):
    for i in range(1, len(t)):
        x = t[i]
        j = i-1
        while(x < t[j] and j>=0):
            t[j+1]=t[j]
            j -=1
        t[j+1] = x
        
def partition(t, i, j):
    pivot = t[i]
    k = i+1
    for l in range(i+1, j+1):
        if t[l] < pivot:
            t[l], t[k] = t[k], t[l]
            k+=1
    t[i], t[k-1] = t[k-1], pivot
    return k-1

def rapide(t, i, j):
    if j-i > 1:
        pivot = partition(t,i,j)
        rapide(t, i, pivot -1)
        rapide(t, pivot +1, j)
        
def fusion(t1, t2):
    u = [0]*(len(t1)+len(t2))
    i = 0
    j = 0
    while (i < len(t1) and j < len(t2)):
        if t1[i]>t2[j]:
            u[i+j] = t2[j]
            j+= 1
        else:
            u[i+j] = t1[i]
            i += 1
    if i == len(t1):
        for k in range(j, len(t2)):
            u[i+k] = t2[k]
    else:
        for k in range(i, len(t1)):
            u[j+k] = t1[k]
    return u

def triFusion(t):
    if len(t) > 1:
        m = len(t)//2
        t1 = triFusion(t[0:m])
        t2 = triFusion(t[m:len(t)])
        return fusion(t1,t2)
    else:
        return t

    
    
t = [8,5,4,2,1,3,5,8,8,5,0,1,2,4,9]