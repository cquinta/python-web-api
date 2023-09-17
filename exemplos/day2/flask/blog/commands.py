import click
from blog.posts import (
    get_all_posts,
    get_post_by_slug,
    update_post_by_slug,
    new_post,
)

@click.group()
def post():
    """
    Manage blog posts
    """
@post.command()
    
@click.option("--title")
@click.option("--content")
def new(title, content):
    """Add new post to the database"""
    new=(new_post(title, content))
    click.echo(f"New post created with slug: {new}")

@post.command("list")
def _list():
    """List all posts"""
    posts = get_all_posts()
    for post in posts:
        click.echo(post)

@post.command()
@click.argument("slug")
def get(slug):
    """Get post by slug"""
    post = get_post_by_slug(slug)
    if post:
        click.echo(post)
    else:
        click.echo(f"Post with slug {slug} not found")


@post.command()
@click.argument("slug")
@click.option("--content", type=str, default=None)
@click.option("--published", type=str, default=None)
def update(slug,content,published):
    data = {}
    """Update post by slug"""
    if content is not None:
        data["content"] = content
    if published is not None:
        data["published"] = published
    
    post = update_post_by_slug(slug, data)
    click.echo(f"{post['title']} - {post['slug']} - updated")

# TODO criar opção de despublicar.

def configure(app):
    app.cli.add_command(post)
