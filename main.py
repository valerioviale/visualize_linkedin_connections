import pandas as pd
import plotly.express as px

# Read the CSV file
lkd = pd.read_csv('Linkedin_Connections.csv')

# Convert 'Connected On' column to datetime format
lkd['Connected On'] = pd.to_datetime(lkd['Connected On'], format="%d/%m/%Y")

# Display the first 20 rows and the shape of the DataFrame
print(lkd.head(20))
print(lkd.shape)

# Group by month and year, and convert Period to string
monthly_connections = lkd.groupby(lkd['Connected On'].dt.to_period("M")).size().reset_index(name='Number of Connections')
monthly_connections['Connected On'] = monthly_connections['Connected On'].astype(str)

# Create a line plot using Plotly Express
fig = px.line(
    monthly_connections,
    x='Connected On',
    y='Number of Connections',
    labels={'Number of Connections': 'Number of Connections'},
    title='Monthly Connection Timeline'
)

# Show the plot
fig.show()
