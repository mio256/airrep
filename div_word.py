from janome.tokenizer import Tokenizer

def hanya(s):
    if 'はにゃ' in s:
        print('はにゃってる',end='')
    else:
        print('はにゃってない',end='')

def search_word(s1,s2):
    l1=[]
    l2=[]

    t = Tokenizer()

    for token in t.tokenize(s1):
        l1.append(token.surface)

    for token in t.tokenize(s2):
        l2.append(token.surface)
    
    hanya(s1)
    print(l1)
    hanya(s2)
    print(l2)

s1='すもももももももものうち'
s2='はにゃ君はジムラボで講演するくらいだから面構えが違う'

search_word(s1,s2)