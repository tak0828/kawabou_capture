from datetime import datetime, timedelta
import time
import CONST
from kawabou import Kawabou
# from dataclasses import dataclass
# from utils import Area,Pref


class CityBase:
    def __init__(self,prefname:str="東京都",areaname:str="東京都",ovsId="2127900100003",user:str="CFRICSTEST4",pwd:str="fricstest4"):
        self.__kawabou = Kawabou()
        self.kawabou.register(user,pwd)
        self.areaname = areaname
        self.prefname = prefname

    
    ###### プロパティ ######
    @property
    def kawabou(self):
        return self.__kawabou
    
    ###### 雨量 ######
    
    def idw_caution(self):
        '''
        IDW(注意フラグ)
        '''
        print("idw_caution")
    
    def disp_zero(self):
        '''
        降雨時の0.0mm表示
        '''
        print("disp_zero")
    
    ###### 水位 ######
    
    def three_sigma_caution(self):
        '''
        3σ(注意フラグ)
        '''
        print("3シグマ")
    
    def upper_limit_over(self):
        '''
        上限値超過(警戒フラグ)
        '''
        print("上限値超過")

    def law_limit_over(self):
        '''
        下限値超過(注意フラグ)
        '''
        print("下限値超過")
    
    def sp1_caution(self):
        '''
        SP1(注意フラグ)
        '''
        print("SP1(注意フラグ)")

    def no_change_caution(self):
        '''
        無変動(注意フラグ)
        '''
        print("無変動(注意フラグ)")
    
    ###### ダム ######
    def unnatural_dam(self):
        '''
        貯水位の不自然な変動
        '''
        print("貯水位の不自然な変動")
    
    def visual_dam(self):
        '''
        目視監視(貯水位・全流入量0.00m表示)
        '''
        print("目視監視(貯水位・全流入量0.00m表示)")

    ###### 水質 ######
    def cod_zero(self):
        '''
        CODの0.0表示
        '''
        print("CODの0.0表示")
    
    def unnatural_suisitu(self):
        '''
        水温・pH・D0・導電率・濁度の不自然な変動
        '''
        print("水温・pH・D0・導電率・濁度の不自然な変動")

    ###### 海岸 ######
    def visual_kaigan(self):
        '''
        目視監視(海岸)
        '''
        print("目視監視(海岸)")

    ###### 排水機場 ######
    def unnatural_haisui(self):
        '''
        内・外水位の不自然な変動
        '''
        print("内・外水位の不自然な変動")

    ###### 積雪深 ######
    # 関数名変更するべき
    def soon_snow(self):
        '''
        積雪深の急激な変動
        *****関数名変更するべき*****
        '''
        print("積雪深の急激な変動")

    def visual_snow(self):
        '''
        目視監視(積雪深)
        '''
        print("目視監視(積雪深)")

    ###### 気象 ######
    def unnatural_temp(self):
        '''
        気温の不自然な変動
        '''
        print("気温の不自然な変動")
    


def main():
    c = CityBase()
    c.idw_caution()

if __name__ == "__main__":
    main()