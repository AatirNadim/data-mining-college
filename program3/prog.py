docs = []

stop_words = []
params = []


def process_word(word):
  symbols = ['.', ',', '?', '!', ':', ';', '"', "'", '(', ')' , '{', '}', '[', ']', '-', '_', '+', '=', '/']
  # print(word)
  if(word[0] in symbols) :
    word = word[1:]
  
  if(word[-1] in symbols) :
    word = word[:-1]
  return word

for i in range(5):
  with open(f'doc{i+1}.txt') as file_in:
    docs.append(file_in.read())


def get_cosine(tokens, ) :

  pass

def clean(lis) :
  temp = []
  for word in lis :
    if len(word) == 0 : 
      continue
    val = process_word(word)
    if len(val) > 0:
      temp.append(val)
  return temp


def get_similarity(str1, str2, params, res_tuples) :
  tokens = {}
  # str1 = 
  str1 = clean(str1.split(' '))
  str2 = clean(str2.split(' '))
  
  
  

  # str1 = temp
  for word in str1 :
    # if len(word) == 0 : 
    #   continue
    # val = process_word(word)
    if len(word) > 0 :
      if word in tokens :
        tokens[word] += 1
      else :
        tokens[word] = 1
    
   
  for word in str2 :
    if len(word) > 0 :
      if word in tokens :
        tokens[word] += 1
      else :
        tokens[word] = 1
      
  vec1 = get_vector(tokens, str1)
  print(tokens, '\n')



  pass

# for doc in docs:
#   print(doc)

with open('stopWords.txt') as file_in:
  stop_words = file_in.read().splitlines()

# print(stop_words)

# tokens = []
for doc in docs:
  for word in doc.split(' '):
    if word not in stop_words and word not in params and len(word) > 0:
      params.append(process_word(word))

res_tuples = []

for i in range(len(docs)) :
  for j in range(i+1, len(docs)) :
    get_similarity(docs[i], docs[j], params, res_tuples)


# res_tuples = sorted(res_tuples, lambda x: x[0], reverse=True)



