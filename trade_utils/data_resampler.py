import pandas as pd
import logging

logger = logging.getLogger(__name__)

def convert_1min_to_timeframe(df_1min, target_timeframe):
    """
    Converts 1-minute data to a specified timeframe.

    Args:
        df_1min (pd.DataFrame): DataFrame containing 1-minute data with a 'timestamp' column.
        target_timeframe (str): The desired timeframe (e.g., '5T', '15T', '1H', '1D', 'W', 'M').

    Returns:
        pd.DataFrame: DataFrame containing data resampled to the target timeframe, or an empty DataFrame on error.
    """
    try:
        if 'timestamp' not in df_1min.columns:
            logger.error("Input DataFrame must have a 'timestamp' column.")
            return pd.DataFrame()

        df_1min = df_1min.copy()  # Avoid modifying the original DataFrame
        df_1min.set_index('timestamp', inplace=True)
        df_1min.index = pd.to_datetime(df_1min.index)

        if not isinstance(target_timeframe, str):
            logger.error("Target timeframe must be a string.")
            return pd.DataFrame()

        df_resampled = df_1min.resample(target_timeframe).agg({
            'open': 'first',
            'high': 'max',
            'low': 'min',
            'close': 'last',
            'volume': 'sum'
        })

        df_resampled.dropna(inplace=True)  # Remove NaN values from incomplete intervals
        return df_resampled

    except Exception as e:
        logger.error(f"Error converting 1-minute data to {target_timeframe}: {e}")
        return pd.DataFrame()

def convert_day_to_timeframe(df_day, target_timeframe, label='left', closed='left'):
    """
    Converts daily data to a specified timeframe.

    Args:
        df_day (pd.DataFrame): DataFrame containing daily data with a 'timestamp' column.
        target_timeframe (str): The desired timeframe (e.g., '5D', 'W-MON').
        label (str, optional): Passed to pandas resample. Defaults to 'left'.
        closed (str, optional): Passed to pandas resample. Defaults to 'left'.

    Returns:
        pd.DataFrame: DataFrame containing data resampled to the target timeframe, or an empty DataFrame on error.
    """
    try:
        if 'timestamp' not in df_day.columns:
            logger.error("Input DataFrame must have a 'timestamp' column.")
            return pd.DataFrame()

        df_day = df_day.copy()  # Avoid modifying the original DataFrame
        df_day.set_index('timestamp', inplace=True)
        df_day.index = pd.to_datetime(df_day.index)

        if not isinstance(target_timeframe, str):
            logger.error("Target timeframe must be a string.")
            return pd.DataFrame()

        df_resampled = df_day.resample(target_timeframe, label=label, closed=closed).agg({
            'open': 'first',
            'high': 'max',
            'low': 'min',
            'close': 'last',
            'volume': 'sum'
        })

        df_resampled.dropna(inplace=True)
        return df_resampled

    except Exception as e:
        logger.error(f"Error converting daily data to {target_timeframe}: {e}")
        return pd.DataFrame()
