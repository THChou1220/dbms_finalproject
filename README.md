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

>啟動
```shell
python start.py
```
<br>

>(非必要) 另外開啟一個Terminal，執行以下指令
```shell
curl "http://localhost:5000"
```
>若 *StatusCode* 為 *200*，且 *Content* 為 *Hello World* 則表示成功執行
<br>

>(非必要) 在另外開啟的 *Terminal* 下進入 *backend*，執行以下指令:
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

### *Database*

- ***ER Model***

![ER Model](https://github.com/THChou1220/dbms_finalproject/blob/main/image/ER_Model.png)
<br>

- ***Relational Schema***

![Relational_Schema](https://github.com/THChou1220/dbms_finalproject/blob/main/image/Relational_Schema.png)
<br>

- ***Tables***

` Trainers `

| Atrribute | Type | |
| :--- | :--- | :--- |
| **T_ID** | Text | Primary key |
| T_Name | Text | |
| Email_ID | Text | Format: example@example&#8203;.com |
| Phone | Text | Format: xxxx-xxx-xxx |
| Gender | Text | Domain: Male, Female, Others |
| Hire_Date | Text | |
| Salary | Real | At least 50000 |

` Members `

| Atrribute | Type | |
| :--- | :--- | :--- |
| **Mem_ID** | Text | Primary key |
| M_Name | Text | |
| Phone | Text | Format: xxxx-xxx-xxx |
| Start_Date | Text | |
| Gender | Text | Domain: Male, Female, Others |
| *Subs* | Text | Foreign key <br> Not null |
| Height | Real |  |
| Weight | Real |  |
| Age | Integer |  |
| Email_ID | Text | Format: example@example&#8203;.com |
| *Trainer_ID* | Text | Foreign key <br> Not null |

` Subscriptions `

| Atrribute | Type | |
| :--- | :--- | :--- |
| **Sub_ID** | Text | Primary key |
| Price | Real | |
| Duration | Integer | At least 1 |
| Sub_Num | Integer | Default 0 |

` Equipments `

| Atrribute | Type | |
| :--- | :--- | :--- |
| **Eq_ID** | Text | Primary key |
| Name | Text | |
| Quantity | Integer | At least 1 |
| Cost | Real |  |

` Exercises `

| Atrribute | Type | |
| :--- | :--- | :--- |
| **EX_ID** | Text | Primary key |
| EX_Name | Text | |
| Type | Text | Domain: Upper Body, Lower Body, Arm |
| Time_Slot | Integer | Unit: minutes per time <br> At least 1 |
| Frequency | Integer | Unit: times per week <br> At least 1 |

` Use `

| Atrribute | Type | |
| :--- | :--- | :--- |
| ***Member_ID*** | Text | Primary key <br> Foreign key |
| ***Equipment_ID*** | Text | Primary key <br> Foreign key |

` Do `

| Atrribute | Type | |
| :--- | :--- | :--- |
| ***Member_ID*** | Text | Primary key <br> Foreign key |
| ***Exercise_ID*** | Text | Primary key <br> Foreign key |

` Consist `

| Atrribute | Type | |
| :--- | :--- | :--- |
| ***Sub_Pack*** | Text | Primary key <br> Foreign key |
| ***Exercise_ID*** | Text | Primary key <br> Foreign key |
