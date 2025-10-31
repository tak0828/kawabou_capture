from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from datetime import datetime, timedelta
import time
import CONST
from sitebase import SiteBase


class Kawabou(SiteBase):
    def __init__(self,window_width:int=1920,window_height:int=1500,debug:bool=False):
        super().__init__(window_width=window_width,window_height=window_height,debug=debug)

    # ログイン
    def login(self):
        print("login kawabou")
        self.get_page("https://city.river.go.jp/kawabou/cityLogin.do")
        self.driver.find_element(By.XPATH, '//*[@id="userId"]').send_keys(self.user)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(self.pwd)
        self.driver.find_element(By.XPATH, '//*[@id="login"]').click()
        time.sleep(5)  # ログイン処理が終わるまで待機


def main():
    kawabou = Kawabou(debug=True)
    kawabou.register("CFRICSTEST4","fricstest4")
    kawabou.login()
    kawabou.save_screenshot_png("temp.png")

if __name__ == "__main__":
    main()