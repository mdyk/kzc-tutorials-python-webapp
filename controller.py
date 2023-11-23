from fastapi import FastAPI


app = FastAPI()


@app.post("/blog/post")
def create_new_post(title: str, post_text: str):
    pass
