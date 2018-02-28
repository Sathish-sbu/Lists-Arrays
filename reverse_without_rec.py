def reverse(list1, s, e):
  while s < e:
    list1[s], list1[e] = list1[e], list1[s]
    s += 1 
    e -= 1 
    
  return list1
  
list1 = [9,8,7,6,5,4]
print (list1)
print (reverse(list1, 0 , len(list1)-1))
