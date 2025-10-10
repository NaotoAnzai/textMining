from wordcloud import WordCloud
import matplotlib.pyplot as plt
from pathlib import Path

# 入力の作品名を指定
name = input("book name -> ")
# テキストファイルを読み込む
# 名詞のみ抽出したファイルを使用
input_path = Path(f'texts/tokenized_meishi_{name}.txt')
text_meishi = input_path.read_text(encoding='utf-8')
# 動詞のみ抽出したファイルを使用
input_path = Path(f'texts/tokenized_doushi_{name}.txt')
text_doushi = input_path.read_text(encoding='utf-8')
# 形容詞のみ抽出したファイルを使用
input_path = Path(f'texts/tokenized_keiyoushi_{name}.txt')
text_keiyoushi = input_path.read_text(encoding='utf-8')
# 副詞のみ抽出したファイルを使用
input_path = Path(f'texts/tokenized_hukushi_{name}.txt')
text_hukushi = input_path.read_text(encoding='utf-8')
# 記号のみ抽出したファイルを使用
input_path = Path(f'texts/tokenized_others_{name}.txt')
text_others = input_path.read_text(encoding='utf-8')

# フォントファイルのパスを絶対パスで指定
current_dir = Path(__file__).parent
font_path = current_dir / 'NotoSansJP-VariableFont_wght.ttf'

# 出力フォルダのパスを設定
output_dir = current_dir / 'output'
output_dir.mkdir(exist_ok=True)  # outputフォルダが存在しない場合は作成

# 表示させない単語(stopwords)の指定
stopwords = {'する', 'ある', 'こと', 'それ', 'これ', 'ため', 'よう', 'さん', '私', 'もの', '人', '時', '中', '日', '見', '思う', '行く', 'いる', 'いう', 'し', 'ない', 'さ', 'い', '事', '来', '今', '一'}

def generate_cloud(text):
	return WordCloud(
		font_path=str(font_path),  # 日本語フォントを指定
		stopwords=stopwords,  # ストップワードを指定
		width=1200,
		height=800,
		background_color='white'
	).generate(text)

def plot_and_save(wordcloud, filename):
	plt.figure(figsize=(12,8))
	plt.imshow(wordcloud)
	plt.axis('off') #軸の表示を消す

	output_path = output_dir / filename
	plt.savefig(str(output_path), bbox_inches='tight', pad_inches=0)
	
# 各品詞のワードクラウドを生成・保存
plot_and_save(generate_cloud(text_meishi), f'wordcloud_{name}_meishi.png')
plot_and_save(generate_cloud(text_doushi), f'wordcloud_{name}_doushi.png')
plot_and_save(generate_cloud(text_keiyoushi), f'wordcloud_{name}_keiyoushi.png')
plot_and_save(generate_cloud(text_hukushi), f'wordcloud_{name}_hukushi.png')
plot_and_save(generate_cloud(text_others), f'wordcloud_{name}_others.png')
