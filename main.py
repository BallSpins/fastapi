from fastapi import FastAPI

app = FastAPI()

@app.get('/{msg}')
def root(msg):
    return {'message': msg}