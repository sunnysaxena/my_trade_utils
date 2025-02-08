def calculate_open_high(Open, High):
    if High >= Open:
        output = abs(Open - High)
    else:
        output = -abs(Open - High)
    return output


def calculate_open_low(Open, Low):
    if Low <= Open:
        if Low == Open:
            output = abs(Open - Low)
        else:
            output = -abs(Open - Low)
    else:
        output = -abs(Open - Low)
    return output


def calculate_open_close(Open, Close):
    if Close >= Open:
        output = abs(Open - Close)
    else:
        output = -abs(Open - Close)
    return output


def extract_feature(df):
    open_change = [round(previous - next, 2) for previous, next in zip(df['open'].tolist()[1:], df['close'].tolist())]
    open_change.insert(0, 0)
    df['open_change'] = open_change

    change = [round(next - previous, 2) for previous, next in zip(df['close'].tolist(), df['close'].tolist()[1:])]
    change.insert(0, 0)
    df['mkt_change'] = change

    # change_percent = [float((next-previous) / previous * 100) for previous, next in zip(df['close'].tolist(), df['close'].tolist()[1:])]
    # change_percent.insert(0, 0)
    # df['mkt_change_%'] = change_percent

    # (today_close - yesterday) / yesterday * 100
    change_percent = [round(float((next - previous) / previous * 100), 2) for previous, next in
                      zip(df['close'].tolist(), df['close'].tolist()[1:])]
    change_percent.insert(0, 0)
    df['mkt_change_%'] = change_percent

    open_high = [calculate_open_high(open, high) for open, high in zip(df['open'].tolist(), df['high'].tolist())]
    df['open_high'] = open_high

    open_low = [calculate_open_low(open, low) for open, low in zip(df['open'].tolist(), df['low'].tolist())]
    df['open_low'] = open_low

    open_close = [calculate_open_close(open, close) for open, close in zip(df['open'].tolist(), df['close'].tolist())]
    df['open_close'] = open_close

    return df


# define trend classification function
def classify_trend_v1(row, prev_row):
    """
        Usage:
        # Apply trend classification (classify_trend_v1)
        df['trend'] = df.apply(lambda row: classify_trend(row, df.shift(1).loc[row.name]), axis=1)

        :param row:
        :param prev_row:
        :return: 'trend_type'
    """
    if prev_row.isnull().any():  # Handle missing previous row
        return "Unknown"
    if row['close'] > prev_row['close'] and row['high'] > prev_row['high']:
        return "Uptrend"
    elif row['close'] < prev_row['close'] and row['low'] < prev_row['low']:
        return "Downtrend"
    elif prev_row['low'] <= row['close'] <= prev_row['high']:
        return "Sideways"
    elif row['range'] > row['avg_range'] * 1.2:
        return "Volatility"
    else:
        return "Unknown"


# define trend classification function
def classify_trend_v2(row, prev_row):
    """
        Usage:
        # Apply trend classification (classify_trend_v2)
        df['trend'] = df.apply(lambda row: classify_trend(row, df.shift(1).loc[row.name]), axis=1)

        :param row:
        :param prev_row:
        :return: 'trend_type'
    """
    if prev_row.isnull().any():  # Handle missing previous row
        return "Unknown"
    if row['close'] > prev_row['close'] and row['high'] > prev_row['high']:
        return "Uptrend"
    elif row['close'] < prev_row['close'] and row['low'] < prev_row['low']:
        return "Downtrend"
    elif prev_row['low'] <= row['close'] <= prev_row['high']:
        return "Sideways"
    else:
        return "Volatile"
