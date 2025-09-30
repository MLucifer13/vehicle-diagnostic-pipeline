import pandas as pd
import sqlite3
import os

def load_data_to_db():
    """
    Reads cleaned data from a CSV file and loads it into a SQLite database table.
    This script is designed to be run from the root of the project directory.
    """
    # Define relative paths from the project root
    processed_data_path = os.path.join('data', 'processed', 'cleaned_sensor_data.csv')
    db_path = os.path.join('database', 'vehicle_diagnostics.db')
    table_name = 'sensor_readings'

    # Ensure the database directory exists
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    # Read the cleaned data
    try:
        df = pd.read_csv(processed_data_path)
        print(f"Successfully loaded {len(df)} records from cleaned data")
    except FileNotFoundError:
        print(f"Error: Processed data file not found at {processed_data_path}")
        print("Please run the 'notebooks/01_data_cleaning.ipynb' notebook first to generate it.")
        return

    # Create a connection to the SQLite database
    conn = sqlite3.connect(db_path)

    # Load the DataFrame into the SQLite table
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    
    print(f"Data successfully loaded into the '{table_name}' table")
    print(f"Database location: '{db_path}'")
    print(f"Total records in database: {len(df)}")

    # Close the connection
    conn.close()

if __name__ == "__main__":
    load_data_to_db()