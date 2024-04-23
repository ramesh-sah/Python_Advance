from fastapi import FastAPI ,Path
import uvicorn



app = FastAPI()

@app.get('/')
def home():
    return "This is the home page"

@app.get("/hello")
async def hello():
    return "Hello World"

@app.get("/hello/{name}")
async def hello_name(name:str):
    return f"Hello {name}"

@app.get("/query")
async def query_func(name:str , roll_no=int):
    var_name = {"Name:":name,"Roll No:":roll_no} 
       
    
    


if __name__=='__main__':
   
    uvicorn.run(app,host='127.0.0.1',port=8000)