from . import *
from utils.error import *
import requests


class Api(object):
    def __init__(self):
        self.api_key = None
        self.secret_key = None
        self.headers = {}
        self.set_headers()

    def set_headers(self):
        """
        기본 헤더 생성
        :return:
        """
        self.api_key = API_KEY
        self.secret_key = SECRET_KEY
        self.headers = {
            "apiKey": self.api_key,
            "secretKey": self.secret_key
        }

    def get_ticker(self, url):
        """
        bithumb 거래소 마지막 거래 정보 api
        :return:
        """
        r = requests.get(BITHUMB_BASE_URL + '/public/ticker/' + url)

        if r.status_code == 200:
            return r.json()
        elif r.status_code == 401:
            Unauthorized(r.text)
            self.get_ticker()
        elif r.status_code == 503:
            ServiceUnavailable(r.text)
            return None

    def get_order_book(self, url):
        """
        bithumb 거래소 판/구매 등록 대기 또는 거래 중 내역 정보 api
        :return:
        """
        r = requests.get(BITHUMB_BASE_URL + '/public/orderbook/' + url)

        if r.status_code == 200:
            return r.json()
        elif r.status_code == 401:
            Unauthorized(r.text)
            self.get_order_book()
        elif r.status_code == 503:
            ServiceUnavailable(r.text)
            return None

    def get_recent_transactions(self, url, count):
        """
        bithumb 거래소 거래 체결 완료 내역 api
        :return:
        """
        r = requests.get(BITHUMB_BASE_URL + '/public/recent_transactions/' + url, json=count)

        if r.status_code == 200:
            return r.json()
        elif r.status_code == 401:
            Unauthorized(r.text)
            self.get_recent_transactions()
        elif r.status_code == 503:
            ServiceUnavailable(r.text)
            return None