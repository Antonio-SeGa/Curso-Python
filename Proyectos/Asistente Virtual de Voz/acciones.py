import yfinance as yf

# Diccionario de empresas y sus tickers
empresas_tickers = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Amazon': 'AMZN',
    'Tesla': 'TSLA',
    'Google': 'GOOGL',
    'Meta': 'META',
    'Nvidia': 'NVDA',
    'Netflix': 'NFLX',
    'Coca Cola': 'KO',
    'Pepsi': 'PEP',
    'Disney': 'DIS',
    'Visa': 'V',
    'Berkshire Hathaway': 'BRK-B',
    'JPMorgan Chase': 'JPM',
    'Johnson & Johnson': 'JNJ',
    'Procter & Gamble': 'PG',
    'Pfizer': 'PFE',
    'Intel': 'INTC',
    'Ibm': 'IBM',
    'Goldman Sachs': 'GS'
}

# Función para obtener el precio regular de mercado
def obtener_precio_mercado(ticker):
    
    accion = yf.Ticker(ticker)
    info = accion.info
    return info['regularMarketDayHigh']
    

accion = input().title().strip()
print(accion)

# Ejemplo: Obtener el precio actual de Apple
precio_empresa = obtener_precio_mercado(empresas_tickers[accion])
print(f"El precio actual {accion} de es: {precio_empresa}")