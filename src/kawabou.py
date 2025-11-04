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

### 基準値超過(over)

### 欠測・未受信(miss)

    # 概況図スクリーンショット
    def screenshot_miss_gaikyo_map(self):
        self.__miss_city_top_gaikyo_map()
        self.save_screenshot_png("city_top_gaikyo_map.png")

    # 雨量グラフスクリーンショット
    def screenshot_miss_rain_graph(self,areacode=83):
        self.__miss_rain_graph(areacode)
        self.save_screenshot_png("rain_graph.png")
    
    # 雨量グラフ(対象観測所)スクリーンショット
    # 例は、篠崎
    def screenshot_miss_rain_graph_kobetu(self,areacode=2127900100003):
        self.__miss_rain_graph_kobetu(areacode)
        self.save_screenshot_png("rain_graph_kobetu.png")

    # 市町村向け川の防災(時間雨量グラフ)スクリーンショット
    # 例は、篠崎
    def screenshot_miss_city_rain_kobetu(self,areacode=2127900100003):
        self.__miss_city_rain_kobetu(areacode)
        self.save_screenshot_png("city_rain_kobetu.png")

    # 市町村向け川の防災(経過表)スクリーンショット
    # 例は、東京都
    def screenshot_miss_city_rain_keika(self,prefcode=1301):
        self.__miss_city_rain_keika(prefcode)
        self.save_screenshot_png("city_rain_keika.png")

    # 時間雨量経過表スクリーンショット
    # 例は、東京都
    def screenshot_miss_rain_keika(self,prefcode=1301):
        self.__miss_rain_keika(prefcode)
        self.save_screenshot_png("rain_keika.png")

    # レーダ雨量（現況）Cバンドスクリーンショット
    def screenshot_miss_radar_genkyo(self,prefcode=1301):
        self.__miss_radar_genkyo(prefcode)
        self.save_screenshot_png("radar_genkyo.png")

    # 時刻水位・流量経過表
    # 例は東京都
    def screenshot_miss_suii_keika(self,prefcode=1301):
        self.__miss_suii_keika(prefcode)
        self.save_screenshot_png("suii_keika.png")
    # 時刻水位・流量経過表
    # 例は高砂
    def screenshot_miss_suii_keika_kobetu(self,areacode=2127900400049):
        self.__miss_suii_keika_kobetu(areacode)
        self.save_screenshot_png("suii_keika_kobetu.png")

    # 時刻ダム情報経過表
    # 例は東京都
    def screenshot_miss_dam_keika(self,prefcode=1301):
        self.__miss_dam_keika(prefcode)
        self.save_screenshot_png("dam_keika.png")

    # 時刻ダム情報グラフ
    # 例は白丸調整池
    def screenshot_miss_dam_kobetu(self,areacode:str="0332900700101"):
        self.__miss_dam_kobetu(areacode)
        self.save_screenshot_png("dam_kobetu.png")

    # 時刻水質情報経過表
    # 例は東京都
    def screenshot_miss_suisitu_keika(self,prefcode=1301):
        self.__miss_suisitu_keika(prefcode)
        self.save_screenshot_png("suisitu_keika.png")

    # 時刻水質情報グラフ
    # 例は京葉大橋平均
    def screenshot_miss_suisitu_kobetu(self,areacode:str="2127900600025"):
        self.__miss_suisitu_kobetu(areacode)
        self.save_screenshot_png("suisitu_kobetu.png")

    # 堰グラフ
    # 例は前川水門
    def screenshot_miss_weir_kobetu(self,areacode=83,prefcode:str="2127000800004"):
        self.__miss_weir_kobetu(areacode,prefcode)
        self.save_screenshot_png("weir_kobetu.png")

    # 海岸グラフ
    # 例は東京(晴海)
    def screenshot_miss_kaigan_kobetu(self,areacode:str="1617201200001"):
        self.__miss_kaigan_kobetu(areacode)
        self.save_screenshot_png("kaigan_kobetu.png")

    # 時刻排水ポンプ場情報グラフ
    # 例は利根機場
    def screenshot_miss_haisui_kobetu(self,areacode:str="2127300900001"):
        self.__miss_haisui_kobetu(areacode)
        self.save_screenshot_png("haisui_kobetu.png")

############################################################################################
####            ページ表示 処理群                                                      ######
############################################################################################

### 基準値超過(over) ###

