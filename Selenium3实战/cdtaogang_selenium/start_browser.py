from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('http://www.5itest.cn/register')
time.sleep(3)
res = ec.title_contains('注册')  # 不需要定位元素，直接查找是否有特定文本字样
print(res)

locator = (By.CLASS_NAME, 'controls')
result = ec.visibility_of_element_located(locator)
WebDriverWait(driver, 1).until(result)

email_element = driver.find_element_by_id("register_email")
print(email_element.get_attribute("placeholder"))
email_element.send_keys("xxx@163.com")
print(email_element.get_attribute("value"))

# location：始终不滚动，返回相对整个html或者对应frame的坐标
# location_once_scrolled_into_view：
# chrome完全可见不滚动，firefox始终会滚动；而且chrome底部元素会底部对齐，其余情况两者都是顶部对齐。
# 一般返回相对可视区域坐标，但是firefox的frame依旧返回相对frame的坐标
driver.save_screenshot('./data/captcha.png')
code_element = driver.find_element_by_id('getcode_num')
print(code_element.location)
x = code_element.location['x']
y = code_element.location['y']
width = code_element.size['width'] + x
height = code_element.size['height'] + y
im = Image.open('./data/captcha.png')
img = im.crop((x, y, width, height))  # 裁剪图片
img.save('./data/captcha_1.png')
# 需要编写识别验证码的流程，可使用第三方库进行识别


# driver.find_element_by_id("register_email").send_keys("cdtaogang@163.com")
# # driver.find_element_by_class_name("controls").find_element_by_class_name("form-control").send_keys("cdtaogang@163.com")
# driver.find_element_by_id("register_nickname").send_keys("cdtaogang")
# driver.find_element_by_id("register_password").send_keys("111111")
# driver.find_element_by_xpath('//*[@id="captcha_code"]').send_keys("xrfdw")



driver.close()
