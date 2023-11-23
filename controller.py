from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    text: str
    author: str


# """
# {
#     "title" : "",
#     "text": "",
#     "author": ""
# }

# """


@app.post("/blog/post")
def create_new_post(new_post: Post):
    pass
