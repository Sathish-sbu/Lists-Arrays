# rotate a list using reverse   
def reverse(t,s,e):
    print s, e
    while s < e:
        t[s], t[e] = t[e], t[s]
        s += 1
        e -= 1

def rotate(arr,d):
    reverse(arr, 0,d-1)
    reverse(arr, d, len(arr)-1)
    reverse(arr, 0, len(arr)-1)
    return arr


arr = [1,2,3,4,5,6,7]
print (arr)
print rotate(arr,4)
