from blog.database import mongo
import pymongo
from datetime import datetime


def get_all_posts(published=True):
    posts = mongo.db.posts.find({"published": published})
    return posts.sort("date", pymongo.DESCENDING)


def get_post_by_slug(slug: str) -> dict:
    post = mongo.db.posts.find_one({"slug": slug})
    return post


def update_post_by_slug(slug: str, data: dict) -> dict:
    # TODO: check if slug already exists
    post = mongo.db.posts.find_one_and_update(
        {"slug": slug}, {"$set": data}, return_document=True
    )
    return post


def new_post(title: str, content: str, published: bool = True) -> str:
    slug = title.replace(" ", "-").replace("_", "-").lower()
    # TODO: check if slug already exists
    # TODO: remove special characters (acentos)
    # TODO: não deixar o slug ser "new" para não conflitar com a rota.
    mongo.db.posts.insert_one(
        {
            "title": title,
            "content": content,
            "published": published,
            "slug": slug,
            "date": datetime.now(),
        }
    )
    return slug
