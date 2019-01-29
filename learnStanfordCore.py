from nltk.parse.stanford import StanfordParser

eng_parser = StanfordParser()
print(list(eng_parser.parse("the quick brown fox jumps over the lazy dog".split())))
