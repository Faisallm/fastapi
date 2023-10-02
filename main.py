from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():

    # fastApi will automatically convert output to json
    return {'message': "Hello Faisal"}