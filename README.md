Cryptocurrency data scraping
=============================
> 가상화폐 시세 데이터 가져오기

### Prerequisites
* Python 3.5

### 거래소
* [UPbit](https://upbit.com)
* [bithumb](https://www.bithumb.com)

### UPbit 비공식 API URL 분석
* HOST
> https://crix-api-endpoint.upbit.com/v1/crix
* 홈페이지 거래소 하단의 체결/일별 정보에 대한 데이터 URL
> /trades/{정보단위}?code=CRIX.UPBIT.{기준화폐}-{거래화폐}&count={데이터수}
>   > * 정보단위
>   >   * ticks : 실시간 체결 정보
>   >   * days : 하루 단위 거래 정보
>   > * 기준화폐
>   >   * KRW
>   >   * BTC
>   >   * ETH
>   >   * USDT
>   > * 거래화폐
>   >   * BTC
>   >   * ETH
>   >   * XRP
>   >   * ADA
>   >   * etc..
* 홈페이지 거래소 중앙의 그래프에 대한 데이터 URL
> /candles/{정보단위}?code=CRIX.UPBIT.{기준화폐}-{거래화폐}&count={데이터수}&to={날짜}%20{시간}
>   > * 정보단위
>   >   * months : 월 단위 거래 정보
>   >   * weeks : 주 단위 거래 정보
>   >   * days : 하루 단위 거래 정보
>   >   * minutes : 분 단위 거래 정보
>   >       * minutes/{분단위숫자} : 1/3/5/10/15/30/60/240
>   > * 기준화폐
>   >   * KRW
>   >   * BTC
>   >   * ETH
>   >   * USDT
>   > * 거래화폐
>   >   * BTC
>   >   * ETH
>   >   * XRP
>   >   * ADA
>   >   * etc..
>   > * 데이터수 (최대 200개까지 조회 가능)
>   >   * 숫자
>   > * 날짜
>   >   * YYYY-MM-DD
>   > * 시간 (UTC 24시 기준)
>   >   * HH:MM:SS