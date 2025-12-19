# FamPay – Data Engineering Intern Take-Home Assignment

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

## Assumptions
- Dataset contains valid trading days only
- No missing months per ticker in the given time range
- EMA initialization follows Pandas default behavior
- Designed for batch processing, not real-time streaming

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


## How to Run
```bash
pip install -r requirements.txt
python main.py
