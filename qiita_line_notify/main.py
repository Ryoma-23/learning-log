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

# メイン処理
if __name__ == "__main__":
    tags = ["python", "AI"]  # 複数のタグを指定
    articles = get_qiita_articles(tags, 6)

    if not articles:
        print("記事が取得できませんでした。")
    else:
        message = ":memo: *Qiita新着記事（#python）*\n"
        for article in articles:
            message += f"\n• <{article['url']}|{article['title']}>"

        send_slack_notification(message, slack_webhook_url)
        print("Slack通知を送りました ✅")
