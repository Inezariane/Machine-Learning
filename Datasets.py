import pandas as pd 
import seaborn as sns 
from matplotlib import style
import matplotlib.pyplot as plt

csv = "Codes/ML/vehicles.csv"
df = pd.read_csv(csv)

print("All is done")
print(df.head(10))
print(df.tail())
print(df.describe())
print(df.shape)

# To calculate the variance of the year column 
variance = df['year'].var()
print(variance)

# To find the occurence of a value in a single column
print(df["seating_capacity"].value_counts())

# To delete a column
df = df.drop(columns=["Unnamed: 0"])

# To find the occurence of values in the whole df
for col in df.columns:
    print(df[col].value_counts())

# To return columns name
print(df.columns.tolist())

# To know the types of the features you have
print(df.dtypes) # ps the object datatype shows that it is categorical data

# To count the number of unique values in the df 
print(df.nunique())

#.unique returns the actual unique values not the count of all the unique values
categorical_columns = df.select_dtypes(include=["object"]).columns
for col in categorical_columns:
    unique_values = df[col].unique()
    print(f"{col}:{len(unique_values)}")

# Checking null
print(df.isnull().sum())

df.drop(columns=["owner_name","vin"],axis=1,inplace=True)

df["selling_price"] = df["selling_price"].astype(float)
df["proposed_purchase_price"] = pd.to_numeric(df["proposed_purchase_price"],errors="coerce")
print(df.dtypes)

# Making a chart 
sns.set(rc={ #rc stands for "runtime configuration".  This sets the default figure size for Seaborn plots to 20x20 inches.
    'figure.figsize': (20, 20),        # Set figure size to 10x6 inches
    'font.size': 14,                   # Set default font size to 14
    'axes.titlesize': 16,              # Set axes title font size to 16
    'xtick.labelsize': 12,             # Set x-tick label font size to 12
    'ytick.labelsize': 12,             # Set y-tick label font size to 12
    'lines.linewidth': 2,              # Set default line width to 2
    'axes.labelsize': 14               # Set axes label font size to 14
})

g = sns.FacetGrid(df, hue='transmission', height=5, aspect=2, xlim=(df["proposed_purchase_price"].min(),df["proposed_purchase_price"].max())) #
# Map the KDE plot
g.map(sns.kdeplot, 'proposed_purchase_price', fill=True)
g.add_legend(title='Purchase Price')
g.set_axis_labels('Purchase Price', 'Density')
g.fig.suptitle('KDE of Purchase Price by transmission', fontsize=16)
plt.show()