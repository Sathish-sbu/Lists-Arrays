def reverse(list1):
  if len(list1) > 1 :
    return reverse(list1[1:]) + [list1[0]] 
  else:
    return list1
  
list1 = [9,8,7,6,5,4]
print (list1)
print (reverse(list1))
