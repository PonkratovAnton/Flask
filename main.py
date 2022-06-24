import flask
main = flask.Flask(__name__)


# @main.route('/book/<book_id>/')
# def render_book(book_id):
#     print(type(book_id))
#     return ''


@main.route('/book/<int:book_id>/')
def render_book(book_id):
    print(type(book_id))
    return ""


@main.errorhandler(500)
def render_server_error(error):
    return "Что-то не так, но мы все починим", 500

