
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

#change date range
nov_lost_df= lost_df.loc[lost_df["Modification Date"].dt.month >= 11]


nov_lost_df["Modification Date"] = nov_lost_df["Modification Date"].dt.strftime('%d-%b')
nov_lost_df["Due Date"] = nov_lost_df["Due Date"].dt.strftime('%d-%b')


nov_lost_df["Type / Creator / Imprint"] = nov_lost_df["Type / Creator / Imprint"].str.replace(r"(Book By)", "")
nov_lost_df["Type / Creator / Imprint"] = nov_lost_df["Type / Creator / Imprint"].str.replace(r"(Music By)","")
nov_lost_df["Type / Creator / Imprint"] = nov_lost_df["Type / Creator / Imprint"].str.replace(r"[\(\[].*?[\)\]]","")
nov_lost_df["Type / Creator / Imprint"] = nov_lost_df["Type / Creator / Imprint"].str.replace(r"[\d]","")
nov_lost_df["Type / Creator / Imprint"] = nov_lost_df["Type / Creator / Imprint"].str.replace(r"[\)]","")
nov_lost_df["Type / Creator / Imprint"] = nov_lost_df["Type / Creator / Imprint"].str.replace(r"[\.]","")
nov_lost_df["Type / Creator / Imprint"] = nov_lost_df["Type / Creator / Imprint"].str.replace(r"[\,]", "")


nov_final = nov_lost_df[["Barcode","title", "Type / Creator / Imprint", "Call Number","Permanent Location", "Material Type", "Copy ID", "Description", "Orders", "Requests", "Modification Date", "Due Date"]]
nov_final = nov_final.rename(columns={"Type / Creator / Imprint": "Author"})


nov_final.to_csv("nov_final.csv")
