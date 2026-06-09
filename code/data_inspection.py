from pathlib import Path
import pandas as pd

project = Path("Penguin Research Project")
data_folder = project / "data"
output_folder = project / "outputs"

# read the input file
input_csv = data_folder / "penguins_size.csv"

#convert to a dataframe
penguins_df = pd.read_csv(input_csv)

# basic facts
row_count = penguins_df.shape[0] # row_count
column_count = penguins_df.shape[1] #column count
penguins_df.columns # column names
penguins_df.isna().sum() # missing columns (NA) with the number of missing values
df_shape = penguins_df.shape

# category count for a specific column

if "species" in penguins_df.columns:
    species_count = penguins_df["species"].value_counts()

# Descriptive values

head_val = penguins_df.head() #First 5 values
tail_val = penguins_df.tail() #last 5 values
d_types_df = penguins_df.dtypes # type of data for each column
df_desc = penguins_df.decribe() #numeric values --- mean, median, ...

# Get values for specific columns

sex_val = penguins_df["sex"]

#rename the columns to body length and depth

names = {
     "culmen_length_mm" : "body_length",
     "culmen_depth_mm" : "body_depth"
 }
 penguin_df = penguin_df.rename(columns=names)
 
# drop all na values from the dataframe

penguins_df = penguins_df.dropna()





penguin_df_clean = penguin_df.dropna()

penguin_df_csv = project / "outputs" / "penguin_df_clean.csv"

penguin_df_clean.to_csv(penguin_df_csv, index=False)


review_output = project / "outputs" / "inspection.txt"
with open(review_output, "a") as file:
    file.write(f"Shape of the dataframe: {df_shape}\n")
    file.write(f"# of rows: {row_count}\n")
    file.write(f"# of columns: {column_count}\n")

    file.write("column names: \n")
    for column in column_count:
        file.write(f"- {column_count}\n")

    file.write(f"species count for each category: {species_count}\n")
    file.write(f"top 5 rows: {head_val}\n")
    file.write(f"bottom 5 rows: {tail_val}")
    file.write(f"datatypes of each column: {d_types_dfl}\n")
    file.write(f"Numeric values for all data: {df_desc}")
