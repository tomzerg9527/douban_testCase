Feature: 豆瓣注册功能测试
  Scenario: 邮箱注册
  Given 打开豆瓣网点击注册
  When 输入帐号68291094@qq.com/密码OldSoldiers1257/名号fuckCenter/手机号18817314957
  When 点击获取验证码
  When 输入验证码fuck
  When 勾选同意
  When 点击注册
