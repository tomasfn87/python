import time as t
import datetime as dt
from selenium import webdriver # control the browser
from selenium.webdriver.common.keys import Keys # keyboard
from selenium.webdriver.common.by import By # access HTML elements

class NpmPackage:
    def __init__(self, package_name, publication_dateDMY):
        # '@organization/name' or 'name'
        self.pname = package_name
        
        # DD-MM-YYYY
        self.pdateDMY = publication_dateDMY
    
    def show_total_downloads(self, show=True):
        # YYYY-MM-DD -> DD-MM-YYYY
        todayYMD = str(dt.date.today())
        todayDMY = f"{todayYMD[8:10]}-{todayYMD[5:7]}-{todayYMD[0:4]}"
        
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')

        browser = webdriver.Chrome(options=options)

        package_info = self.pname.split("/")
        organization = package_info[0]
        package_name = package_info[1]
        
        # DD-MM-YYYY -> YYYY-MM-DD
        pdateDMY = self.pdateDMY.split("-")
        pdateYMD = f"{pdateDMY[2]}-{pdateDMY[1]}-{pdateDMY[0]}"

        # format 'npm-stat' package search from publication date to today
        npm_stat_url = f"https://npm-stat.com/charts.html?package={organization}%2F{package_name}&from={pdateYMD}&to={todayYMD}"

        browser.get(npm_stat_url)

        t.sleep(1)
        browser.implicitly_wait(1)

        # get total downloads from <td>
        td_list = browser.find_elements(By.TAG_NAME, 'td')
        total_downloads = td_list[-1].text

        browser.quit()

        if show == True:
            print(f"package {self.pname}'s")
            print(f"Total downloads from {self.pdateDMY.replace('-', '/')}")
            print(f"                  to {todayDMY.replace('-', '/')}: {total_downloads}")
        else:
            return(int(total_downloads.replace(",", "")))

pkg = NpmPackage(package_name="@nighly/sort-object-array-by-property", publication_dateDMY="02-02-2022")

pkg.show_total_downloads()
