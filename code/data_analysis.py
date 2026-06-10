from pathlib import Path
import csv
import pandas as pd
import matplotlib.pyplot as plt

project = Path("Penguin Research Project")
data_folder = project / "data"
output_folder = project / "outputs"

# read the input file
input_csv = output_folder / "penguin_df_clean.csv"

#convert to a dataframe
penguins_df = pd.read_csv(input_csv)

species_df = penguins_df["species"].value_counts()

#line graph/ bar graph

# plt.figure(figsize=(5,5))
# species_df.plot(kind="bar")
# plt.title("count for each penguin: ")
# plt.xlabel("Species")
# plt.ylabel("# of penguins")
# plt.xticks(rotation=40)
# plt.tight_layout()
# plt.savefig(output_folder / "bar_species_count.png", dpi=250)
# # plt.show()


#histogram

# species_body_mass= penguins_df.groupby("species")["body_mass_g"].mean()
# # species_body_mass.plot(kind="hist")
# plt.figure(figsize=(5,5))
# plt.hist(penguins_df["body_mass_g"], bins=5, color="red", edgecolor="black")
# plt.title("Showing different species for rang of body mass ")
# plt.xlabel("body mass")
# plt.ylabel("# of penguin species")
# plt.xticks(rotation=40)
# plt.tight_layout()
# plt.savefig(output_folder / "hist_species_count.png", dpi=250)


# Scatter plot

# species_body_mass= penguins_df.groupby("species")["body_mass_g"].mean()
# plt.figure(figsize=(5,5))
# plt.scatter(penguins_df["flipper_length_mm"], penguins_df["body_mass_g"], s=4)
# plt.title("Showing different species for rang of body mass ")
# plt.xlabel("flipper_length")
# plt.ylabel("body mass")
# plt.xticks(rotation=40)
# plt.yticks(rotation=40)
# plt.grid(True, alpha=0.2)
# plt.tight_layout()
# plt.savefig(output_folder / "scatter_species_count.png", dpi=250)


#Scatter plot

# species_body_mass= penguins_df.groupby("species")["body_mass_g"].mean()
# plt.figure(figsize=(5,5))
# plt.scatter(penguins_df["flipper_length_mm"], penguins_df["body_mass_g"], s=4)
# plt.title("Showing different species for rang of body mass ")
# plt.xlabel("flipper_length")
# plt.ylabel("body mass")
# plt.xticks(rotation=40)
# plt.yticks(rotation=40)
# plt.grid(True, alpha=0.2)
# plt.tight_layout()
# plt.savefig(output_folder / "scatter_species_count.png", dpi=250)


#Box plot

# plt.figure(figsize=(5,5))
# penguins_df.boxplot(column="body_mass_g", by="species")
# plt.title("Showing different species for rang of body mass ")
# plt.xlabel("species")
# plt.ylabel("body mass")
# plt.xticks(rotation=40)
# plt.yticks(rotation=40)
# plt.grid(False)
# plt.tight_layout()
# plt.savefig(output_folder / "boxplot_species_count.png", dpi=250)


#Multi label graphs


stu = ["a", "b", "c", "d"]
x = [1, 2 ,3 ,4]
y= [4, 6, 8, 10]

plt.figure()
plt.bar(stu, x, label="first exam scores")
plt.bar(stu, y, label="second exame scores")
plt.xlabel("students")
plt.ylabel("Scores")
plt.legend()

plt.show()