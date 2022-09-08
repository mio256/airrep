from janome.tokenizer import Tokenizer

t = Tokenizer()

s = 'すもももももももものうち'

print(s)

print(type(t.tokenize(s)))

print(type(t.tokenize(s).__next__()))

for token in t.tokenize(s):
    print(token.surface)