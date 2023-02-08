import spacy
nlp = spacy.load('en_core_web_md')

# Create empty lists
movie_list = []
score_list = []


# Reading in movies.txt file
f = open("movies.txt", "r", encoding="utf-8")
for line in f:
    movie_list.append(line)
f.close()

# The movie description we will compare against in the function saved as variable
planet_hulk = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator."""

hulk_description = nlp(planet_hulk)


def find_similar_movie(description):
    # Function that takes in movie description (saved to variable) and finds the most similar movie to watch

    # Loop through movie list and find similarity score and append to score list
    for movie in movie_list:
        similarity = nlp(movie).similarity(description)
        score_list.append(similarity)

    # Loop through score list to find maximum and index value
    ranking = 0
    index = 0
    for rating in score_list:
        if rating > ranking:
            ranking = rating
            index += 1

    # Print maximum score movie result
    print(f"The most similar movie to watch is {movie_list[index][:7]} with a score of {round(score_list[index],4)}")
    print(f"Description: {movie_list[index][9:]}")

find_similar_movie(hulk_description)