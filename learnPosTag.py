import nltk

text = nltk.word_tokenize('This beautiful future is just his imagination so far')
print(nltk.pos_tag(text, tagset='universal'))