def merge_func(s1 : str, s2 : str) :
  res = ''
  for itr in s1 : 
    if itr not in res : 
      res = res + itr
  for itr in s2 :
    if itr not in res :
      res = res + itr
  return res

print(merge_func('aatir', 'nadim'))