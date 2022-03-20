import time as t
import datetime as dt
from selenium import webdriver  # control the browse
from selenium.webdriver.common.by import By  # access HTML elements

class NpmPackage:
    def __init__(self, package_name, publication_dateDMY):
        self.pname = package_name
        self.pdateDMY = publication_dateDMY

    def show_total_downloads(self, show=True):
        todayYMD = str(dt.date.today())
        todayDMY = f"{todayYMD[8:10]}-{todayYMD[5:7]}-{todayYMD[0:4]}"

        package_info = self.pname.split("/")
        organization, package_name = "", ""

        if len(package_info) == 1:
            package_name = package_info[0]
        elif len(package_info) == 2:
            organization, package_name = package_info[0], package_info[1]

        pdateYMD = self.pdateDMY.split("-")
        pdateYMD = f"{pdateYMD[2]}-{pdateYMD[1]}-{pdateYMD[0]}"

        npm_stat_url = "https://npm-stat.com/charts.html?package="
        if organization:
            npm_stat_url += f"{organization}%2F"
        npm_stat_url += f"{package_name}&from={pdateYMD}&to={todayYMD}"

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        browser = webdriver.Chrome(options=options)
        browser.get(npm_stat_url)
        t.sleep(1)
        browser.implicitly_wait(1)
        total_downloads = browser.find_elements(By.TAG_NAME, 'td')[-1].text
        browser.quit()

        if show == True:
            print(f"package {self.pname}'s")
            print(f"Total downloads from {self.pdateDMY.replace('-', '/')}")
            print(f"                  to {todayDMY.replace('-', '/')}: {total_downloads}")

        return int(total_downloads.replace(",", ""))

pkg = NpmPackage(
    package_name="@nighly/sort-object-array-by-property",
    publication_dateDMY="02-02-2022")

print(pkg.show_total_downloads())
