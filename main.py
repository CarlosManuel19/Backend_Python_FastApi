from fastapi import FastAPI

app = FastAPI()

# url local : http://127.0.0.1:8000 

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/url")
async def url():
    return {"url":"https://mouredev.com/"}


#Iniciar el server: uvicorn main:app --reload
#Detener el server: ctrl+c

#Documentación con swagger: http://127.0.0.1:8000/docs
#Documentación con redocly: http://127.0.0.1:8000/redoc


