import MeCab
from pathlib import Path

def tokenize(text,hinshi):
    mecab = MeCab.Tagger()
    nodes = mecab.parseToNode(text)
    tokens = []
    
    while nodes:
        if nodes.surface != "": # 品詞情報を取得（最初のカンマまでが品詞大分類）
            pos = nodes.feature.split(',')[0]
            
            # 対象となる品詞の場合のみtokensに追加
            if pos in hinshi:
                tokens.append(nodes.surface)
        nodes = nodes.next
    return tokens


def tokenize_other(text):
    mecab = MeCab.Tagger()
    nodes = mecab.parseToNode(text)
    tokens = []
    
    # 抽出したい品詞のリスト
    target_pos = ['名詞', '動詞', '形容詞', '副詞', '助詞', '助動詞']
    
    while nodes:
        if nodes.surface != "": # 品詞情報を取得（最初のカンマまでが品詞大分類）
            pos = nodes.feature.split(',')[0]
            
            # 対象となる品詞の場合のみtokensに追加
            if not (pos in target_pos):
                tokens.append(nodes.surface)
        nodes = nodes.next
    return tokens


# 入出力ファイルのパスを設定
name = input("book name -> ")
input_path = Path(f'texts/cleaned_{name}.txt')
output_path_meishi = Path(f'texts/tokenized_meishi_{name}.txt')
output_path_doushi = Path(f'texts/tokenized_doushi_{name}.txt')
output_path_keiyoushi = Path(f'texts/tokenized_keiyoushi_{name}.txt')
output_path_hukushi = Path(f'texts/tokenized_hukushi_{name}.txt')
output_path_others = Path(f'texts/tokenized_others_{name}.txt')


#トークンに分割
text = input_path.read_text(encoding='utf-8')

# 名詞のみ抽出
tokens = tokenize(text,['名詞'])
text_tokenized = ' '.join(tokens)
output_path_meishi.write_text(text_tokenized, encoding='utf-8')

# 動詞のみ抽出
tokens = tokenize(text,['動詞'])
text_tokenized = ' '.join(tokens)
output_path_doushi.write_text(text_tokenized, encoding='utf-8')

# 形容詞のみ抽出
tokens = tokenize(text,['形容詞'])
text_tokenized = ' '.join(tokens)
output_path_keiyoushi.write_text(text_tokenized, encoding='utf-8')

# 副詞のみ抽出
tokens = tokenize(text,['副詞'])
text_tokenized = ' '.join(tokens)
output_path_hukushi.write_text(text_tokenized, encoding='utf-8')

# 記号を抽出
tokens = tokenize_other(text)
text_tokenized = ' '.join(tokens)
output_path_others.write_text(text_tokenized, encoding='utf-8')
