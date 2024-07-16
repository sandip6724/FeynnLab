def univariate(df):
    import matplotlib.pyplot as plt
    import seaborn as sns
    # separate cat and con features
    cat = list(df.columns[df.dtypes=='object'])
    con = list(df.columns[df.dtypes!='object'])
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
        