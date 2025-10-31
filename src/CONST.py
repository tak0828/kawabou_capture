import os
from zoneinfo import ZoneInfo
from dataclasses import dataclass

# config.iniのパス
CONFIG_FILE_PATH = './config.ini'

# 地点と地点コードを紐づける
PLACE_CODE = {
    "北海道": 81,
    "東北"  : 82,
    "関東"  : 83,
    "北陸"  : 84,
    "中部"  : 85,
    "近畿"  : 86,
    "中国"  : 87,
    "四国"  : 88,
    "九州"  : 89,
    "沖縄"  : 90,
}

# ===== 設定 =====
TZ = ZoneInfo(os.getenv("TZ", "Asia/Tokyo"))
LOG_DIR = os.getenv("LOG_DIR", "./logs")

@dataclass
class MODE:
    timing = "timing"
    absolute = "absolute"
