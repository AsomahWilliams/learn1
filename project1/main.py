from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Sample data
all_todos = [
    {'todos_id': 1, 'todos_name': 'Sports', 'todos_description': 'Go to the gym'},
    {'todos_id': 2, 'todos_name': 'Read', 'todos_description': 'Read 10 pages'},
    {'todos_id': 3, 'todos_name': 'Shop', 'todos_description': 'Go shopping'},
    {'todos_id': 4, 'todos_name': 'Study', 'todos_description': 'Study for exams'},
    {'todos_id': 5, 'todos_name': 'Meditate', 'todos_description': 'Meditate for 20 minutes'}
]

# Pydantic model for the Todo item
class TodoCreate(BaseModel):
    todos_name: str
    todos_description: str


class TodoUpdate(BaseModel):
    todos_name: str
    todos_description: str


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo['todos_id'] == todo_id:
            return {'result': todo}
    raise HTTPException(status_code=404, detail="Todo not found")


@app.get("/todos")
def get_todos(first_n: int = None):
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos


@app.post('/todos', response_model=dict)
def create_todo(todo: TodoCreate):
    new_todo_id = (max(item['todos_id'] for item in all_todos) + 1) if all_todos else 1
    new_todo = {
        'todos_id': new_todo_id,
        'todos_name': todo.todos_name,
        'todos_description': todo.todos_description
    }
    all_todos.append(new_todo)
    return new_todo


@app.put("/todos/{todo_id}", response_model=dict)
def update_todo(todo_id: int, updated_todo: TodoUpdate):
    for todo in all_todos:
        if todo['todos_id'] == todo_id:  # Corrected key name
            todo['todos_name'] = updated_todo.todos_name
            todo['todos_description'] = updated_todo.todos_description
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")  # Raise exception if not found


@app.delete("/todos/{todo_id}", response_model=dict)
def delete_todo(todo_id: int):
    for index, todo in enumerate(all_todos):
        if todo['todos_id'] == todo_id:  # Corrected key name
            deleted_todo = all_todos.pop(index)
            return deleted_todo
    raise HTTPException(status_code=404, detail="Todo not found")  # Raise exception if not found
