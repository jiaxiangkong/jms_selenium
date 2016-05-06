# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


def get_ele_times(web_driver, times, func):
    return WebDriverWait(web_driver, times).until(func)


class OpenBrowser:
    @staticmethod
    def open_browser():
        """
        打开浏览器
        :return: web_driver Handle
        """
        try:
            web_driver = webdriver.Firefox()
        except:
            web_driver = webdriver.Chrome()
        return web_driver


class LoadUrl:
    @staticmethod
    def load_url(web_driver, url):
        """
        加载 url
        :param web_driver: webdriver.Firefox()
        :param url: http://192.168.20.155/login/
        :return:
        """
        web_driver.get(url)
        web_driver.maximize_window()


class FindElement:
    """
    元素定位是自动化测试核心部分：
    """

    def by_id(self, web_driver, arg):
        byid = get_ele_times(web_driver, 5, lambda func: web_driver.find_element_by_id(arg))
        return byid

    def by_name(self, web_driver, arg):
        byname = get_ele_times(web_driver, 5, lambda func: web_driver.find_element_by_name(arg))
        return byname

    def by_link_text(self, web_driver, arg):
        get_ele_times(web_driver, 5, lambda func: web_driver.find_element_by_link_text(arg))
        return self.by_link_text

    def by_xpath(self, web_driver, arg):
        byxpath = get_ele_times(web_driver, 5, lambda func: web_driver.find_element_by_xpath(arg))
        return byxpath

    def by_css_selector(self, web_driver, arg):
        bycssselector = get_ele_times(web_driver, 5, lambda func: web_driver.find_element_by_css_selector(arg))
        return bycssselector


class SendVals:
    @staticmethod
    def send_vals(ele_tuple, list_key, arg):
        """
        在登录界面输入帐号信息并登录： admin, admin
        :param ele_tuple: tuple
        :param list_key: list
        :param arg: must be dict
        :return:
        """
        i = 0
        for key in list_key:
            ele_tuple[i].send_keys('')
            ele_tuple[i].clear()
            ele_tuple[i].send_keys(arg[key])
            i += 1
        ele_tuple[i].click()


class CheckResult(FindElement):
    def check_result(self, web_driver, find_dict, arg, log, msg):
        """
        检查结果
        :param web_driver: webdriver.Firefox()
        :param find_dict: 定位元素
        :param arg: 操作时输入相关的内容信息
        :param log: 将检查结果写到xls文件中
        :param msg: 根据操作事件 进行事件对应检查结果
        :return: result
        """
        result = False
        if 'login' in msg:
            try:
                login_err = self.by_css_selector(web_driver, find_dict['login_err'])

                log.log_write(arg['user'], arg['pwd'], 'Error', login_err.text)
                print('%s__%s__%s__%s' % (arg['user'], arg['pwd'], 'Error', login_err.text))

            except:
                login_ok = self.by_xpath(web_driver, find_dict['login_ok'])

                log.log_write(arg['user'], arg['pwd'], 'Pass', login_ok.text)
                print('%s__%s__%s__%s' % (arg['user'], arg['pwd'], 'Pass', login_ok.text))
                result = login_ok.text

        if 'addusergroup' == msg:
            try:
                addusergroup_err = self.by_css_selector(web_driver, find_dict['add_user_group_err'])
                log.log_write(arg['user_group_name'], arg['user_group_remark'], 'Error', addusergroup_err.text)
                print('%s__%s__%s__%s' % (
                    arg['user_group_name'], arg['user_group_remark'], 'Error', addusergroup_err.text))

            except:
                addusergroup_ok = self.by_css_selector(web_driver, find_dict['add_user_group_ok'])
                log.log_write(arg['user_group_name'], arg['user_group_remark'], 'Pass', addusergroup_ok.text)
                print(
                    '%s__%s__%s__%s' % (arg['user_group_name'], arg['user_group_remark'], 'Pass', addusergroup_ok.text))
                result = True

        if 'adduser' == msg:
            try:
                adduser_err = self.by_css_selector(web_driver, find_dict['add_user_err'])
                log.log_write(arg['user_name'], arg['name'], 'Error', adduser_err.text)
                print('%s__%s__%s__%s' % (arg['user_name'], arg['name'], 'Error', adduser_err.text))

            except:
                adduser_ok = self.by_css_selector(web_driver, find_dict['add_user_ok'])
                log.log_write(arg['user_name'], arg['name'], 'Pass', adduser_ok.text)
                print('%s__%s__%s__%s' % (arg['user_name'], arg['name'], 'Pass', adduser_ok.text))
                result = True

        if 'addassetgroup' == msg:
            try:
                addassetgroup_err = self.by_css_selector(web_driver, find_dict['add_asset_group_err'])
                log.log_write(arg['host_group_name'], arg['host_group_remark'], 'Error', addassetgroup_err.text)
                print('%s__%s__%s__%s' % (
                    arg['host_group_name'], arg['host_group_remark'], 'Error', addassetgroup_err.text))

            except:
                addassetgroup_ok = self.by_css_selector(web_driver, find_dict['add_asset_group_ok'])
                log.log_write(arg['host_group_name'], arg['host_group_remark'], 'Pass', addassetgroup_ok.text)
                print('%s__%s__%s__%s' % (
                    arg['host_group_name'], arg['host_group_remark'], 'Pass', addassetgroup_ok.text))
                result = True

        # if 'defaultset' == msg:
        #     try:
        #         defaultset_err = self.by_css_selector(web_driver, find_dict['single_add_asset_err'])
        #         log.log_write(arg['default_manage_user'], arg['default_password'], 'Error', defaultset_err.text)
        #         print('%s__%s__%s__%s' % (
        #             arg['default_manage_user'], arg['default_password'], 'Error', defaultset_err.text))
        #
        #     except:
        #         defaultset_ok = self.by_css_selector(web_driver, find_dict['single_add_asset_ok'])
        #         log.log_write(arg['default_manage_user'], arg['default_password'], 'Pass', defaultset_ok.text)
        #         print('%s__%s__%s__%s' % (
        #             arg['default_manage_user'], arg['default_password'], 'Pass', defaultset_ok.text))
        #         result = True

        if 'singleaddasset' == msg:
            try:
                singleaddasset_err = self.by_css_selector(web_driver, find_dict['single_add_asset_err'])
                log.log_write(arg['host_name'], arg['host_ip'], 'Error', singleaddasset_err.text)
                print('%s__%s__%s__%s' % (
                    arg['host_name'], arg['host_ip'], 'Error', singleaddasset_err.text))

            except:
                singleaddasset_ok = self.by_css_selector(web_driver, find_dict['single_add_asset_ok'])
                log.log_write(arg['host_name'], arg['host_ip'], 'Pass', singleaddasset_ok.text)
                print('%s__%s__%s__%s' % (
                    arg['host_name'], arg['host_ip'], 'Pass', singleaddasset_ok.text))
                result = True
        return result
