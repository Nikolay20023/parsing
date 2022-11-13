from selenium import webdriver
from tqdm import tqdm_notebook as tqdmn
import pandas as pd
import folium

pd.set_option('display.max_columns', 60)

acnc = pd.read_excel('data/datadotgov_main.xlsx', keep_default_na=False)

mel = acnc[acnc.Town_City.str.contains('melbourne', case=False)][
    [
        'ABN',
        'Charity_Legal_Name',
        'Address_Line_1',
        'Address_Line_2',
        'Address_Line_3',
        'Town_City',
        'State',
        'Postcode',
        'Country',
        'Date_Organisation_Established',
        'Charity_Size',
    ]
].copy()

mel.Town_City.value_counts()
mel.head()

mel['Full_Address'] = mel['Address_Line_1'].str.cat(mel[['Address_Line_2', 'Address_Line_3', 'Town_City']], sep=' ')
