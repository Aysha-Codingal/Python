import random
import pandas as pd
from textblob import TextBlob

df = pd.read_csv("imdb_top_1000.csv")
df["combined_features"] = df["Genre"].fillna("") + " " + df["Overview"].fillna("")


def get_genres(df):
    genres = []
    for g in df["Genre"].dropna():
        for item in g.split(","):
            genres.append(item.strip())
    return sorted(set(genres))


genres = get_genres(df)


def recommend_movies_ai(genre, mood, min_rating=7.5, top_n=5):
    movies = df.copy()

    movies = movies[movies["Genre"].str.contains(genre, case=False, na=False)]
    movies = movies[movies["IMDB_Rating"] >= min_rating]

    recommendation = []
    user_sentiment = TextBlob(mood).sentiment.polarity

    for _, row in movies.iterrows():
        if pd.isna(row["Overview"]):
            continue

        movie_sentiment = TextBlob(row["Overview"]).sentiment.polarity

        if user_sentiment < 0 and movie_sentiment > 0:
            recommendation.append(row)
        elif user_sentiment >= 0:
            recommendation.append(row)

        if len(recommendation) == top_n:
            break

    return recommendation


def get_random_movie():
    return df.sample(n=1).iloc[0]


def display_movie_details(row):
    overview = row.get("Overview", "N/A")
    polarity = TextBlob(str(overview)).sentiment.polarity
    sentiment_label = (
        "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
    )

    print("-" * 50)
    print(f"Title            : {row.get('Series_Title', 'N/A')}")
    print(f"Genre(s)         : {row.get('Genre', 'N/A')}")
    print(f"Overview         : {overview}")
    print(f"IMDB Rating      : {row.get('IMDB_Rating', 'N/A')}")
    print(f"Sentiment Analysis: {sentiment_label} (Polarity: {polarity:.2f})")
    print("-" * 50)


def main():
    print("🎥 Welcome to the Movie Recommender 🎥\n")
    name = input("Enter your name: ")
    print(f"\nHello, {name}!")

    while True:
        print("\nChoose an option:")
        print("1. AI-based Recommendation")
        print("2. Random Recommendation")
        print("3. Exit")

        choice = input("Enter option (1/2/3): ").strip()

        if choice == "1":
            print("\n--- AI-based Recommendation ---")
            print("Available Genres:")
            for i, g in enumerate(genres, 1):
                print(f"{i}. {g}")

            try:
                genre_choice = int(input("\nChoose Genre Number: "))
                selected_genre = genres[genre_choice - 1]
            except (ValueError, IndexError):
                print("Invalid genre choice. Defaulting to Action.")
                selected_genre = "Action"

            mood = input("How do you feel today? ")
            rating_input = input(
                "Minimum IMDB rating (press Enter to skip, default 7.5): "
            ).strip()
            min_rating = float(rating_input) if rating_input else 7.5

            results = recommend_movies_ai(selected_genre, mood, min_rating)

            if not results:
                print("\nNo movies found matching your criteria.")
            else:
                print(f"\nTop AI Recommendations for {name}:")
                for movie in results:
                    display_movie_details(movie)

        elif choice == "2":
            print("\n--- Random Recommendation ---")
            movie = get_random_movie()
            display_movie_details(movie)

        elif choice == "3":
            print(f"\nGoodbye, {name}! Thanks for using the Movie Recommender.")
            break

        else:
            print("Invalid option. Please try again.")
            continue

        again = (
            input("\nWould you like another recommendation? (yes/no): ")
            .strip()
            .lower()
        )
        if again not in ["yes", "y"]:
            print(f"\nGoodbye, {name}! Thanks for using the Movie Recommender.")
            break


if __name__ == "__main__":
    main()