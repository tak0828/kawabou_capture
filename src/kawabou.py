from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

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
####            iframe内　処理群(概況図)                                              ######
############################################################################################
    # iframe内の操作
    # 都道府県と地方で共通なので、外にプライベートとして用意
    def __switch_into_area_iframe(self,wait):
        self.driver.switch_to.default_content()
        frame = wait.until(EC.presence_of_element_located((By.ID, "ctrlAreaRvrsysPrefTownFrm")))
        self.driver.switch_to.frame(frame)
        return frame
    
    def __choise_pref(self,prefcode:str=CONST.PREF_CODE['東京都']):
        '''
        概況図の都道府県を選択

        :param str prefcode: CONST.PREF_CODEより都道府県を選択
        '''
        wait = WebDriverWait(self.driver, 20)

        wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    
        # 2) iFrameに入る
        frame_el = self.__switch_into_area_iframe(wait)

        pref_sel = wait.until(EC.element_to_be_clickable((By.ID, "form1_commonForm_selectPref")))
        Select(pref_sel).select_by_value(prefcode)
        link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@onclick,'showPrefTown')]")))
        link.click()
    
    def __choise_area(self,areacode:str=CONST.AREA_CODE['全国']):
        '''
        概況図の都道府県を選択

        :param str prefcode: CONST.PREF_CODEより都道府県を選択
        '''
        wait = WebDriverWait(self.driver, 20)

        wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

        # 2) iFrameに入る
        frame_el = self.__switch_into_area_iframe(wait)

        pref_sel = wait.until(EC.element_to_be_clickable((By.ID, "form1_commonForm_selectArea")))
        Select(pref_sel).select_by_value(areacode)
        link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@onclick,'showAreaRvrs')]")))
        link.click()

############################################################################################
####            スクリーンショット　処理群                                              ######
############################################################################################

### 概況図
    def screenshot_pref_gaikyo(self,prefname:str="和歌山県",pngname:str="pref_gaikyou.png"):
        '''
        都道府県キャプチャ

        :param str pngname: ファイル名
        '''
        self.__pref_gaikyo(prefname)
        self.save_screenshot_png(pngname)

    def screenshot_area_gaikyo(self,areaname:str="全国",pngname:str="area_gaikyou.png"):
        '''
        地方キャプチャ

        :param str areaname : 地方名
        :param str pngname: ファイル名
        '''
        self.__area_gaikyo(areaname)
        self.save_screenshot_png(pngname)


