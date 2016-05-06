# -*- coding: utf-8 -*-
import time

from data_modeule import XlWebInfo, XlUserInfo
from OLFSC_modeule import *
from logs_module import XlLogInfo
from login_modeule import LocateLoginElement
from super_user_manage_module import LocateUserManageElement, LocateAssetManageElement, DefaultSet


class WebSelenium(OpenBrowser, LoadUrl, SendVals, CheckResult):
    def __init__(self, ele_locate_login=LocateLoginElement(),
                 ele_locate_user_manage=LocateUserManageElement(),
                 ele_locate_asset_manage=LocateAssetManageElement(),
                 ele_default_set=DefaultSet()):
        self.ele_locate_login = ele_locate_login
        self.ele_locate_user_manage = ele_locate_user_manage
        self.ele_locate_asset_manage = ele_locate_asset_manage
        self.ele_default_set = ele_default_set

    def log_out(self, web_driver, logout_id):
        web_driver.find_element_by_xpath(logout_id).click()

    def add_user_mgroups(self, web_driver, super_manage_element_dict,
                         add_user_group_list, add_user_group_list_key, log):
        self.ele_locate_user_manage.find_user_mgroups(web_driver, super_manage_element_dict)
        find_user_group_tuple = self.ele_locate_user_manage.find_element_add_user_mgroups(web_driver,
                                                                                          super_manage_element_dict)
        time.sleep(2)

        group_number = len(add_user_group_list)
        for arg in add_user_group_list:
            self.send_vals(find_user_group_tuple, add_user_group_list_key, arg)
            result_add_user_group = self.check_result(web_driver, super_manage_element_dict, arg, log,
                                                      'addusergroup')
            time.sleep(2)
            if result_add_user_group:
                pass

            group_number -= 1
            if group_number > 0:
                find_user_group_tuple = self.ele_locate_user_manage.find_element_add_user_mgroups(
                    web_driver, super_manage_element_dict)

    def add_user(self, web_driver, super_manage_element_dict, add_user_list, add_user_list_key, log):
        user_group_id = 1
        competence_id = 1
        other_id = 1
        # self.ele_locate_user_manage.find_element_user(web_driver, super_manage_element_dict)
        find_user_tuple = self.ele_locate_user_manage.find_element_add_user(web_driver, super_manage_element_dict,
                                                                            user_group_id, competence_id,
                                                                            other_id)
        time.sleep(2)

        user_number = len(add_user_list)
        for arg in add_user_list:
            self.send_vals(find_user_tuple, add_user_list_key, arg)
            result_add_user = self.check_result(web_driver, super_manage_element_dict, arg, log,
                                                'adduser')
            time.sleep(2)

            if result_add_user:
                pass

            user_number -= 1
            if user_number > 0:
                user_group_id += 1
                competence_id += 1
                other_id += 1
                # self.ele_locate_user_manage.find_element_user(web_driver, super_manage_element_dict)
                find_user_tuple = self.ele_locate_user_manage.find_element_add_user(web_driver,
                                                                                    super_manage_element_dict,
                                                                                    user_group_id, competence_id,
                                                                                    other_id)

    def add_host_groups(self, web_driver, super_manage_element_dict,
                        add_asset_group_list, add_asset_group_list_key, log):
        self.ele_locate_asset_manage.find_asset_group(web_driver, super_manage_element_dict)

        find_asset_group_tuple = self.ele_locate_asset_manage.find_element_add_host_groups(web_driver,
                                                                                           super_manage_element_dict)
        time.sleep(2)

        group_number = len(add_asset_group_list)
        for arg in add_asset_group_list:
            self.send_vals(find_asset_group_tuple, add_asset_group_list_key, arg)
            result_add_asset_group = self.check_result(web_driver, super_manage_element_dict, arg, log, 'addassetgroup')

            time.sleep(2)

            if result_add_asset_group:
                pass

            group_number -= 1
            if group_number > 0:
                find_asset_group_tuple = self.ele_locate_asset_manage.find_element_add_host_groups(web_driver,
                                                                                                   super_manage_element_dict)

    def default_set(self, web_driver, super_manage_element_dict, default_set_list, default_set_list_key, log):
        self.ele_default_set.find_set(web_driver, super_manage_element_dict)

        find_default_set_tuple = self.ele_default_set.find_element_default_set(web_driver,
                                                                               super_manage_element_dict)
        time.sleep(2)

        group_number = len(default_set_list)
        for arg in default_set_list:
            self.send_vals(find_default_set_tuple, default_set_list_key, arg)
            # result_default_set = self.check_result(web_driver, super_manage_element_dict, arg, log, 'defaultset')
            group_number -= 1
            if group_number > 0:
                find_default_set_tuple = self.ele_default_set.find_element_default_set(web_driver,
                                                                                       super_manage_element_dict)

    def single_add_asset(self, web_driver, super_manage_element_dict,
                         single_add_asset_list, single_add_asset_list_key, log):
        asset_user_manage_id = 1
        asset_host_group_id = 10
        asset_is_activated_id = 1
        self.ele_locate_asset_manage.find_asset(web_driver, super_manage_element_dict)

        find_single_add_asset_tuple = self.ele_locate_asset_manage.find_element_single_add_asset(web_driver,
                                                                                                 super_manage_element_dict,
                                                                                                 asset_user_manage_id,
                                                                                                 asset_host_group_id,
                                                                                                 asset_is_activated_id)
        time.sleep(2)

        group_number = len(single_add_asset_list)
        for arg in single_add_asset_list:
            if (asset_user_manage_id % 2) != 0:
                add_asset_list_key = single_add_asset_list_key[0:3]
                self.send_vals(find_single_add_asset_tuple, add_asset_list_key, arg)
                find_single_add_asset_tuple[3].click()
            else:
                add_asset_list_key = single_add_asset_list_key
                self.send_vals(find_single_add_asset_tuple, add_asset_list_key, arg)
                # find_single_add_asset_tuple[3].click()

            time.sleep(2)

            result_single_add_asset = self.check_result(web_driver, super_manage_element_dict, arg, log,
                                                        'singleaddasset')
            if result_single_add_asset:
                pass
            group_number -= 1
            if group_number > 0:
                asset_user_manage_id += 1
                asset_host_group_id += 1
                asset_is_activated_id += 1
                find_single_add_asset_tuple = self.ele_locate_asset_manage.find_element_single_add_asset(web_driver,
                                                                                                         super_manage_element_dict,
                                                                                                         asset_user_manage_id,
                                                                                                         asset_host_group_id,
                                                                                                         asset_is_activated_id)

    def login_test(self, login_element_dict, super_manage_element_dict,
                   manage_user_list, manage_user_list_key,
                   add_user_group_list, add_user_group_list_key,
                   add_user_list, add_user_list_key,
                   add_asset_group_list, add_asset_group_list_key,
                   single_add_asset_list, single_add_asset_list_key,
                   default_set_list, default_set_list_key):
        web_driver = self.open_browser()
        self.load_url(web_driver, login_element_dict['url'])
        time.sleep(2)
        log = XlLogInfo()
        log.log_init('Sheet1', 'User', 'Pwd', 'Result', 'Msg')

        find_login_tuple = self.ele_locate_login.find_element_login(web_driver, login_element_dict)
        for arg in manage_user_list:
            self.send_vals(find_login_tuple, manage_user_list_key, arg)
            time.sleep(2)
            result_login = self.check_result(web_driver, login_element_dict, arg, log, 'login')
            if result_login:
                if '超级管理员' in result_login:

                    self.ele_locate_user_manage.find_user_manage(web_driver, super_manage_element_dict)

                    time.sleep(2)

                    try:
                        self.add_user_mgroups(web_driver, super_manage_element_dict,
                                              add_user_group_list, add_user_group_list_key, log)
                    except:
                        print('Add user group failed')

                    time.sleep(2)

                    try:
                        self.add_user(web_driver, super_manage_element_dict,
                                      add_user_list, add_user_list_key, log)
                    except:
                        print('Add user failed')

                    time.sleep(2)

                    try:
                        self.default_set(web_driver, super_manage_element_dict,
                                         default_set_list, default_set_list_key, log)
                    except:
                        print('Default settings failed')

                    self.ele_locate_asset_manage.find_asset_manage(web_driver, super_manage_element_dict)

                    time.sleep(2)

                    try:
                        self.add_host_groups(web_driver, super_manage_element_dict,
                                             add_asset_group_list, add_asset_group_list_key, log)
                    except:
                        print('Add host group failed')

                    time.sleep(2)

                    try:
                        self.single_add_asset(web_driver, super_manage_element_dict,
                                              single_add_asset_list, single_add_asset_list_key, log)
                    except:
                        print('Single add host failed')



                else:
                    pass

                self.log_out(web_driver, login_element_dict['logout_id'])
            find_login_tuple = self.ele_locate_login.find_element_login(web_driver, login_element_dict)

        log.log_close()


if __name__ == '__main__':
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

    test = WebSelenium()
    test.login_test(login_element_dict, super_manage_element_dict,
                    manage_user_list, manage_user_list_key,
                    add_user_group_list, add_user_group_list_key,
                    add_user_list, add_user_list_key,
                    add_asset_group_list, add_asset_group_list_key,
                    single_add_asset_list, single_add_asset_list_key,
                    default_set_list, default_set_list_key)
