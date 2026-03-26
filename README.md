# Job-Market-Analyzer

## Overview

A simple Python project that analyzes job market data from a CSV file using Pandas and Matplotlib.

## Features

- Load job data from a CSV file
- Display basic dataset information
- Calculate average salary by category
- Count jobs by location
- Generate charts automatically

## Tech Stack

- Python
- Pandas
- Matplotlib

## Project Structure

```bash
job-market-analyzer/
│
├── data/
│   └── jobs.csv
│
├── scripts/
│   └── analyzer.py
│
├── output/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

1. Clone the repository
2. Create a virtual environment
3. Install dependencies
```bash
pip install -r requirements.txt
```

## Run the Project
```bash
python main.py
```

## Output

The project generates:
- console analysis
- charts saved in the `output` folder

## Example Data

```csv
title,location,salary,category
Python Developer,Bucharest,8000,IT
Frontend Developer,Cluj,7000,IT
Data Analyst,Bucharest,7500,Data
```
