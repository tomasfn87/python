import time as t
import datetime as dt
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from typing import Any, List

class NpmPackage:
    def __init__(
        self:Any, package_name: str, publication_dateDMY: str) -> None:

        self.pName = package_name
        self.pDateDMY = publication_dateDMY

    def show_total_downloads(self, show=True) -> int|None:
        todayYMD:str = str(dt.date.today())
        todayDMY:str = "{}-{}-{}".format(
            todayYMD[8:10], todayYMD[5:7], todayYMD[0:4])

        package_info:List[str] = self.pName.split("/")
        organization: str = ""
        package_name: str = ""

        if len(package_info) == 1:
            package_name = package_info[0]
        elif len(package_info) == 2:
            organization, package_name = package_info[0], package_info[1]

        lPDateYMD: List[str] = self.pDateDMY.split("-")
        pDateYMD: str = f"{lPDateYMD[2]}-{lPDateYMD[1]}-{lPDateYMD[0]}"

        try:
            npm_stat_url: str = "https://npm-stat.com/charts.html?package="
            if organization:
                npm_stat_url += f"{organization.replace('@', '%40')}%2F"
            npm_stat_url += f"{package_name}&from={pDateYMD}&to={todayYMD}"

            options: wd.ChromeOptions = wd.ChromeOptions()
            options.add_argument('--headless')
            browser: wd.Chrome = wd.Chrome(options=options)
            browser.get(npm_stat_url)

            t.sleep(1)
            browser.implicitly_wait(1)

            total_downloads: str = browser.find_elements(
                By.TAG_NAME, 'td')[-1].text
            browser.quit()

            if show == True:
                print(f"package {self.pName}'s")
                print("Total downloads from {}".format(
                    self.pDateDMY.replace('-', '/')))
                print("                  to {}: {}".format(
                    todayDMY.replace('-', '/'), total_downloads))

            return int(total_downloads.replace(",", ""))
        except:
            print("ERRO: não foi possível recuperar os dados. ", end="")
            print("Tente novamente mais tarde.")
            return None

pkg: NpmPackage = NpmPackage(
    package_name="@nighly/sort-object-array-by-property",
    publication_dateDMY="02-02-2022")

pkg.show_total_downloads()
