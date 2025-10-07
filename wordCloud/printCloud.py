from wordcloud import WordCloud
import matplotlib.pyplot as plt
from pathlib import Path

# テキストファイルを読み込む
input_path = Path('texts/tokenized_dogura.txt')
text = input_path.read_text(encoding='utf-8')

# フォントファイルのパスを絶対パスで指定
current_dir = Path(__file__).parent
font_path = current_dir / 'NotoSansJP-VariableFont_wght.ttf'

# 出力フォルダのパスを設定
output_dir = current_dir / 'output'
output_dir.mkdir(exist_ok=True)  # outputフォルダが存在しない場合は作成

wordcloud = WordCloud(
    font_path=str(font_path),  # 日本語フォントを指定
    width=800,
    height=600,
    background_color='white'
	).generate(text)

plt.figure(figsize=(12,12))
plt.imshow(wordcloud)
plt.axis('off') #軸の表示を消す

# 画像を保存
output_path = output_dir / 'wordcloud.png'
plt.savefig(str(output_path), bbox_inches='tight', pad_inches=0)