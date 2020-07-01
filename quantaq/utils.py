import pandas as pd


def to_dataframe(data, **kwargs) -> pd.DataFrame:
    """Convert an array of dictionaries into a pd.DataFrame.

    :param list data: Data in the form of a list of dicts
    :param bool force_ts: Force timestamp columns to timestamps

    :returns: DataFrame with all data
    :rtype: pd.DataFrame
    """
    force_ts = kwargs.pop("force_ts", True)

    if not isinstance(data, list):
        raise TypeError("Current data must be a list")
    
    data = pd.json_normalize(data)

    if force_ts:
        for col in [c for c in data.columns if "timestamp" in c.lower()]:
            try:
                data[col] = data[col].apply(pd.to_datetime)
            except: #pragma: no cover
                pass
    
    return data