#### 雨量関連 ####

    # 雨量グラフ(10分)ページ
    def __over_city_rain_keika(self,areacode=84):
        self.get_page(f"https://city.river.go.jp/kawabou/cityRainKeika.do?init=init&prefCd=&townCd=&areaCd={areacode}&rvrsysCd=&gamenId=02-0902")
    # 時間雨量経過表ページ
    # 雨量グラフ(10分)ページと同一URL
    def __over_city_rain_keika_1(self,areacode=84):
        self.get_page(f"https://city.river.go.jp/kawabou/cityRainKeika.do?init=init&prefCd=&townCd=&areaCd={areacode}&rvrsysCd=&gamenId=02-0902")
    # 雨量グラフ(対象観測所)ページ
    def __over_city_rain_kobetu(self,ovsrvId:str="0332900100039"):
        self.get_page(f"https://city.river.go.jp/kawabou/cityRainKobetu.do?init=init&obsrvId={ovsrvId}&gamenId=02-0904&timeType=60&requestType=1")
    # 時間雨量経過表(対象観測所1か所)
    # 雨量グラフ(対象観測所)ページと同一URL
    def __over_city_rain_kobetu_1(self,ovsrvId:str="2152800100021"):
        self.get_page(f"https://city.river.go.jp/kawabou/cityRainKobetu.do?init=init&obsrvId={ovsrvId}&gamenId=02-0904&timeType=60&requestType=1")
    # 時間雨量経過表(比較観測所3か所)
    def __over_city_rain_kobetuMLT(self,areacode=84):
        self.get_page(f"https://city.river.go.jp/kawabou/cityRainKobetuMlt.do?init=init&prefCd=&townCd=&areaCd={areacode}&rvrsysCd=&gamenId=02-0903")
    # レーダ雨量(現況)(Cバンド)
    def __over_city_radar_genkyo(self,areacode=80):
        self.get_page(f"https://city.river.go.jp/kawabou/cityRadarGenkyo.do?init=init&areaCd={areacode}&gamenId=02-1801")
    # レーダ雨量(累加)(Cバンド)
    def __over_city_radar_ruika(self,areacode=84):
        self.get_page(f"https://city.river.go.jp/kawabou/cityRadarRuika.do?init=init&areaCd={areacode}&gamenId=02-1802")
    # レーダ雨量(現況)(XRAIN)
    def __over_city_radar_yosokuD(self,areacode=84):
        self.get_page(f"https://city.river.go.jp/kawabou/cityRadarYosokuD.do?init=init&areaCd={areacode}&gamenId=02-1805")
    # レーダ雨量(現況)(Cバンド)(気象庁)
    # 現況の気象庁無verと同一URL
    def __over_city_radar_genkyo_kisyou(self,areacode=84):
        self.get_page(f"https://city.river.go.jp/kawabou/cityRadarGenkyo.do?init=init&areaCd={areacode}&gamenId=02-1801")
    # レーダ雨量(履歴4分割)(Cバンド)(2枚)
    def __over_city_radar_rerekiB(self,areacode=84):
        self.get_page(f"https://city.river.go.jp/kawabou/cityRadarRirekiB.do?init=init&areaCd={areacode}&gamenId=02-1804")

    ### 一般向けの引数は適当に抽出、使用するときに調整必要
    # 一般向け川の防災情報(雨量グラフ)
    def __over_common_uryou(self,zm=15,ofcCd=15617,obsCd=127,lat:float=44.737,lon:float=142.1183611):
        self.get_page(f"https://www.river.go.jp/kawabou/pc/tm?zm=15&itmkndCd=1&ofcCd=15617&obsCd=127&fld=0&clat=44.737&clon=142.1183611&mapType=0&viewGrpStg=0&viewRd=1&viewRW=1&viewRiver=1&viewPoint=1")
    # 一般向け川の防災情報(XRAIN4分割)
    def __over_common_xrain(self,zm=15,ofcCd=15617,obsCd=127,lat:float=44.737,lon:float=142.1183611):
        self.get_page(f"https://www.river.go.jp/kawabou/pc/rd?zm=15&clat=44.737&clon=142.1183611&fld=0&mapType=0&viewGrpStg=0&viewRd=1&viewRW=1&viewRiver=1&viewPoint=1&ext=0&rdtype=xrain&rdnum=4&rdopa=50&rdint=5")
    
