from ydata_profiling import ProfileReport
import pandas as pd 

filepath_wdbc_csv = r'/Users/edward/is477-fall2023-final-project/data/car+evaluation/car.csv'

df = pd.read_csv(r'/Users/edward/is477-fall2023-final-project/data/car+evaluation/car.csv')

profile = ProfileReport(df, title = "Car Evaluation Report")
profile.to_file(r'/Users/edward/is477-fall2023-final-project/profiling/report.html')