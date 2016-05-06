# -*- coding: utf-8 -*-
import time

import xlsxwriter

class XlLogInfo:
    def __init__(self, path=''):
        fname = path + time.strftime('%Y-%m-%d', time.gmtime())
        self.row = 0
        self.xl = xlsxwriter.Workbook(path + fname + '.xlsx')
        self.style = self.xl.add_format({'bg_color': 'red'})

    def xl_write(self, *args):
        col = 0
        style = ''
        if 'Error' in args:
            style = self.style
        for value in args:
            self.sheet.write_string(self.row, col, value, style)
            col += 1
        self.row += 1

    def log_init(self, sheet_name, *title):
        self.sheet = self.xl.add_worksheet(sheet_name)
        self.sheet.set_column('A:E', 30)
        self.xl_write(*title)

    def log_write(self, *args):
        self.xl_write(*args)

    def log_close(self):
        self.xl.close()


if __name__ == '__main__':
    # log = Loginfo()
    # log.log_write('test Loginfo 测试')
    # log.log_close()
    log = XlLogInfo()
    log.log_init('Sheet1', 'user', 'pwd', 'result', 'msg')
    log.log_close()

