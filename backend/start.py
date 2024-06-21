import os

cmd = 'pip install -r requirements.txt --user'
os.system(cmd)

cmd = 'python database.py'
os.system(cmd)

cmd = 'python app.py'
os.system(cmd)