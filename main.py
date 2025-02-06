from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {'message': 'message'}

@app.get('/{msg}')
def msg(msg):
    return {'message': msg}
