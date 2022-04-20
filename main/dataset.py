import pandas as pd

def read_xl(filelist="static/data/company_2020_12.xls"):
    df = pd.read_excel(filelist)
    return df