### 基準値超過(over)

    # 雨量グラフ(10分)ページスクリーンショット
    def screenshot_over_city_rain_keika(self,areacode="84",pngname:str="over_city_rain_keika.png"):
        '''
        雨量グラフ(10分)ページスクリーンショット

        :param str areacode : 地方コード
        :param str pngname: ファイル名
        '''
        self.login()
        self.__over_city_rain_keika(areacode)
        self.save_screenshot_png(pngname)

    # 時間雨量経過表ページスクリーンショット
    def screenshot_over_city_rain_keika_1(self,areacode="84",pngname:str="over_city_rain_keika_1.png"):
        '''
        時間雨量経過表ページスクリーンショット

        :param str areacode : 地方コード
        :param str pngname: ファイル名
        '''
        self.login()
        self.__over_city_rain_keika_1(areacode)
        self.save_screenshot_png(pngname)

    # 時間雨量経過表(対象観測所1か所)ページスクリーンショット
    def screenshot_over_city_rain_kobetu_1(self,ovsrvId="2152800100021",pngname:str="over_city_rain_kobetu_1.png"):
        '''
        時間雨量経過表(対象観測所1か所)ページスクリーンショット

        :param str ovsrvId : 観測所コード
        :param str pngname: ファイル名
        '''
        self.login()
        self.__over_city_rain_kobetu_1(ovsrvId)
        self.save_screenshot_png(pngname)

    # 雨量グラフ(対象観測所)スクリーンショット
    def screenshot_over_city_rain_kobetu(self,pngname:str="over_city_rain_kobetu.png"):
        '''
        雨量グラフ(対象観測所)スクリーンショット

        :param str pngname: ファイル名
        '''
        self.login()
        self.__over_city_rain_kobetu()
        self.save_screenshot_png(pngname)

    # 雨量グラフ(比較3か所)スクリーンショット
    def screenshot_over_city_rain_kobetuMLT(self,pngname:str="over_city_rain_kobetuMLT.png"):
        '''
        雨量グラフ(比較3か所)スクリーンショット

        :param str pngname: ファイル名
        '''
        self.login()
        self.__over_city_rain_kobetuMLT()
        self.save_screenshot_png(pngname)

    # レーダ雨量(現況)(Cバンド)ページスクリーンショット
    def screenshot_over_city_radar_genkyo(self,areacode="80",pngname:str="over_city_radar_genkyo.png"):
        '''
        レーダ雨量(現況)(Cバンド)ページスクリーンショット

        :param str areacode : 地方コード
        :param str pngname: ファイル名
        '''
        self.login()
        self.__over_city_radar_genkyo(areacode)
        self.save_screenshot_png(pngname)

    # レーダ雨量(累加)(Cバンド)スクリーンショット
    def screenshot_over_city_radar_ruika(self,pngname:str="over_city_radar_ruika.png"):
        '''
        レーダ雨量(累加)(Cバンド)スクリーンショット

        :param str pngname: ファイル名
        '''
        self.login()
        self.__over_city_radar_ruika()
        self.save_screenshot_png(pngname)

    # レーダ雨量(現況)(XRAIN)ページスクリーンショット
    def screenshot_over_city_radar_yosokuD(self,areacode="84",pngname:str="over_city_radar_yosokuD.png"):
        '''
        レーダ雨量(現況)(XRAIN)ページスクリーンショット

        :param str areacode : 地方コード
        :param str pngname: ファイル名
        '''
        self.login()
        self.__over_city_radar_yosokuD(areacode)
        self.save_screenshot_png(pngname)

    # レーダ雨量(現況)(Cバンド)(気象庁)ページスクリーンショット
    def screenshot_over_city_radar_genkyo_kisyou(self,areacode="84",pngname:str="over_city_radar_genkyo_kisyou.png"):
        '''
        レーダ雨量(現況)(Cバンド)(気象庁)ページスクリーンショット

        :param str areacode : 地方コード
        :param str pngname: ファイル名
        '''
        self.login()
        self.__over_city_radar_genkyo_kisyou(areacode)
        self.save_screenshot_png(pngname)

    # レーダ雨量(履歴4分割)(Cバンド)(2枚)ページスクリーンショット
    def screenshot_over_city_radar_rirekiB(self,areacode="84",pngname:str="over_city_radar_genkyo_rirekiB.png"):
        '''
        レーダ雨量(履歴4分割)(Cバンド)(2枚)ページスクリーンショット

        :param str areacode : 地方コード
        :param str pngname: ファイル名
        '''
        self.login()
        self.__over_city_radar_rirekiB(areacode)
        self.save_screenshot_png(pngname)

