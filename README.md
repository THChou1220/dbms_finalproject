# dbms_finalproject

## 題目: 健身房會員管理系統
   Database: **SQLite** <br>
   Back-End Framework: **Python - Flask** <br>
   Front-End Framework: **JavaScript - React**

### *Pre-Start*
  至 https://sqlite.org/download.html 下載SQLite

### *Start*

* 啟動 *Back-End* 

>進入 *backend*
```shell
cd backend
```
<br>

>安裝需要的套件
```shell
pip install -r requirements.txt --user
```
<br>

>建立資料庫
```shell
python database.py
```
<br>

>執行 *app.py*
```shell
python app.py
```
<br>

>另外開啟一個Terminal，執行以下指令
```shell
curl "http://localhost:5000"
```
>若 *StatusCode* 為 *200*，且 *Content* 為 *Hello World* 則表示成功執行
<br>

>在另外開啟的 *Terminal* 下進入 *backend*，執行以下指令:
```shell
python data.py
```
>即能將預先設定好的資料輸入進資料庫中
<br>

* 啟動 *Front-End*

>進入 *frontend*
```shell
cd frontend
```
<br>

>安裝需要的套件
```shell
npm install
```
<br>

>啟動
```shell
npm start
```
