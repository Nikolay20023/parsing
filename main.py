from selenium import webdriver
from tqdm import tqdm_notebook as tqdmn
import pandas as pd
import folium

pd.set_option('display.max_columns', 60)

df = pd.read_excel('C:\\Dev\\parsing\\data\\2021.xlsx', keep_default_na=False)

Url_With_Coordinate = []

option = webdriver.ChromeOptions()
prefs = {'profile.default_content_setting_values': {'images': 2, 'javascript': 2}}
option.add_experimental_option('prefs', prefs)


driver = webdriver.Chrome('C:\\Dev\\parsing\\chromedriver.exe')

for url in tqdmn(df['Url'], leave=False):
    driver.get(url)
    Url_With_Coordinate.append(driver.find_element_by_css_selector('meta[itemprop=image]').get_attribute('content'))

driver.close()
