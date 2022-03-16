import time as t
import datetime as dt
from selenium import webdriver # control the browser
from selenium.webdriver.common.keys import Keys # keyboard
from selenium.webdriver.common.by import By # access HTML elements

class NpmPackage:
    def __init__(self, package_name, publication_date):
        # '@organization/name' or 'name'
        self.pname = package_name
        
        # DD-MM-YYYY
        self.pdate = publication_date
    
    def show_total_downloads(self, show=True):
        # YYYY-MM-DD -> DD-MM-YYYY
        today = str(dt.date.today())
        today = f"{today[8:10]}-{today[5:7]}-{today[0:4]}"
        
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')

        browser = webdriver.Chrome(options=options)

        # search for 'npm-stat'
        browser.get("https://www.duckduckgo.com/")
        browser.find_element(By.XPATH, '//*[@id="search_form_input_homepage"]').send_keys("npm-stat", Keys.ENTER)
        # enter 'https://npm-stat.com/'
        browser.find_element(By.XPATH, '//*[@id="r1-0"]/div/h2/a[1]').click()

        # reach search fields and enter package name, publication date and today's date
        browser.find_element(By.XPATH, '//*[@id="name"]').send_keys(
                self.pname, Keys.TAB, self.pdate.replace("-", ""), Keys.TAB, today.replace("-", ""), Keys.ENTER)

        t.sleep(2)
        browser.implicitly_wait(2)

        # get total downloads from <body>
        td_list = browser.find_elements(By.TAG_NAME, 'td')
        total_downloads = td_list[-1].text

        browser.quit()

        if show == True:
            print(f"package {self.pname}'s")
            print(f"Total downloads from {self.pdate.replace('-', '/')}")
            print(f"                  to {today.replace('-', '/')}: {total_downloads}")
        else:
            return(int(total_downloads.replace(",", "")))

pkg = NpmPackage(package_name="@nighly/sort-object-array-by-property", publication_date="02-02-2022")

pkg.show_total_downloads()
