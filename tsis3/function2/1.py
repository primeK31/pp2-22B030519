movies = [
    {
    "name": "Usual Suspects",
    "imdb": 7.0,
    "category": "Thriller"
    },
    {
    "name": "Hitman",
    "imdb": 6.3,
    "category": "Action"
    },
    {
    "name": "Dark Knight",
    "imdb": 9.0,
    "category": "Adventure"
    },
    {
    "name": "The Help",
    "imdb": 8.0,
    "category": "Drama"
    },
    {
    "name": "The Choice",
    "imdb": 6.2,
    "category": "Romance"
    },
    {
    "name": "Colonia",
    "imdb": 7.4,
    "category": "Romance"
    },
    {
    "name": "Love",
    "imdb": 6.0,
    "category": "Romance"
    },
    {
    "name": "Bride Wars",
    "imdb": 5.4,
    "category": "Romance"
    },
    {
    "name": "AlphaJet",
    "imdb": 3.2,
    "category": "War"
    },
    {
    "name": "Ringing Crime",
    "imdb": 4.0,
    "category": "Crime"
    },
    {
    "name": "Joking muck",
    "imdb": 7.2,
    "category": "Comedy"
    },
    {
    "name": "What is the name",
    "imdb": 9.2,
    "category": "Suspense"
    },
    {
    "name": "Detective",
    "imdb": 7.0,
    "category": "Suspense"
    },
    {
    "name": "Exam",
    "imdb": 4.2,
    "category": "Thriller"
    },
    {
    "name": "We Two",
    "imdb": 7.2,
    "category": "Romance"
    }
]


def imdb(movie):
    return movie['imdb'] > 5.5


def get_movies_imdb():
    return [movie for movie in movies if imdb(movie)]


def movies_category(category):
    return [movie for movie in movies if movie['category'] == category]


def average_imdb(movies):
    score = sum(movie['imdb'] for movie in movies)
    return (score / len(movies))


def average_category_imdb_score(category):
    movies_in_category = movies_category(category)
    return average_imdb(movies_in_category)


s = input("Enter film name: ")
m = next(item for item in movies if item["name"] == s)
print(imdb(m))
print("Films that imdb is bigger than 5.5: ")
print(get_movies_imdb())
c = input("Enter film category: ")
print(movies_category(c))
print("Average imdb score: ")
print(average_imdb(movies))
print("Average imdb category score: ")
print(average_category_imdb_score(c))