#### 水位 ####
    # 水位グラフページスクリーンショット
    def screenshot_over_city_suii_kobetu_dt60(self,ovsrvId="0153700400092",pngname:str="over_city_suii_kobetu60.png"):
        '''
        水位グラフページスクリーンショット

        :param str ovsrvId : 観測所コード
        :param str pngname: ファイル名
        '''
        self.login()
        self.__over_city_suii_kobetu_dt60(ovsrvId)
        self.save_screenshot_png(pngname)

    # 水位グラフ(10分)ページスクリーンショット
    def screenshot_over_city_suii_kobetu_dt10(self,ovsrvId="0153700400092",pngname:str="over_city_suii_kobetu10.png"):
        '''
        水位グラフ(10分)ページスクリーンショット

        :param str ovsrvId : 観測所コード
        :param str pngname: ファイル名
        '''
        self.login()
        self.__over_city_suii_kobetu_dt10(ovsrvId)
        self.save_screenshot_png(pngname)

    # 時刻水位・流量グラフページスクリーンショット
    def screenshot_over_city_timesuii(self,ovsrvId="0153700400092",pngname:str="over_city_timesuii.png"):
        '''
        時刻水位・流量グラフページスクリーンショット

        :param str ovsrvId : 観測所コード
        :param str pngname: ファイル名
        '''
        self.login()
        self.__over_city_timesuii(ovsrvId)
        self.save_screenshot_png(pngname)

    # 時刻水位・流量現況表ページスクリーンショット
    def screenshot_over_city_timesuii_genkyou(self,areacode="84",pngname:str="over_city_timesuii_genkyou.png"):
        '''
        時刻水位・流量現況表ページスクリーンショット

        :param str areacode : 地方コード
        :param str pngname: ファイル名
        '''
        self.login()
        self.__over_city_timesuii_genkyou(areacode)
        self.save_screenshot_png(pngname)

    # 時刻水位・流量経過表ページスクリーンショット
    def screenshot_over_city_timesuii_keika(self,areacode="84",pngname:str="over_city_timesuii_keika.png"):
        '''
        時刻水位・流量経過表ページスクリーンショット

        :param str areacode : 地方コード
        :param str pngname: ファイル名
        '''
        self.login()
        self.__over_city_timesuii_keika(areacode)
        self.save_screenshot_png(pngname)

    # 時刻水位・流量グラフ(対象観測所)スクリーンショット
    def screenshot_over_city_timesuii_kobetu(self,pngname:str="over_city_timesuii_kobetu.png"):
        '''
        時刻水位・流量グラフ(対象観測所)スクリーンショット

        :param str pngname: ファイル名
        '''
        self.login()
        self.__over_city_timesuii_kobetu()
        self.save_screenshot_png(pngname)

    # 時刻水位・流量グラフ(比較観測所1か所)
    def screenshot_over_city_timesuii_kobetuMLT(self,pngname:str="over_city_timesuii_kobetuMLT.png"):
        '''
        時刻水位・流量グラフ(比較観測所1か所)

        :param str pngname: ファイル名
        '''
        self.login()
        self.__over_city_timesuii_kobetuMLT()
        self.save_screenshot_png(pngname)

#### ダム ####
    # 時刻ダム情報スクリーンショット
    def screenshot_over_city_dam_info(self,pngname:str="over_city_dam_info.png"):
        '''
        時刻ダム情報スクリーンショット

        :param str pngname: ファイル名
        '''
        self.login()
        self.__over_city_dam_info()
        self.save_screenshot_png(pngname)

#### 水質 ####
    # 時刻水質経過表スクリーンショット
    def screenshot_over_city_timesuisitu_keika(self,pngname:str="over_city_timesuisitu_keika.png"):
        '''
        時刻水質経過表スクリーンショット

        :param str pngname: ファイル名
        '''
        self.login()
        self.__over_city_timesuisitu_keika()
        self.save_screenshot_png(pngname)
    # 時刻水質グラフスクリーンショット
    def screenshot_over_city_suisitu_kobetu(self,pngname:str="over_city_suisitu_kobetu.png"):
        '''
        時刻水質グラフスクリーンショット

        :param str pngname: ファイル名
        '''
        self.login()
        self.__over_city_suisitu_kobetu()
        self.save_screenshot_png(pngname)
    # 時刻水質詳細表スクリーンショット
    def screenshot_over_city_timesuisitu_kobetuDt1(self,pngname:str="over_city_timesuisitu_kobetuDt1.png"):
        '''
        時刻水質詳細表スクリーンショット

        :param str pngname: ファイル名
        '''
        self.login()
        self.__over_city_timesuisitu_kobetuDt1()
        self.save_screenshot_png(pngname)

