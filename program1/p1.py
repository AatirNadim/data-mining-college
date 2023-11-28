strs = ''
with open('text.txt', 'r') as f:
  strs = f.read()

map = {}

for str in strs.split(' ') :
  if(map.get(str) == None) :
    map[str] = 1
  else :
    map[str] += 1


print(map)

ls = []

for item in map.items() :
  ls.append(item)

print(ls)

sorted_ls = sorted(ls, key=lambda x : x[1], reverse=True)

print(sorted_ls)