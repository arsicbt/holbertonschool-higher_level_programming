#!/usr/bin/python3


import requests, csv


def fetch_and_print_posts():
    response_get = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status code :", response_get.status_code)

    if response_get.status_code == 200:
        posts = response_get.json()
        result = [posts['title'] for posts in posts]
        print(result)
    return response_get

def fetch_and_save_posts():

    response_post = fetch_and_print_posts()

    if response_post.status_code == 200:
        posts = response_post.json()

    with open('response_post', 'w', encoding='utf-8') as file:
        # Define the columns from the key of the first post
        field = posts[0].keys()
        writer = csv.DictWriter(file, fieldnames=field)

        writer.writeheader() # Print the column
        writer.writerows(posts)  # Print the lines

