# from pydantic_settings import BaseSettings
import pandas as pd
# from pandas_profiling import ProfileReport
from ydata_profiling import ProfileReport
df=pd.read_csv('Residential_Energy_Consumption.csv')
print(df)

profile = ProfileReport(df)
profile.to_file(output_file="Residential_Energy_analysis.html")