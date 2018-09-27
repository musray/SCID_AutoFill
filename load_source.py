import os
from openpyxl import load_workbook

def split_by_lang(message):
    # TODO 根据\n的位置，把message里的中文和英文分开
    splited_message = []
    return splited_message

files = os.listdir('./source')
col_keyword = '功能描述'

pool = []
for file in files:
    wb = load_workbook(os.path.join(os.getcwd(), 'source', file)) 
    ws = wb.active
    # id_des = [(row[3].value, [row[3].value]) for row in ws]
    id_des = []
    double_description_col = col_keyword in ws['D1'].value
    for row in ws.rows:
        # print(row)
        id = row[0].value
        if double_description_col:
            description = [row[2].value, row[3].value]
        else:
            description = split_by_lang(row[2])
        id_des.append((id, description))
    pool.extend(id_des)    

print(pool)