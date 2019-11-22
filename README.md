pyeze-test-generator
--------------------

used to create `synthetic-symbols.csv` and `ALERTS.DAT` for pyeze testing.

`make`

 - reads a list of symbols from STDIN,

 - queries yahoo finance for open,high,low,close from most recent intraday minute

 - generate synthetic symbol name for each symbol-lot

 - generate 5 Lot bands of alerts for each symbol
   - L = Last 
   - v = (high - low) * FACTOR
   - Lot 1 alert: Last < L-v, Last > L+v
   - Lot 2 alert: Last < L-v*2, Last > L+v*2
   - Lot 3 alert: Last < L-v*3, Last > L+v*3
   - Lot 4 alert: Last < L-v*4, Last > L+v*4
   - Lot 5 alert: Last < L-v*5, Last > L+v*5

- generate output ssm.csv

- generate output alerts.csv


