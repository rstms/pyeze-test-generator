#!/usr/bin/env python

import sys
import yfinance as yf

def read_symbols():
    return [s.strip() for s in sys.stdin.readlines() if s.strip()]

def generate(symbol):
    ticker = yf.Ticker(symbol)
    bars = ticker.history(interval='1m', period='1d')
    b = bars.iloc[-1]
    return [symbol, b.name.strftime('%Y-%m-%d'), b.name.strftime('%H:%M'),
            b['Open'], b['High'], b['Low'], b['Close']]

LOTS = 5
INTERVAL_FACTOR = .5

def main():
    data = [generate(symbol) for symbol in read_symbols()]

    for d in data:
          print(repr(d))

    with open('ssm.csv', 'w') as ssm_file:
        with open('alerts.csv', 'w') as alert_file:
            for d in data:
                _symbol, _date, _time, _open, _high, _low, _close = d
                v = (_high-_low) * INTERVAL_FACTOR
                for lot in range(1, LOTS+1):
                    ssm = '=%s-L%d' % (_symbol, lot)
                    description = 'Lot %d' % lot

                    ssm_file.write('%s,%s,%s\n' % (ssm, _symbol, description))

                    alert_file.write('%s,higher,%.2f\n' % (ssm, _close+(v*lot)))
                    alert_file.write('%s,lower,%.2f\n' % (ssm, _close-(v*lot)))

if __name__ == '__main__':
    main()
