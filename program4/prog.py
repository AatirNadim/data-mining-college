# associate que with ans and dict of words with frequency,
def process_text(word) :
  symbols = ['.', ',', '?', '!', ':', ';', '"', "'"]
  if(word[0] in symbols) :
    word = word[1:]
  if(word[-1] in symbols) :
    word = word[:-1]
  return word
  pass

def get_freq(que : str) :
  words = que.split(' ')
  temp = []
  for word in words :
    temp.append(process_text(word).lower())
  words = temp
  dic = {}
  for word in words :
    if word in dic :
      dic[word] += 1
    else :
      dic[word] = 1
  # print(dic)
  return dic
  # pass


def cosine_sim(vec1, vec2) :
  sum1 = 0
  sum2 = 0
  sum3 = 0
  for i in range(len(vec1)) :
    a = vec1[i]
    b = vec2[i]
    sum1 += a*a
    sum2 += b*b
    sum3 += a*b
  # print(sum1**0.5, sum2**0.5, sum3)
  return (sum3/((sum1**0.5)*(sum2**0.5)))


def get_vector(dic, tokens) :
  res = []
  for token in tokens :
    if token in dic.keys() :
      res.append(dic[token])
    else :
      res.append(0)
  return res
  pass

def get_sim(que_map_ans, que_dict, que1, input_dict, res_pairs) :
  dic1 = que_dict[que1]
  # print(inp_dict)

  tokens = []
  for word in dic1.keys() :
    if word not in tokens :
      tokens.append(word)
  
  for word in input_dict.keys() :
    if word not in tokens :
      tokens.append(word)

  # print(tokens)
  vec1 = get_vector(dic1, tokens)
  vec2 = get_vector(input_dict, tokens)
  cos_sim = cosine_sim(vec1, vec2)
  # print(vec1)
  # print(vec2)
  # print(cos_sim)
  res_pairs.append([cos_sim, que_map_ans[que1]])
  # for que in dic2.keys() :
  #   print(que)
  pass


que_dict = {}
que_map_ans = {}
val = []
inp = None
with open ('./text.txt') as file : 
  inp = file.read()

inp = inp.split('\n')
# print(inp.split('\n'))

for i in range(0, len(inp), 3) :
  # print(inp[i])
  q = inp[i]
  a = inp[i+1]
  
  que_map_ans[q] = a

# print(que_map_ans)

for i in que_map_ans.keys() :
  que_dict[i] = get_freq(i)

# print(que_dict)

inp_que = input('Give the new question: ')
# print(inp_que)

inp_dict = get_freq(inp_que)

res_pairs = []

for que in que_map_ans.keys() :
  get_sim(que_map_ans=que_map_ans, que_dict=que_dict, que1=que, input_dict=inp_dict, res_pairs=res_pairs)

res_pairs = sorted(res_pairs, key=lambda x: x[0], reverse=True)

for p in res_pairs :
  print(p)

