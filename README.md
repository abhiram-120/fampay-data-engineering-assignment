# FamPay – Data Engineering Intern Take-Home Assignment

## Overview

This repository contains my solution to the FamPay Data Engineering Intern take-home assignment. The objective is to transform daily stock price data into **monthly OHLC aggregates** and compute **technical indicators (SMA & EMA)** on monthly closing prices using **pure Pandas**.

The solution emphasizes **correct financial logic**, **vectorized transformations**, and **clean separation of concerns** between computation and I/O.

---

## Problem Summary

Given 2 years of daily stock price data for 10 tickers:

* Resample daily data to **monthly frequency**
* Compute monthly **Open, High, Low, Close** values
* Calculate **SMA-10, SMA-20, EMA-10, EMA-20** on **monthly closing prices**
* Output **one CSV per ticker**, each containing exactly **24 rows**

---

## Assumptions

* Input data is mostly clean but may not be strictly ordered → data is explicitly **sorted by date** before processing
* Monthly aggregation uses **actual trading days**:

  * **Open** → first trading day of the month
  * **Close** → last trading day of the month
  * **High / Low** → monthly max / min
* Technical indicators are calculated **after monthly aggregation**, not on daily data

---

## Technical Indicators Implementation

### Simple Moving Average (SMA)

* Calculated using Pandas rolling windows:

  * `SMA-10` → 10-month rolling mean of monthly close
  * `SMA-20` → 20-month rolling mean of monthly close

### Exponential Moving Average (EMA)

* Calculated using Pandas `ewm` with `adjust=False`
* This follows the **recursive EMA definition**:

```
EMA_today = (Price_today × α) + (EMA_yesterday × (1 − α))
α = 2 / (N + 1)
```

* Pandas initializes the first EMA value using the first available data point, which is acceptable for this analytical use case

---

## Approach

1. Load daily stock price data using Pandas
2. Process each ticker independently to avoid cross-symbol contamination
3. Resample daily data into monthly OHLC values using Pandas `resample` + `agg`
4. Compute SMA and EMA indicators on monthly closing prices
5. Persist one CSV file per ticker following the required naming convention

---

## Code Structure

```
fam_assignment/
├── main.py               # Pipeline orchestration
├── src/
│   ├── processing.py     # Aggregation & indicator logic
│   └── utils.py          # Data loading & CSV writing
├── data/
│   ├── input/
│   └── output/
├── requirements.txt
└── README.md
```

* **main.py** coordinates the end-to-end pipeline
* **processing.py** contains all transformation logic
* **utils.py** handles file I/O

This separation improves readability, testability, and maintainability.

---

## Vectorization & Performance

* Uses Pandas `resample`, `rolling`, and `ewm` functions
* Avoids explicit Python loops over rows
* Suitable for in-memory analytical workloads

---

## Validation & Safety Checks

* Data is explicitly sorted by date before resampling
* Each output file contains **exactly 24 rows**, representing 24 months of data

---

## Trade-offs & Limitations

* Designed for **small to medium datasets** that fit in memory
* No schema enforcement or anomaly detection
* CSV output chosen for simplicity

In a production environment, this logic would likely move to:

* Spark / Flink for scale
* Parquet storage
* Or a warehouse-backed transformation layer

---

## Production Extensions (If This Ran Daily)

* Schema validation before processing
* Data quality checks (missing days, duplicate records)
* Partitioned outputs by `year/month/ticker`
* Orchestration using Airflow or Dagster

---

## How to Run

```
pip install -r requirements.txt
python main.py
```
