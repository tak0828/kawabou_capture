from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from datetime import datetime, timedelta
import time
import CONST
import os

class SiteBase:
    def __init__(self,window_width:int=1920,window_height:int=1500,debug:bool=False):
        # オプションを設定
        self.__options = Options()
        self.__options.add_argument("--no-sandbox")         # Docker向け
        self.__options.add_argument("--disable-dev-shm-usage") # メモリ対策
        self.__options.add_argument("--disable-gpu")        # GPU無効化
        self.__options.add_argument("--remote-debugging-port=9222") # デバッグ用
        self.__options.add_argument(f"--user-data-dir=/tmp/selenium_user_data_{os.getpid()}")  # ユニークなプロファイル
        self.__options.add_argument(f"--window-size={window_width},{window_height}") # ウィンドウサイズ指定(ヘッドレスモードで必要)
        self.__options.add_argument("--lang=ja-JP")         # 日本語対応
        # debug時はヘッドレスモードとしない。
        if not debug:
            self.__options.add_argument("--headless")           # GUIなしで実行
        # 保存先変更
        # self.__options.add_experimental_option('prefs', {'download.default_directory': downloadPath})
        # ChromeDriver更新
        self.__driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=self.__options)

    
    # アカウント登録関数
    def register(self,user, pwd):
        self.__user = user
        self.__pwd  = pwd
        print(f"アカウント登録{self.user} {self.pwd}")

    # ログイン
    def login(self):
        print("login")
    
    # 必要ページ選択
    def get_page(self,url):
        self.driver.get(url)
    
    # スクリーンショット
    def screenshot(self,path):
        self.driver.save_screenshot(path)
        print("screenshot")
    
    # のちほど配置先パスを動的にするように変更予定(今docker仕様なので)
    def save_screenshot_png(self, file_name_png):
        png_dir = "/app/media/png"
        os.makedirs(png_dir, exist_ok=True)
        png_path = os.path.join(png_dir, os.path.basename(file_name_png))
        self.screenshot(png_path)
        print(f"スクショ保存: {png_path}")

    # ドライバーを止める
    def shutdown(self):
        self.driver.stop()
        
    ###### プロパティ ######
    @property
    def driver(self):
        return self.__driver
    @property
    def user(self):
        return self.__user
    @property
    def pwd(self):
        return self.__pwd




def main():
    site = SiteBase()
    site.register("test","test")
    site.login()

if __name__ == "__main__":
    main()