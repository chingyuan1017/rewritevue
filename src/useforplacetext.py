import src.replacetext as rt







jsonpath=""     # 這邊輸入串流googlesheet api 的json檔案路徑
sheetname = ""   #這邊輸入表單名稱
file_path = ""   #輸入需要修改Vue檔案的路徑
 
rt.operation(jsonpath,sheetname,file_path)