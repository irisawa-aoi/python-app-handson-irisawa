# カフェ注文シミュレーター

Python と Streamlit で動作する、ローカル環境向けのカフェ注文アプリです。ブラウン系テーマの画面でメニューをカード形式で表示し、カート追加・削除・全削除ができます。外部 API やデータベースは使用しません。

## 主な機能

- ブラウン系の配色テーマ（`.streamlit/config.toml` で永続適用）
- 商品カード表示（絵文字アイコン付き）
- スマートフォン幅でも崩れにくいレスポンシブレイアウト
- カート追加・商品ごとの削除・カート全削除
- 店名とキャッチコピーのヘッダー表示

## 店名・キャッチコピーの変更方法

`store_settings.toml` を編集すると、コードを書き換えずに表示名を変更できます。

```toml
store_name = "AOI CAFE"
tagline = "香りとくつろぎを、毎日の一杯に。"
```

変更後にアプリを再読み込み（または再起動）すると反映されます。

## Windows（PowerShell）

1. Python をインストールし、このリポジトリのフォルダーを PowerShell で開きます。
2. 仮想環境を作成して有効化します。

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

3. 依存パッケージをインストールします。

   ```powershell
   python -m pip install -r requirements.txt
   ```

4. アプリを起動します。

   ```powershell
   streamlit run app.py
   ```

## macOS

1. Python 3 をインストールし、ターミナルでこのリポジトリのフォルダーに移動します。
2. 仮想環境を作成して有効化します。

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. 依存パッケージをインストールします。

   ```bash
   python -m pip install -r requirements.txt
   ```

4. アプリを起動します。

   ```bash
   streamlit run app.py
   ```

起動後、ブラウザーに表示される画面で注文できます。仮想環境を終了するときは `deactivate` を実行してください。
