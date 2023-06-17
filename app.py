# 导入Flask类
from flask import Flask

# 创建实例
# __name__：代表当前app.py这个模块
# 1.以后出现bug，他可以帮助我们快速定位
# 2.对于寻找模板文件，有一个相对路径

app = Flask(__name__)


# 创建一个路由和视图函数映射
@app.route('/')
def hello_word():
    return 'Hello'


# 1.debug模式
# 修改代码保存自动重新加载
    # 社区版 PYTHONUNBUFFERED=1;FLASK_DEBUG=1;FLASK_ENV=development;FLASK_APP=main.py
    # app.run(debug=True)
# 2.修改host:
# Additional options: --host=0.0.0.0
# 3.修改端口号:
# Additional options: --host=0.0.0.0 --port=8000

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8888')
