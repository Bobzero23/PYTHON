import yfinance
import pandas
import numpy as np
import datetime
import plotly.graph_objects as go
import plotly.express as px

#getting the current date
today = datetime.date.today()

#creating our own date format
#so even if someoen enter something different it will render like this
d1 = today.strftime('%Y-%m-%d')

#setting the current data as end date
end_date = d1

#getting the same day of today but one year ago
d2 = datetime.date.today() - datetime.timedelta(days=365)

#setting the same day of today of one year ago as the start date
start_date = d2

data = yfinance.download('TSLA', start= start_date, end= end_date, progress= False)
data.head()
