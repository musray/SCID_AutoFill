# -*- coding: utf-8 -*-

# import pandas as pd
# # import os

# file = './source/source.xlsm'

# xl = pd.ExcelFile(file)

# print(xl.sheet_names)

import collections
from openpyxl import load_workbook

# source_file = './source/source.xlsx'
target_file = './target/target.xlsm'

# SCID Excel数据库文件固定的sheet页名称
sheet_titles = ['OWP', 'ACP', 'RSS', 'DTC']

# 固定位置
start_line = 8
line_offset = 6

target_wb = load_workbook(target_file)
# source_wb = load_workbook(source_wb)
# for sheet_name in sheet_names:
#     ws = wb.
anchor = start_line
for sheet in target_wb:
    if sheet.title in sheet_titles:
        # 看一看H列都有多少行
        # print('len of column %s: %s' % (sheet.title ,len(sheet['H'])) )

        # values = [(cell.value, ) for cell in sheet['H']]
        iteror = 1
        target_cells = []
        for cell in sheet['H']:
            value = cell.value
            row_index = iteror 
            iteror += 1
            target_cells.append((value, row_index))
        # valid_values = values[]


        

