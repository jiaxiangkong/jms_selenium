# -*- coding: utf-8 -*-
import time

from OLFSC_modeule import *


class LocateUserManageElement(FindElement):
    def find_user_manage(self, web_driver, arg):
        """
        定位用户管理元素
        :param web_driver: webdriver.Firefox()
        :param arg: must be dict
        :return:
        """

        user_manage = self.by_xpath(web_driver, arg['user_manage'])
        user_manage.click()

    def find_user_mgroups(self, web_driver, arg):
        """
        定位查看用户组元素
        :param web_driver: webdriver.Firefox()
        :param arg: must be dict
        :return:
        """

        view_user_groups = self.by_xpath(web_driver, arg['view_user_groups'])
        view_user_groups.click()

        add_user_group = self.by_xpath(web_driver, arg['add_user_group'])
        add_user_group.click()

    def find_element_add_user_mgroups(self, web_driver, arg):
        """
        定位添加用户组元素
        :param web_driver: webdriver.Firefox()
        :param arg: must be dict
        :return:
        """

        user_group_name = self.by_id(web_driver, arg['user_group_name'])
        user_group_remark = self.by_id(web_driver, arg['user_group_remark'])
        confirm_save = self.by_id(web_driver, arg['confirm_save'])
        return user_group_name, user_group_remark, confirm_save

    def find_element_user(self, web_driver, arg):
        """
        定位查看用户元素
        :param web_driver: webdriver.Firefox()
        :param arg: must be dict
        :return:
        """

        view_user = self.by_xpath(web_driver, arg['view_user'])
        view_user.click()

        add_user = self.by_xpath(web_driver, arg['add_user'])
        add_user.click()

    def find_element_add_user(self, web_driver, arg, user_group_id, competence_id, other_id):
        """
        定位添加用户元素
        :param web_driver:
        :param arg:
        :param user_group_id:
        :param user_competence_id:
        :param user_other_id:
        :return:
        """

        self.find_element_user(web_driver, arg)

        group_id = self.by_xpath(web_driver, arg[user_group_id])
        group_id.click()
        group_id.click()

        time.sleep(1)
        if (competence_id % 2) == 0:
            competence_general_user = self.by_xpath(web_driver, arg['competence_general_user'])
            competence_general_user.click()
        else:
            competence_super_user = self.by_xpath(web_driver, arg['competence_super_user'])
            competence_super_user.click()

        time.sleep(1)
        if (other_id % 2) == 0:
            other_disable = self.by_xpath(web_driver, arg['other_disable'])
            other_disable.click()
        else:
            other_send_email = self.by_xpath(web_driver, arg['other_send_email'])
            other_send_email.click()

        time.sleep(1)

        username = self.by_id(web_driver, arg['username'])
        name = self.by_id(web_driver, arg['name'])
        email = self.by_id(web_driver, arg['email'])
        confirm_save = self.by_id(web_driver, arg['confirm_save'])
        return username, name, email, confirm_save


class DefaultSet(FindElement):
    def find_set(self, web_driver, arg):
        """
        定位设置元素
        :param web_driver:
        :param arg:
        :return:
        """
        set = self.by_xpath(web_driver, arg['default_set'])
        set.click()

    def find_element_default_set(self, web_driver, arg):
        """
        定位默认设置元素
        :param web_driver:
        :param arg:
        :return:
        """
        default_manage_user = self.by_xpath(web_driver, arg['default_manage_user'])
        default_password = self.by_xpath(web_driver, arg['default_password'])
        default_ssh_port = self.by_xpath(web_driver, arg['default_ssh_port'])
        default_ssh_key = self.by_xpath(web_driver, arg['default_ssh_key'])
        confirm_save = self.by_id(web_driver, arg['confirm_save'])
        return default_manage_user, default_password, default_ssh_port, default_ssh_key, confirm_save


