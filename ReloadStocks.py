# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 02:59:10 2016

@author: Hugo
"""
from pymongo import MongoClient

def ReloadStocks():
    client = MongoClient()
    db = client.HistPrices
    
    db.Stocks.delete_many({})
    db.Stocks.insert_many([{'QuandlID':'WIKI/FOXA','BBGTicker':'FOXA', 'Name' :'21ST CENTRY FOX A CM'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/FOX','BBGTicker':'FOX', 'Name' :'21ST CENTRY FOX B CM'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/ATVI','BBGTicker':'ATVI', 'Name' :'ACTIVISION BLIZZARD'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/ADBE','BBGTicker':'ADBE', 'Name' :'ADOBE SYSTEMS INC'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/AKAM','BBGTicker':'AKAM', 'Name' :'AKAMAI TECHNOLOGIES'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/ALXN','BBGTicker':'ALXN', 'Name' :'ALEXION PHARM INC'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/GOOGL','BBGTicker':'GOOGL', 'Name' :'ALPHABET CL A CMN'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/GOOG','BBGTicker':'GOOG', 'Name' :'ALPHABET CL C CAP'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/AMZN','BBGTicker':'AMZN', 'Name' :'AMAZON.COM INC'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/AAL','BBGTicker':'AAL', 'Name' :'AMERICAN AIRLINES GP'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/AMGN','BBGTicker':'AMGN', 'Name' :'AMGEN'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/ADI','BBGTicker':'ADI', 'Name' :'ANALOG DEVICES CMN'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/AAPL','BBGTicker':'AAPL', 'Name' :'APPLE INC.'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/AMAT','BBGTicker':'AMAT', 'Name' :'APPLIED MATERIALS'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/ADSK','BBGTicker':'ADSK', 'Name' :'AUTODESK INC'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/ADP','BBGTicker':'ADP', 'Name' :'AUTOMATIC DATA PROCS'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/AVGO','BBGTicker':'AVGO', 'Name' :'AVAGO TECHNOLOGIES L'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/BIDU','BBGTicker':'BIDU', 'Name' :'BAIDU INC.'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/BBBY','BBGTicker':'BBBY', 'Name' :'BED BATH & BEYOND'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/BIIB','BBGTicker':'BIIB', 'Name' :'BIOGEN INC CMN'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/BMRN','BBGTicker':'BMRN', 'Name' :'BIOMARIN PHARMACEUT'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/BRCM','BBGTicker':'BRCM', 'Name' :'BROADCOM CORP'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/CHRW','BBGTicker':'CHRW', 'Name' :'C.H. ROBINSON WW'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/CA','BBGTicker':'CA', 'Name' :'CA INC'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/CELG','BBGTicker':'CELG', 'Name' :'CELGENE CORP'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/CERN','BBGTicker':'CERN', 'Name' :'CERNER CORP'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/CHTR','BBGTicker':'CHTR', 'Name' :'CHARTER COMMUNICATIO'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/CHKP','BBGTicker':'CHKP', 'Name' :'CHECK POINT SOFTWARE'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/CSCO','BBGTicker':'CSCO', 'Name' :'CISCO SYSTEMS INC'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/CTXS','BBGTicker':'CTXS', 'Name' :'CITRIX SYSTEMS INC'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/CTSH','BBGTicker':'CTSH', 'Name' :'COGNIZANT TECH SOL'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/CMCSK','BBGTicker':'CMCSK', 'Name' :'COMCAST CL A SPCL'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/CMCSA','BBGTicker':'CMCSA', 'Name' :'COMCAST CORP A'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/COST','BBGTicker':'COST', 'Name' :'COSTCO WHOLESALE'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/DISCA','BBGTicker':'DISCA', 'Name' :'DISCOVERY COMM A'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/DISCK','BBGTicker':'DISCK', 'Name' :'DISCOVERY COMM INC'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/DISH','BBGTicker':'DISH', 'Name' :'DISH NETWORK CORP'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/DLTR','BBGTicker':'DLTR', 'Name' :'DOLLAR TREE INC'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/EBAY','BBGTicker':'EBAY', 'Name' :'EBAY INC.'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/EA','BBGTicker':'EA', 'Name' :'ELECTRONIC ARTS INC'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/EXPD','BBGTicker':'EXPD', 'Name' :'EXPEDITORS INTL'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/ESRX','BBGTicker':'ESRX', 'Name' :'EXPRESS SCRIPTS'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/FB','BBGTicker':'FB', 'Name' :'FACEBOOK INC'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/FAST','BBGTicker':'FAST', 'Name' :'FASTENAL CO'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/FISV','BBGTicker':'FISV', 'Name' :'FISERV INC.'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/GRMN','BBGTicker':'GRMN', 'Name' :'GARMIN LTD'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/GILD','BBGTicker':'GILD', 'Name' :'GILEAD SCIENCES INC'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/HSIC','BBGTicker':'HSIC', 'Name' :'HENRY SCHEIN INC.'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/ILMN','BBGTicker':'ILMN', 'Name' :'ILLUMINA INC.'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/INCY','BBGTicker':'INCY', 'Name' :'INCYTE CORPORATION'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/INTC','BBGTicker':'INTC', 'Name' :'INTEL CORP'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/INTU','BBGTicker':'INTU', 'Name' :'INTUIT INC'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/ISRG','BBGTicker':'ISRG', 'Name' :'INTUITIVE SURG INC.'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/KLAC','BBGTicker':'KLAC', 'Name' :'K L A-TENCOR CORP'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/GMCR','BBGTicker':'GMCR', 'Name' :'KEURIG GREEN MTN CMN'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/KHC','BBGTicker':'KHC', 'Name' :'KRAFT HEINZ CO CMN'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/LRCX','BBGTicker':'LRCX', 'Name' :'LAM RESEARCH CORP'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/LBTYA','BBGTicker':'LBTYA', 'Name' :'LIBERTY GLOBAL ORD A'}])
    #db.Stocks.insert_many([{'QuandlID':'WIKI/LBTYK','BBGTicker':'LBTYK', 'Name' :'LIBERTY GLOBAL ORD C'}])
    #db.Stocks.insert_many([{'QuandlID':'GOOG/NASDAQ_LMCK','BBGTicker':'LMCK', 'Name' :'LIBERTY MEDIA C'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/LMCA','BBGTicker':'LMCA', 'Name' :'LIBERTY MEDIA SRS A'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/LVNTA','BBGTicker':'LVNTA', 'Name' :'LIBERTY VNTRS SRS A'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/LLTC','BBGTicker':'LLTC', 'Name' :'LINEAR TECHNOLOGY'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/MAR','BBGTicker':'MAR', 'Name' :'MARRIOT INT CL A'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/MAT','BBGTicker':'MAT', 'Name' :'MATTEL INC'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/MU','BBGTicker':'MU', 'Name' :'MICRON TECHNOLOGY'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/MSFT','BBGTicker':'MSFT', 'Name' :'MICROSOFT CORP'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/MDLZ','BBGTicker':'MDLZ', 'Name' :'MONDELEZ INTL CMN A'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/MNST','BBGTicker':'MNST', 'Name' :'MONSTER BEVERAGE CP'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/MYL','BBGTicker':'MYL', 'Name' :'MYLAN NV ORD SHS'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/NTAP','BBGTicker':'NTAP', 'Name' :'NETAPP INC.'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/NFLX','BBGTicker':'NFLX', 'Name' :'NETFLIX INC.'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/NVDA','BBGTicker':'NVDA', 'Name' :'NVIDIA CORPORATION'}])
    #db.Stocks.insert_many([{'QuandlID':'WIKI/NXPI','BBGTicker':'NXPI', 'Name' :'NXP SEMICONDUCTORS'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/ORLY','BBGTicker':'ORLY', 'Name' :'OREILLY AUTOMOTIVE'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/PCAR','BBGTicker':'PCAR', 'Name' :'PACCAR INC.'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/PAYX','BBGTicker':'PAYX', 'Name' :'PAYCHEX INC.'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/QCOM','BBGTicker':'QCOM', 'Name' :'QUALCOMM INC'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/REGN','BBGTicker':'REGN', 'Name' :'REGENERON PHARMACEUT'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/ROST','BBGTicker':'ROST', 'Name' :'ROSS STORES INC.'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/SNDK','BBGTicker':'SNDK', 'Name' :'SANDISK CORPORATION'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/SBAC','BBGTicker':'SBAC', 'Name' :'SBA COMMUNICATIONS'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/STX','BBGTicker':'STX', 'Name' :'SEAGATE TECHNOLOGY'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/SIRI','BBGTicker':'SIRI', 'Name' :'SIRIUS XM HOLDINGS I'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/SWKS','BBGTicker':'SWKS', 'Name' :'SKYWORKS SOLUTIONS'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/SPLS','BBGTicker':'SPLS', 'Name' :'STAPLES INC.'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/SBUX','BBGTicker':'SBUX', 'Name' :'STARBUCKS CORP'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/SRCL','BBGTicker':'SRCL', 'Name' :'STERICYCLE INC.'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/SYMC','BBGTicker':'SYMC', 'Name' :'SYMANTEC CORPORATION'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/TSLA','BBGTicker':'TSLA', 'Name' :'TESLA MOTORS INC'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/TXN','BBGTicker':'TXN', 'Name' :'TEXAS INSTRUMENTS'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/PCLN','BBGTicker':'PCLN', 'Name' :'THE PRICELINE GP CM'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/TSCO','BBGTicker':'TSCO', 'Name' :'TRACTOR SUPPLY CO'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/TRIP','BBGTicker':'TRIP', 'Name' :'TRIPADVISOR INC.'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/VRSK','BBGTicker':'VRSK', 'Name' :'VERISK ANALYTICS INC'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/VRTX','BBGTicker':'VRTX', 'Name' :'VERTEX PHARMACEUTIC'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/VIAB','BBGTicker':'VIAB', 'Name' :'VIACOM INC CL B'}])
    db.Stocks.insert_many([{'QuandlID':'GOOG/NASDAQ_VIP','BBGTicker':'VIP', 'Name' :'VIMPELCOM LTD'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/VOD','BBGTicker':'VOD', 'Name' :'VODAFONE GRP PLC ADS'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/WBA','BBGTicker':'WBA', 'Name' :'WALGREENS BTS ALN CM'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/WDC','BBGTicker':'WDC', 'Name' :'WESTERN DIGITAL CP'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/WFM','BBGTicker':'WFM', 'Name' :'WHOLE FOODS MARKET'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/WYNN','BBGTicker':'WYNN', 'Name' :'WYNN RESORTS LIMITED'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/XLNX','BBGTicker':'XLNX', 'Name' :'XILINX INC.'}])
    db.Stocks.insert_many([{'QuandlID':'WIKI/YHOO','BBGTicker':'YHOO', 'Name' :'YAHOO! INC.'}])
