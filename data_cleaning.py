import pandas as pd

# 1. Loading the Data
df = pd.read_csv('extracted_output.csv')

# 2. Handling Missing Data
# Drop rows with any missing values
df.dropna(inplace=True)

# Or, you can fill missing values with a default value or forward fill
# df.fillna(value="DEFAULT_VALUE", inplace=True)  # replace "DEFAULT_VALUE" with what you'd like
# df.fillna(method='ffill', inplace=True)  # forward fill

# 3. Removing Duplicates
df.drop_duplicates(inplace=True)


# Remove leading and trailing whitespaces
df['content'] = df['content'].str.strip()
df['ip_location_new']= df['ip_location'][4:]

# (Additional cleaning can include removing punctuations, numbers, or applying more complex transformations.)

# Save the cleaned data back to CSV (or to a new file, if you prefer)
df.to_csv('cleaned_output.csv', index=False)
print('Saved to cleaned_output.csv.')
