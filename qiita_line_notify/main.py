import requests # type: ignore
import os
import re
from dotenv import load_dotenv # type: ignore
from datetime import datetime, timedelta

load_dotenv()
slack_webhook_url = os.getenv("SLACK_WEBHOOK_URL")

# Qiita APIから記事取得
def get_qiita_articles(tag="python", per_page=3):
    url = f"https://qiita.com/api/v2/tags/{tag}/items"
    params = {"per_page": per_page}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"エラー ({tag}) : {response.status_code}")
        return []

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
            return set(
                line.strip()
                for line in file
                if line.strip() and not line.startswith("##")
            )
    return set()

# 新しく通知すべき記事と、通知済み記事を判別
def filter_new_articles(articles, notified_urls):
    new_articles = []
    new_urls = []
    for article in articles:
        if article["url"] not in notified_urls:
            new_articles.append(article)
            new_urls.append(article["url"])
    return new_articles, new_urls

# 新たに通知したURLを日付付きでファイルに追記する
def save_notified_urls_with_date(urls, file_path="notified_urls.txt"):
    if not urls:
        return

    today_str = datetime.now().strftime("%Y-%m-%d")
    dated_block = f"## {today_str}\n" + "\n".join(urls) + "\n"

    # 1. 既存内容を読み込む
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            existing_data = file.read()
    else:
        existing_data = ""

    # 2. 既存内容に追加（同日重複防止）
    if f"## {today_str}" in existing_data:
        # 同日ブロックがある場合は追記せずスキップ（または上書きしたければ調整）
        return

    new_data = existing_data + "\n" + dated_block

    # 3. 古いデータを削除（7日より前のブロックを削除）
    new_data = remove_old_blocks(new_data, keep_days=7)

    with open(file_path, "w") as file:
        file.write(new_data.strip() + "\n")

# 過去履歴を削除
def remove_old_blocks(text, keep_days=7):
    blocks = re.findall(r"(## (\d{4}-\d{2}-\d{2})\n(?:[^\#]*?))(?=(?:## |\Z))", text, re.MULTILINE)
    today = datetime.now().date()
    kept_blocks = []

    for block, date_str in blocks:
        try:
            block_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            if (today - block_date).days <= keep_days:
                kept_blocks.append(block.strip())
        except ValueError:
            continue  # 日付が壊れてたらスキップ

    return "\n\n".join(kept_blocks)

# メイン処理
if __name__ == "__main__":
    # 複数のタグを指定
    tags = ["python", "AI"]
    
    # 通知済みURLを読み込む
    notified_urls = load_notified_urls()

    all_new_urls = []
    slack_message = ""

    for tag in tags:
        articles = get_qiita_articles(tag, 5)
        
        # 新しい記事と通知済みURLを分ける
        new_articles, new_urls = filter_new_articles(articles, notified_urls)

        if new_articles:
            slack_message += f":label: *#{tag} の新着記事*\n"
            for article in new_articles:
                slack_message += f"• <{article['url']}|{article['title']}>\n"
            all_new_urls.extend(new_urls)
        else:
            slack_message += f":label: *#{tag} の新規記事はありませんでした。*\n"
    
    if slack_message:
        send_slack_notification(slack_message.strip(), slack_webhook_url)
        print("Slack通知を送りました ✅")
    
    if all_new_urls:
        save_notified_urls_with_date(all_new_urls)
