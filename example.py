import giphy_py
import asyncio

client = giphy_py.get_client("sG7s4XlraVmx9qXGofsQBqkQUQMnC91L")

client.set_language(giphy_py.language.es)

search = asyncio.get_event_loop().run_until_complete(client.search_gifs("Giphy"))

print(search.results[1].image_url)
print(search.results[0])
print(search)
print(search.pagination)
print(search.meta)
