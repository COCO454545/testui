# -*- coding: utf-8 -*-
# @Time : 2023/10/23 15:14
# @Author : Lenovo
# @Email : 953215836@qq.com
# @File : testdriver.py
# @Project : pythonknowledge
# @desc :
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located, presence_of_all_elements_located
from selenium.webdriver.chrome.service import Service as chromeservice
from autotest.common.getdriver import GetDriver

# op=webdriver.ChromeOptions()####配置浏览器的选项类 可用于设置chromedriver实例参数
# op.add_experimental_option("detach", True)######添加实质性的选项 例如启动无头模式
# driver = webdriver.Chrome(options=op)
# driver.maximize_window()


# op=webdriver.ChromeOptions()####配置浏览器的选项类 可用于设置chromedriver实例参数
# op.add_experimental_option("detach", True)######添加实质性的选项 例如启动无头模式
# driver = webdriver.Chrome(options=op)
# # op.binary_location=r'D:\python\project\python学习\autotest\drivers\chromedriver.exe'
# driver.get("https://app-yd.solutions.iqvia.cn/sit/pc#/login")
#
# driver.find_element('xpath','//input[@name="Username"]').send_keys("13600000023")


# options = webdriver.ChromeOptions()  ####  实例化谷歌浏览器   配置浏览器的选项类 可用于设置chromedriver实例参数
# # driver_path =r'D:\python\iter\Scripts\chromedriver.exe'
# driver_path =r"D:\python\project\python学习\autotest\drivers\chromedriver.exe"
# s = Service(r"D:\python\project\python学习\autotest\drivers\chromedriver.exe")
# abc=Service(r"D:\python\iter\Scripts\chromedriver.exe")
# # #
# options.add_experimental_option("detach", True)######添加实质性的选项 例如启动无头模式
# # options.add_experimental_option("useAutomationExtension", False)######添加实质性的选项 例如启动无头模式
#
# # options.add_argument("headless") ######将浏览器设置成无界面模式  适用于服务器上面运行
# driver = webdriver.Chrome(service=Service(driver_path),options=options)
# # driver = webdriver.Chrome(service=abc)
# driver.maximize_window()
# driver.get("https://app-yd.solutions.iqvia.cn/sit/pc#/login")



# s = Service(executable_path=r"D:\python\project\python学习\python_ui部分\pythonui自动化\drivers\chromedriver.exe")
# driver=webdriver.Chrome(service=s)
# ###driver的相关操作
# # driver.get('https://app-yd.solutions.iqvia.cn/sit/pc#/')  ###访问指定网址
# driver.get('http://localhost:8080/WoniuSales_V1_3_bin/goods')
# driver.maximize_window()  # 窗口最大化
from autotest.conf.pathconfig import PathConfig

options = webdriver.ChromeOptions()  ####  实例化谷歌浏览器   配置浏览器的选项类 可用于设置chromedriver实例参数
driver_path = r"D:\python\project\python学习\autotest\drivers\chromedriver.exe"
options.add_experimental_option("detach", True)######添加实质性的选项 例如启动无头模式
options.add_argument('--ignore-ssl-errors')
options.add_argument("--no-sandbox")
options.add_argument('--enable-logging')
options.add_argument('--v=1')
# options.add_experimental_option('useAutomationExtension', False)
# options.add_argument("headless") ######将浏览器设置成无界面模式  适用于服务器上面运行
driver = webdriver.Chrome(service=chromeservice(PathConfig.Chromedriver),options=options)
driver.maximize_window()
# time.sleep(10)
driver.get('https://app-yd.solutions.iqvia.cn/sit/pc#/login')
driver.find_element(By.XPATH, '//input[@name="Username"]').send_keys("13600000020")
driver.find_element(By.XPATH, '//input[@name="Password"]').send_keys("Zz1234567890")

"""
options = webdriver.ChromeOptions()
options.add_argument('lang=zh_CN.utf-8')  # 设置默认编码为utf-8
options.add_argument('--no-sandbox') # # 以最高权限运行
options.add_argument('--user-agent=""')  # 设置请求头的User-Agent
options.add_argument('--window-size=1280x1024')  # 设置浏览器分辨率（窗口大小）
options.add_argument('--start-maximized')  # 最大化运行（全屏窗口）,不设置，取元素会报错
options.add_argument('--disable-infobars')  # 禁用浏览器正在被自动化程序控制的提示
options.add_argument('--incognito')  # 隐身模式（无痕模式）
options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
options.add_argument('--disable-javascript')  # 禁用javascript
options.add_argument('--blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
options.add_argument('--headless')  # 浏览器不提供可视化页面
options.add_argument('--ignore-certificate-errors')  # 禁用扩展插件并实现窗口最大化
options.add_argument('--disable-gpu')  # 禁用谷歌浏览器GPU加速-配置1
options.add_argument('–disable-software-rasterizer')  # 禁用谷歌浏览器GPU加速-配置2
options.add_argument('--disable-extensions')  #禁用扩展插件
options.add_argument("--proxy-server=http://" + ip_port) # HTTP代理
options.add_experimental_option('useAutomationExtension', False) # # 取消chrome受自动控制提示
option.add_experimental_option("excludeSwitches", ['enable-automation'])  # 正常浏览器window.navigator.webdriver的值为undefined,而使用selenium访问则该值为true,该方法规避这种风险。
这里是测试gitee的更新操作
这是最后一次修改专门测试远程仓库的更新操作
特试探试探推三推四
"""
