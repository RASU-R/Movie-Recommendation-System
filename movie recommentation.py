# Import required libraries
import pandas as pd

# Define a dictionary with emotions and associated movie genres
emotions_dict = {
    'happy': ['comedy', 'romantic comedy'],
    'sad': ['drama', 'romance'],
    'scared': ['horror', 'thriller'],
    'angry': ['action', 'revenge'],
    'bored': ['documentary', 'biography']
}

# Define a function to recommend movies based on user's emotion input
def recommend_movies(emotion):
    # Get movie genres associated with the given emotion
    genres = emotions_dict.get(emotion.lower())
    if genres is None:
        return "Sorry, we couldn't find any movie recommendations for the given emotion."

    # Load the dataset of movies and filter by genres associated with the given emotion
    movies_df = pd.read_csv('movies.csv') # use your directory
    recommended_movies = movies_df[movies_df['Genre'].isin(genres)]

    # Sort the recommended movies by their rating in descending order
    recommended_movies = recommended_movies.sort_values(by='Year', ascending=False)

    # Return top 5 recommended movies
    return recommended_movies.head(5)['Film']

# Test the function with an example emotion
emotion = 'sad'
print(f"Recommended movies for '{emotion}': \n{recommend_movies(emotion)}")
