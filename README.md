# Vehicle Diagnostic Data Pipeline

## Objective
This project demonstrates a complete ETL (Extract, Transform, Load) pipeline for processing vehicle sensor data. The goal is to clean raw sensor logs, load them into a SQLite database, and prepare the data for analysis and visualization in a tool like Power BI. This project is designed to showcase foundational data engineering skills for the automotive industry.

## Tech Stack
- **Data Transformation:** Python (Pandas)
- **Database:** SQLite
- **BI & Visualization:** Power BI
- **Development Environment:** Jupyter Notebook

## Project Structure

volvo_diagnostic_project/
├── data/             # Contains raw and processed data
│   ├── raw/
│   └── processed/
├── database/         # Stores the final SQLite database
├── notebooks/        # Jupyter Notebook for data cleaning
├── scripts/          # Python script for the ETL process
├── .gitignore
├── requirements.txt
└── README.md         # Project documentation


## ETL Pipeline Overview
1.  **Extract:** Raw vehicle sensor data is read from `data/raw/sensor_data.csv` using Pandas.
2.  **Transform:** The data is cleaned in the `notebooks/01_data_cleaning.ipynb` notebook. The primary cleaning step involves handling missing values by filling them with the column's mean. The resulting clean data is saved to `data/processed/cleaned_sensor_data.csv`.
3.  **Load:** The `scripts/load_to_db.py` script reads the processed CSV file and loads it into a `sensor_readings` table within the `database/vehicle_diagnostics.db` SQLite database.

## Dashboard & Findings
The final database (`vehicle_diagnostics.db`) is the single source of truth for analysis. It can be connected directly to Power BI to build an interactive dashboard. Key visualizations would include:
-   Trends of sensor readings (e.g., RPM, speed, temperature) over time.
-   Distribution of fault codes to identify common issues.
-   Correlation analysis between different sensor readings to spot anomalies.



## How to Run This Project
1.  **Clone the repository:** `git clone <repository-url>`
2.  **Navigate to the project directory:** `cd volvo_diagnostic_project`
3.  **Set up the environment:**
    - Create a virtual environment: `python -m venv venv`
    - Activate it: `source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
    - Install dependencies: `pip install -r requirements.txt`
4.  **Place the dataset:** Download the dataset and place the `sensor_data.csv` file inside the `data/raw/` folder.
5.  **Run the data cleaning notebook:** Open and run all cells in `notebooks/01_data_cleaning.ipynb`. This will create the `cleaned_sensor_data.csv` file.
6.  **Run the ETL script:** Execute the script from the root directory to create and populate the database: `python scripts/load_to_db.py`
7.  **Visualize:** Connect Power BI to the `database/vehicle_diagnostics.db` file and build your dashboard.
