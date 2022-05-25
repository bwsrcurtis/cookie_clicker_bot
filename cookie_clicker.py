import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "F:/Downloads/Coding and Data Stuff/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")
# cookie.click()
cookies_count = int(driver.find_element_by_id("money").text)

cursor = driver.find_element_by_id("buyCursor")
cursor_num = int(
    driver.find_element_by_css_selector("#store #buyCursor b")
    .text.split("-")[1]
    .strip()
    .replace(",", "")
)
print(cursor_num)
grandma = driver.find_element_by_id("buyGrandma")
grandma_num = int(
    driver.find_element_by_css_selector("#store #buyGrandma b")
    .text.split("-")[1]
    .strip()
    .replace(",", "")
)
factory = driver.find_element_by_id("buyFactory")
factory_num = int(
    driver.find_element_by_css_selector("#store #buyFactory b")
    .text.split("-")[1]
    .strip()
    .replace(",", "")
)
mine = driver.find_element_by_id("buyMine")
mine_num = int(
    driver.find_element_by_css_selector("#store #buyMine b")
    .text.split("-")[1]
    .strip()
    .replace(",", "")
)
shipment = driver.find_element_by_id("buyShipment")
shipment_num = int(
    driver.find_element_by_css_selector("#store #buyShipment b")
    .text.split("-")[1]
    .strip()
    .replace(",", "")
)
alchemy_lab = driver.find_element_by_id("buyAlchemy lab")
alchemy_lab_num = int(
    driver.find_element_by_css_selector("#store #buyAlchemy\ lab b")
    .text.split("-")[1]
    .strip()
    .replace(",", "")
)
portal = driver.find_element_by_id("buyPortal")
portal_num = int(
    driver.find_element_by_css_selector("#store #buyPortal b")
    .text.split("-")[1]
    .strip()
    .replace(",", "")
)
time_machine = driver.find_element_by_id("buyTime machine")
time_machine_num = int(
    driver.find_element_by_css_selector("#store #buyTime\ machine b")
    .text.split("-")[1]
    .strip()
    .replace(",", "")
)

timeout = time.time() + 2
five_min = time.time() + 60 * 5  # 5minutes


while True:
    cookie = driver.find_element_by_id("cookie")
    cookie.click()
    # time.sleep(.01)
    if time.time() > timeout:
        cookies_count = int(driver.find_element_by_id("money").text.replace(",", ""))
        time_machine_num = int(
            driver.find_element_by_css_selector("#store #buyTime\ machine b")
            .text.split("-")[1]
            .strip()
            .replace(",", "")
        )
        portal_num = int(
            driver.find_element_by_css_selector("#store #buyPortal b")
            .text.split("-")[1]
            .strip()
            .replace(",", "")
        )
        alchemy_lab_num = int(
            driver.find_element_by_css_selector("#store #buyAlchemy\ lab b")
            .text.split("-")[1]
            .strip()
            .replace(",", "")
        )
        shipment_num = int(
            driver.find_element_by_css_selector("#store #buyShipment b")
            .text.split("-")[1]
            .strip()
            .replace(",", "")
        )
        mine_num = int(
            driver.find_element_by_css_selector("#store #buyMine b")
            .text.split("-")[1]
            .strip()
            .replace(",", "")
        )
        factory_num = int(
            driver.find_element_by_css_selector("#store #buyFactory b")
            .text.split("-")[1]
            .strip()
            .replace(",", "")
        )
        grandma_num = int(
            driver.find_element_by_css_selector("#store #buyGrandma b")
            .text.split("-")[1]
            .strip()
            .replace(",", "")
        )
        
        if cookies_count > time_machine_num:

            time_machine = driver.find_element_by_id("buyTime machine")
            time_machine.click()
        elif cookies_count > portal_num and portal_num < 100000000:

            portal = driver.find_element_by_id("buyPortal")
            portal.click()
        elif cookies_count > alchemy_lab_num and alchemy_lab_num < 750000:

            alchemy_lab = driver.find_element_by_id("buyAlchemy lab")
            alchemy_lab.click()
        elif cookies_count > shipment_num and shipment_num < 30000:

            shipment = driver.find_element_by_id("buyShipment")
            shipment.click()
        elif cookies_count > mine_num and mine_num < 5000:

            mine = driver.find_element_by_id("buyMine")
            mine.click()
        elif cookies_count > factory_num and factory_num < 1400:

            factory = driver.find_element_by_id("buyFactory")
            factory.click()
        elif cookies_count > grandma_num and grandma_num < 350:

            grandma = driver.find_element_by_id("buyGrandma")
            grandma.click()
            
        # elif cookies_count > cursor_num and cursor_num < 60:
           
        #     cursor = driver.find_element_by_id("buyCursor")
        #     cursor.click()
        timeout = time.time() + 5
    elif time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break
