from selenium import webdriver
from selenium.webdriver.common.keys import Keys

SELENIUM_DOC = "https://selenium-python.readthedocs.io/locating-elements.html"
#
chrome_driver_path = "F:/udemy/chromedriver"
#
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
#
# driver.get("https://www.w3schools.com/")
#
# search = driver.find_element('search2')
# print(search.get_attribute("placeholder"))
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver.get("https://de.aliexpress.com/item/1005003961611840.html?spm=a2g0o.productlist.0.0.649860464lcWKb&algo_pvid"
#            "=641750ef-aa36-4508-9fcc-85955cf999c1&aem_p4p_detail=202210171322357110430278219400000887137&algo_exp_id"
#            "=641750ef-aa36-4508-9fcc-85955cf999c1-0&pdp_ext_f=%7B%22sku_id%22%3A%2212000027576630493%22%7D&pdp_npi=2"
#            "%40dis%21EUR%21224.49%21179.59%21%21%21%21%21%402103399116660381559348699e3be8%2112000027576630493%21sea"
#            "&curPageLogUid=03WDpLKcbMhX&ad_pvid=202210171322357110430278219400000887137_1")
# price = driver.find_element(By.CLASS_NAME, "product-price-value")
# price = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[5]/div[1]/span/font/font')
# logo = driver.find_element(By.CLASS_NAME, "logo-base")
# print(price.text)
# print(logo.size)

driver.get("https://www.python.org/")
event_times = driver.find_elements(By.CSS_SELECTOR, ".shrubbery time")
event_name = driver.find_elements(By.CSS_SELECTOR, ".shrubbery li a")

events={

}
for n in range(len(event_times)):

    events[n]= {
        "time": event_times[n].text,
        "name": event_name [n].text
    }

print(events)

driver.quit()

# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://www.google.com")
