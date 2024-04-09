import pandas as pd
import plotly.express as px

# Read the CSV file
lkd = pd.read_csv('Linkedin_Connections_10k_2_Feb_2024.csv')

# Convert 'Connected On' column to datetime format
lkd['Connected On'] = pd.to_datetime(lkd['Connected On'], format="%d/%m/%Y")

# Display the first 20 rows and the shape of the DataFrame
print(lkd.head(20))
print(lkd.shape)

# Sort the DataFrame by 'Connected On' column
lkd = lkd.sort_values(by='Connected On')

# Create a line plot using Plotly Express
fig = px.line(
    lkd.groupby(by='Connected On').count().reset_index(),
    x='Connected On',
    y='First Name',
    labels={'First Name': 'Number of Connections'},
    title='Connection Timeline')

# Save the plot as an HTML file
fig.write_html('chart.html')

# Open the HTML file in the default web browser
import webbrowser
webbrowser.open('chart.html')
