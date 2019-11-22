pyeze-test-generator
--------------------

used to create `synthetic-symbols.csv` and `ALERTS.DAT` for pyeze testing.

ptg:
 - reads a list of symbols from STDIN,
 - gets open,high,low,close from last minute of data from yahoo finance
 - generate 5 Lot bands of data for each symbol
   - L = Last 
   - v = (high - low)/2
   - Lot 1 alert: Last < L-v, Last > L+v
   - Lot 2 alert: Last < L-v*2, Last > L+v*3
   - Lot 3 alert: Last < L-v*3, Last > L+v*3
   - Lot 4 alert: Last < L-v*4, Last > L+v*4
   - Lot 5 alert: Last < L-v*5, Last > L+v*5
- generate output synthetic-symbols.csv
- generate output JSON pmap.json 
  - portfolio map format
