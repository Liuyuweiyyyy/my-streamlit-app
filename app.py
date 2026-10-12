import streamlit as st
import mysql.connector

st.title("📢 最新公告")

# 連接 MariaDB
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="B11317027",
    database="django_db",
    port=3306
)

# 讀取公告資料
cursor = conn.cursor(dictionary=True)

cursor.execute("""
    SELECT title, content
    FROM announcements_announcement
    ORDER BY created_at DESC
""")

announcements = cursor.fetchall()

# 顯示公告
for announcement in announcements:
    st.subheader(announcement["title"])
    st.write(announcement["content"])

cursor.close()
conn.close()
