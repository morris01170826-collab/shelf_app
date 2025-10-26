import streamlit as st
import pandas as pd
from datetime import datetime

st.title("📦 棚管理アプリ")

# データ保存用CSVファイル名
DATA_FILE = "shelf_data.csv"

# CSVを読み込み（初回は空データ）
try:
    df = pd.read_csv(DATA_FILE)
except FileNotFoundError:
    df = pd.DataFrame(columns=["日時", "棚番号", "横番号", "縦番号", "操作", "材料名"])

# 入力フォーム
st.header("🔹 入出庫 登録")
col1, col2, col3 = st.columns(3)
with col1:
    shelf_no = st.number_input("棚番号（1 or 2）", min_value=1, max_value=2, step=1)
with col2:
    x_no = st.number_input("横番号（1〜19）", min_value=1, max_value=19, step=1)
with col3:
    y_no = st.number_input("縦番号（1〜4）", min_value=1, max_value=4, step=1)

material = st.text_input("材料名")
operation = st.selectbox("操作", ["入庫", "出庫"])

if st.button("登録"):
    new_data = pd.DataFrame([{
        "日時": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "棚番号": shelf_no,
        "横番号": x_no,
        "縦番号": y_no,
        "操作": operation,
        "材料名": material
    }])
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)
    st.success("登録しました！")

# 履歴表示
st.header("📜 履歴")
st.dataframe(df)


