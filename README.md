# FamPay – Data Engineering Intern Take-Home Assignment
---


Solution for the Data Engineering assignment.
Calculates monthly OHLC and SMA/EMA (10, 20) for the provided tickers.

## Assumptions
- The "Open" price is the first available day of the month, and "Close" is the last.
- For the first EMA calculation, the logic requires a previous value. I calculated the initial SMA (first 10/20 months) and used that as the starting point for the EMA series, then applied the formula for the rest.
- Input data is assumed to be clean, but I added a sort by date just in case.

## Note on Vectorization
I used `groupby` and `resample` to avoid loops. The EMA calculation uses Pandas `ewm` but I had to handle the initial seed value manually to match the requirements.

## Objective
Transform noisy daily stock price data into clean monthly summaries that are easier to analyze for long-term trends, and compute SMA/EMA indicators on monthly closing prices.

---

## Why Monthly Aggregation?
Daily stock prices are highly volatile and often obscure long-term movement.
By aggregating to monthly OHLC values:
- Short-term noise is reduced
- Trends become easier to observe
- Technical indicators become more stable and interpretable

---

## Approach
1. Load daily stock price data using Pandas
2. Process each ticker independently to avoid cross-symbol contamination
3. Resample daily data into monthly OHLC values using exact trading-day logic:
   - Open → first trading day of the month  
   - Close → last trading day of the month  
   - High/Low → monthly max/min  
4. Calculate SMA-10, SMA-20, EMA-10, EMA-20 on **monthly closing prices**
5. Write one output CSV per ticker

---

## Key Design Decisions
- **Pandas** was used as the dataset comfortably fits in memory and the assignment explicitly allows it
- Indicators are calculated **after aggregation**, not on daily data, to avoid noisy signals
- Calculation logic and IO logic are separated for clarity and maintainability
- Vectorized Pandas operations are used instead of loops for correctness and performance

---


## Trade-offs & Limitations
- This solution is not optimized for large-scale or distributed datasets
- No schema validation or anomaly detection is implemented
- For production scenarios, this logic would move to Spark or a data warehouse

---
##additional
-If this pipeline were to run daily in production:
-I would validate schema using pandas dtypes before aggregation
-Add data quality checks for missing days per month
-partition output by year/month/ticker instead of flat CSVs
-Schedule using Airflow / Dagster

]
pip install -r requirements.txt
python main.py
