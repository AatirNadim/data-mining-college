sorted_pairs = []

def getDiff(par1, par2, key1, key2) :
  num1 = 0
  num2 = 0
  num3 = 0
  for i in range(len(par1)):
    v1 = par1[i]
    v2 = par2[i]
    if(v1 == 'NA'):
      v1 = 1 if v2 == '2' else 2
    if(v2 == 'NA'):
      v2 = 1 if v1 == '2' else 2
    v1 = float(v1)
    v2 = float(v2)
    num1 += v1*v2
    num2 += v1*v1
    num3 += v2*v2
    # print(v1, v2, key1, key2)
  # print(key1, key2, num1/(num2**0.5*num3**0.5))
  sorted_pairs.append((key1, key2, num1/(num2**0.5*num3**0.5)))

lines = []
# format
# name --> [p1, p2,.. pn]

vectors = {}

with open('animal.txt') as file_in:
  for line in file_in:
    lines.append(line)

# print(lines)

# for line in lines:
#   print(line.split(','))

for i in range(1, len(lines)) :
  line = lines[i]
  line = line.split(',')
  name = line[0][1:-1]
  vector = line[1:]
  vector[-1] = vector[-1].strip()
  vectors[name] = vector

# for item in vectors.items():
#   print(item)

done_keys = []

for key1 in vectors.keys():
  done_keys.append(key1)
  for key2 in vectors.keys():
    if(key2 in done_keys) :
      continue
      # print(vectors[key], vectors[key])
      # print(cosine_similarity(vectors[key], vectors[key]))
    getDiff(vectors[key1], vectors[key2], key1, key2)


sorted_pairs = sorted(sorted_pairs, key=lambda x: x[2], reverse=True)

for item in sorted_pairs:
  print(item)
