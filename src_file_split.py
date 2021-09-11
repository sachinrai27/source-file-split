"""The below script requires a third party module pandas to be installed in order to execute.
The script can split one or multiple files present in the source folder in 100MB chunks.
While running, the script takes destination path as input from user.
Secondly the file to be split is converted to a dataframe using pandas and is then sorted as per Order Date column,recent date being on top.
Further the file is split."""

import csv
import pandas as pd
import os
import math
import sys

dest_path=sys.argv[1]

def main():
    file_path=os.getcwd()
    files=os.listdir(file_path)

    """Looping over all the csv files present in the source folder to split"""
    for file in files:
        if file.endswith(".csv") and not file.startswith("target"):
            src_file_size=os.stat(f'{file_path}\{file}')
            src_file_size=src_file_size.st_size
            
            df=pd.read_csv(f'{file_path}\{file}')
            df["Order Date"]=pd.to_datetime(df["Order Date"])
            df=df.sort_values(by="Order Date",ascending=False)

    
    counter1=0
    header=df.columns.values

    """Creating destination path if it doesn't exist"""
    if not os.path.exists(dest_path):
        os.mkdir(dest_path)
    
    for i in df.itertuples():
        if not os.path.exists(f"{dest_path}\\target{counter1}.csv"):
            f=open(f"{dest_path}//target{counter1}.csv",'w')
            writer=csv.writer(f)
            writer.writerow(header)
        else:
            f=open(f"{dest_path}//target{counter1}.csv",'a')
            writer=csv.writer(f)
            writer.writerow(i[1:])
            f.close()
        file_size=os.stat(f"{dest_path}//target{counter1}.csv")
        file_size=file_size.st_size
        
        if file_size>=104857600:
            counter1+=1
    
        
if __name__=="__main__":
    main()


