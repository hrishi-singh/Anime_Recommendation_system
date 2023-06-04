
anime_search = get_search_results(query="Naruto", page=1)

for k in anime_search:
    print(k.get('title'))