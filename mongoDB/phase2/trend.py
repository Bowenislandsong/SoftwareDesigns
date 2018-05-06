from pytrends.request import TrendReq
import pandas as pd


def tredreport(keyword):
    pytrend = TrendReq(hl='en-US')
    pytrend.build_payload(kw_list=[keyword], timeframe='today 1-m', geo='US', gprop='news')
    # Interest Over Time
    interest_over_time_df = pytrend.interest_over_time()
    print(interest_over_time_df.head())



if __name__ == "__main__":
    tredreport("mama")