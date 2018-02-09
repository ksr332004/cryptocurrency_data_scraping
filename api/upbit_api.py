from . import *
from utils.error import *
import requests


class Api():
    def __init__(self):
        self.headers = {}
        self.set_headers()

    def set_headers(self):
        """
        기본 헤더 생성
        :return:
        """
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }

    def get_daily_trade_data(self, currency, count, to_date):
        """
        upbit 하루단위 거래 데이터를 가져오는 api
        :return:
        """
        count = str(count)
        url = UPBIT_BASE_URL + '/candles/days?code=CRIX.UPBIT.KRW-' + currency + '&count=' + count + '&to=' + to_date + '%2000:00:00'
        r = requests.get(url, headers=self.headers)

        if r.status_code == 200:
            return r.json()
        elif r.status_code == 401:
            Unauthorized(r.text)
            self.get_daily_trade_data()
        elif r.status_code == 503:
            ServiceUnavailable(r.text)
            return None

    def get_minutes_trade_data(self, unit, currency, count, to_date, to_time):
        """
        upbit 분단위 거래 데이터를 가져오는 api
        :return:
        """
        unit = str(unit)
        count = str(count)
        url = UPBIT_BASE_URL + '/candles/minutes/' + unit + '?code=CRIX.UPBIT.KRW-' + currency + '&count=' + count + '&to=' + to_date + '%20' + to_time
        r = requests.get(url, headers=self.headers)

        if r.status_code == 200:
            return r.json()
        elif r.status_code == 401:
            Unauthorized(r.text)
            self.get_daily_trade_data()
        elif r.status_code == 503:
            ServiceUnavailable(r.text)
            return None