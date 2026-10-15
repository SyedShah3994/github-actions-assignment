from fastapi import FastAPI

app = FastAPI()


def add(a: int, b: int) -> int:
    return a + b


@app.get('/')
def read_root():
    return {'message': 'Hello from GitHub Actions!'}


@app.get('/health')
def health():
    return {'status': 'ok'}


@app.get('/add')
def add_numbers(a: int, b: int):
    return {'result': add(a, b)}