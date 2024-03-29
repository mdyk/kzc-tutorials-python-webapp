from fastapi import FastAPI
from service import BlogService, Post

app = FastAPI()

blog_service = BlogService()


@app.post("/blog/posts")
def create_new_post(new_post: Post):
    blog_service.add_post(new_post)


@app.get("/blog/posts")
def get_all_posts():
    return blog_service.get_all_posts()
