# learning-log

このリポジトリでは、日々の学習記録（SQL / Python / Git / ツール作成など）を残しています。  
目的は知識の定着と、成果物として副業・ポートフォリオへの活用です。

---

## 🛠 使用技術・環境

- macOS
- VS Code（エディタ）
- Git / GitHub
- XAMPP（MariaDB）
- Python 3.12.1
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
├── tools/                 # 自動化・ツール関連
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

## 学習記録やToDo

### 🗒️ 今後のToDo
```markdown
- [x] SQL環境構築
- [x] worldcup2014.sqlのインポート
- [ ] SQL文の実行練習
- [ ] PythonでDBアクセス
- [ ] 自動化スクリプト作成
```

