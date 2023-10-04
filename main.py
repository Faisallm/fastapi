from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

my_posts = [{"title": "Machina", "content": "John Wick", "id": 1},
            {"title": "Machine", "content": "Artificial Intelligence", "id": 2},]
# schema


class Post(BaseModel):
    title: str
    content: str
    # if the user does not provide published
    # it's default value should be set to published.
    # boolean field with a default value of True
    published: bool = True
    # this is an optional field if the user
    # does not provide it, it's gonna
    # default to none.
    # integer optional field with a default value of None
    rating: Optional[int] = None


def find_post(id):
    for post in my_posts:
        if post['id'] == id:
            return post
    return "post not found"

# the user needs to send the data in a format/scheme
# that we expect the data to look in a certain way
# the frontend can't just send random data
# we can use pydantic to define our schema


# it's like we are applying magic to a function,
# home pages
# landing api page
@app.get('/')
def root():

    # fastApi will automatically output to json
    return {'message': "Faisal Lawan Muhammad Ahmad Barde"}


@app.get('/posts')
def get_posts():
    return {'data-post': my_posts}


# extract fields from the body (data from the client side)
# store them as a dictionary on a variable payLoad.

# fastapi will automatically validate the data it receives...
# from the client based off the pydantic schema
@app.post('/posts')
def createposts(post: Post):
    # converting a pydantic model to dictionary
    print(post)
    print(post.dict())
    print("#############################################################3")
    print('rating:', post.rating)
    print('published=', post.published)
    return {"data": post}

# data required to create post
# title str, content str, category, published Bool


@app.get('/posts/latest')
def get_latest_post():
    latestPost = my_posts[len(my_posts)-1]
    return {"detail": latestPost}

# id represents a part parameter


@app.get('/posts/{id}')
def get_post(id: int):
    # logic for getting
    post = find_post(id)
    return {"post-detail": post}

# the next crud is retrieving a single post
