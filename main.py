import os
import sys
sys.path.append(os.getcwd())
from src.categorize_comments import categorize_comment
from src.helper import *

def main():
    with open('categories.json', 'r') as file:
        categories = json.load(file)

    with open('comments.json', 'r') as file:
        comments = json.load(file)

    categorized_comments = {}
    for comment in comments:
        category = categorize_comment(comment, categories)
        if category not in categorized_comments:
            categorized_comments[category] = [comment]
        else:
            categorized_comments[category].append(comment)

    with open('categorized_comments.json', 'w') as file:
        json.dump(categorized_comments, file, indent=4)

if __name__ == "__main__":
    main()