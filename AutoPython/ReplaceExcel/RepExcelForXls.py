from xlrd import open_workbook
from xlutils.copy import copy
import re


def get_safe_xls(filepath):
    wb = open_workbook(filepath, formatting_info=True)  # formatting_info保留原格式，只支持xls文件，对xlsx格式无效
    sheets = wb.sheets()
    newwb = copy(wb)  # 原文件只能读，不能写，需要复制一份可以写的文件对象
    for sheet in sheets:  # 读取原文件数据遍历每个单元格，并替换指定内容
        newsheet = newwb.get_sheet(sheets.index(sheet))
        rows = sheet.nrows
        cols = sheet.ncols
        for row in range(rows):
            for col in range(cols):
                value = sheet.cell(row, col).value
                # 正则实现替换手机号和邮箱
                if re.search(r"1\s*[345789]\d\s*[-]?\s*\d\s*\d\s*\d\s*[-]?\s*\d\s*[-]?\s*\d\s*\d\s*\d\s*\d",
                             str(value)) or \
                        re.search(r"[a-zA-Z0-9._]{1,64}@[a-zA-Z0-9]{1,64}(.net|.cn|.com.cn|.com|.org|.edu.cn)",
                                  str(value)):
                    newsheet.write(row, col, '***')
    safe_file_path = './test.xls'
    newwb.save(safe_file_path)
    return safe_file_path
