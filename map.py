import plotly.express as px

data = {
    'Country': ['United States', 'Canada', 'Brazil', 'Russia', 'India'],
    'Values': [100, 50, 80, 90, 78]
}

fig = px.choropleth(
    data_frame=data,
    locations='Country',
    locationmode='country names',
    color='Values',
    color_continuous_scale='Blues',
    title='Choropleth Map of Values by Country'
)

# Save the plot as an HTML file
fig.write_html("/workspaces/pythontest/choropleth_map.html")
print("Plot saved as 'choropleth_map.html'")
