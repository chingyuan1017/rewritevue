from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import re
import sys
sheetname = "測試"
jsonpath = 'C:\\Users\\07367\\Downloads\\level-datum-462407-t2-538db9b207a9.json'
file_path = './src/App.vue'
with open(file_path, 'r', encoding='utf-8') as f:
    vue_content = f.read()
'''

template_match = re.search(r'(<template>)([\s\S]*?)(</template>)', vue_content)
if not template_match:
    print("❌ 找不到 <template> 區塊")
    sys.exit()

template_start = template_match.group(1)
template_content = template_match.group(2)
template_end = template_match.group(3)



soup = BeautifulSoup(template_content, 'html.parser')




inner_voice = soup.find('inner-voice')


if inner_voice:
    if inner_voice.has_attr('text'):
        inner_voice['text'] = '12'
        print("✅ text 屬性修改成功")
    else:
        print("❌ inner-voice 沒有 text 屬性")
else:
    print("❌ 找不到 inner-voice 標籤")


# 5. 將修改後的 template 內容轉成字串
new_template_content = str(soup)

# 6. 把新的 template 區塊替換回原檔案內容中
vue_content_modified = vue_content.replace(
    template_start + template_content + template_end,
    template_start + new_template_content + template_end
)

# 7. 寫回原檔
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(vue_content_modified)

print("✅ 修改後內容已寫回檔案")

'''

def modify_tag_attribute_if_match(
    file_path: str, tag_name: str, attr_name: str, old_attr_value: str, new_attr_value: str
):
    # 讀取檔案
    with open(file_path, 'r', encoding='utf-8') as f:
        vue_content = f.read()

    # 取出 <template> 區塊
    template_match = re.search(r'(<template>)([\s\S]*?)(</template>)', vue_content)
    if not template_match:
        print("❌ 找不到 <template> 區塊")
        sys.exit()

    template_start = template_match.group(1)
    template_content = template_match.group(2)
    template_end = template_match.group(3)

    # 用 BeautifulSoup 解析 template 內容
    soup = BeautifulSoup(template_content, 'html.parser')

    # 找到指定標籤並檢查屬性
    tags = soup.find_all(tag_name)
    if not tags:
        print(f"❌ 找不到任何 {tag_name} 標籤")
        return

    modified_count = 0
    for tag in tags:
        if tag.has_attr(attr_name):
            current_value = tag[attr_name]
            if current_value == old_attr_value:
                tag[attr_name] = new_attr_value
                modified_count += 1

    if modified_count == 0:
        print(f"❌ 沒有找到 {tag_name} 中 {attr_name} 屬性值為 '{old_attr_value}' 的標籤")
        return

    # 將修改後的內容放回 <template> 中
    new_template_content = str(soup)
    new_vue_content = vue_content.replace(template_content, new_template_content)

    # 寫回檔案
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_vue_content)

    print(f"✅ 成功修改 {modified_count} 個 {tag_name} 的 {attr_name} 從 '{old_attr_value}' 到 '{new_attr_value}'")

def replace_text_in_tag(vue_content, tagname, oldtext, newtext, file_path):
    # 找出 <template> 區塊
    template_match = re.search(r'<template>([\s\S]*?)</template>', vue_content)
    if not template_match:
        print("❌ 找不到 <template> 區塊")
        return

    template_content = template_match.group(1)
    soup = BeautifulSoup(template_content, 'html.parser')

    # 找出所有目標標籤
    target_tags = soup.find_all(tagname)

    for tag in target_tags:
        # 遍歷標籤下所有文字節點（NavigableString）
        for text_node in tag.find_all(string=True):
            if oldtext in text_node:
                new_text = text_node.replace(oldtext, newtext)
                text_node.replace_with(new_text)
               
               

    # 將修改後的 template 內容轉成字串
    new_template_content = str(soup)

    # 把原本的 template 內容替換掉
    new_vue_content = vue_content.replace(template_content, new_template_content)
    #print(new_vue_content)

    # 寫回檔案
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_vue_content)

    print("✅ 替換完成！")

def loadgooglesheet(jsonpath,sheetname):
    SERVICE_ACCOUNT_FILE = jsonpath;#'C:\\Users\\07367\\Downloads\\level-datum-462407-t2-538db9b207a9.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']; 
    creds = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=SCOPES
    );
    client = gspread.authorize(creds);
    spreadsheet = client.open(sheetname)  # 或 client.open_by_url('https://docs.google.com/spreadsheets/d/...');

    sheet = spreadsheet.sheet1;
    data = sheet.get_all_values();
    data = [row for row in data if any(cell.strip() for cell in row)];
    # 轉成 numpy array
    np_data = np.array(data);
    # 用第一列當欄位名稱，剩下的當資料
    df = pd.DataFrame(np_data[1:], columns=np_data[0]);
    original_old_text = df["舊文字"].copy()
    df['舊文字'] = df["新文字"]
    updated_data = [df.columns.tolist()] + df.values.tolist()
    # 清除舊資料
    #sheet.clear()
    # 寫入更新後的資料
    #sheet.update(updated_data)

    print("✅ 寫入完成！")
    return  original_old_text,df["新文字"],df["tag"],df["att"],df["method"]

#replace_text_in_tag(vue_content, "nmd-menu-item", "篇章三","abc" , file_path)
'''
oldtext,newtext,tagname,attribute,method = loadgooglesheet(jsonpath,sheetname);
for old, new,tag,att, m in zip(oldtext, newtext,tagname,attribute,method):
    with open(file_path, 'r', encoding='utf-8') as f:
            vue_content = f.read()
    if m == "1":
        replace_text_in_tag(vue_content, str(tag), str(old), str(new), file_path)
    elif m =="2":
        modify_tag_attribute_if_match(file_path,tag,att,old,new)

'''

def operation(jsonpath,sheetname,file_path):
    oldtext,newtext,tagname,attribute,method = loadgooglesheet(jsonpath,sheetname);
    for old, new,tag,att, m in zip(oldtext, newtext,tagname,attribute,method):
        with open(file_path, 'r', encoding='utf-8') as f:
            vue_content = f.read()
        if m == "1":
            replace_text_in_tag(vue_content, str(tag), str(old), str(new), file_path)
        elif m =="2":
            modify_tag_attribute_if_match(file_path,tag,att,old,new)
