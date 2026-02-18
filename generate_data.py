import pandas as pd
import numpy as np

print("Generating data... this might take a few seconds.")

# 3 million rows will comfortably generate a file around 150MB - 200MB
num_rows = 3_000_000

data = {
    'Product_Category': np.random.choice(['Electronics', 'Clothing', 'Home', 'Sports', 'Toys'], size=num_rows),
    'Sales_Volume': np.random.randint(1, 1000, size=num_rows),
    'Profit_Margin': np.random.uniform(5.0, 55.0, size=num_rows),
    'Customer_Rating': np.random.uniform(1.0, 5.0, size=num_rows)
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv('massive_test_dataset.csv', index=False)

print("Success! 'massive_test_dataset.csv' has been created in your folder.")
