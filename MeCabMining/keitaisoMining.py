import MeCab
def tokenize(text):
    mecab = MeCab.Tagger()
    nodes = mecab.parseToNode(text)
    tokens = []
    while nodes:
        if nodes.surface != "":
            tokens.append(nodes.surface)
        nodes = nodes.next
    return tokens

#トークンに分割
text = open('cleaned_dogura.txt', 'r', encoding='utf-8').read()
tokens = tokenize(text)

#結果をresult.pyに保存
with open('result.py', 'w', encoding='utf-8') as f:
    f.write('tokens = ' + repr(tokens))
