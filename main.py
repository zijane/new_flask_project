from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

def get_search_results(q):
    if q == "cat":
        result = ["mice", "Tom"]
    else:
        result = ["Jerry"]
    return result

@app.route('/api/search', methods=["get", "post"])
def api_search():
    q = request.values.get("q", "")
    result = get_search_results(q)
    return jsonify({'results': result})

@app.route('/search', methods=["get", "post"])
def search():
    q = request.values.get("q", "")
    print(q)
    result = get_search_results(q)
    return render_template("search.html", q=q, result=result)


if __name__ == '__main__':
    app.run(debug=True)
