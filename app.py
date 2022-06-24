from flask import Flask, render_template

app = Flask(__name__) # объявим экземпляр фласка

#
# @app.route('/')
# def render_main():
# 	return 'Здесь будет главная'
#
#
# @app.route('/products/')
# def render_products():
# 	return 'Продукты'
#
#
# @app.route('/videos/<video_id>/')
# def render_videos_item(video_id):
# 	return "Здесь будет видео " + video_id
#
#
# # @app.route('/book/<author>/<title>/')
# # def render_book(author, title):
# # 		return "Здесь будет страница книги " + title + " автора " + author
#
#
# @app.route('/book/<book_id>/')
# def render_book(book_id):
# 	print(type(book_id))
# 	return "хуй"
#
#
# @app.errorhandler(404)
# def render_server_error(error):
# 	return "Что-то не так, но мы все починим:\n{}".format(error), 404
#
#
# @app.route("/example/")
# def render_example():
# 	return "<h2>Привет, я функция Example </h2>"


# @app.route('/')
# def temlate():
# 	name = "Alex"
# 	place = "Lab"
# 	output = render_template('test.html', name = name, place = place )  # рендерим шаблон, передавая переменныеreturn output
# 	return output


@app.route('/')
def main():
    return render_template('index.html')


# @app.route('/about/<int:id_students>')
# def about(id_students):
#     student = {
#         1: "Oleg",
#         2: "Anton",
#         3: "Alex"
#     }
#     student_name = student.get(id_students)
#     return render_template('about.html', student_name = student_name)


# @app.route('/about/')
# def about():
#     student = {
#         1: "Oleg",
#         2: "Anton",
#         3: "Alex"
#     }
#     return render_template('about.html', student = student)


@app.route('/about/')
def about():
    return render_template('about.html', user={"name": "alex"}, online=True, notifications={"friends":43, "messages":177, "calls":4},)




app.run()



