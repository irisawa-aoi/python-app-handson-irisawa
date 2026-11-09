# カフェ注文シミュレーター

Python と Streamlit で動作する、ローカル環境向けの簡単なカフェ注文アプリです。メニューから商品を選び、カートに追加すると合計金額を確認できます。外部 API やデータベースは使用しません。

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
