import streamlit as st
import pandas as pd
from deep_translator import GoogleTranslator

# 翻訳関数
def translate_text(text, src_lang, dest_lang):
    translated = GoogleTranslator(source=src_lang, target=dest_lang).translate(text)
    return translated

# Excelファイルをアップロード
st.title("Excelファイル翻訳ツール")
uploaded_file = st.file_uploader("Excelファイルをアップロード", type="xlsx")

if uploaded_file is not None:
    # ファイルを読み込む
    df = pd.read_excel(uploaded_file)

    # 表示する
    st.write("アップロードしたExcelファイルの内容:")
    st.write(df)

    # 翻訳言語選択
    lang_option = st.selectbox("翻訳方向を選んでください", ["日本語 -> 英語", "英語 -> 日本語"])

    if lang_option == "日本語 -> 英語":
        src_lang = "ja"
        dest_lang = "en"
    else:
        src_lang = "en"
        dest_lang = "ja"

    # 翻訳処理
    if st.button("翻訳実行"):
        st.write("翻訳中...")

        # データフレームの各セルを翻訳
        translated_df = df.applymap(lambda x: translate_text(str(x), src_lang, dest_lang) if isinstance(x, str) else x)

        # 翻訳後の結果を表示
        st.write("翻訳後の内容:")
        st.write(translated_df)

        # 翻訳後のファイルをダウンロードリンクとして提供
        translated_file = "/tmp/translated_file.xlsx"
        translated_df.to_excel(translated_file, index=False)

        st.download_button(
            label="翻訳されたExcelファイルをダウンロード",
            data=open(translated_file, "rb").read(),
            file_name="translated_file.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
