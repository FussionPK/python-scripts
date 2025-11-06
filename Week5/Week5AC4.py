try:
    movies = (("Inception", 2010), ("Matrix", 1999), ("Interstellar", 2014))
    
    # Extracting titles and years
    years = [movie[1] for movie in movies] 

    #Showcase the years
    print(years)

    titles = [movie[0] for movie in movies] 

    #showcase the titles
    print(titles)
    
    # Finding the oldest movie
    oldest_year = min(years)
    print(f"\nThe oldest movie is released in {oldest_year}.")

    # Displaying all movie titles
    print("\nAll movie titles:")
    for title in titles:
        print(title)

    # Attempting to change a year (this will cause an error)
    print("\nTrying to change the year of a movie:")
    movies[0][1] = 2021  # This line will raise an error

except TypeError as e:  # Catching the TypeError for attempting to modify a tuple
    print("Execution Error: Cannot change a value in a tuple:", e)
