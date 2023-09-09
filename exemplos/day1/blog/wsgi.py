import cgi
from pathlib import Path
from database import conn

def get_posts_from_database(post_id=None):
    cursor = conn.cursor()
    fields = ["id", "title", "content", "author"]
    if post_id:
        results = cursor.execute(f"SELECT * FROM posts WHERE id = ?;", (post_id,))
    else:
        results = cursor.execute("SELECT * FROM posts;")
    return [dict(zip(fields, row)) for row in results]


def render_template(template_name, **context):
    template = Path(template_name).read_text()
    return template.format(**context).encode("utf-8")


def get_post_list(posts):
    post_list = [
        f"""<li><a href="/{post['id']}">{post['title']}</a></li>""" for post in posts
    ]
    return "\n".join(post_list)


def add_new_post(post):
    cursor = conn.cursor()
    cursor.execute(
        """\
            INSERT INTO posts (title, content, author) 
            values(:title, :content, :author)
        """,
        post,
    )
    conn.commit()


def application(environ, start_response):
    body = b"Content Not Found"
    status = "404 Not Found"
    path = environ.get("PATH_INFO")
    method = environ.get("REQUEST_METHOD")

    # Roteamento de URLs
    if path == "/" and method == "GET":
        posts = get_posts_from_database()
        body = render_template("list.template.html", post_list=get_post_list(posts))
        status = "200 OK"
    elif path.split("/")[-1].isdigit() and method == "GET":
        post_id = path.split("/")[-1]
        body = render_template(
            "post.template.html", post=get_posts_from_database(post_id=post_id)[0]
        )
        status = "200 OK"
    elif path == "/new" and method == "GET":
        body = render_template("form.template.html")
        status = "200 OK"
    elif path == "/new" and method == "POST":
        form = cgi.FieldStorage(
            fp=environ["wsgi.input"], environ=environ, keep_blank_values=True
        )
        post = {item.name: item.value for item in form.list}
        add_new_post(post)
        body = b"New post created with success"
        status = "201 Created"

    headers = [("Content-type", "text/html")]
    start_response(status, headers)
    return [body]
