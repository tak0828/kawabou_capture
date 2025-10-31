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
    
    # 降雨グラフスクリーンショット
    def screenshot_rain_graph(self,areacode=83):
        self.__rain_graph(areacode)
        self.save_screenshot_png("rain_graph.png")

    # レーダ雨量（現況）Cバンドスクリーンショット
    def screenshot_radar_genkyo(self,prefcode=1301):
        self.__radar_genkyo(prefcode)
        self.save_screenshot_png("radar_genkyo.png")
    
    # 降雨グラフページ
    def __rain_graph(self,areacode):
        self.get_page(f"https://city.river.go.jp/kawabou/cityRainKobetuMlt.do?requestType=1&init=city&gamenId=02-0903&areaCd={areacode}&rvrsysCd=&prefCd=&townCd=")
    # レーダ雨量（現況）Cバンド
    def __radar_genkyo(self,prefcode):
        self.get_page(f"https://city.river.go.jp/kawabou/cityRadarGenkyo.do?init=init&prefCd={prefcode}&gamenId=03-1801")


def main():
    kawabou = Kawabou(debug=True)
    kawabou.register("CFRICSTEST4","fricstest4")
    kawabou.login()
    kawabou.screenshot_radar_genkyo()

if __name__ == "__main__":
    main()