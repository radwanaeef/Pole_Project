import pandas as pd
import os
from datetime import datetime

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
'''extract timestamp'''


def save_to_excel(data, output_file="outputs/pole_data2.xlsx"):
    '''def save_to_excel(data, output_file=f"outputs/pole_data_{timestamp}.xlsx"):'''
    """
    data = list of dicts
    """
    
    df = pd.DataFrame(data)

    if os.path.exists(output_file):
        # append if file exists
        old_df = pd.read_excel(output_file)
        df = pd.concat([old_df, df], ignore_index=True)
        df = df.drop_duplicates()


    df.to_excel(output_file, index=False)
    print(f"📁 Saved to {output_file}")