class LocateAssetManageElement(FindElement):
    def find_asset_manage(self, web_driver, arg):
        """
        定位资产管理元素
        :param web_driver: webdriver.Firefox()
        :param arg: must be dict
        :return:
        """

        asset_manage = self.by_xpath(web_driver, arg['asset_manage'])
        asset_manage.click()

    def find_asset_group(self, web_driver, arg):
        """
        定位查看资产组元素
        :param web_driver: webdriver.Firefox()
        :param arg: must be dict
        :return:
        """

        view_asset_group = self.by_xpath(web_driver, arg['view_asset_group'])
        view_asset_group.click()

        add_host_group = self.by_xpath(web_driver, arg['add_host_group'])
        add_host_group.click()

    def find_element_add_host_groups(self, web_driver, arg):
        """
        定位添加主机组元素
        :param web_driver: webdriver.Firefox()
        :param arg: must be dict
        :return:
        """

        host_group_name = self.by_xpath(web_driver, arg['host_group_name'])
        host_group_remark = self.by_xpath(web_driver, arg['host_group_remark'])
        add_asset_group_submit = self.by_id(web_driver, arg['add_asset_group_submit'])
        return host_group_name, host_group_remark, add_asset_group_submit

    def find_asset(self, web_driver, arg):
        """
        定位查看资产元素
        :param web_driver: webdriver.Firefox()
        :param arg: must be dict
        :return:
        """
        view_asset = self.by_xpath(web_driver, arg['view_asset'])
        view_asset.click()
        add_asset = self.by_xpath(web_driver, arg['add_asset'])
        add_asset.click()

    def find_element_single_add_asset(self, web_driver, arg, asset_user_manage_id, asset_host_group_id,
                                      asset_is_activated_id):
        """
        定位单台添加资产元素
        :param web_driver: webdriver.Firefox()
        :param arg: must be dict
        :return:
        """

        if (asset_user_manage_id % 2) == 0:
            host_name = self.by_id(web_driver, arg['host_name'])
            host_ip = self.by_id(web_driver, arg['host_ip'])
            asset_manage_users = self.by_id(web_driver, arg['asset_manage_users'])
            asset_manage_users.click()
            asset_username = self.by_xpath(web_driver, arg['asset_username'])
            asset_password = self.by_xpath(web_driver, arg['asset_password'])
            asset_port = self.by_xpath(web_driver, arg['asset_port'])
            asset_host_group_id = self.by_xpath(web_driver, arg[asset_host_group_id])
            asset_host_group_id.click()
            asset_host_group_id.click()
            if (asset_is_activated_id % 2) == 0:
                assets_is_activation = self.by_xpath(web_driver, arg['assets_is_activation'])
                assets_is_activation.click()
            else:
                assets_is_disabled = self.by_xpath(web_driver, arg['assets_is_disabled'])
                assets_is_disabled.click()
            asset_submit = self.by_xpath(web_driver, arg['asset_submit'])
            return host_name, host_ip, asset_port, asset_username, asset_password, asset_submit

        else:
            host_name = self.by_id(web_driver, arg['host_name'])
            host_ip = self.by_id(web_driver, arg['host_ip'])
            asset_port = self.by_xpath(web_driver, arg['asset_port'])
            asset_host_group_id = self.by_xpath(web_driver, arg[asset_host_group_id])
            asset_host_group_id.click()
            asset_host_group_id.click()
            if (asset_is_activated_id % 2) == 0:
                assets_is_activation = self.by_xpath(web_driver, arg['assets_is_activation'])
                assets_is_activation.click()
            else:
                assets_is_disabled = self.by_xpath(web_driver, arg['assets_is_disabled'])
                assets_is_disabled.click()
            asset_submit = self.by_xpath(web_driver, arg['asset_submit'])
            return host_name, host_ip, asset_port, asset_submit

    # def find_element_batch_add_asset(self, web_driver, arg):
    #     """
    #     定位批量添加资产元素
    #     :param web_driver: webdriver.Firefox()
    #     :param arg: must be dict
    #     :return:
    #     """
    #     pass
    #
    # def view_room(self, web_driver, arg):
    #     pass
