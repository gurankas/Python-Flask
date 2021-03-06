from flask import Flask,  render_template
import json
import requests

app = Flask(__name__)


@app.route('/authors', methods=['POST', 'GET'])
def authors():
    users_uri = 'https://jsonplaceholder.typicode.com/users'
    posts_uri = 'https://jsonplaceholder.typicode.com/posts'

    try:
        users_raw_data = requests.get(users_uri)
        posts_raw_data = requests.get(posts_uri)
    except requests.ConnectionError:
        return "Connection error"

# convert JSON data for python
    users_data = users_raw_data.text
    data = json.loads(users_data)

    posts_data = posts_raw_data.text
    data1 = json.loads(posts_data)

# finding author ID from JSON data retrieved
    author_id = []
    for i in range(len(data)):
        author_id.append(data[i]["id"])

# instantiating number of posts by each author in the list to 0
    number_of_posts = {}
    for k in range(len(author_id)):
        number_of_posts[k] = 0

# find number of posts of each author
    for posts in range(len(data)):
        for j in range(len(data1)):
            if data1[j]["userId"] == author_id[i]:
                number_of_posts[posts] += 1

# find names of authors corresponding to their IDs to be sent to the template for displaying
    author_name = []
    for i in range(len(data)):
        author_name.append(data[i]["name"])

    return render_template("authors.html", number_of_posts=number_of_posts, author_name=author_name)


if __name__ == "__main__":
    app.run(debug=True)