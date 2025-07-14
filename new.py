import database
import pandas as pd

choice = pd.read_sql("select * from choices", database.engine)
print(choice)