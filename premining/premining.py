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
# ...existing code...

def merge_text_files(input_files, output_file):
    """
    複数のテキストファイルを半角スペースで区切って1つのファイルに統合する

    :param input_files: 入力ファイルのパスのリスト
    :param output_file: 出力ファイルのパス
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for i, file_path in enumerate(input_files):
                with open(file_path, 'r', encoding='utf-8') as infile:
                    content = infile.read().strip()  # 前後の空白を削除
                    outfile.write(content)
                    # 最後のファイル以外の後にスペースを追加
                    if i < len(input_files) - 1:
                        outfile.write(' ')
        
        print(f"ファイルの統合が完了しました。結果は '{output_file}' に保存されました。")

    except FileNotFoundError as e:
        print(f"エラー: ファイルが見つかりません: {e}")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

# --- ここから実行部分 ---
if __name__ == '__main__':
    # 入力ファイルの数を指定
    num_files = int(input("input file num -> "))
    input_files = []
    for i in range(num_files):
        file_name = input(f"input file {i+1} -> ")
        output_file = f"texts/output{i+1}.txt"
        remove_tags_from_file("texts/" + file_name, output_file)
        input_files.append(output_file)
    output_file = "texts/" + input("output flie -> ")
    merge_text_files(input_files, output_file)