#### 排水機場 ####
    def screenshot_over_city_haisui_kobetu_target(self,pngname:str="over_city_haisui_kobetu_target.png"):
        '''
        時刻排水ポンプ場情報グラフ(対象観測所)スクリーンショット

        :param str pngname: ファイル名
        '''
        self.login()
        self.__over_city_haisui_kobetu_target()
        self.save_screenshot_png(pngname)

#### 積雪深 ####
    def screenshot_over_city_snow_kobetu_target(self,pngname:str="over_city_snow_kobetu_target.png"):
        '''
        時刻積雪深グラフ(対象観測所)スクリーンショット

        :param str pngname: ファイル名
        '''
        self.login()
        self.__over_city_snow_kobetu_target()
        self.save_screenshot_png(pngname)

#### 気象 ####
    def screenshot_over_city_weather_kobetu(self,pngname:str="over_city_weather_kobetu.png"):
        '''
        時刻気象詳細表スクリーンショット

        :param str pngname: ファイル名
        '''
        self.login()
        self.__over_city_weather_kobetu()
        self.save_screenshot_png(pngname)
    


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

### 概況図

    # 都道府県概況図
    def __pref_gaikyo(self,prefname):
        '''
        都道府県概況図

        :param str prefname: 都道府県の名前(例:"東京都") CONST.PREF_CODEを確認すること
        '''
        self.get_page(f"https://city.river.go.jp/kawabou/cityTopGaikyoMap.do")
        self.__choise_pref(CONST.PREF_CODE[prefname])

    # 地方概況図
    def __area_gaikyo(self,areaname):
        '''
        地方概況図

        :param str areaname: 都道府県の名前(例:"全国") CONST.AREA_CODEを確認
        '''
        self.get_page(f"https://city.river.go.jp/kawabou/cityTopGaikyoMap.do")
        self.__choise_area(CONST.AREA_CODE[areaname])

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
    def __over_city_radar_rirekiB(self,areacode=84):
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
    def __over_city_suii_kobetu_dt60(self,obsrvId:str="0153700400092"):
        self.get_page(f"https://city.river.go.jp/kawabou/citySuiiKobetu.do?obsrvId={obsrvId}&gamenId=02-1006&stgGrpKind=survFore&fvrt=yes&timeType=60")
    # 水位グラフ(10分)
    def __over_city_suii_kobetu_dt10(self,obsrvId:str="0153700400092"):
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

#### ダム関連 ####
    # ダムグラフ(10分)
    def __over_city_dam_kobetu(self,obsrvId:str="2152800700001"):
        self.get_page(f"https://city.river.go.jp/kawabou/cityDamKobetu.do?obsrvId={obsrvId}&gamenId=02-1104&fvrt=yes&timeType=10")
    # 時刻ダム情報グラフ
    def __over_city_dam_info(self,obsrvId:str="0025700700001"):
        self.get_page(f"https://city.river.go.jp/kawabou/cityDamKobetu.do?init=init&obsrvId={obsrvId}&gamenId=02-1104&timeType=60&requestType=1")
    # 時刻ダム情報グラフ(対象観測所)
    # 上記と同じURL
    def __over_city_dam_info_target(self,obsrvId:str="0204900700006"):
        self.get_page(f"https://city.river.go.jp/kawabou/cityDamKobetu.do?init=init&obsrvId={obsrvId}&gamenId=02-1104&timeType=60&requestType=1")
    # 時刻ダム情報グラフ(10分)
    def __over_city_dam_info_target_dt10(self,obsrvId:str="0025700700001"):
        self.get_page(f"https://city.river.go.jp/kawabou/cityDamKobetu.do?obsrvId={obsrvId}&gamenId=02-1104&fvrt=yes&timeType=10")
    # 時刻ダム情報詳細表
    def __over_city_dam_info_kobetu_dt10(self,obsrvId:str="0025700700001"):
        self.get_page(f"https://city.river.go.jp/kawabou/cityDamKobetu.do?obsrvId={obsrvId}&gamenId=02-1104&fvrt=yes&timeType=10")
    # 時刻ダム情報詳細表(対象観測所)
    # 時刻ダム情報グラフ(10分)からここまで同じURL
    def __over_city_dam_info_kobetu_target_dt10(self,obsrvId:str="0025700700001"):
        self.get_page(f"https://city.river.go.jp/kawabou/cityDamKobetu.do?obsrvId={obsrvId}&gamenId=02-1104&fvrt=yes&timeType=10")
    # 時刻ダム情報経過表
    def __over_city_dam_info_keika(self,areacode:str="81"):
        self.get_page(f"https://city.river.go.jp/kawabou/cityDamKeika.do?init=init&prefCd=&townCd=&areaCd={areacode}&rvrsysCd=&gamenId=02-1102")
    # 時刻ダム情報詳細表(10分)
    def __over_city_dam_info_keiak_dt10(self,areacode:str="81"):
        self.get_page(f"https://city.river.go.jp/kawabou/cityDamKeika.do?prefCd=&townCd=&areaCd={areacode}&rvrsysCd=&gamenId=02-1102&fvrt=yes&timeType=10")

