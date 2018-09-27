# -*- coding: utf-8 -*-
import os
import collections
from openpyxl import load_workbook
from load_source import load_source

def main(target_file):
    print(source_ids)
    target_wb = load_workbook(target_file, keep_vba=True)
    # source_wb = load_workbook(source_wb)
    # for sheet_name in sheet_names:
    #     ws = wb.
    # anchor = start_line
    # print(source_pool)
    for sheet in target_wb:
        # 在target.xlsm文件里，肉眼只能看见4张sheet
        # 但用代码读取的时候，能看见n多张sheet
        # 所以写了下面这一行：
        
        if sheet.title in sheet_titles:
            # 看一看H列都有多少行
            # print('len of column %s: %s' % (sheet.title ,len(sheet['H'])) )

            # values = [(cell.value, ) for cell in sheet['H']]
            iteror = 7
            # target_cells = []
            # 对于当前sheet，H列(点名)的每个cell来说
            for cell in sheet['H'][7:]:
                if cell.value and (cell.value.strip() in source_ids):
                    print('valide cell value: ', cell.value)
                    signal_description = source_pool[source_ids.index(cell.value.strip())][1]
                    sheet['K'+str(iteror+1)].value = signal_description[lang_selector]
                iteror += 1

    target_wb.save(os.path.join('./output/', os.path.basename(target_file)))
    target_wb.close()

if __name__ == '__main__':
    ####### 在这里做一些设定 #######
    target_files = [file for file in os.listdir('./target') if file.endswith(('xlsm', 'xlsx'))]
    sheet_titles = ['OWP', 'ACP', 'RSS', 'DTC'] # SCID Excel数据库文件固定的sheet页名称
    lang_selector = 0   # 1 for Chinese, 0 for English; 1和0的含义，跟load_source函数中return的结果有关系

    source_pool = load_source()
    source_ids = [element[0].strip() for element in source_pool]

    for file in target_files:
        main(os.path.join('./target', file))

        