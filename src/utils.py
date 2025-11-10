import CONST
from CONST import MODE
import configparser
from datetime import datetime, timezone
from dataclasses import dataclass
import os
import re


# # ログの処理をまとめる
# import logging
# from logging.handlers import RotatingFileHandler

# os.makedirs(CONST.LOG_DIR, exist_ok=True)
# kawabou_logger = logging.getLogger("kawabou_logger")
# kawabou_logger.setLevel(logging.INFO)
# handler = RotatingFileHandler(
#     os.path.join(CONST.LOG_DIR, "kawabou_logger.log"), maxBytes=2_000_000, backupCount=5
# )
# handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
# kawabou_logger.addHandler(handler)


from csv import DictReader

def load_csv_as_records(path, encoding="cp932"):
    with open(path, newline="", encoding=encoding) as f:
        return list(DictReader(f))  # 1行=1dict

def build_index(records, key):
    """key列でレコードを引ける dict を作成"""
    return {r[key]: r for r in records}

# 使い方
# rows = load_csv_as_records("data.csv")
# by_id = build_index(rows, key="id")  # 主キー列名に合わせて
# print(rows[0])          # 行番号でアクセス
# print(by_id["A00123"])  # 主キーで高速アクセス

@dataclass
class Area:
    name:str
    code:str

@dataclass
class Pref:
    name:str
    code:str


@dataclass
class AbsoluteTime:
    starthour:str
    endhour  :str
    startmin :str
    endmin   :str

# 設定ファイルの読み込み
def read_config():
    config = configparser.ConfigParser()
    try:
        with open(CONST.CONFIG_FILE_PATH, "r", encoding='utf-8') as f:
            config.read_file(f)
    except FileNotFoundError:
        print("設定ファイルが見つかりません")
        return None, None
    
    # start_dateとdlpathを読み込み
    start_date = config.get('settings', 'start_date', fallback='')
    dlpath = config.get('dl_settings', 'dlpath', fallback='')
    login = {"user":config.get('login','USER',fallback=''),"pw":config.get('login','PW',fallback='')}

    if MODE.absolute == config["settings"]["mode"]:
        print("absolute")
        starthour = normalize_hour_str(int(config['range']['starthour']))
        endhour = normalize_hour_str(int(config['range']['endhour']))
        startmin = normalize_minute_str(int(config['range']['startmin']))
        endmin = normalize_minute_str(int(config['range']['endmin']))

        absolute = AbsoluteTime(starthour,endhour,startmin,endmin)
        # absolute = {"starthour":starthour,"endhour":endhour,"startmin":startmin,"endmin":endmin}
        return start_date, dlpath,login,absolute
    else:
        print("timing")
        minute = normalize_minute_str(int(config['range']['minute']))
        return start_date, dlpath,login,minute

# 2025-10-29 11:11
# 例のように出力される
def now_asia_str():
    now = datetime.now(CONST.TZ)
    year, month, day = now.year, now.month, now.day
    hour, minute    = now.hour, now.minute

    start_time_str = f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}"
    return start_time_str

def normalize_hour_str(v: int) -> str:
    if 0 <= v <= 24:
        return str(v)
    if 24  <= v:
        return "24"
    if v < 0:
        return "00"
    
def normalize_minute_str(v: int) -> str:
    if 0 <= v <= 59:
        return str(v)
    if v == 60:
        return "00"
    if 61  <= v:
        return "59"
    if v < 0:
        return "00"


def split_datetime_parts(s: str):
    """
    CSVの観測日時項目より時間を使用する

    例: "2025/6/1  0:00:00" -> {
        "year_month": "20256",
        "hour": "00",
        "minute": "00",
        "day": "01",
    }
    """
    # 数字だけ抜き出して int に変換（年, 月, 日, 時, 分, 秒 を想定）
    nums = list(map(int, re.findall(r'\d+', s)))
    if len(nums) < 6:
        raise ValueError("日時文字列から年/月/日/時/分/秒を特定できません。")

    y, mo, d, h, mi, sec = nums[:6]
    dt = datetime(y, mo, d, h, mi, sec)

    return {
        "year_month": f"{dt.year}{dt.month:02d}",
        "hour": f"{dt.hour:02d}",
        "minute": f"{dt.minute:02d}",
        "day": f"{dt.day:02d}",
    }
