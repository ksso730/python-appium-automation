
# -*- coding: utf-8 -*-
import os
from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def setUp(serverIp, port):
    # serverIp = '192.168.25.185'
    # port = '5555'
    udid = '{0}:{1}'.format(serverIp, port)

    driver = webdriver.Remote(
        #command_executor='http://192.168.25.178:7100/wd/hub',
        command_executor='http://127.0.0.1:4723/wd/hub',
        desired_capabilities={
                'app': 'C:\\APPIUM\\apk\\toss.apk',
                'platformName': 'Android',
                'platformVersion': '10',
                'deviceName': 'Galaxy 10',
                'automationName': 'Appium',
                'appPackage': 'viva.republica.toss',
                'appActivity': 'viva.republica.toss.splash.SplashActivity',
                'udid': udid,
                'newCommandTimeout': 300,
                'noReset': True
            })
    wait = WebDriverWait(driver, 20)
    sleep(3)
    return driver

def tearDown():
    driver.quit()


def goStock():
    wait = WebDriverWait(driver, 20)
    # stockPath = '//android.view.ViewGroup[@content-desc="주식 탭"]/android.widget.LinearLayout/android.widget.ImageView'
    stockPath = '//android.view.ViewGroup[@content-desc="주식 탭" and @index=3]'
    stockBtn= driver.find_element_by_xpath(stockPath)
    stockBtn.click()
    sleep(30)

def searchStocks(param):
    searchBtnPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.widget.ListView/android.view.View[1]/android.widget.Button'
    searchBox = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View/android.widget.EditText'
    


if (__name__=='__main__'):
   
    # load driver
    driver = setUp('192.168.25.185','5555')
    
    # 주식탭
    goStock()

    # 검색
    # searchString="삼성"
    # searchStocks(searchString)

    tearDown()