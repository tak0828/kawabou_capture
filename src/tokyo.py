from datetime import datetime, timedelta
import time
import CONST
from citybase import CityBase
# from utils import load_csv_as_records,build_index

class Tokyo(CityBase):
    def __init__(self,areacode="83",ovsId="2127900100003",user:str="CFRICSTEST4",pwd:str="fricstest4"):
        super().__init__(areacode=areacode,ovsId=ovsId,user=user,pwd=pwd)

    def idw_caution(self):
        self.kawabou.screenshot_over_city_rain_kobetu()
        self.kawabou.screenshot_over_city_rain_kobetuMLT()
        self.kawabou.screenshot_over_city_radar_ruika()
        self.kawabou.screenshot_gaikyo()



def main():
    tokyo = Tokyo()
    tokyo.idw_caution()

if __name__ == "__main__":
    main()