import pandas as pd
import numpy as np

# Set a random seed for reproducibility
np.random.seed(42)

# Number of rows in the dataset
num_rows = 15000

# Generate synthetic data
data = {
    'propertyType': np.random.choice(['House', 'Apartment', 'Condo', 'Townhouse','Villa'], size=num_rows),
    'bedrooms': np.random.randint(1, 6, size=num_rows),  # 1 to 5 bedrooms
    'bathrooms': np.random.randint(1, 4, size=num_rows),  # 1 to 3 bathrooms
    'squareFeet': np.random.randint(800, 4000, size=num_rows),  # 800 to 4000 sq. ft.
    'lot_size': np.random.randint(2000, 15000, size=num_rows),  # 2000 to 15000 sq. ft.
    'oceanProximity': np.random.choice(['<1H OCEAN', 'INLAND', 'NEAR OCEAN', 'NEAR BAY'], size=num_rows),
    'yearBuilt': np.random.randint(1900, 2023, size=num_rows),  # Year built between 1900 and 2023
    'price': np.random.randint(100000, 3000000, size=num_rows),  # Price between $100,000 and $1,000,000
    'has_garage': np.random.choice([True, False], size=num_rows, p=[0.5, 0.5]),  # 50% chance of having a garage
    'has_pool': np.random.choice([True, False], size=num_rows, p=[0.2, 0.8]),  # 20% chance of having a pool
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the first few rows of the dataset
print(df.head())

# Save the dataset to a CSV file (optional)
df.to_csv('housing.csv', index=False)