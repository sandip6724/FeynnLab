def univariate(df):
    """ This function calculates and displays key statistical measures and visualizations for univariate analysis of the specified column in the dataset. 
    The analysis includes:
        - Descriptive statistics: mean, median, mode, variance, standard deviation, skewness, and kurtosis.
        - Distribution plots: histogram and boxplot."""
    import matplotlib.pyplot as plt
    import seaborn as sns
    # separate cat and con features
    cat = list(df.columns[df.dtypes=='object'])
    con = list(df.columns[df.dtypes!='object'])
    # Descriptive statistics
    print(f'Descriptive Analysis : {df.describe().T}')
    print('\n=========================================\n')
    # Applying for loop for categural variables for countplot
    print(f'Categorical variable : {cat} countplot\n')
    for i in cat:
        plt.figure(figsize=(13,6))
        sns.countplot(data=df,x=i)
        plt.title(f'countplot for {i}')
        plt.show()
    print('\n==============================================================================================================\n')
    # apply for loop for con variable
    print(f'Contineous variable : {con} Histogram')
    for j in con:
        plt.figure(figsize=(13,6))
        sns.histplot(data=df,x=j,kde=True)
        plt.title(f'Histogram plot for {j}')
        plt.show()         
        
