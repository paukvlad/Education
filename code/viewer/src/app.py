import sys
sys.path.append('/Users/studio/Work/Projects/Education/code/')

from flask import Flask
from views import index, search_urls, about

app = Flask(__name__, template_folder='../templates', static_folder='../static')

app.add_url_rule('/about', view_func=about, methods=["GET"])
app.add_url_rule('/', view_func=index, methods=["GET", "POST"])
app.add_url_rule('/search-urls', view_func=search_urls, methods=["GET"])


if __name__ == "__main__":
    app.run(debug=True)
