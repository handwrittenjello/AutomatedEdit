from tmdbv3api import TMDb
from tmdbv3api import Movie
tmdb = TMDb()
tmdb.api_key = '03efb1cb001d35e7a9c5a2569f12d10c'
tmdb.language = 'en'
tmdb.debug = False




movie = Movie()
print('Which UFC Card? (placeholder)')
##Movie Search
search = movie.search('UFC ' + input())

print(search[0].id)

cardID = search[0].id

print(search[0].poster_path)
print(search[0].backdrop_path)
backdropLink = search[0].backdrop_path
originalPath = 'https://image.tmdb.org/t/p/original/'
directBackdrop = originalPath + backdropLink
print(directBackdrop)

"""
for res in search:
    print(res.id)
    print(res.title)
    print(res.overview)
    print(res.poster_path)
    print(res.vote_average)


m = movie.details()
print(m.title)
print(m.overview)
print(m.popularity)

"""