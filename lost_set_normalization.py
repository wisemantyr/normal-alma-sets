
import pandas as pd
import os
import re

lost_path = "../../downloads/results.xlsx" 
lost_df = pd.read_excel(lost_path)

all_null_cols = lost_df.columns[lost_df.isna().all()].tolist()

lost_df = lost_df.drop(columns=all_null_cols)
lost_df=lost_df.drop(columns=["Library", "Call Number Type", "Item ID", "Holdings ID", "Process type", "Item Policy", "Creation Date"])

mode = lost_df['Copy ID'].mode().values[0]
lost_df['Copy ID'].fillna(value=mode, inplace=True)
lost_df["Copy ID"] = lost_df["Copy ID"].astype(int)

lost_df["Modification Date"] = pd.to_datetime(lost_df["Modification Date"])
lost_df["Due Date"] = pd.to_datetime(lost_df["Due Date"])

#change month when necessary
#new_lost_df= lost_df.loc[lost_df["Modification Date"].dt.month >= 11]


new_lost_df["Modification Date"] = new_lost_df["Modification Date"].dt.strftime('%d-%b')
new_lost_df["Due Date"] = new_lost_df["Due Date"].dt.strftime('%d-%b')


new_lost_df["Type / Creator / Imprint"] = new_lost_df["Type / Creator / Imprint"].str.replace(r"(Book By)", "")
new_lost_df["Type / Creator / Imprint"] = new_lost_df["Type / Creator / Imprint"].str.replace(r"(Music By)","")
new_lost_df["Type / Creator / Imprint"] = new_lost_df["Type / Creator / Imprint"].str.replace(r"[\(\[].*?[\)\]]","")
new_lost_df["Type / Creator / Imprint"] = new_lost_df["Type / Creator / Imprint"].str.replace(r"[\d]","")
new_lost_df["Type / Creator / Imprint"] = new_lost_df["Type / Creator / Imprint"].str.replace(r"[\)]","")
new_lost_df["Type / Creator / Imprint"] = new_lost_df["Type / Creator / Imprint"].str.replace(r"[\.]","")
new_lost_df["Type / Creator / Imprint"] = new_lost_df["Type / Creator / Imprint"].str.replace(r"[\,]", "")


new_final = new_lost_df[["Barcode","title", "Type / Creator / Imprint", "Call Number","Permanent Location", "Material Type", "Copy ID", "Description", "Orders", "Requests", "Modification Date", "Due Date"]]
new_final = new_final.rename(columns={"Type / Creator / Imprint": "Author"})


new_final.to_csv("new_final.csv")
