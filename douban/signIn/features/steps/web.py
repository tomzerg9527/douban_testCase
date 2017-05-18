# -*- coding:utf8 -*-

from selenium import webdriver
from behave import *
import re,sys,time

reload(sys)
sys.setdefaultencoding('utf-8')
browser = webdriver.Firefox()

@Given(u"打开豆瓣网")
def open_url(context):
    browser.get('http://www.douban.com')

@When(u"输入帐号{user}/密码{pwd}")
def input(context,user,pwd):
    browser.find_element_by_xpath(".//*[@id='form_email']").send_keys(user)
    browser.find_element_by_xpath(".//*[@id='form_password']").send_keys(pwd)

@When(u'点击登录')
def click(context):
    browser.find_element_by_xpath(".//*[@id='lzform']/fieldset/div[3]/input").click()