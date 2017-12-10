import config
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from pyquery import PyQuery as pq


def login():
    driver =config.DRIVER
    driver.get(config.LOGIN_URL)
    input("完成登陆后按回车键继续")

    try:
        WebDriverWait(driver,config.TIMEOUT).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.indexwdks a[href]")))
    except TimeoutException:
        print("超时")

    try:
        exam_btn = driver.find_element_by_css_selector("div.indexwdks a[href]")
        exam_btn.send_keys(Keys.ENTER)
    except NoSuchElementException:
        print("没有找到我的考试")

    try:
        WebDriverWait(driver, config.TIMEOUT).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "ul#currcontainer a[href]")))
    except TimeoutException:
        print("超时")

    try:
        exam_btn = driver.find_element_by_css_selector("ul#currcontainer a[href]")
        exam_btn.send_keys(Keys.ENTER)
    except NoSuchElementException:
        print("没有找到进入考试 ")

    switch_new(driver)

    try:
        WebDriverWait(driver, config.TIMEOUT).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div#timucontent")))
    except TimeoutException:
        print("超时")
    return driver



def answer(driver):
    while(1):
        doc = get_html(driver)
        question = doc('#timucontent h2').text()
        print(question)
        try:
            option = driver.find_element_by_css_selector('input[value=A]')
            option.click()
        except NoSuchElementException:
            print("no A ")
        try:
            option = driver.find_element_by_css_selector('input[value="1"]')
            option.click()
        except NoSuchElementException:
            print("no 1 ")
        try:
            next = driver.find_element_by_css_selector('[id=nextButton]')
            next.click()
        except NoSuchElementException:
            print("没有找到下一题 ")
            break

    # print(doc('#timucontent h2').text())

def get_html(driver):
    html = driver.page_source
    # 必须去掉xmlns属性，不然不能正确解析
    html = html.replace('xmlns','another_attr')
    return pq(html)

def switch_new(driver):
    # 获取所有页面的句柄，并循环判断不是当前的句柄
    for handle in driver.window_handles:
        if(handle != driver.current_window_handle):
            driver.close()
            driver.switch_to.window(handle)
            break

if __name__ =='__main__':
    driver = login()
    answer(driver)
    # driver.close()