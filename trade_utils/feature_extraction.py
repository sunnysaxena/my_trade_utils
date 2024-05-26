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
    
    change = [round(next-previous, 2) for previous, next in zip(df['close'].tolist(), df['close'].tolist()[1:])]
    change.insert(0, 0)
    df['mkt_change'] = change
    
    # change_percent = [float((next-previous) / previous * 100) for previous, next in zip(df['close'].tolist(), df['close'].tolist()[1:])]
    # change_percent.insert(0, 0)
    # df['mkt_change_%'] = change_percent
    
    # (today_close - yesterday) / yesterday * 100
    change_percent = [round(float((next-previous) / previous * 100), 2) for previous, next in zip(df['close'].tolist(), df['close'].tolist()[1:])]
    change_percent.insert(0, 0)
    df['mkt_change_%'] = change_percent
    
    open_high = [calculate_open_high(open, high) for open, high in zip(df['open'].tolist(), df['high'].tolist())]
    df['open_high'] = open_high
    
    open_low = [calculate_open_low(open, low) for open, low in zip(df['open'].tolist(), df['low'].tolist())]
    df['open_low'] = open_low
    
    open_close = [calculate_open_close(open, close) for open, close in zip(df['open'].tolist(), df['close'].tolist())]
    df['open_close'] = open_close

    return df
