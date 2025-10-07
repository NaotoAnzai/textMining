import MeCab
from pathlib import Path

# 入出力ファイルのパスを設定
input_path = Path('texts/cleaned_dogura.txt')
output_path = Path('texts/tokenized_dogura.txt')

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
text = input_path.read_text(encoding='utf-8')
tokens = tokenize(text)

# スペース区切りでトークンを結合
text_tokenized = ' '.join(tokens)

# 結果を保存
output_path.write_text(text_tokenized, encoding='utf-8')