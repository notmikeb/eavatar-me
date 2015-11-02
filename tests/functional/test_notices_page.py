# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

from selenium import webdriver

from webpages import *


class TestNoticesPage(PageTest):

    def setUp(self):
        super(TestNoticesPage, self).setUp()
        self.home_page = NoticesPage(self.browser, self.live_server_url, self.access_token)

    def test_should_find_page_div(self):
        self.home_page.open()
        div = self.browser.find_element_by_id('notices')
        assert div is not None
