import pandas as pd
import re
from selenium import webdriver

class Extract_Apt_Data:
    def __init__(self, theURL, AptCmplx):
        self.dtheURL = theURL
        self.dAptCmplx = AptCmplx

    #Deal with higher end Apts
    def extractData(self, driver):

        #Apt URL
        driver.get(self.dtheURL)

        tempTable = driver.find_element_by_class_name('au-table')
        rows = tempTable.find_elements_by_tag_name('tr')

        cols = ['Apt_Complex', 'Unit', 'Rent_Low','Rent_High', 'Sq_Ft', 'Baths', 'Available']
        df = pd.DataFrame(index = range(len(rows)-1), columns = cols)

        i = 0

        for row in rows:
            if row.text == 'UNIT RENT SQ FT BATHS AVAILABLE':
                continue
            else:
                dApt_Complex = self.dAptCmplx

                dUnit = row.find_elements_by_tag_name('td')[0].text
                dRent_Low = row.find_elements_by_tag_name('td')[1].text.split("-")[0]
                dRent_High = row.find_elements_by_tag_name('td')[1].text.split("-")[1]
                dSq_Ft = row.find_elements_by_tag_name('td')[2].text
                dBaths = row.find_elements_by_tag_name('td')[3].text
                dAvailable = row.find_elements_by_tag_name('td')[5].text

                df.iloc[i] = [dApt_Complex, dUnit, dRent_Low, dRent_High, dSq_Ft, dBaths, dAvailable]

                i += 1

        
        return df