from janome.tokenizer import Tokenizer

def hanya(s):
    if 'はにゃ' in s:
        return True
    else:
        return False

def search_word(s1,s2):
    t = Tokenizer()

    l1=[token.surface for token in t.tokenize(s1)
       if token.part_of_speech.startswith('名詞')]

    l2=[token.surface for token in t.tokenize(s2)
       if token.part_of_speech.startswith('名詞')]
    
    print(l1)
    print(l2)

    if len(list(set(l1)&set(l2))) !=0:
        return True
    else:
        return False


s1='すもももももももものうち'
s2='もも君はジムラボで講演するくらいだから面構えが違う'

print(search_word(s1,s2))