#### 水位関連 ####
    # 水位グラフ
    def __over_city_suii_kobetu(self,obsrvId:str="0153700400092"):
        self.get_page(f"https://city.river.go.jp/kawabou/citySuiiKobetu.do?obsrvId={obsrvId}&gamenId=02-1006&stgGrpKind=survFore&fvrt=yes&timeType=60")
    # 水位グラフ(10分)
    def __over_city_suii_kobetu(self,obsrvId:str="0153700400092"):
        self.get_page(f"https://city.river.go.jp/kawabou/citySuiiKobetu.do?obsrvId={obsrvId}&gamenId=02-1006&stgGrpKind=survFore&fvrt=yes&timeType=10")

    # 時刻水位・流量グラフ
    def __over_city_timesuii(self,obsrvId:str="0153700400092"):
        self.get_page(f"https://city.river.go.jp/kawabou/citySuiiKobetu.do?obsrvId={obsrvId}&gamenId=02-1006&stgGrpKind=survFore&fvrt=yes")
    # 時刻水位・流量グラフ(対象観測所)
    # 上記と同一URL
    def __over_city_timesuii_kobetu(self,obsrvId:str="0153700400092"):
        self.get_page(f"https://city.river.go.jp/kawabou/citySuiiKobetu.do?obsrvId={obsrvId}&gamenId=02-1006&stgGrpKind=survFore&fvrt=yes")

    # 時刻水位・流量グラフ(比較観測所)
    def __over_city_timesuii_kobetuMLT(self,areacode=84):
        self.get_page(f"https://city.river.go.jp/kawabou/citySuiiKobetuMlt.do?prefCd=&townCd=&areaCd={areacode}&rvrsysCd=&gamenId=02-1004&stgGrpKind=survFore&fvrt=yes")

    # 時刻水位・流量現況表
    def __over_city_timesuii_genkyou(self,areacode=84):
        self.get_page(f"https://city.river.go.jp/kawabou/citySuiiGenkyou.do?prefCd=&townCd=&areaCd={areacode}&rvrsysCd=&gamenId=02-1001&fvrt=yes")
    # 時刻水位・流量経過表
    def __over_city_timesuii_keika(self,areacode=84):
        self.get_page(f"https://city.river.go.jp/kawabou/citySuiiKeika.do?init=init&prefCd=&townCd=&areaCd={areacode}&rvrsysCd=&gamenId=02-1002")

#### 水質関連 ####
    # 水質経過表
    def __over_city_suisitu_keika(self,areacode=84):
        self.get_page(f"https://city.river.go.jp/kawabou/citySuisituKeikaDay.do?init=init&prefCd=&townCd=&areaCd={areacode}&rvrsysCd=&gamenId=02-1306")

    # 水質詳細表
    def __over_city_suisitu_keika(self,areacode=84,obsrvId:str="2152800600001"):
        self.get_page(f"https://city.river.go.jp/kawabou/citySuisituKobetuDayDtl.do?init=init&prefCd=&townCd=&areaCd={areacode}&rvrsysCd=&obsrvId={obsrvId}&gamenId=02-1308")

    # 時刻水質グラフ
    def __over_city_suisitu_kobetu(self,obsrvId:str="2152800600001"):
        self.get_page(f"https://city.river.go.jp/kawabou/citySuisituKobetu.do?init=init&obsrvId={obsrvId}&gamenId=02-1303&timeType=60&requestType=1")
    # 時刻水質グラフ(対象観測所)
    # 同一URL
    def __over_city_suisitu_kobetu_1(self,obsrvId:str="2152800600001"):
        self.get_page(f"https://city.river.go.jp/kawabou/citySuisituKobetu.do?init=init&obsrvId={obsrvId}&gamenId=02-1303&timeType=60&requestType=1")

    # 時刻水質現況表
    def __over_city_timesuisitu_genkyou(self,areacode=84):
        self.get_page(f"https://city.river.go.jp/kawabou/citySuisituGenkyou.do?init=init&areaCd={areacode}&gamenId=02-1301")

    # 時刻水質経過表
    def __over_city_timesuisitu_keika(self,areacode=84):
        self.get_page(f"https://city.river.go.jp/kawabou/citySuisituKeika.do?init=init&prefCd=&townCd=&areaCd={areacode}&rvrsysCd=&gamenId=02-1302")

    # 時刻水質経過表(対象観測所)
    def __over_city_timesuisitu_keika_kobetu(self,areacode=83):
        self.get_page(f"https://city.river.go.jp/kawabou/citySuisituKeika.do?init=init&areaCd={areacode}&gamenId=02-1302")

    # 時刻水質詳細表
    def __over_city_timesuisitu_kobetuDt1(self,areacode=84,obsrvId:str="2152800600001"):
        self.get_page(f"https://city.river.go.jp/kawabou/citySuisituKobetuDtl.do?init=init&prefCd=&townCd=&areaCd={areacode}&rvrsysCd=&obsrvId={obsrvId}&gamenId=02-1304")

    # 日水質詳細表
    def __over_city_daysuisitu_kobetuDt1(self,areacode=84,obsrvId:str="2152800600001"):
        self.get_page(f"https://city.river.go.jp/kawabou/citySuisituKobetuDayDtl.do?init=init&prefCd=&townCd=&areaCd={areacode}&rvrsysCd=&obsrvId={obsrvId}&gamenId=02-1308")


