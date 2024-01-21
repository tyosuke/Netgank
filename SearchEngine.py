from flask import Flask, request

app = Flask(__name__)

class SearchEngine:
    def __init__(self, documents):
        self.documents = documents

    def search(self, query):
        results = []
        for doc in self.documents:
            if query.lower() in doc["text"].lower():
                results.append(doc)
        return results

# Sample document data
documents = [
    {
        "id": 1,
        "text": "Pythonは汎用の高水準言語です。"
    },
    {
        "id": 2,
        "text": "検索エンジンは情報を検索するためのツールです。"
    },
    {
        "id": 3,
        "text": "人工知能はコンピュータによる知的な振る舞いを実現する技術です。"
    },
    {
        "id": 4,
        "text": "Web開発では、HTML、CSS、JavaScriptなどの技術が使われます。"
    },
    {
        "id": 5,
        "text": "データサイエンティストはデータから有益な情報を引き出す専門家です。"
    }
]

search_engine = SearchEngine(documents)

@app.route("/", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        query = request.form["query"]
        search_results = search_engine.search(query)
        if not search_results:
            return "検索結果はありません。"
        else:
            result_text = "\n".join([f"ID: {result['id']}, Text: {result['text']}" for result in search_results])
            return result_text
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>検索エンジン</title>
    </head>
    <body>
        <h1>検索エンジン</h1>
        <form method="POST">
            <label for="query">検索キーワード:</label>
            <input type="text" name="query" id="query" required>
            <input type="submit" value="検索">
        </form>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
