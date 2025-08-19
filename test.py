# SLNP 
# FAST API
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

user_db = {

    1: {"name": "Abhishek", "Surname": "Hukkerikar"},
    2: {"name": "Vikas", "Surname": "Joshi"}, 
    3: {"name": "Vidyarthi", "Surname": "Vidyarthi"}
}

class User(BaseModel): 
    name: str
    surname: str

@app.get("/addition")

def addition(a:float, b:float) -> float: 
    result_add = a + b
    return (result_add)
    
    
@app.post("/substract")
def substraction(a:float, b:float) ->float: 
    result_sub = (a - b)
    return(result_sub)

@app.put("/update")
def user_data_update(user_id: int, user:User):
    if user_id in user_db:
        user_db[user_id] = user.dict()
        print(user_db)
        return {f"User data updated successfully for {user_id}"}
    else: 
        return {f"Unable to update the data for {user_id}"}

@app.delete("/erase")    
def del_data(user_id: int): 
    try: 
        if user_id in user_db:
            del user_db[user_id]
            return {f"Successfully deleted the details of {user_id}"}
        else: 
            return {f"Data not found for {user_id}"}
    except Exception as e: 
        print(str(e))


