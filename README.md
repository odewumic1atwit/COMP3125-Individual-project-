# QS World University Rankings 2025 – Data Analysis

A Python-based data analysis project exploring global university performance using the QS 2025 rankings dataset.

## Overview
This project loads, cleans, and analyzes the QS World University Rankings 2025 dataset. It performs data munging, feature scaling, descriptive statistics, and visualizations to understand how universities compare across academic reputation, employer reputation, research strength, sustainability, and overall ranking.

## Dataset
- **Source:** `datasets/qs_world_rankings_2025.csv`
- **Universities:** ~1,503
- **Key Features:** Academic reputation, employer reputation, citations per faculty, sustainability, faculty/student ratio, internationalization metrics, and QS overall score.

### Data Outputs
- `qs_data_cleaned.csv` — cleaned + scaled dataset (ready for analysis)
- Plots saved in `plots/`

## Project Structure
```
project/
├── src/
│ ├── data_munging.py # Cleans and scales dataset
│ ├── data_analysis.py # Visualizations + summary statistics
│ └── main.py # Pipeline runner
│
├── datasets/
│ ├── qs_world_rankings_2025.csv # Raw dataset
│ └── qs_data_cleaned.csv # Cleaned dataset
│
└── plots/ # Generated charts
```

## Features

### Data Cleaning & Engineering
- Standardized column names  
- Converted numeric fields  
- Median imputation of missing values  
- Added MinMax-scaled versions of numeric metrics  

### Analysis Outputs
- Correlation heatmap  
- QS score distribution  
- Academic vs employer reputation  
- Sustainability vs QS score  
- Top 20 universities  

## Installation

### 1. Clone the repository:

1. Clone the repository:
```bash
git clone <repo-url>
cd qs-ranking-project
```
2. Create a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # macOS/Linux
```
3. Install dependencies:
```bash
pip install pandas numpy seaborn matplotlib scikit-learn
```

## Usage
1. Clean the dataset
python src/data_munging.py

2. Generate visualizations and summaries
python src/data_analysis.py

3.  Run the full pipeline
python src/main.py


## Insights
The analysis explores:

- Relationships between academic quality, research output, and ranking
- Sustainability performance across institutions
- Patterns among top-ranked universities
- Rankings changes from 2024 to 2025

## Technologies
- Python 
- Pandas 
- NumPy
- Scikit-learn
- Seaborn 
- Matplotlib 
