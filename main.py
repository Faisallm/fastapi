from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


# it's like we are applying magic to a function,
# home pages
@app.get('/')
def root():

    # fastApi will automatically output to json
    return {'message': "Faisal Lawan Muhammad"}


@app.get('/posts')
def get_posts():
    return {'data-post': "Faisal, This is your posts, All-for-one, One-for-All"}


# extract fields from the body (data from the client side)
# store them as a dictionary on a variable payLoad.
@app.post('/createposts')
def create_posts(payLoad: dict = Body(...)):
    print(payLoad)
    return {"new_post": f"title: {payLoad['title']},  content: {payLoad['content']}"}  
