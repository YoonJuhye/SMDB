import urllib.request
from pprint import pprint
import json

API_KEY = f"631c5758767f580641f6e6996282a3b5"
HOST = "https://api.themoviedb.org"
MOVIE_LIST_URI = "/3/movie/popular"
MOVIE_INFO_URI = "/3/movie/"
GENRE_LIST_URI = "/3/genre/movie/list"
CREDIT_LIST_URI = "/3/movie/"

movie_list = []
movie_Ids = []
genre_list = []
# credit_Ids = []
cast_list = []
# credit_list = []
crew_list = []

# 장르 데이터 genre_list
genre_request = (f'{HOST}{GENRE_LIST_URI}?api_key={API_KEY}&language=ko')
response = urllib.request.urlopen(genre_request)
json_str = response.read().decode('utf-8')
json_object = json.loads(json_str)

genre_data = json_object.get("genres")

for data in genre_data:

    my_data = {
        "number": data.get("id"),
        "name": data.get("name")
    }

    my_genre = {
        "model": "movies.genre",
        "pk": my_data.get("number"),
        "fields": {
            "name": my_data.get("name")
        },
    }
    genre_list.append(my_genre)

# # 크레딧 데이터 credit_Ids

# request = (f'{HOST}{CREDIT_LIST_URI}?api_key={API_KEY}&language=ko')
# response = urllib.request.urlopen(request)
# json_str = response.read().decode('utf-8')
# json_object = json.loads(json_str)

# data_credits = (json_object.get("results"))

# for movie in data_credits:
#     credit_Ids.append(movie.get("id"))




# 무비 id 데이터 movie_Ids

for i in range(1, 26):
    request = (f'{HOST}{MOVIE_LIST_URI}?api_key={API_KEY}&language=ko&page={i}')
    response = urllib.request.urlopen(request)
    json_str = response.read().decode('utf-8')
    json_object = json.loads(json_str)

    data_movies = (json_object.get("results"))

    for movie in data_movies:
        movie_Ids.append(movie.get("id"))


# 무비 데이터 movie_list
for idx, movie_Id in enumerate(movie_Ids):
    movie_request = (f'{HOST}{MOVIE_INFO_URI}{movie_Id}?api_key={API_KEY}&language=ko&')
    response = urllib.request.urlopen(movie_request)
    json_str = response.read().decode('utf-8')
    json_object = json.loads(json_str)



    if json_object.get("poster_path"):
        if json_object.get('genres'):
            genres = []
            for i in json_object.get("genres"):
                genres.append(i['id'])

            my_object = {
                "model": "movies.movie",
                "pk": json_object.get("id"),
                "fields": {
                    "title": json_object.get("title"),
                    "overview": json_object.get("overview"),
                    "vote_average": json_object.get("vote_average"),
                    "vote_count": json_object.get("vote_count"),
                    # "adult": json_object.get("adult"),
                    "popularity": json_object.get("popularity"),
                    "release_date": json_object.get("release_date"),
                    # "runtime": json_object.get("runtime"),
                    "poster_path": json_object.get("poster_path"),
                    "video": json_object.get("video"),
                    "genre_ids" : genres,
                    # "original_title": json_object.get("original_title"),
                }  
            }

        print(my_object["fields"]["genre_ids"])
        movie_list.append(my_object)



# 캐스트 데이터 cast_list
for idx, movie_Id in enumerate(movie_Ids):
    credit_request = (f'{HOST}{CREDIT_LIST_URI}{movie_Id}/credits?api_key={API_KEY}&language=ko&')
    response = urllib.request.urlopen(credit_request)
    json_str = response.read().decode('utf-8')
    json_object = json.loads(json_str)
    cast_data = json_object.get("cast")
    for data in cast_data:
        
        cast_data = {
            "id": data.get("id"),
            "name": data.get("name"),
            "character": data.get("character"),
            # "profile_path": data.get("profile_path")
        }

        my_cast = {
            "model": "movies.cast",
            "pk": cast_data.get("id"),
            "fields": {
                "movie": json_object.get("id"),
                "name": cast_data.get("name"),
                "character": cast_data.get("character"),
                # "profile_path": cast_data.get("profile_path")
            },
        }
        cast_list.append(my_cast)

# 크루 데이터 crew_list
for idx, movie_Id in enumerate(movie_Ids):
    credit_request = (f'{HOST}{CREDIT_LIST_URI}{movie_Id}/credits?api_key={API_KEY}&language=ko&')
    response = urllib.request.urlopen(credit_request)
    json_str = response.read().decode('utf-8')
    json_object = json.loads(json_str)
    crew_data = json_object.get("crew")
    for data in crew_data:
        
        crew_data = {
            "id": data.get("id"),
            "name": data.get("name"),
            "job": data.get("job"),
            # "profile_path": data.get("profile_path")
        }

        my_crew = {
            "model": "movies.crew",
            "pk": crew_data.get("id"),
            "fields": {
                "movie": json_object.get("id"),
                "name": crew_data.get("name"),
                "job": crew_data.get("job"),
                # "profile_path": crew_data.get("profile_path")
            },
        }
        crew_list.append(my_crew)

with open('movies.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(movie_list, ensure_ascii=False))

with open('genres.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(genre_list, ensure_ascii=False))

with open('casts.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(cast_list, ensure_ascii=False))

with open('crews.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(crew_list, ensure_ascii=False))