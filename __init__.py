from flask import Flask

app = Flask(__name__)

for url in urls : 
    app.add_url_rule(url[0], methods=url[1], view_func=url[2])

if __name__ == '__main__':
    app.run(debug=True)

