import pandas as pd
import json

data = pd.read_excel("Scan_Report_Innovations_Internal_VA_Q1_2024_2025_20240419.xlsx", sheet_name="Vulnerabilities")
# print(data.columns)
# print(data['IP'])
# for index, row in data.iterrows():
#     print(index, row)
dfs = []
for i in data['Application Owner'].unique():
    print(i)
    name = i.replace(".", " ").strip(" ")
    data_i = data.loc[data['Application Owner'] == i, :]
    data_i.to_excel(f"Innovations_Internal_VA_Q1_2024_2025_{name}.xlsx", index=False)
    # for j in data_i['IP'].unique():
    #     data_j = data_i.loc[data_i['IP'] == j, :]
    #     print(data_j['Category'].unique())
    #     print(data_j['Vendor Reference'].unique())
    dfs.append(data_i.copy())
print(dfs)
