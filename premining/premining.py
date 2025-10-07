import re

def remove_tags_from_file(input_path, output_path):
    """
    テキストファイルから<>で囲まれた部分を削除し、別ファイルに保存する。

    :param input_path: 入力ファイルのパス
    :param output_path: 出力ファイルのパス
    """
    # 削除したいパターンの正規表現:
	# '《'で始まり、'》'で終わる文字列
    # '|'
    # '［＃'で始まり、'］'で終わる文字列
    # '.*?' は「最短マッチ」を意味し、複数のタグがある行でも正しく動作します。
    pattern = r'《.*?》|［＃.*?］|｜'

    try:
        # with文を使うことで、ファイルの閉じ忘れを防ぎます。
        # encoding='utf-8' は日本語などのマルチバイト文字の文字化けを防ぐためです。
        with open(input_path, 'r', encoding='utf-8') as infile, \
             open(output_path, 'w', encoding='utf-8') as outfile:

            # 入力ファイルを1行ずつ読み込んで処理
            for line in infile:
                # re.sub()でパターンに一致する部分を空文字列('')に置換（=削除）
                cleaned_line = re.sub(pattern, '', line)
                # 結果を新しいファイルに書き込む
                outfile.write(cleaned_line)
        
        print(f"処理が完了しました。結果は '{output_path}' に保存されました。")

    except FileNotFoundError:
        print(f"エラー: 入力ファイル '{input_path}' が見つかりません。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

# --- ここから実行部分 ---
if __name__ == '__main__':
    # 入力ファイル名と出力ファイル名を指定
    input_file = 'dogura_magura.txt'
    output_file = 'texts/cleaned_dogura.txt'

    # 関数の実行
    remove_tags_from_file(input_file, output_file)