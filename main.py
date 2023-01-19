from flask import Flask, render_template, request, redirect, flash
from db import *

app = Flask('flask-blogs')

app.secret_key = b'f_fs45'

@app.route('/')
def home():
    all_blogs = get_all_blogs()
    return render_template('index.html', blogs=all_blogs, title='Home')

@app.route('/blogs/create', methods=['POST', 'GET'])
def create():
    if request.method == 'GET':
        return render_template('create.html', title='New Blog')
    elif request.method == 'POST':
        save_blog(request.form)
        flash('Blog created!')
        return redirect('/')

@app.route('/blogs/<id>') # <string: page_id>
def show_blog(id): #page_id
    blog = get_blog_by_id(id)
    return render_template('blog.html', blog=blog, title='Blog Details')

@app.route('/blogs/delete/<id>')
def delete_blog(id):
    delete_blog_by_id(id)
    flash('Blog deleted!')
    return redirect('/')

@app.route('/blogs/update/<id>', methods=['POST', 'GET'])
def update_blog(id):
    blog = get_blog_by_id(id)
    if request.method == 'GET':
        return render_template('update.html', blog=blog, title='Update Blog')
    elif request.method == 'POST':
        update_blog_by_id(request.form, id)
        flash('Blog updated!')
        return redirect('/')
    

if __name__ == '__main__':
    app.run()