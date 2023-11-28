orig = {}

min_support = 3

res_pairs = []

tokens = []
itr_tokens = []

c1 = {}

def key_present(s : str, lis : list) :
  for itr in lis : 
    val1 = sorted(itr)
    val2 = sorted(s)
    if val1 == val2 :
      return True
  return False

def merge_possible(s1 : str, s2 : str) :
  if len(s1) == 1 and len(s2) == 1 :
    return True
  for itr in s1 :
    if itr in s2 :
      return True
  return False
  pass

def merge_func(s1 : str, s2 : str) :
  res = ''
  for itr in s1 : 
    if itr not in res : 
      res = res + itr
  for itr in s2 :
    if itr not in res :
      res = res + itr
  return res
  pass

def get_c1() :
  for token in tokens :
    temp = 0
    for key in orig.values() : 
      if token in key :
        temp += 1
    c1[token] = temp
  pass

def present(s : str, lis : list) :
  for itr in s :
    if itr not in lis :
      return False
  return True
  pass

def get_freq(s : str) :
  temp = 0
  for lis in orig.values() :
    if present(s, lis) :
      temp = temp + 1
  return temp

  pass

def get_cn( dic : dict ) :
  res = {}
  keys = list(dic.keys())
  for i in range(len(keys)) :
    for j in range(i + 1, len(keys), 1) : 
      if not merge_possible(keys[i], keys[j]) :
        continue
      to_search = merge_func(keys[i], keys[j])
      if key_present(to_search, list(res.keys())) :
        continue
      fr = get_freq(to_search)
      res[to_search] = fr
  return res
  pass

# freq less than abs support, prune

def get_ln(dic : dict) :
  print('cn value --> ', dic)
  res = {}
  for itr in dic.items() :
    # print(itr)
    if itr[1] >= min_support :
      res[itr[0]] = itr[1]

  print('corresponding ln --> ', res)
  return res

def str_in_str(s1 : str, s2 : str) :
  # print('s1 --> ', s1, 's2 --> ', s2)
  for itr in s1 :
    if itr not in s2 :
      return False
  return True

def get_result(res_pairs : list) :
  res = []
  for i in range(len(res_pairs)) :
    temp = True
    for j in range(i + 1, len(res_pairs), 1) :
      if str_in_str(res_pairs[i], res_pairs[j]) :
        temp = False
        break
    if temp : 
      res.append(res_pairs[i])
  return res


def split_func(s : str) :
  val = s.split(',')
  val[-1] = val[-1].strip()
  for itr in val :
    if itr not in tokens :
      tokens.append(itr)
  return val

with open ('./text.txt') as file : 
  for line in file : 
    temp = line.split(' ')
    orig[temp[0]] = split_func(temp[1])

itr_tokens = tokens

get_c1()

# print('orig --> ', orig)

# print(c1)

# print(get_ln(c1))

# print(c1)
cn = get_ln(c1)
# print('ln value --> ', cn)
while len(cn) > 0 : 
  cn = get_ln(get_cn(cn))
  # print('ln value --> ', cn)
  for itr in cn.keys() :
    if itr not in res_pairs :
      res_pairs.append(itr)


print(res_pairs)

print(get_result(res_pairs))


# print(orig)
# print(tokens)