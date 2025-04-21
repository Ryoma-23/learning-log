# learning-log

このリポジトリでは、日々の学習記録（SQL / Python / Git / ツール作成など）を残しています。  
目的は知識の定着と、成果物として副業・ポートフォリオへの活用です。

---

## 🛠 使用技術・環境

- macOS
- VS Code（エディタ）
- Git / GitHub
- Github actions
- XAMPP（MariaDB）
- Python 3.11.7
- SQLTools（VS Code拡張機能）

---

## 📁 フォルダ構成

```
learning-log/
├── .vscode/               # VSCode関連
│   └── settings.json      # DB環境設定
├── sql/                   # SQL学習関連
│   ├── README.md          # 環境構築や操作手順など
│   ├── images/            # 画像保存場所
│   ├── query_practice.sql # 学習用スクリプト
│   ├── worldcup2014.sql   # テストデータ
│   └── ...
├── python/                # Pythonスクリプト
│   ├── script.py          # 学習用スクリプト
│   └── ...
├── qiita_line_notify/     # 自動化・ツール関連
│   ├── images/            # 画像保存場所
│   ├── venv/              # Python仮想環境フォルダ（ローカル実行用）
│   ├── .env               # 環境変数を定義
│   ├── main.py            # メインスクリプト
│   ├── notified_url.txt   # URL記録用（重複防止）
│   ├── README.md          # スクリプトの詳細解説
│   ├── requirements.txt   # 使用ライブラリを記載
│   └── ...
└── README.md              # このファイル
```

---

## 📝 Git 運用メモ

### 新しいファイルを追加したとき

```bash
git add .
git commit -m "ファイル追加：◯◯"
git push
```

### 特定ファイルだけを追加したいとき

```bash
git add ファイル名.sql
git commit -m "コメント"
git push
```
### 🔄 GitHub に push できないときの対処法メモ

例：GitHubで先にリポジトリ＋READMEを作って、ローカルと履歴が合わないとき
```bash
git pull origin main --no-rebase --allow-unrelated-histories
# マージ画面が出たら、コメントを残して :wq で抜ける
```

---

## 🔔 Qiita記事のSlack通知ツール（qiita_line_notify）

Qiitaの特定タグの新着記事を毎朝Slackに自動通知するスクリプトを作成しました。   
PythonによるAPI連携・通知処理・重複排除、さらにGitHub Actionsを活用して毎日20時に自動実行しています。

### 🧩 主な機能

- Qiita APIを使って特定タグの新着記事を取得

- SlackのIncoming Webhookで通知を送信

- 通知済みURLをファイルで管理し、重複を防止

- macOSのlaunchdを用いて、毎朝8時に自動実行（+手動実行も可能）

- GitHub Actionsで毎日20時に自動実行（+手動実行も可能）（ローカル依存をなくす）

### 🗂️ ディレクトリ構成（抜粋）
```bash
leaning-log/                # リポジトリ
├── .github/workflows/
│   └── notify.yml          # GitHub Actionsの設定ファイル
└── qiita_line_notify/
    ├── main.py             # 通知処理のメインスクリプト
    ├── requirements.txt    # 使用ライブラリ
    └── README.md           # スクリプトの詳細解説
```

---

## 学習記録やToDo

### 🗒️ 今後のToDo
```markdown
- [x] SQL環境構築
- [x] worldcup2014.sqlのインポート
- [x] Qiita通知スクリプトの作成
- [x] Slack通知の自動化（GitHub Actions）
- [ ] PythonでDBアクセス
```
