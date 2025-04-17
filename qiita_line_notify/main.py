import requests
import os
from dotenv import load_dotenv

load_dotenv()
slack_webhook_url = os.getenv("SLACK_WEBHOOK_URL")

# Qiita APIから記事取得
def get_qiita_articles(tags=["python"], per_page=3):
    articles = []  #タグをリストとして取得
    for tag in tags:
        url = f"https://qiita.com/api/v2/tags/{tag}/items"
        params = {"per_page": per_page}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            articles.extend(response.json())
        else:
            print(f"エラー: {response.status_code} for tag {tag}")
    return articles

# Slackにメッセージ送信
def send_slack_notification(message, webhook_url):
    payload = {
        "text": message
    }
    response = requests.post(webhook_url, json=payload)
    if response.status_code != 200:
        print("Slack通知失敗:", response.text)

# 以前通知したURLをファイルから読み込む
def load_notified_urls(file_path="notified_urls.txt"):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return set(line.strip() for line in file)
    return set()

# 新たに通知したURLをファイルに追記する
def save_notified_urls(urls, file_path="notified_urls.txt"):
    with open(file_path, "a") as file:
        for url in urls:
            file.write(url + "\n")

# 新しく通知すべき記事と、通知済み記事を判別
def filter_new_articles(articles, notified_urls):
    new_articles = []
    new_urls = []
    for article in articles:
        if article["url"] not in notified_urls:
            new_articles.append(article)
            new_urls.append(article["url"])
    return new_articles, new_urls

# メイン処理
if __name__ == "__main__":
    tags = ["python", "AI"]  # 複数のタグを指定
    articles = get_qiita_articles(tags, 3)

    # 通知済みURLを読み込む
    notified_urls = load_notified_urls()

    # 新しい記事と通知済みURLを分ける
    new_articles, new_urls = filter_new_articles(articles, notified_urls)

    if not new_articles:
        print("記事が取得できませんでした。")
    else:
        message = ":memo: *Qiita新着記事（#python）*\n"
        for article in new_articles:
            message += f"\n• <{article['url']}|{article['title']}>"

        send_slack_notification(message, slack_webhook_url)
        print("Slack通知を送りました ✅")

        # 新しいURLを保存
        save_notified_urls(new_urls)
