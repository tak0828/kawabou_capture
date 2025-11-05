from datetime import datetime, timedelta
import time
import CONST
from citybase import CityBase

class Tokyo(CityBase):
    def __init__(self,areacode="83",ovsId="2127900100003",user:str="CFRICSTEST4",pwd:str="fricstest4"):
        super().__init__(areacode=areacode,ovsId=ovsId,user=user,pwd=pwd)

    def idw_caution(self):
        self.kawabou.screenshot_over_city_rain_kobetu()
        self.kawabou.screenshot_over_city_rain_kobetuMLT()
        self.kawabou.screenshot_over_city_radar_ruika()
        self.kawabou.screenshot_pref_gaikyo("東京都")
    
    def disp_zero(self):
        self.kawabou.screenshot_area_gaikyo("関東")
        self.kawabou.screenshot_pref_gaikyo("東京都")
        self.kawabou.screenshot_over_city_radar_ruika()




def main():
    tokyo = Tokyo()
    tokyo.idw_caution()

if __name__ == "__main__":
    main()