
import pandas as pd
import numpy as np

lost_path = "../../downloads/results.xlsx" 
lost_df = pd.read_excel(lost_path)

#drop all null columns
all_null_cols = lost_df.columns[lost_df.isna().all()].tolist()
lost_df = lost_df.drop(columns=all_null_cols)

#reorder desired cols
lost_df=lost_df[
    ["MMS ID", "Barcode", "title", "Type / Creator / Imprint", "Call Number", "Permanent Location", "Material Type", "Process type", "Description", "Orders", "Requests", "Modification Date", "Due Date"]
    ]

#change month when necessary
#new_lost_df= lost_df.loc[lost_df["Modification Date"].dt.month >= 11]

#otherwise use this
new_lost_df = lost_df

#reformat dates
new_lost_df["Modification Date"] = new_lost_df["Modification Date"].dt.strftime('%d-%b-%y')
new_lost_df["Due Date"] = new_lost_df["Due Date"].dt.strftime('%d-%b-%y')

###regex to isolate author###
#remove common phrases
new_lost_df["Type / Creator / Imprint"] = new_lost_df["Type / Creator / Imprint"].str.strip(r"(Book By)")
new_lost_df["Type / Creator / Imprint"] = new_lost_df["Type / Creator / Imprint"].str.strip(r"(Music By)")
#remove most parenthethical info
new_lost_df["Type / Creator / Imprint"] = new_lost_df["Type / Creator / Imprint"].str.replace(r'\([^()]*', '')
#remove lingering parentheses
new_lost_df["Type / Creator / Imprint"] = new_lost_df["Type / Creator / Imprint"].str.replace(r"[\)]","")
#remove numbers
new_lost_df["Type / Creator / Imprint"] = new_lost_df["Type / Creator / Imprint"].str.replace(r"[\d]","")
#remove periods
new_lost_df["Type / Creator / Imprint"] = new_lost_df["Type / Creator / Imprint"].str.replace(r"[\.]","")
#remove commas
new_lost_df["Type / Creator / Imprint"] = new_lost_df["Type / Creator / Imprint"].str.replace(r"[\,]", "")
#remove extra white space
new_lost_df["Type / Creator / Imprint"] = new_lost_df["Type / Creator / Imprint"].str.strip()

#rename col and save
final = new_lost_df.rename(columns={"Type / Creator / Imprint": "Author"})

#replace 0 values for excel readability
final.loc[final['Orders'] == 0, 'Orders'] = np.nan
final.loc[final['Requests'] == 0, 'Requests'] = np.nan

#export
final.to_csv("new_final.csv")
