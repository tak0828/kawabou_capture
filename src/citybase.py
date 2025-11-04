from datetime import datetime, timedelta
import time
import CONST
from kawabou import Kawabou
from dataclasses import dataclass
# from utils import load_csv_as_records,build_index
@dataclass
class City:
    areacode:str
    ovsId : str

class CityBase:
    def __init__(self,areacode="83",ovsId="2127900100003",user:str="CFRICSTEST4",pwd:str="fricstest4"):
        self.__kawabou = Kawabou()
        self.kawabou.register(user,pwd)
        self.city = City(areacode,ovsId)

    
    ###### プロパティ ######
    @property
    def kawabou(self):
        return self.__kawabou
    
    def idw_caution(self):
        '''
        IDW(注意フラグ)
        '''
        self.kawabou.screenshot_over_city_rain_kobetu()
        print("idw_caution")


def main():
    c = CityBase()
    c.idw_caution()

if __name__ == "__main__":
    main()