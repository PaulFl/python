def tri_selection(t):
    n = len(t)
    for i in range(n-1, 0, -1):
        j = indice_max(t,i)
        t[j], t[i] = t[i], t[j]


def indice_max(t,i):
    j = 0
    for k in range(0, i+1):
        if t[k] > t[j]:
            j = k
    return j

def tri_insertion(t):
    n = len(t)
    for i in range(1,n):
        x = t[i]
        k = i
        while k >= 1 and t[k-1] > x:
            t[k] = t[k-1]
            k -= 1
        t[k] = x

def partition(t,i,j):
    pivot = t[i]
    k = i + 1
    for l in range(i+1, j+1):
        if t[l] < pivot:
            t[l], t[k] = t[k], t[l]
            k += 1
    t[i], t[k-1] = t[k-1], t[i]
    return k-1

def tri_rapide(t,i,j):
    if i < j:
        m = partition(t,i,j)
        tri_rapide(t,i,m-1)
        tri_rapide(t,m+1, j)

def fusion(t1, t2):
    u = [0]*(len(t1) + len(t2))
    i = j = 0
    while i < len(t1) and j < len(t2):
        if t1[i] <= t2[j]:
            u[i+j] = t1[i]
            i += 1
        else:
            u[i+j] = t2[j]
            j += 1
    if i == len(t1):
        for k in range(j, len(t2)):
            u[i+k] = t2[k]
    else:
        for k in range(i, len(t1)):
            u[j+k] = t1[k]
    return u

def tri_fusion(t):
    if len(t) <= 1:
        return t
    else:
        m = len(t)//2
        t1 = tri_fusion(t[:m])
        t2 = tri_fusion(t[m:])
        return fusion(t1, t2)