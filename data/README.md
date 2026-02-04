# Data

# CFPB Consumer Complaints (Washington State, 2016–2026)

This folder contains the dataset used for the UMBC DATA 606 Capstone project titled:

**“Analysis of Consumer Complaint Root Causes Using Large Language Models”**

The data is derived from the **Consumer Complaint Database** published by the **Consumer Financial Protection Bureau (CFPB)** and has been filtered to include:

- Complaints submitted in **Washington state (WA)**
- Complaints received between **February 2, 2016 and February 2, 2026**

Each record represents a **single consumer complaint**, including an unstructured complaint narrative and structured metadata such as product type, issue category, company name and response status.

---

## Data Source

- **Original source:** CFPB Consumer Complaint Database  
- **Official website:** https://www.consumerfinance.gov/data-research/consumer-complaints/
- **Original format:** CSV (downloaded and filtered locally)

---

## Dataset Storage Format

Due to GitHub’s file size limitations, the original dataset (~85 MB) has been split into **five CSV files**, each under 25 MB.

### Files in This Folder

- `complaints_part_1.csv`
- `complaints_part_2.csv`
- `complaints_part_3.csv`
- `complaints_part_4.csv`
- `complaints_part_5.csv`

⚠️ **Important:**  
All five files together represent the **complete dataset**.

---

## Dataset Size and Shape

- **Total rows:** 110,879 consumer complaints  
- **Total columns:** 18  
- **Approximate combined size:** ~85 MB  
- **Granularity:** One row = one consumer complaint

---

## How to Recombine the Dataset

To load the full dataset for analysis, concatenate the split CSV files using the following Python code:

```python
import pandas as pd
import glob

files = sorted(glob.glob("data/complaints_part_*.csv"))
df = pd.concat((pd.read_csv(f) for f in files), ignore_index=True)

print(df.shape)
