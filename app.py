import json
from curses.ascii import isdigit

from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    """
    The index route, which shows all the blog posts
    """
    with open('storage/blog_posts.json') as f:
        blog_posts = json.load(f)
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """
    The add route for both GET and POST methods, the GET method shows the form for a new post
    and the POST method save the post to JSON file and redirect user to the index route
    """
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        content = request.form.get('content')

        with open('storage/blog_posts.json', 'r') as f:
            posts = json.load(f)

        posts.append({'id': posts[-1]['id'] + 1, 'title': title, 'author': author, 'content': content})
        with open('storage/blog_posts.json', 'w') as f:
            json.dump(posts, f)
        return redirect(url_for('index'))

    return render_template('add.html')


@app.route('/delete/<post_id>', methods=['POST'])
def delete(post_id):
    """
    The delete route deletes the post with given id and redirects to the index route
    """
    if not isdigit(post_id):
        print('Invalid post id')
        return redirect(url_for('index'))

    with open('storage/blog_posts.json', 'r') as f:
        posts = json.load(f)
    posts = [post for post in posts if post['id'] != int(post_id)]
    with open('storage/blog_posts.json', 'w') as f:
        json.dump(posts, f)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)