import tkinter as tk

class SearchEngineApp:
    def __init__(self, root, documents):
        self.root = root
        self.root.title("検索エンジン")
        self.documents = documents

        self.create_widgets()

    def create_widgets(self):
        # 検索バーの作成
        self.search_entry = tk.Entry(self.root, width=40)
        self.search_entry.grid(row=0, column=0, padx=10, pady=10)

        # 検索ボタンの作成
        self.search_button = tk.Button(self.root, text="検索", command=self.search)
        self.search_button.grid(row=0, column=1, padx=10, pady=10)

        # 検索結果表示用のテキストボックスの作成
        self.results_text = tk.Text(self.root, width=50, height=10, wrap="word")
        self.results_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    def search(self):
        query = self.search_entry.get()
        search_results = self._search(query)

        self.display_results(search_results)

    def _search(self, query):
        results = []
        for doc in self.documents:
            if query.lower() in doc["text"].lower():
                results.append(doc)
        return results

    def display_results(self, search_results):
        self.results_text.delete(1.0, tk.END)
        if search_results:
            for result in search_results:
                text = f"ID: {result['id']}, Text: {result['text']}\n"
                self.results_text.insert(tk.END, text)
        else:
            self.results_text.insert(tk.END, "検索結果はありません。")

# サンプルの文章データ
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

if __name__ == '__main__':
    root = tk.Tk()
    search_app = SearchEngineApp(root, documents)
    root.mainloop()
