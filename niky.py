# create a FastAPI CODE
from fastapi import FastAPI

app = FastAPI()

## end point test we pass some value inside get
#@app.get("/")
# # return {"message": "Welcome to digital World"}
# for get input from user using GET method
@app.get("/welcome/{my_query}")
def home(my_query):
     return {"message":"Welcome to digital World","user_input":my_query}
#def home(my_query, qr:Optional[str]=None):
   