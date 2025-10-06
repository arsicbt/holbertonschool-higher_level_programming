#!/usr/bin/python3


import requests
import csv


def fetch_and_print_posts():
    response_get = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status code :", response_get.status_code)

    if response_get.status_code == 200:
        posts = response_get.json()
        for posts in posts:
            print(posts['title'])

        print()



def fetch_and_save_posts():

    response_post = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response_post.status_code == 200:
        posts = response_post.json()

        clean_posts = [
                {'id': post['id'], 'title': post['title'], 'body': post['body']}
                for post in posts
            ]

        with open('response_post', 'w', encoding='utf-8') as file:

            field = ['id', 'title', 'body']
            writer = csv.DictWriter(file, fieldnames=field)
            writer.writeheader()
            writer.writerows(clean_posts)

        print("All done ! CSV file sucessfully created")
    else:
        print("Erreur HTTP :", response.status_code)