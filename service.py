from pydantic import BaseModel


class Post(BaseModel):
    id: str
    title: str
    text: str
    author: str


class BlogService:
    def __init__(self):
        self.POST_DB = {}

    def add_post(self, new_post: Post) -> None:
        self.POST_DB[new_post.id] = new_post

    def get_all_posts(self):
        return self.POST_DB
