import time
import requests

URLS = [
    'https://jsonplaceholder.typicode.com/posts',
    'https://jsonplaceholder.typicode.com/comments',
    'https://jsonplaceholder.typicode.com/albums',
    'https://jsonplaceholder.typicode.com/photos',
    'https://jsonplaceholder.typicode.com/todos',
    'https://jsonplaceholder.typicode.com/users'
]

def fetch_single(url: str) -> None:
    print(f'Fetching: {url}...')
    requests.get(url)
    time.sleep(1)
    print(f'Fetched {url}!')


if __name__ == '__main__':
    time_start = time.time()
    
    for url in URLS:
        fetch_single(url)

    time_end = time.time()
    print(f'\nAll done! Took {round(time_end - time_start, 2)} seconds')