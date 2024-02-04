import pandas as pd
from sqlalchemy import create_engine, text

def extract_transform_load(source_path, engine):
    # Extract
    source_data = pd.read_csv(source_path)

    # Transform
    # Write your code here :O)

    # Load
    source_data.to_sql('product_sales', engine, index=False, if_exists='replace')

def get_top_products_by_revenue(engine, top_n=5):
    # Make sure the engine is connected to the database
    connection = engine.connect()
    # Define the SQL query to calculate total revenue for each product
    query = text(f'''
        -- Write your query here 
    ''')

    # Execute the query
    cursor = connection.execute(query)

    # Fetch the results
    results = cursor.fetchall()

    # Cleanup after ourselves
    connection.close()

    return results

if __name__ == "__main__":
    # Source CSV file path
    source_csv_path = 'resources/sales_data.csv'

    # Target database connection string (SQLite in this example)
    database_url = 'sqlite:///sales.db'

    # Create a DB engine
    engine = create_engine(database_url, echo=True)

    # Execute ETL operation
    extract_transform_load(source_csv_path, engine)

    # Get top products and print them
    top_products = get_top_products_by_revenue(engine, 2)

    # Print out the result

    # Clean up after ourselves
    engine.dispose()
