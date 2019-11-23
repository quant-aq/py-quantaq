import pandas as pd

def list_to_dataframe(data, **kwargs):
    """Convert an array of dictionaries into a pd.DataFrame.
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list")
    
    data = pd.io.json.json_normalize(data)

    for col in [c for c in data.columns if "timestamp" in c.lower()]:
        try:
            data[col] = data[col].apply(pd.to_datetime)
        except: pass
    
    return data
