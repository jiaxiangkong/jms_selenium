# -*- coding: utf-8 -*-

import xlrd


class XlSheetInfo:
    def __init__(self, path=''):
        self.xl = xlrd.open_workbook(path)

    def float_to_str(self, value):
        if isinstance(value, float):
            value = str(int(value))
        return value

    def get_sheet_info_by_name(self, name):
        self.sheet = self.xl.sheet_by_name(name)
        return self.get_info()

    def get_sheet_info_by_index(self, index):
        self.sheet = self.xl.sheet_by_index(index)
        return self.get_info()


class XlUserInfo(XlSheetInfo):
    def get_info(self):
        list_key = self.sheet.row_values(0)
        user_info = []
        for row in range(1, self.sheet.nrows):
            info = [self.float_to_str(value) for value in self.sheet.row_values(row)]
            tmp = zip(list_key, info)
            user_info.append(dict(tmp))
        return user_info, list_key


class XlWebInfo(XlSheetInfo):
    def get_info(self):
        list_key = self.sheet.col_values(0)
        web_info = {}
        for col in range(1, self.sheet.ncols):
            info = [self.float_to_str(value) for value in self.sheet.col_values(col)]
            tmp = zip(list_key, info)
            web_info.update(dict(tmp))
        return web_info


if __name__ == '__main__':
    # xinfo = XlUserInfo(r'F:\PycharmProjects\selenium\datainfo.xlsx')
    # info = xinfo.get_sheet_info_by_name('userinfo')[0]
    # list_key = xinfo.get_sheet_info_by_name('userinfo')[1]
    # info = xinfo.get_sheet_info_by_index(0)
    # for key in info:
    #     print(key)
    # print(info)

    input_info = XlUserInfo(r'F:\PycharmProjects\selenium\Data_info.xlsx')
    manage_user_list = input_info.get_sheet_info_by_name('Web_Manage_User')[0]
    manage_user_list_key = input_info.get_sheet_info_by_name('Web_Manage_User')[1]

    add_user_group_list = input_info.get_sheet_info_by_name('Web_Add_User_Group')[0]
    add_user_group_list_key = input_info.get_sheet_info_by_name('Web_Add_User_Group')[1]

    add_user_list = input_info.get_sheet_info_by_name('Web_Add_User')[0]
    add_user_list_key = input_info.get_sheet_info_by_name('Web_Add_User')[1]

    add_asset_group_list = input_info.get_sheet_info_by_name('Web_Add_Asset_Group')[0]
    add_asset_group_list_key = input_info.get_sheet_info_by_name('Web_Add_Asset_Group')[1]

    default_set_list = input_info.get_sheet_info_by_name('Web_Default_Set')[0]
    default_set_list_key = input_info.get_sheet_info_by_name('Web_Default_Set')[1]

    single_add_asset_list = input_info.get_sheet_info_by_name('Web_Add_Asset')[0]
    single_add_asset_list_key = input_info.get_sheet_info_by_name('Web_Add_Asset')[1]

    web_info = XlWebInfo(r'F:\PycharmProjects\selenium\Data_info.xlsx')
    login_element_dict = web_info.get_sheet_info_by_name('Web_Login_Element_Dict')
    super_manage_element_dict = web_info.get_sheet_info_by_name('Web_Super_Manage_Element_Dict')
