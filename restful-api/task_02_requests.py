#!/usr/bin/python3


import requests
import csv


def fetch_and_print_posts():
    response_get = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code:", response_get.status_code)

    if response_get.status_code == 200:
        posts = response_get.json()
        for post in posts:
            print(post['title'])

        print("All done!")
    else:
        print("Error")


def fetch_and_save_posts():

    response_post = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response_post.status_code == 200:
        posts = response_post.json()

        clean_posts = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in posts
        ]

        with open('posts.csv', 'w', newline='', encoding='utf-8') as f:

            field = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=field)
            writer.writeheader()
            writer.writerows(clean_posts)

    else:
        print("Error")
