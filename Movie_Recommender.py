def movie_5recommendations():
    ## Read the data from IMDB movies using pandas
    import pandas as pd

    df = pd.read_csv('imdb_top_1000.csv')

    ## getting the Genre and IMDB rating from user

    genre = input('which genre do you interested in?').strip().lower()
    rating = float(input('now tell me about minimum rating: (eg.:7.1)'))

    ## filtering the data from CSV file based on the input variables

    filtered = df[
        df['Genre'].str.lower().str.contains(genre) &
        (df['IMDB_Rating'] >= rating)
    ]

    ## randomize the result

    random_top_n= filtered.sample(n=5, random_state= None)

    for i, row in random_top_n.iterrows():
        print(f"{row['Series_Title'], row['IMDB_Rating'], row['Genre'], row['Released_Year']}")




print(movie_5recommendations())