#### 積雪関連 ####
    # 時刻積雪深グラフ
    def __over_city_snow_kobetu(self,obsrvId:str="2075700300016"):
        self.get_page(f"https://city.river.go.jp/kawabou/citySnowKobetu.do?init=init&obsrvId={obsrvId}&gamenId=02-1602&timeType=60&requestType=1")
    # 時刻積雪深グラフ(対象観測所)
    # 同様URL
    def __over_city_snow_kobetu_target(self,obsrvId:str="2075700300016"):
        self.get_page(f"https://city.river.go.jp/kawabou/citySnowKobetu.do?init=init&obsrvId={obsrvId}&gamenId=02-1602&timeType=60&requestType=1")
    # 時刻積雪深経過表
    def __over_city_snow_keika(self,areacode:str="81"):
        self.get_page(f"https://city.river.go.jp/kawabou/citySnowKeika.do?init=init&prefCd=&townCd=&areaCd={areacode}&rvrsysCd=&gamenId=02-1601")

#### 海岸関連 ####
    # 時刻海岸情報グラフ
    def __over_city_kaigan_kobetu(self,obsrvId:str="2081701200001"):
        self.get_page(f"https://city.river.go.jp/kawabou/cityKaiganKobetu.do?init=init&obsrvId={obsrvId}&gamenId=02-1203&timeType=60&requestType=1")
    # 時刻海岸情報経過表
    def __over_city_kaigan_keika(self,areacode:str="81"):
        self.get_page(f"https://city.river.go.jp/kawabou/cityKaiganKeika.do?init=init&areaCd={areacode}&gamenId=02-1202")
    # 海岸2か月データ
    def __over_city_kaigan_2mon(self,areacode:str="90",obsrvId:str="1622001200001"):
        self.get_page(f"https://city.river.go.jp/kawabou/dataOutPre.do?gamenId=02-2001&gamenIdPrnt=02-1203&prefCd=&townCd=&areaCd={areacode}&rvrsysCd=&obsrvId={obsrvId}&timeType=60&timeType2=10&yokeiObsrvs=&kanriKubuns=&dispDataTypes=&foreStgKind=usual&dispTeles=&basinDataType=&dispShogens=&dispRuika=")
    # 海岸詳細表
    def __over_city_kaigan_kobetu_dt1(self,areacode:str="81",obsrvId:str="2081701200001"):
        self.get_page(f"https://city.river.go.jp/kawabou/cityKaiganKobetuDtl.do?init=init&prefCd=&townCd=&areaCd={areacode}&rvrsysCd=&obsrvId={obsrvId}&gamenId=02-1204")
    # 海岸現況表
    def __over_city_kaigan_genkyo(self,areacode:str="90"):
        self.get_page(f"https://city.river.go.jp/kawabou/cityKaiganGenkyou.do?init=init&areaCd={areacode}&gamenId=02-1201")

