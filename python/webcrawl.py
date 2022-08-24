from selenium import webdriver
from selenium.webdriver.common.by import By

# pip install chromedriver-autoinstaller 
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

driver.implicitly_wait(5)

driver.set_window_size(1920,1280)

keyword = '코로나'
driver.get(f'https://search.naver.com/search.naver?query={keyword}')


se = '#_cs_production_type > div > div.main_tab_area > div > div > ul > li.info_01 > p'
we = driver.find_element(By.CSS_SELECTOR,se)
print(we.text)




input()
driver.quit()