import pandas as pd
import plotly.graph_objs as go

# Use this file to read in your data and prepare the plotly visualizations. The path to the data files are in
# `data/file_name.csv`

def group_bar(df1, df2, col_name, title, x_title, y_title, x=None, x1='More Than 80% Booked', x2='Less Than 80% Booked'):

    if x==None:
        x = df1[col_name].unique()
    y1 = df1[col_name].value_counts(normalize=True)
    y2 = df2[col_name].value_counts(normalize=True)
    
    fig = go.Figure(
            data=[
                go.Bar(name=x1, x=x, y=y1),
                go.Bar(name=x2, x=x, y=y2)
                ],
            layout = dict(
                title = title,
                xaxis = dict(title = x_title,),
                yaxis = dict(title = y_title),
                showlegend = False
                )
            )
    print(fig)
    
    return fig
    
    
    
def clean_data():
    df = pd.read_csv('data/listings.csv')

    df['Booking Percentage'] = (365-df['availability_365'])/365 * 100

    df_popular_listing = df[df['Booking Percentage']>=80]
    df_other_listing = df[df['Booking Percentage']<80]
    
    return df_popular_listing, df_other_listing


    
def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

    df1, df2 = clean_data()
    
    
    figure_one = group_bar(df1, df2, 'neighbourhood_group_cleansed', \
                                      'Popular Listings VS Others Based On Neighborhood', 'Neighborhood', 'Booking Ratio')
    figure_two = group_bar(df1, df2, 'property_type', \
                                      'Popular Listings VS Others Based On Property Type', 'Property Type', 'Booking Ratio')
    figure_three = group_bar(df1, df2, 'host_is_superhost', \
                                      'Popular Listings VS Others Based On Superhost Status', 'Superhost Status', \
                                      'Booking Ratio', ['Not Superhost','Superhost'])
    figure_four = group_bar(df1, df2, 'host_identity_verified', \
                                      'Popular Listings VS Others Based On Host ID\nVerification Status', 'Host Identity', \
                                      'Booking Ratio', ['Host Identity Verified','Host Identity Not Verified'])


    # append all charts to the figures list
    figures = []
    figures.append(figure_one)
    figures.append(figure_two)
    figures.append(figure_three)
    figures.append(figure_four)
#     figures.append(dict(data=graph_one, layout=layout_one))


    return figures
