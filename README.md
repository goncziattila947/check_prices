# Competitor Price Monitor & Alert System

## 1. Business problem

The Challenge: Market prices fluctuate daily. Keeping track of competitors is essential to stay competitive.

Current process: a marketing colleague manually visits competitor websites every morning to check prices and records them in Excel.

Time-consuming: Takes ~150 minutes/month (approx. 30 hours/year wasted on manual data entry).

Human Error: High risk of typos or missed price changes.

Lag: Reaction time is slow; we might lose customers before we notice the price drop.

## 2. The solution

An automated Python script that acts as a "digital robot":

Runs automatically every morning at 08:00.

Scrapes the exact price from competitor product pages.

Compares it with our Internal Reference Price.

Alerting: Sends an immediate warning only if the competitor is cheaper.

## 🛠 Tech Stack
![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![BS4](https://img.shields.io/badge/Scraping-BeautifulSoup-green)
![CSV](https://img.shields.io/badge/Storage-CSV%2FExcel-lightgrey)



## 📊 Data Output Sample
Below is an example of the automated report generated for the marketing team. This dataset is used to support immediate pricing decisions.

<img width="295" height="102" alt="Screenshot 2026-01-28 014334" src="https://github.com/user-attachments/assets/e7b4911b-8fe9-4df0-ba37-3ebe5a996f7d" />

*(The screenshot demonstrates how the system tracks daily price fluctuations.)*



## Process flow

```mermaid
graph TD;
    Start(["Start: Run Script at 08:00"]) --> Fetch["Fetch Product Page"];
    Fetch --> Parse["Parse HTML & Extract Price"];
    Parse --> Clean["Clean Data (e.g. '$50.00' -> 50.00)"];
    Clean --> Decision{"Price < Target?"};
    Decision -- Yes --> Alert["ALERT: Send Email"];
    Decision -- No --> Log["Log Data to CSV"];
    Alert --> End([Stop]);
    Log --> End([Stop]);















