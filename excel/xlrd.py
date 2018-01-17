#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 22:56:23 2017

@author: wei
"""

import xlrd

XLS = '權證達人寶典_NEWVOL_2017-09-22.xls'
TICKER = ('2454', '聯發科')

def read_xls(xls, tk):
    """ 從Excel檔案讀取 """
    ret = []
    book = xlrd.open_workbook(xls)
    sheet = book.sheet_by_index(0)    # 第一個工作表
    for row_index in range(5, sheet.nrows - 1):        # 略過前面5列的標頭
        ticker = sheet.cell(row_index, 17).value    # 第18欄，標的代碼
        if ticker != tk:
            continue
        remain = int(sheet.cell(row_index, 15).value)    # 剩餘天數
        if remain <= 60:
            continue
        code = sheet.cell(row_index, 0).value    # 權證代碼
        name = sheet.cell(row_index, 1).value    # 權證名稱
        price = sheet.cell(row_index, 19).value  # 標的價格
        sp = sheet.cell(row_index, 22).value     # 最新履約價
        w_type = sheet.cell(row_index, sheet.ncols - 1).value    # 最後一欄，認購/售類別

        ret.append([code, name, remain, price, sp, w_type])
        # print(ret[-1])
    return ret

wlist = read_xls(XLS, TICKER[0])