#### 排水関連 ####
    # 時刻排水ポンプ場情報グラフ
    def __over_city_haisui_kobetu(self,obsrvId:str="2329700900001"):
        self.get_page(f"https://city.river.go.jp/kawabou/cityHaisuiKobetu.do?init=init&obsrvId={obsrvId}&gamenId=02-1502&timeType=60&requestType=1")
    # # 時刻排水ポンプ場情報グラフ(2枚)　はてなとなっている
    # def __over_city_haisui_keika(self,areacode:str="81"):
    #     self.get_page(f"https://city.river.go.jp/kawabou/cityKaiganKeika.do?init=init&areaCd={areacode}&gamenId=02-1202")
    # 時刻排水ポンプ場情報グラフ(対象観測所)
    def __over_city_haisui_kobetu_target(self,obsrvId:str="2127300900001"):
        self.get_page(f"https://city.river.go.jp/kawabou/cityHaisuiKobetu.do?init=init&obsrvId={obsrvId}&gamenId=02-1502&timeType=60&requestType=1")
    # 時刻排水ポンプ場情報グラフ詳細表
    def __over_city_haisui_kobetu_dt1(self,areacode:str="81",obsrvId:str="2329700900001"):
        self.get_page(f"https://city.river.go.jp/kawabou/cityHaisuiKobetuDtl.do?init=init&prefCd=&townCd=&areaCd={areacode}&rvrsysCd=&obsrvId={obsrvId}&gamenId=02-1503")

#### 気象関連 ####
    # 気象現況表
    def __over_city_weather_genkyo(self,areacode:str="84"):
        self.get_page(f"https://city.river.go.jp/kawabou/cityWeatherGenkyou.do?init=init&areaCd={areacode}&gamenId=02-1701")
    # 気象詳細表
    def __over_city_weather_kobetu(self,obsrvId:str="2154601300001"):
        self.get_page(f"https://city.river.go.jp/kawabou/cityWeatherKobetu.do?init=init&obsrvId={obsrvId}&gamenId=02-1702&timeType=60&requestType=1")
    # 気象詳細表(前日)
    def __over_city_haisui_kobetu_target_yes(self,obsrvId:str="2154601300001"):
        self.get_page(f"https://city.river.go.jp/kawabou/cityWeatherKobetu.do?obsrvId={obsrvId}&gamenId=02-1702&fvrt=yes")
    # # 気象詳細表(天気図)不明のためコメント
    # def __over_city_haisui_kobetu_dt1(self,areacode:str="81",obsrvId:str="2329700900001"):
    #     self.get_page(f"https://city.river.go.jp/kawabou/cityHaisuiKobetuDtl.do?init=init&prefCd=&townCd=&areaCd={areacode}&rvrsysCd=&obsrvId={obsrvId}&gamenId=02-1503")

#### 堰関連 ####
    # 堰グラフ
    def __over_city_weir_kobetu(self,areacode:str="83",obsrvId:str="2127000800004"):
        self.get_page(f"https://city.river.go.jp/kawabou/cityWeirKobetu.do?init=init&prefCd=&townCd=&areaCd={areacode}&rvrsysCd=&obsrvId={obsrvId}&gamenId=02-1402")
    # 堰グラフ(10分)
    def __over_city_weir_kobetu_dt10(self,obsrvId:str="2127000800004"):
        self.get_page(f"https://city.river.go.jp/kawabou/cityWeirKobetu.do?obsrvId={obsrvId}&gamenId=02-1402&fvrt=yes&timeType=10")

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
    kawabou.screenshot_over_city_timesuii_keika()

if __name__ == "__main__":
    main()