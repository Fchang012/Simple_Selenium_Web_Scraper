import pandas as pd
from selenium import webdriver
from Class_Extract_Apt_Data import Extract_Apt_Data

#Main Script
if __name__ == "__main__":

    driver = webdriver.Firefox(executable_path="C:\\Users\\fh_ch\\AppData\\Local\\Programs\\Python\\Python37\\Environments\\Selenium\\bin\\geckodriver.exe")
    
    #Westside
    df_Westside = Extract_Apt_Data('http://www.thevillagedallas.com/neighborhoods/westside.html', 'Westside').extractData(driver)

    #Dakota
    df_Dakota = Extract_Apt_Data('http://www.thevillagedallas.com/neighborhoods/dakota.html', 'Dakota').extractData(driver)

    #NorthBridge
    df_NorthBridge = Extract_Apt_Data('http://www.thevillagedallas.com/neighborhoods/northbridge.html', 'North_Bridge').extractData(driver)

    #Upper_East_Side
    df_Upper_East_Side = Extract_Apt_Data('http://www.thevillagedallas.com/neighborhoods/upper-east-side.html', 'Upper_East_Side').extractData(driver)

    #Lakes
    df_Lakes = Extract_Apt_Data('http://www.thevillagedallas.com/neighborhoods/lakes.html', 'Lakes').extractData(driver)

    #Combine all
    frames = [df_Westside, 
                df_Dakota,
                df_NorthBridge,
                df_Upper_East_Side,
                df_Lakes]

    df = pd.concat(frames)

    #Write to Excel
    with pd.ExcelWriter('Apt_Compare.xlsx') as writer:
        df.to_excel(writer, sheet_name = 'RAW_DATA', index = False)

    driver.quit()