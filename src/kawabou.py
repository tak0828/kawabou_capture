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
# from utils import load_csv_as_records,build_index


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


############################################################################################
####            スクリーンショット　処理群                                              ######
############################################################################################
    # 概況図スクリーンショット
    def screenshot_gaikyo_map(self):
        self.__city_top_gaikyo_map()
        self.save_screenshot_png("city_top_gaikyo_map.png")

    # 雨量グラフスクリーンショット
    def screenshot_rain_graph(self,areacode=83):
        self.__rain_graph(areacode)
        self.save_screenshot_png("rain_graph.png")
    
    # 雨量グラフ(対象観測所)スクリーンショット
    # 例は、篠崎
    def screenshot_rain_graph_kobetu(self,areacode=2127900100003):
        self.__rain_graph_kobetu(areacode)
        self.save_screenshot_png("rain_graph_kobetu.png")

    # 市町村向け川の防災(時間雨量グラフ)スクリーンショット
    # 例は、篠崎
    def screenshot_city_rain_kobetu(self,areacode=2127900100003):
        self.__city_rain_kobetu(areacode)
        self.save_screenshot_png("city_rain_kobetu.png")

    # 市町村向け川の防災(経過表)スクリーンショット
    # 例は、東京都
    def screenshot_city_rain_keika(self,prefcode=1301):
        self.__city_rain_keika(prefcode)
        self.save_screenshot_png("city_rain_keika.png")

    # 時間雨量経過表スクリーンショット
    # 例は、東京都
    def screenshot_rain_keika(self,prefcode=1301):
        self.__rain_keika(prefcode)
        self.save_screenshot_png("rain_keika.png")

    # レーダ雨量（現況）Cバンドスクリーンショット
    def screenshot_radar_genkyo(self,prefcode=1301):
        self.__radar_genkyo(prefcode)
        self.save_screenshot_png("radar_genkyo.png")

    # 時刻水位・流量経過表
    # 例は東京都
    def screenshot_suii_keika(self,prefcode=1301):
        self.__suii_keika(prefcode)
        self.save_screenshot_png("suii_keika.png")
    # 時刻水位・流量経過表
    # 例は高砂
    def screenshot_suii_keika_kobetu(self,areacode=2127900400049):
        self.__suii_keika_kobetu(areacode)
        self.save_screenshot_png("suii_keika_kobetu.png")

    # 時刻ダム情報経過表
    # 例は東京都
    def screenshot_dam_keika(self,prefcode=1301):
        self.__dam_keika(prefcode)
        self.save_screenshot_png("dam_keika.png")

    # 時刻ダム情報グラフ
    # 例は白丸調整池
    def screenshot_dam_kobetu(self,areacode:str="0332900700101"):
        self.__dam_kobetu(areacode)
        self.save_screenshot_png("dam_kobetu.png")

############################################################################################
####            ページ表示 処理群                                                      ######
############################################################################################
    
    # 概況図ページ
    # 地方選択方法がわからないので、引数なし、要確認
    def __city_top_gaikyo_map(self):
        self.get_page(f"https://city.river.go.jp/kawabou/cityTopGaikyoMap.do?init=init&gamenId=02-0201")
    # 雨量グラフページ
    def __rain_graph(self,areacode):
        self.get_page(f"https://city.river.go.jp/kawabou/cityRainKobetuMlt.do?requestType=1&init=city&gamenId=02-0903&areaCd={areacode}&rvrsysCd=&prefCd=&townCd=")
    # 雨量グラフ(対象観測所)ページ
    def __rain_graph_kobetu(self,areacode):
        self.get_page(f"https://city.river.go.jp/kawabou/cityRainKobetu.do?init=init&obsrvId={areacode}&gamenId=03-0803&timeType=60&requestType=1")
    # 市町村向け川の防災(時間雨量グラフ)
    def __city_rain_kobetu(self,areacode):
        self.get_page(f"https://city.river.go.jp/kawabou/cityRainKobetu.do?obsrvId={areacode}&gamenId=03-0803&requestType=1&init=city")

    # 市町村向け川の防災(経過表)
    def __city_rain_keika(self,prefcode):
        self.get_page(f"https://city.river.go.jp/kawabou/cityRainKeika.do?init=init&prefCd={prefcode}&gamenId=03-0801")

    # 時間雨量経過表ページ
    def __rain_keika(self,prefcode):
        self.get_page(f"https://city.river.go.jp/kawabou/cityRainKeika.do?init=init&prefCd={prefcode}&gamenId=03-0801")
    # レーダ雨量（現況）Cバンド
    def __radar_genkyo(self,prefcode):
        self.get_page(f"https://city.river.go.jp/kawabou/cityRadarGenkyo.do?init=init&prefCd={prefcode}&gamenId=03-1801")

    # 時刻水位・流量経過表ページ
    def __suii_keika(self,prefcode):
        self.get_page(f"https://city.river.go.jp/kawabou/citySuiiKeika.do?requestType=1&init=city&gamenId=03-1001&areaCd=&rvrsysCd=&prefCd={prefcode}&townCd=&stgGrpKind=crsSect")

    # 時刻水位・流量経過表ページ(対象観測所)
    def __suii_keika_kobetu(self,areacode):
        self.get_page(f"https://city.river.go.jp/kawabou/citySuiiKobetu.do?obsrvId={areacode}&gamenId=03-1005&stgGrpKind=survFore&fvrt=yes")

    # 水位グラフ
    # def __suii_kobetu(self,areacode):
    #     self.get_page(f"https://city.river.go.jp/kawabou/citySuiiKobetu.do?obsrvId={areacode}&gamenId=03-1005&stgGrpKind=survFore&fvrt=yes")

    # 時刻ダム情報経過表
    def __dam_keika(self,prefcode):
        self.get_page(f"https://city.river.go.jp/kawabou/cityDamKeika.do?init=init&prefCd={prefcode}&townCd=&areaCd=&rvrsysCd=&gamenId=03-1101")

    # 時刻ダム情報グラフ
    def __dam_kobetu(self,areacode):
        self.get_page(f"https://city.river.go.jp/kawabou/cityDamKobetu.do?init=init&obsrvId={areacode}&gamenId=03-1102&timeType=60&requestType=1")



def main():
    kawabou = Kawabou(debug=True)
    kawabou.register("CFRICSTEST4","fricstest4")
    kawabou.login()
    kawabou.screenshot_dam_keika()
    kawabou.screenshot_dam_kobetu()

if __name__ == "__main__":
    main()