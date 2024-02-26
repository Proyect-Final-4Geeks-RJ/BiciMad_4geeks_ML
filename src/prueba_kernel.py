import pandas as pd
import glob
import os

file_json_list = glob.glob("../data/raw/json/*.json")

# Create an empty list to store the DataFrames
data_frames = []

# Read each JSON file into a DataFrame and append it to the list
for file in file_json_list:
    data_frame = pd.read_json(file, lines=True)  
    data_frames.append(data_frame)

# Concatenate all DataFrames into one
combined_df = pd.concat(data_frames, ignore_index=True)

# Save the combined DataFrame to a new JSON file
combined_df.to_json('combined_json.json', orient='records', lines=True)

data_stations = pd.read_json('../data/raw/json/combined_json.json', lines=True)
print(data_stations.head())
