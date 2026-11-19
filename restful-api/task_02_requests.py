#!/usr/bin/python3
"""Module for fetching posts from JSONPlaceholder"""
import requests
import csv

url = 'https://jsonplaceholder.typicode.com/posts'


def fetch_and_print_posts():
    """Function to send request to JSONPlaceholder"""

    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()

        for response in data:
            title = response["title"]
            print(title)

  
    else:
        print("Request was not successful.")


def fetch_and_save_posts():
    """Function to save the response data to a dictionary"""
   

    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        csvf = 'posts.csv'
        datalist = []

        for element in data:
            post = {
                'id': element.get('id'),
                'title': element.get('title'),
                'body': element.get('body')
            }
            datalist.append(post)

        with open(csvf, 'w', encoding='UTF-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(datalist)

    else:
        print("Request was not successful.")
