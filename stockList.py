#lists of stocks based on industry/market share

def t10MarketShare():
    stocks = ["AAPL", "MSFT", "GOOG", "AMZN", "NVDA", "META", "TSLA", "V", "UNH", "XOM"]
    return(stocks)

def t10Commerical():
    stocks = ["V", "MA", "SPGI", "PYPL", "MCO", "CPRT", "GPN", "EFX", "AIU", "OMC"]
    return(stocks)

def t10Communications():
    stocks = ["TMUS", "VZ", "T", "LBRDA", "IRDM", "FYBR", "CCOI", "TIGO", "GSAT", "GOGO"]
    return(stocks)

def t10ConsDurables():
    stocks = ["TSLA", "F", "GM", "DHI", "LEN", "NVR", "PHM", "LKQ", "RIVN", "SNA"]
    return(stocks)

def t10ConsNonDurables():
    stocks = ["PG", "KO", "PEP", "NKE", "PM", "MDLZ", "MO", "EL", "CL", "MNST"]
    return(stocks)

def t10ConsServices():
    stocks = ["MCD", "CMCSA", "DIS", "SBUX", "BKNG", "ABNB", "CMG", "MAR", "CTAS", "CHTR"]
    return(stocks)

def t10DistServices():
    stocks = ["BSX", "MCK", "ABC", "GWW", "FAST", "FERG", "CAH", "GPC", "POOL", "HSIC"]
    return(stocks)

def t10Electronics():
    stocks = ["AAPL", "NVDA", "AVGO", "CSCO", "AMD", "TXN", "RTX", "INTC", "HON", "QCOM"]
    return(stocks)

def t10Energy():
    stocks = ["XOM", "CVX", "COP", "EOG", "OXY", "PXD", "MPC", "PSX", "HES", "VLO"]
    return(stocks)

def t10Finance():
    stocks = ["JPM", "BAC", "WFC", "MS", "AXP", "GS", "BX", "BLK", "SCHW", "C"]
    return(stocks)

def t10HealthServices():
    stocks = ["UNH", "ELV", "CI", "HCA", "HUM", "IQV", "CNC", "LH", "MOH", "DGX"]
    return(stocks)

def t10HealthTech():
    stocks = ["LLY", "JNJ", "MRK", "ABBV", "PFE", "TMO", "ABT", "DHR", "BMY", "AMGN"]
    return(stocks)

def t10IndServices():
    stocks = ["WM", "SLB", "EPD", "RSG", "ET", "KMI", "MPLX", "BKR", "HAL", "PWR"]
    return(stocks)

def t10Misc():
    stocks = ["TPL", "VNOM", "BXSL", "BSM", "KRP", "DMLP", "WT", "BCSF", "TCPC", "CION"]
    return(stocks)

def t10Mine():
    stocks = ["SCCO", "FCX", "NEM", "NUE", "GOLD", "VMC", "MLM", "STLD", "RS", "RGLD"]
    return(stocks)

def t10Process():
    stocks = ["LIN", "APD", "SHW", "ECL", "ADM", "CTVA", "DOW", "PPG", "DD", "LYB"]
    return(stocks)

def t10Manu():
    stocks = ["GE", "AMAT", "CAT", "DE", "LRCX", "ETN", "ITW", "MMM", "PH", "JCI"]
    return(stocks)

def t10Retail():
    stocks = ["AMZN", "WMT", "HD", "COST", "BABA", "LOW", "CVS", "TJX", "PDD", "MELI"]
    return(stocks)

def t10Tech():
    stocks = ["MSFT", "GOOG", "META", "ORCL", "CRM", "ACN", "ADBE", "NFLX", "INTU", "IBM"]
    return(stocks)

def t10Transport():
    stocks = ["UPS", "UNP", "UBER", "CSX", "FDX", "NSC", "SYY", "ODFL", "DAL", "JBHT"]
    return(stocks)

def t10Util():
    stocks = ["NEE", "SO", "DUK", "SRE", "AEP", "D", "EXC", "XEL", "PCG", "ED"]
    return(stocks)

def allMajor():
    stocks = []
    stocks = stocks + t10Commerical() + t10Communications() + t10ConsDurables() + t10ConsNonDurables() + t10ConsServices() + t10DistServices() + t10Electronics() + t10Energy() + t10Finance() + t10HealthServices() + t10HealthTech() + t10IndServices() + t10Manu() + t10Mine() + t10Misc() + t10Process() + t10Retail() + t10Tech() + t10Transport() + t10Util()
    return(stocks)

def test():
    stocks = ["NEE", "SO"]
    return(stocks)