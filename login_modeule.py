# -*- coding: utf-8 -*-

from OLFSC_modeule import *


class LocateLoginElement(FindElement):
    def find_element_login(self, web_driver, arg):
        ele_use = self.by_name(web_driver, arg['user_id'])
        ele_pwd = self.by_name(web_driver, arg['pwd_id'])
        ele_login = self.by_xpath(web_driver, arg['login_id'])
        return ele_use, ele_pwd, ele_login