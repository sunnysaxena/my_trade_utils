import os
import time
import datetime
import pandas as pd
from datetime import datetime

time_zone = 'Asia/Kolkata'

option_symbols = {
    'indiavix': 'NSE:INDIAVIX-INDEX',

    'nifty50': 'NSE:NIFTY50-INDEX',

    'niftybank': 'NSE:NIFTYBANK-INDEX',

    'finnifty': 'NSE:FINNIFTY-INDEX'
}

option_symbols_yahoo = {
    'indiavix': '^INDIAVIX',

    'nifty50': '^NSEI',

    'niftybank': '^NSEBANK',

    'finnifty': 'NIFTY_FIN_SERVICE.NS'
}

trend_types = [
    'Uptrend',
    'Downtrend',
    'Sideways',
    'Reversal',
    'Volatility',
    'Seasonal',
    'Random or Chaotic',
    'Range Bound'
]


def generate_dates(end='2023-09-30', periods=1095 + 366 + 365 + 365 + 80):
    df = pd.date_range(end=end, periods=periods).to_pydatetime().tolist()
    dates = [d.strftime("%Y-%m-%d") for d in df]
    return dates


def epoc_to_timestamp(epoch_time):
    if issubclass(type(epoch_time), list):
        return [datetime.fromtimestamp(ep_time).strftime('%Y-%m-%d %H:%M:%S') for ep_time in epoch_time]
    else:
        return datetime.fromtimestamp(epoch_time).strftime('%Y-%m-%d %H:%M:%S')


def epoc_to_timestamp1(epoch_time):
    print(epoch_time)
    if issubclass(type(epoch_time), list):
        return [datetime.fromtimestamp(ep_time).strftime('%Y-%m-%d') for ep_time in epoch_time]
    else:
        return datetime.fromtimestamp(epoch_time).strftime('%Y-%m-%d')


def timestamp_to_epoc(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Convert datetime to Unix timestamp
    df['epoch'] = (df['timestamp'] - pd.Timestamp("1970-01-01")) // pd.Timedelta('1ms')
    return df


def get_today_date():
    return datetime.today().strftime("%Y-%m-%d")


def delete_duplicate_rows(df, verbose=False):
    number = df.duplicated(subset=["open", "high", "low", "close", "volume"], keep=False).sum()

    # check for duplicated indexes
    duplicated_indexes = df.duplicated(keep=False, subset=["open", "high", "low", "close", "volume"])
    duplicated_rows = df[duplicated_indexes]

    # drop duplicated indexes
    df = df[~df.duplicated(keep=False, subset=["open", "high", "low", "close", "volume"])]
    df.drop_duplicates(inplace=True)

    if verbose:
        print(duplicated_rows)

    return df

