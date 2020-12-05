word1='Hello world'
word2='HERD'
word2_lower=word2.lower()
for i,e in enumerate(word1, 1):
    if e.lower() in word2_lower:
        ind=word2_lower.index(e.lower())
        print(f'{i} символ встречается в строке поиска: {word2_lower[:ind]+word2_lower[ind].upper()+word2_lower[ind+1:]}')