### 欠測・未受信(miss)
    
    # 概況図ページ
    # 地方選択方法がわからないので、引数なし、要確認
    def __miss_city_top_gaikyo_map(self):
        self.get_page(f"https://city.river.go.jp/kawabou/cityTopGaikyoMap.do?init=init&gamenId=02-0201")
    # 雨量グラフページ
    def __miss_rain_graph(self,areacode):
        self.get_page(f"https://city.river.go.jp/kawabou/cityRainKobetuMlt.do?requestType=1&init=city&gamenId=02-0903&areaCd={areacode}&rvrsysCd=&prefCd=&townCd=")
    # 雨量グラフ(対象観測所)ページ
    def __miss_rain_graph_kobetu(self,areacode):
        self.get_page(f"https://city.river.go.jp/kawabou/cityRainKobetu.do?init=init&obsrvId={areacode}&gamenId=03-0803&timeType=60&requestType=1")
    # 市町村向け川の防災(時間雨量グラフ)
    def __miss_city_rain_kobetu(self,areacode):
        self.get_page(f"https://city.river.go.jp/kawabou/cityRainKobetu.do?obsrvId={areacode}&gamenId=03-0803&requestType=1&init=city")

    # 市町村向け川の防災(経過表)
    def __miss_city_rain_keika(self,prefcode):
        self.get_page(f"https://city.river.go.jp/kawabou/cityRainKeika.do?init=init&prefCd={prefcode}&gamenId=03-0801")

    # 時間雨量経過表ページ
    def __miss_rain_keika(self,prefcode):
        self.get_page(f"https://city.river.go.jp/kawabou/cityRainKeika.do?init=init&prefCd={prefcode}&gamenId=03-0801")
    # レーダ雨量（現況）Cバンド
    def __miss_radar_genkyo(self,prefcode):
        self.get_page(f"https://city.river.go.jp/kawabou/cityRadarGenkyo.do?init=init&prefCd={prefcode}&gamenId=03-1801")

    # 時刻水位・流量経過表ページ
    def __miss_suii_keika(self,prefcode):
        self.get_page(f"https://city.river.go.jp/kawabou/citySuiiKeika.do?requestType=1&init=city&gamenId=03-1001&areaCd=&rvrsysCd=&prefCd={prefcode}&townCd=&stgGrpKind=crsSect")

    # 時刻水位・流量経過表ページ(対象観測所)
    def __miss_suii_keika_kobetu(self,areacode):
        self.get_page(f"https://city.river.go.jp/kawabou/citySuiiKobetu.do?obsrvId={areacode}&gamenId=03-1005&stgGrpKind=survFore&fvrt=yes")

    # 水位グラフ
    # def __suii_kobetu(self,areacode):
    #     self.get_page(f"https://city.river.go.jp/kawabou/citySuiiKobetu.do?obsrvId={areacode}&gamenId=03-1005&stgGrpKind=survFore&fvrt=yes")

    # 時刻ダム情報経過表
    def __miss_dam_keika(self,prefcode):
        self.get_page(f"https://city.river.go.jp/kawabou/cityDamKeika.do?init=init&prefCd={prefcode}&townCd=&areaCd=&rvrsysCd=&gamenId=03-1101")

    # 時刻ダム情報グラフ
    def __miss_dam_kobetu(self,areacode):
        self.get_page(f"https://city.river.go.jp/kawabou/cityDamKobetu.do?init=init&obsrvId={areacode}&gamenId=03-1102&timeType=60&requestType=1")

    # 時刻水質経過表
    def __miss_suisitu_keika(self,prefcode):
        self.get_page(f"https://city.river.go.jp/kawabou/citySuisituKeika.do?init=init&prefCd={prefcode}&townCd=&areaCd=&rvrsysCd=&gamenId=03-1301")

    # 時刻水質グラフ
    def __miss_suisitu_kobetu(self,areacode):
        self.get_page(f"https://city.river.go.jp/kawabou/citySuisituKobetu.do?init=init&obsrvId={areacode}&gamenId=03-1302&timeType=60&requestType=1")

    # 堰グラフ
    def __miss_weir_kobetu(self,areacode,prefcode):
        self.get_page(f"https://city.river.go.jp/kawabou/cityWeirKobetu.do?init=init&prefCd=&townCd=&areaCd={areacode}&rvrsysCd=&obsrvId={prefcode}&gamenId=02-1402")

    # 海岸グラフ
    def __miss_kaigan_kobetu(self,areacode):
        self.get_page(f"https://city.river.go.jp/kawabou/cityKaiganKobetu.do?init=init&obsrvId={areacode}&gamenId=03-1202&timeType=60&requestType=1")
    # 海岸グラフ
    def __miss_haisui_kobetu(self,areacode):
        self.get_page(f"https://city.river.go.jp/kawabou/cityHaisuiKobetu.do?init=init&obsrvId={areacode}&gamenId=02-1502&timeType=60&requestType=1")



def main():
    kawabou = Kawabou(debug=True)
    kawabou.register("CFRICSTEST4","fricstest4")
    kawabou.login()
    kawabou.screenshot_miss_haisui_kobetu()

if __name__ == "__main__":
    main()