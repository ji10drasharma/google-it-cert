#!/usr/bin/env python3

import os
import requests
import time

# Directory that contains the actual feedback
feedback_dir = '/data/feedback'

URL = "https://example.com/path/to/api"


def get_feedbacks(feedback_dir):
    """This reuturns list of dictionaries containing title, name, date and feedback as key"""
    fb_list = []
    feedbacks = {}
    # List that contains all of the feedback files
    feedback_list = os.listdir(feedback_dir)

    for feedback in feedback_list:
        feedback_file = os.path.join(feedback_dir, feedback)
        try:
            with open(feedback_file, 'r') as fb:
                lines = fb.readlines()
                feedbacks["title"] = lines[0].strip()
                feedbacks["name"] = lines[1].strip()
                feedbacks["date"] = lines[2].strip()
                feedbacks["feedback"] = "".join(lines[3:]).replace('\n', '')
                fb_list.append(feedbacks.copy())
        except:
            print("Something is wrong.")
    return fb_list


def post_feedback(URL, feedback_list):
    """For each item in the feedback_list, it tries to perform HTTP Post request"""
    for item in feedback_list:
        response = requests.post(URL, json=item)
        if response.status_code == 201:
            print("Success")
        else:
            print(response.status_code)
        time.sleep(1)


def main():
    reviews = get_feedbacks(feedback_dir)
    post_feedback(URL, reviews)


if __name__ == "__main__":
    main()
