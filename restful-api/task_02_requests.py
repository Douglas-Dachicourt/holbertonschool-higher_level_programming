#!/usr/bin/python3
"""import requests and csv modules"""
import requests
import csv


def fetch_and_print_posts():
    """
    Function : fetch_and_print_posts

    This one fetches all post from JSONPlaceholder (as example).
    We are using the python requests module to make a request to the adress

    We print out the result we would like : Here all the titles of all posts

    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    success_code = response.status_code
    print("Status Code: {}".format(success_code))

    if success_code == 200:
        data = response.json()
        for item in data:
            print(item["title"])


def fetch_and_save_posts():
    """
    Function : fetch_and_save_posts

    This one fetches all post from JSONPlaceholder two.
    We are using the python requests module to make a request to the adress

    We are managing each dictarionary in a python list, where each one have
    a specific order by keys.

    We then save the results into a csv file using the csv module



    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    success_code = response.status_code

    results = []

    if success_code == 200:
        data = response.json()

        for item in data:
            item_dict = {}

            for key, value in item.items():
                item_dict["id"] = item.get("id")
                item_dict["title"] = item.get("title")
                item_dict["body"] = item.get("body")
            results.append(item_dict)

        with open("posts.csv", "w") as file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
