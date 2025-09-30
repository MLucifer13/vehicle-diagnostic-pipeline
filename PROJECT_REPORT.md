# Vehicle Diagnostics Data Pipeline

## 📊 Project Overview
This project demonstrates a complete ETL (Extract, Transform, Load) pipeline for processing vehicle sensor data from 14 vehicles over a 59-day period. The project showcases end-to-end data analytics skills including data cleaning, database management, and interactive dashboard creation—all essential skills for a Data Analyst role.

**Live Dashboard Preview:**
![Dashboard](volvo_proj.pdf)

## 🎯 Business Problem
Fleet management companies need to monitor vehicle health in real-time to:
- Identify vehicles requiring immediate maintenance
- Prevent costly breakdowns through predictive insights
- Optimize fleet performance and reduce operational costs
- Ensure driver safety through proactive diagnostics

## 🔍 Key Insights from Analysis

### Fleet Performance Metrics
- **Total Vehicles Monitored:** 14
- **Average Speed:** 22.66 mph (indicates mixed urban/highway driving)
- **Average Engine Temperature:** 81.87°F (within optimal range)
- **Distinct Trouble Codes:** 13 (requiring further investigation)
- **Data Collection Period:** 59 days (July 18 - September 15, 2017)

### Critical Findings

**🚨 High-Priority Maintenance Alerts:**
- **car4** - Appears in BOTH high temperature AND high speed lists → **IMMEDIATE INSPECTION REQUIRED**
- **car5** - Highest average engine temperature → Check cooling system
- **car2** - Second highest temperature → Schedule preventive maintenance

**📈 Operational Patterns:**
- Speed variability from 5 mph to 79 mph suggests diverse driving conditions
- Engine coolant temperature increased from 45°F to 89°F over monitoring period
- Strong correlation between RPM and speed indicates healthy transmission performance

**💡 Business Recommendations:**
1. Prioritize maintenance for car4, car5, and car2
2. Investigate the 13 trouble codes for severity classification
3. Implement weekly monitoring for high-risk vehicles
4. Consider driver behavior training for high-speed vehicles (car11, car14)

## 🛠️ Tech Stack
- **Data Processing:** Python, Pandas
- **Database:** SQLite
- **Visualization:** Power BI Desktop
- **Development:** Jupyter Notebook

## 📁 Project Structure

```
volvo_diagnostic_project/
├── data/
│   ├── raw/                          # Original sensor data
│   │   └── sensor_data.csv
│   └── processed/                    # Cleaned data
│       └── cleaned_sensor_data.csv
├── database/
│   └── vehicle_diagnostics.db        # SQLite database
├── notebooks/
│   └── 01_data_cleaning.ipynb        # Data cleaning process
├── scripts/
│   └── load_to_db.py                 # ETL script
├── dashboards/
│   └── volvo_proj.pdf                # Power BI dashboard export
├── .gitignore
├── requirements.txt
├── README.md
└── PROJECT_REPORT.md                 # Detailed analysis report
```

## 🔄 ETL Pipeline

### 1. Extract
- Raw vehicle sensor data loaded from CSV using Pandas
- Data includes: timestamps, vehicle IDs, speed, RPM, engine temperature, trouble codes

### 2. Transform
- **Data Cleaning Steps:**
  - Handled missing values using mean imputation
  - Verified data types and consistency
  - Validated data completeness (100% after cleaning)
- Cleaned data saved to `data/processed/cleaned_sensor_data.csv`

### 3. Load
- Cleaned data loaded into SQLite database
- Table: `sensor_readings`
- Database serves as single source of truth for analytics

## 🚀 How to Run This Project

### Prerequisites
- Python 3.7+
- Power BI Desktop (for dashboard viewing)

### Step-by-Step Instructions

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd volvo_diagnostic_project
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare the dataset**
   - Place your `sensor_data.csv` file in the `data/raw/` folder

5. **Run data cleaning**
   - Open `notebooks/01_data_cleaning.ipynb` in Jupyter Notebook
   - Run all cells to generate cleaned data
   ```bash
   jupyter notebook notebooks/01_data_cleaning.ipynb
   ```

6. **Load data into database**
   ```bash
   python scripts/load_to_db.py
   ```

7. **View the dashboard**
   - Open Power BI Desktop
   - Connect to `database/vehicle_diagnostics.db`
   - Import the dashboard or build your own visualizations

## 📈 Dashboard Features

The Power BI dashboard includes:
- **KPI Cards:** Total vehicles, avg speed, avg temperature, trouble codes, data duration
- **Time Series:** Average engine coolant temperature and speed trends over time
- **Top Performers:** Vehicles with highest avg temperature and speed
- **Correlation Analysis:** Engine RPM vs Speed scatter plot
- **Interactive Filters:** Date range and vehicle ID selection

## 🎓 Skills Demonstrated

✅ **Data Engineering:** Built complete ETL pipeline from scratch  
✅ **Python Programming:** Pandas for data manipulation and cleaning  
✅ **SQL/Database:** SQLite database design and management  
✅ **Data Visualization:** Interactive Power BI dashboard creation  
✅ **Business Analysis:** Translated data into actionable insights  
✅ **Problem Solving:** Identified critical vehicles requiring maintenance  
✅ **Documentation:** Clear technical documentation and reporting  

## 📊 Sample Queries

Once data is loaded, you can query the database:

```sql
-- Find vehicles with highest average speed
SELECT vehicle_id, AVG(speed) as avg_speed
FROM sensor_readings
GROUP BY vehicle_id
ORDER BY avg_speed DESC
LIMIT 5;

-- Identify all trouble codes by vehicle
SELECT vehicle_id, trouble_code, COUNT(*) as occurrences
FROM sensor_readings
WHERE trouble_code IS NOT NULL
GROUP BY vehicle_id, trouble_code;

-- Temperature trends over time
SELECT date, AVG(coolant_temp) as avg_temp
FROM sensor_readings
GROUP BY date
ORDER BY date;
```

## 📝 Detailed Project Report

For a comprehensive analysis including:
- Statistical analysis and methodology
- Detailed insights and findings
- Business recommendations
- Future enhancements

**👉 See [PROJECT_REPORT.md](PROJECT_REPORT.md) for the full report**

## 🔮 Future Enhancements

- **Predictive Maintenance:** Machine learning model to predict vehicle failures
- **Real-time Monitoring:** Stream live sensor data into dashboard
- **Anomaly Detection:** Automated alerts for unusual sensor readings
- **Cost Analysis:** Calculate ROI of preventive vs. reactive maintenance
- **Geospatial Analysis:** Map vehicle locations and route optimization

## 👤 About This Project

This project was created as part of my data analytics portfolio to demonstrate:
- End-to-end data pipeline development
- Ability to derive business insights from raw data
- Technical proficiency in Python, SQL, and BI tools
- Communication of complex findings to stakeholders

## 📫 Contact

**Prabin KC**
- LinkedIn: (https://www.linkedin.com/feed/)
- Email: kcm9181@gmail.com
- Portfolio: https://mlucifer13.github.io/PrabinKC.github.io/
- GitHub: https://github.com/MLucifer13

---

*This project showcases practical data analytics skills applicable to automotive, IoT, fleet management, and any industry requiring sensor data analysis.*