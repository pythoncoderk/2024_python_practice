import win32com.client

# Excelアプリケーションを起動
excel = win32com.client.Dispatch("Excel.Application")

# Excelファイルを開く
workbook = excel.Workbooks.Open(r"C:\path\to\your\file.xlsx")

# カスタムプロパティを変更（秘密度ラベルを仮に「Confidential」に設定）
workbook.CustomDocumentProperties("Confidential") = "内部"

# ファイルを保存
workbook.Save()

# Excelを終了
workbook.Close()
excel.Quit()