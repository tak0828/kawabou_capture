from citybase import CityBase

class Tokyo(CityBase):
    def __init__(self,areacode="83",ovsId="2127900100003",user:str="CFRICSTEST4",pwd:str="fricstest4"):
        super().__init__(prefname="東京都",areaname="関東",ovsId=ovsId,user=user,pwd=pwd)

    def idw_caution(self):
        self.kawabou.screenshot_over_city_rain_kobetu()
        self.kawabou.screenshot_over_city_rain_kobetuMLT()
        self.kawabou.screenshot_over_city_radar_ruika()
        self.kawabou.screenshot_pref_gaikyo(self.prefname)
    
    def disp_zero(self):
        self.kawabou.screenshot_area_gaikyo(self.areaname)
        self.kawabou.screenshot_pref_gaikyo(self.prefname)
        self.kawabou.screenshot_over_city_radar_ruika()
    
    def three_sigma_caution(self):
        self.kawabou.screenshot_over_city_timesuii_kobetu()
        self.kawabou.screenshot_over_city_timesuii_kobetuMLT()

    def upper_limit_over(self):
        self.kawabou.screenshot_over_city_timesuii_kobetu()

    def law_limit_over(self):
        self.kawabou.screenshot_over_city_timesuii_kobetu()

    def sp1_caution(self):
        self.kawabou.screenshot_over_city_timesuii_kobetu()

    def unnatural_dam(self):
        self.kawabou.screenshot_over_city_dam_info()

    def visual_dam(self):
        self.kawabou.screenshot_over_city_dam_info()
    
    def cod_zero(self):
        self.kawabou.screenshot_over_city_timesuisitu_keika()
        self.kawabou.screenshot_over_city_suisitu_kobetu()

    def unnatural_suisitu(self):
        self.kawabou.screenshot_over_city_timesuisitu_kobetuDt1()
    
    def unnatural_haisui(self):
        self.kawabou.screenshot_over_city_haisui_kobetu_target()
    
    def soon_snow(self):
        self.kawabou.screenshot_over_city_snow_kobetu_target()

    def visual_snow(self):
        self.kawabou.screenshot_over_city_snow_kobetu_target()

    def unnatural_temp(self):
        self.kawabou.screenshot_over_city_weather_kobetu()

    def debug(self):
        self.idw_caution()
        self.disp_zero()
        self.three_sigma_caution()
        self.upper_limit_over()
        self.law_limit_over()
        self.unnatural_dam()
        self.unnatural_haisui()
        self.unnatural_suisitu()
        self.unnatural_temp()
        self.visual_dam()
        self.visual_kaigan()
        self.visual_snow()
        self.cod_zero()
        self.soon_snow()




def main():
    tokyo = Tokyo()
    tokyo.debug()

if __name__ == "__main__":
    main()