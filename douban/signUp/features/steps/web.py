# -*- coding:utf8 -*-

from selenium import webdriver
from behave import Given,When,Then
import sys,re,time

reload(sys)
sys.setdefaultencoding('utf-8')
browser = webdriver.Firefox()

@Given(u'打开豆瓣网点击注册')
def before(context):
    browser.get('http://www.douban.com')
    browser.find_element_by_xpath(".//*[@id='lzform']/fieldset/div[3]/a").click()

@When(u'输入帐号{user}/密码{pwd}/名号{nick}/手机号{phone}')
def input_impl(context,user,pwd,nick,phone):
    time.sleep(3)
    browser.find_element_by_xpath(".//*[@id='email']").clear()
    browser.find_element_by_xpath(".//*[@id='email']").send_keys(user)
    browser.find_element_by_xpath(".//*[@id='password']").clear()
    browser.find_element_by_xpath(".//*[@id='password']").send_keys(pwd)
    browser.find_element_by_xpath(".//*[@id='name']").clear()
    browser.find_element_by_xpath(".//*[@id='name']").send_keys(nick)
    browser.find_element_by_xpath('.//*[@id="verify_phone_num"]').clear()
    browser.find_element_by_xpath('.//*[@id="verify_phone_num"]').send_keys(phone)

@When(u'点击获取验证码')
def click_impl(context):
    browser.find_element_by_xpath(".//*[@id='request-phone-code-btn']").click()

@When(u'输入验证码{text}')
def input_fuck(context,text):
    browser.find_element_by_xpath(".//*[@id='code']").send_keys(text)

@When(u'勾选同意')
def click_agree(context):
    browser.find_element_by_xpath(".//*[@id='agreement']").click()

@When(u'点击注册')
def click_sign(context):
    browser.find_element_by_xpath(".//*[@id='button']").click()
