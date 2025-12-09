📊 Data Visualization Project — Automated Superstore Insights

Welcome to the Data Visualization Task — a fully automated project that generates a synthetic Superstore dataset, processes it, and produces meaningful business insights through visual storytelling.

Everything in this project — dataset creation, environment setup, visualization, and folder structure — was generated via an automated PowerShell pipeline.

🚀 Project Overview

This project simulates a real-world retail analytics workflow:

Creates a 500-row synthetic Superstore dataset

Cleans and processes the data using Pandas

Generates insightful visualizations using
Matplotlib, Seaborn, and Plotly

Saves all charts to the outputs/ folder

Includes complete automation via run_all.ps1

📁 Project Structure
data_visualization_task/
│
├── Superstore.csv           # 500-row synthetic dataset
├── visualize.py             # Data visualization script
├── outputs/                 # Generated charts (PNG)
├── .venv/                   # Auto-created Python virtual environment
├── README.md                # Project documentation
└── .gitignore               # Ignore unnecessary files

🧠 Dataset Summary

The synthetic dataset includes:

Order details: dates, shipping mode, postal codes

Customer info: segment, region, state, city

Product info: category, sub-category

Metrics: sales, quantity, discount, profit

This dataset mimics typical business analytics challenges:
identifying trends, understanding customer segments, and comparing product performance.

📈 Visualizations Produced

The script automatically generates:

1️⃣ Monthly Sales Trend

Shows how sales fluctuate over time, helping identify peaks and seasonal patterns.

2️⃣ Category Sales Breakdown

Compares performance across major categories
(Furniture, Technology, Office Supplies).

3️⃣ Treemap Visualization

Interactive-style treemap (saved as PNG) showing sales contribution by category.

All charts are saved in:

/outputs

🖥️ How to Run the Project
1. Activate Virtual Environment
.\.venv\Scripts\Activate.ps1

2. Run the Visualization Script
python visualize.py


Charts will appear inside:

outputs/

⚙️ Automation Script (run_all.ps1)

The entire project can be rebuilt from scratch using:

run_all.ps1


This script:

Deletes old project files

Regenerates dataset

Rebuilds Python environment

Installs dependencies

Generates visualizations

Initializes Git repo

(Optionally) pushes to GitHub

💡 Key Insights (Example Observations)

You may highlight insights here based on your visualization output:

Technology tends to dominate sales performance

Sales show noticeable monthly fluctuations indicating seasonal patterns

Some categories maintain consistent revenue but weaker profit margins

(You can update this section with insights from your actual charts.)

🧑‍💻 Technologies Used

Python 3

Pandas

Matplotlib

Seaborn

Plotly + Kaleido

PowerShell

Git + GitHub

🌟 Author

Yafai
AIML student who doesn’t give up — ever.
