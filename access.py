#!python
#
# Access data via the EIA API
# See:  https://www.eia.gov/opendata/qb.php?category=371
#

import json, urllib.request
import pandas as pd
import matplotlib.pyplot as plt
from key import myKey
from functools import reduce

def getAPIData(key, series): ###{{{1
    """get sales data via the eia API"""
    urlAPI = "http://api.eia.gov/series/?api_key=" + key + "&series_id=" + series
    with urllib.request.urlopen(urlAPI) as url:
        data = json.loads(url.read().decode())
    df = pd.DataFrame(data["series"])
    cols = ['year', df.units[0]]
    return pd.DataFrame(df.data[0], columns=cols)
###}}}

def merge3(dataframes,joinOn): ###{{{1
    return reduce(lambda left, right: pd.merge(left,right,on=joinOn), dataframes)
###}}}

resSales = getAPIData(myKey(), "ELEC.SALES.PA-RES.A")
comSales = getAPIData(myKey(), "ELEC.SALES.PA-COM.A")
indSales = getAPIData(myKey(), "ELEC.SALES.PA-IND.A")

resSalesSEDS = getAPIData(myKey(), "SEDS.ESRCP.PA.A")
comSalesSEDS = getAPIData(myKey(), "SEDS.ESCCP.PA.A")
indSalesSEDS = getAPIData(myKey(), "SEDS.ESICP.PA.A")

resPrice = getAPIData(myKey(), "ELEC.PRICE.PA-RES.A")
comPrice = getAPIData(myKey(), "ELEC.PRICE.PA-COM.A")
indPrice = getAPIData(myKey(), "ELEC.PRICE.PA-IND.A")

getAPIData(myKey(),"EMISS.CO2-TOTV-EC-TO-PA.A")

# merge residential commercial and industrial datasets
dm = merge3([resSales, comSales, indSales],'years')
dm.columns = ['year', 'Residential', 'Commercial', 'Industrial']


dm.plot(x='year').invert_xaxis()
plt.show()


