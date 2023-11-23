from fastapi import FastAPI
from service import BlogService, Post

app = FastAPI()

blog_service = BlogService()


# """
# {
#     "title" : "",
#     "text": "",
#     "author": ""
# }

# """


@app.post("/blog/post")
def create_new_post(new_post: Post):
    blog_service.add_post(new_post)
