import datetime

from fastapi import FastAPI

from clients.comment_creator import CommentCreator
from clients.post_creator import PostCreator

app = FastAPI()


@app.get("/health")
def health():
    return "Ok"


# create comments macro of sudden attack radio
@app.get("/comments")
async def create_comments_macro():
    comment_creator = CommentCreator()
    end_time = datetime.datetime.now() + datetime.timedelta(minutes=5)  # executes for 5 minutes
    await comment_creator.execute_until(end_time)


# create posts macro of sudden attack radio
@app.post("/posts")
async def create_posts_macro():
    await PostCreator.main()
