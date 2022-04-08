import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts() #returns pd.Series of counts per unique index name. 

    # What is the average age of men?
    maleTot = df[df['sex']=='Male']
    average_age_men = round(maleTot['age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    a = df[df['education']=='Bachelors'].shape[0]
    b = df['education'].shape[0]    
    percentage_bachelors = round(a/b*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    #Higher education calulcation:
    #Total(BMD & >50K) / Total(all BMD education)*100
    hEd = df[df['education'].isin(['Bachelors','Masters','Doctorate'])]
    hEd2 = len(hEd[hEd['salary']=='>50K'])/len(hEd)*100
    hEd3 = round(hEd2,1)
    
    #Lower education calculations:
    #Total(noDeg & >50K) / Total(all no degrees)*100
    lEd = df[~df['education'].isin(['Bachelors','Masters','Doctorate'])]
    lEd2 = len(lEd[lEd['salary']=='>50K'])/len(lEd)*100
    lEd3 = round(lEd2,1)

    # percentage with salary >50K
    higher_education_rich = hEd3
    lower_education_rich = lEd3

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    ## Find->#ppl in HPW == min_work_hours
    num_min_workers = len(df[df['hours-per-week']==min_work_hours])
    ##Find-> #ppl working min & >50K / #ppl working min
    minPpl = len(df[(df['hours-per-week']==min_work_hours) & (df['salary']=='>50K')])/num_min_workers*100
    rich_percentage = round(minPpl)

    # What country has the highest percentage of people that earn >50K?
    rich_countries = df.loc[df['salary']=='>50K', 'native-country'].value_counts()
    all_countries = df['native-country'].value_counts()
    top_country = (rich_countries/all_countries).fillna(0).sort_values(ascending=False).index[0]
    earnersIn_top_country = len(df[(df['native-country']== top_country) & (df['salary'] == '>50K')])
    top_country_total = len(df[df['native-country'] ==top_country])
    highest_earning_country = top_country
    highest_earning_country_percentage = round(earnersIn_top_country/top_country_total*100,1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[ (df['salary'] == ">50K") & (df['native-country'] == 'India')]['occupation'].value_counts().index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
