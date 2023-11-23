from pydantic import BaseModel

POST_DB = {}


class Post(BaseModel):
    id: str
    title: str
    text: str
    author: str


class BlogService:
    def add_post(self, new_post: Post) -> None:
        POST_DB[new_post.id] = new_post
