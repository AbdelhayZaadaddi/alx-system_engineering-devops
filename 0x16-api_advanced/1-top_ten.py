#!/usr/bin/python3
""" Top 10 subscribers """
import requests


def top_ten(subreddit):
    """ Get top 10 subscribers """
    requist = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json",
        headers={},
        params={"limit": 10},
    )

    if requist.status_code == 200:
        data = requist.json().get("data")
        if data and "children" in data:
            for child in data["children"]:
                if "data" in child and "title" in child["data"]:
                    print(child["data"]["title"])
                else:
                    print("Invalud post format:", child)
        else:
            print("No data returned")
    else:
        print(None)
