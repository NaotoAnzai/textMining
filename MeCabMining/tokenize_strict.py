import MeCab
from pathlib import Path

# 入出力ファイルのパスを設定
input_path = Path('texts/cleaned_dogura.txt')
output_path = Path('texts/tokenized_strict_dogura.txt')

def tokenize(text):
    mecab = MeCab.Tagger()
    nodes = mecab.parseToNode(text)
    tokens = []
    
    # 抽出したい品詞のリスト
    target_pos = ['名詞', '動詞', '形容詞']
    
    while nodes:
        if nodes.surface != "": # 品詞情報を取得（最初のカンマまでが品詞大分類）
            pos = nodes.feature.split(',')[0]
            
            # 対象となる品詞の場合のみtokensに追加
            if pos in target_pos:
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