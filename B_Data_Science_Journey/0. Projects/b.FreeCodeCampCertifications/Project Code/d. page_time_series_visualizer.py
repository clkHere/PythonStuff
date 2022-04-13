import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col=['date'])

# Clean data
df = df[
(df.value <= df.value.quantile(.975)) &
(df.value >= df.value.quantile(.025))
]
dfc = df.copy() #TypeError Solution***


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize = (15,5))
    ax.plot(df.index, df.value)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.ticklabel_format(style='plain', axis='y')
    
  
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    
    # Copy and modify data for monthly bar plot
    df_bar = dfc.copy() #TypeError Solution***
    dfc['month'] = df.index.month
    dfc['year'] = df.index.year
    df_bar = dfc.groupby(['year', 'month'])['value'].mean()
    df_bar = df_bar.unstack()
                              
    # Draw bar plot
    fig = df_bar.plot(kind ="bar", legend = True, figsize = (15,10)).figure
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")

    plt.xticks(fontsize = 10)
    plt.yticks(fontsize = 10)
    plt.legend(fontsize = 10,
               title="Months", loc='center left', labels = [
                 'January', 'February', 'March', 'April', 
                 'May', 'June', 'July', 'August', 
                 'September', 'October', 'November', 'December'])
  
  # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]    

    # Draw box plots (using Seaborn)
    df_box['mInt'] = df_box['date'].dt.month #Box 2 Error Solution***
    df_box = df_box.sort_values('mInt') #Box 2 Error Solution***
    fig, (a,b) = plt.subplots(1,2,figsize=(15,10))

    a = sns.boxplot(x=df_box.year, y=df_box.value, ax=a)
    a.set_title('Year-wise Box Plot (Trend)')
    a.set_xlabel('Year')
    a.set_ylabel('Page Views')
    a.ticklabel_format(axis='y', style='plain')
    

    b = sns.boxplot(x=df_box.month, y=df_box.value, ax=b)
    b.set_title('Month-wise Box Plot (Seasonality)')
    b.set_xlabel('Month')
    b.set_ylabel('Page Views')    
    b.ticklabel_format(axis='y', style='plain')
    
  # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
