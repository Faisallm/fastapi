from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

my_posts = [{"title": "Machina", "content":"John Wick", "id":1},
            {"title": "Machine", "content":"Artificial Intelligence", "id":2},]
# schema
class Post(BaseModel):
    title: str
    content: str
    # if the user does not provide published
    # it's default value should be set to published. 
    published: bool = True
    # this is an optional field if the user
    # does not provide it, it's gonna
    # default to none.
    rating: Optional[int] = None


# the user needs to send the data in a format/scheme
# that we expect the data to look in a certain way
# the frontend can't just send random data
# we can use pydantic to define our schema


# it's like we are applying magic to a function,
# home pages
@app.get('/')
def root():

    # fastApi will automatically output to json
    return {'message': "Faisal Lawan Muhammad"}


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