import os
import csv as cs
from utils.logger import logger
from datetime import datetime, timedelta
from api import upbit_api

u_api = upbit_api.Api()

UPBIT_CURRENCY = [
      "SNT"     #스테이터스네트워크토큰
    , "XRP"     #리플
    , "BTC"     #비트코인
    , "ADA"     #에이다
    , "XLM"     #스텔라루멘
    , "QTUM"    #퀀텀
    , "TIX"     #블록틱스
    , "EMC2"    #아인스타이늄
    , "XEM"     #뉴이코노미무브먼트
    , "STEEM"   #스팀
    , "GRS"     #그로스톨코인
    , "BCC"     #비트코인캐시
    , "ETH"     #이더리움
    , "POWR"    #파워렛저
    , "MER"     #머큐리
    , "KMD"     #코모도
    , "ETC"     #이더리움클래식
    , "STORJ"   #스토리지
    , "BTG"     #비트코인골드
    , "STRAT"   #스트라티스
    , "MTL"     #메탈
    , "WAVES"   #웨이브
    , "ARK"     #아크
    , "VTC"     #버트코인
    , "LSK"     #리스크
    , "REP"     #어거
    , "PIVX"    #피벡스
    , "XMR"     #모네로
    , "LTC"     #라이트코인
    , "DASH"    #대시
    , "ZEC"     #지캐시
    , "ARDR"    #아더
    , "OMG"     #오미세고
    , "NEO"     #네오
    , "SBD"     #스팀달러
]


def list_write_csv(file_path, file_name, file_fields, list_data):
    # logger.info("[Z] FUNCTION START : list_write_csv()")

    if not os.path.isdir('./data/' + file_path):
        os.makedirs('./data/' + file_path)

    if not os.path.isfile('./data/' + file_path + file_name + '.csv'):
        file = open('./data/' + file_path + file_name + '.csv', 'w', encoding='UTF-8')
        with file:
            writer = cs.DictWriter(file, file_fields)
            writer.writeheader()
            for line in list_data:
                writer.writerow(line)
    else:
        file = open('./data/' + file_path + file_name + '.csv', 'a', encoding='UTF-8')
        with file:
            writer = cs.DictWriter(file, file_fields)
            for line in list_data:
                writer.writerow(line)

    # logger.info("[Z] FUNCTION END : list_write_csv()")


def save_upbit_daily_trade_data(currency_list, day=100, to_date=datetime.today().strftime("%Y-%m-%d")):
    logger.info("[A] FUNCTION START : save_upbit_daily_trade_data()")

    for currency in currency_list:
        logger.info("[a] GET DATA START : " + currency)

        req_count = 100
        req_date = to_date
        daily_data_list = list()

        for c in range(day, 1, -req_count):
            req_count = req_count if c > req_count else c
            results = u_api.get_daily_trade_data(currency, req_count, req_date)

            if results is None:
                return
            elif len(results) < 1:

                break

            if len(results) > 0:
                daily_data_list.extend(results)
                req_date = datetime.strftime(datetime.strptime(daily_data_list[-1]["candleDateTime"], "%Y-%m-%dT%H:%M:%S+00:00") - timedelta(1), "%Y-%m-%d")

        file_path = "upbit/daily/"
        file_name = "daily_" + currency
        file_fields = list(dict(daily_data_list[0]).keys())
        list_write_csv(file_path, file_name, file_fields, daily_data_list)
        logger.info("[a] GET DATA END : " + currency)

    logger.info("[A] FUNCTION END : save_upbit_daily_trade_data()")


def save_upbit_minutes_trade_data(currency_list, unit, day=10, to_date=datetime.today().strftime("%Y-%m-%d")):
    logger.info("[B] FUNCTION START : save_upbit_minutes_trade_data()")

    for currency in currency_list:
        logger.info("[b] GET DATA START : " + currency)

        count = int(day * (24 * 60 / unit))
        req_count = int((24 * 60 / unit) / 2)
        req_date = to_date
        req_time = "00:00:00"

        for c in range(count, 1, -req_count):
            req_count = req_count if c > req_count else c
            results = u_api.get_minutes_trade_data(unit, currency, req_count, req_date, req_time)

            if results is None:
                return
            elif len(results) < 1:
                break

            if len(results) > 0:
                req_date = datetime.strftime(datetime.strptime(results[-1]["candleDateTime"], "%Y-%m-%dT%H:%M:%S+00:00"), "%Y-%m-%d")
                req_time = datetime.strftime(datetime.strptime(results[-1]["candleDateTime"], "%Y-%m-%dT%H:%M:%S+00:00"), "%H:%M:%S")

                file_path = "upbit/minutes/" + currency + "/"
                file_name = str(results[0]["candleDateTime"]).replace("-", "_")[:7] + "_" + currency
                file_fields = list(dict(results[0]).keys())
                list_write_csv(file_path, file_name, file_fields, results)

        logger.info("[b] GET DATA END : " + currency)

    logger.info("[B] FUNCTION END : save_upbit_minutes_trade_data()")


if __name__ == "__main__":
    # 일단위 upbit 데이터 csv 저장
    save_upbit_daily_trade_data(UPBIT_CURRENCY, 365)
    # 분단위(5/15/30분) upbit 데이터 csv 저장
    save_upbit_minutes_trade_data(UPBIT_CURRENCY, 5, 365)
