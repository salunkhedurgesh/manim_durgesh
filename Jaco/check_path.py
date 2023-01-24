import pandas as pd
import numpy as np

df = pd.read_csv("D:\durghy_manim\Jaco\saved_data_theta1.csv")

path_record = []

for i2 in np.arange(450, len(df)):
    print(f"Index {i2} of the dataframe is being processed")
    elements = 0
    if i2 == 450:
        print("Reached 450")
    for j in range(len(df.columns) - 2):
        if pd.isna(df.iloc[i2, j + 2]):
            break
        else:
            elements += 1

        if i2 == 0:
            path_record.append([0, df.iloc[0, j + 2]])

    # if i2 > 50:
    #     print(f"The number of elements are {elements}")
    if i2 != 0:
        current_path_index = []
        match_found = []

        for j2 in range(len(path_record)):
            if path_record[j2][0] == i2 - 1:
                current_path_index.append(j2)

        # print(path_record)
        # print(f"The number of elements are {elements}")

        for k in current_path_index:
            matching_list = None
            threshold = 0.1
            for k2 in range(elements):
                d1 = abs(path_record[k][-1] - df.iloc[i2, k2 + 2])
                if d1 < threshold:
                    threshold = d1
                    matching_list = [k, k2 + 2]
                    match_found.append(k2)
            if matching_list is not None:
                path_record[matching_list[0]].append(df.iloc[i2, matching_list[1]])
                path_record[matching_list[0]][0] = i2

        if len(match_found) != elements:
            for m in range(elements):
                if m not in match_found:
                    path_record.append([i2, df.iloc[i2, m + 2]])

print(f"The length of path_record is {len(path_record)}")
for j in range(len(path_record)):
    print(f"Path {j} ends at {path_record[j][0]}")

