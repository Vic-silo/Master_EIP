from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return 'Mensaje de bienvenida'
