#!python
#
# Access data via the EIA API
# See:  https://www.eia.gov/opendata/qb.php?category=371
#

import json, urllib.request
import pandas as pd
from key import myKey

def getAPIData(key, series): ###{{{1
    """get sales data via the eia API"""
    urlAPI = "http://api.eia.gov/series/?api_key=" + key + "&series_id=" + series
    with urllib.request.urlopen(urlAPI) as url:
        data = json.loads(url.read().decode())
    df = pd.DataFrame(data["series"])
    cols = ['year', df.units[0]]
    return pd.DataFrame(df.data[0], columns=cols)
###}}}

resSales = getAPIData(myKey(), "ELEC.SALES.PA-RES.A")
comSales = getAPIData(myKey(), "ELEC.SALES.PA-COM.A")
indSales = getAPIData(myKey(), "ELEC.SALES.PA-IND.A")

resPrice = getAPIData(myKey(), "ELEC.PRICE.PA-RES.A")
comPrice = getAPIData(myKey(), "ELEC.PRICE.PA-COM.A")
indPrice = getAPIData(myKey(), "ELEC.PRICE.PA-IND.A")


