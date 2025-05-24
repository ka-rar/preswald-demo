import pandas as pd
import plotly.express as px
from preswald import connect, get_df, query, text, table, plotly

connect()
df = get_df("salary")

filtered_df = query("""
    SELECT * FROM salary
    WHERE CAST(REPLACE(REPLACE("Average of Base Salary", '$', ''), ',', '') AS FLOAT) > 100000
    ORDER BY CAST(REPLACE(REPLACE("Average of Base Salary", '$', ''), ',', '') AS FLOAT) DESC
""", "salary")

text('# Salary Explorer')
text("Here are all job roles making more than $100K annually, sorted in ascending order:")
table(filtered_df, title=">$100K Roles")

fig = px.bar(filtered_df,
            x='Position Title',
            y='Average of Base Salary',
            title='High Earning Roles',
            labels={'Average of Base Salary': 'Avg Salary ($)'},
            text='Average of Base Salary')

fig.update_layout(xaxis_tickangle=45, height=600)
plotly(fig)