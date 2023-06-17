# 导入Flask类
from flask import Flask, request, render_template

# 创建实例
# __name__：代表当前app.py这个模块
# 1.以后出现bug，他可以帮助我们快速定位
# 2.对于寻找模板文件，有一个相对路径

app = Flask(__name__)


# 创建一个路由和视图函数映射
@app.route('/hello')
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


# 可使用类型：
# string
# int
# float
# path
# uuid
# any
@app.route("/user/<int:user_id>")
def user_detail(user_id):
    return 'userID为' + user_id


# 可选参数
@app.route('/url/list')
def url_list():
    # arguments:参数
    # args:类字典
    page = request.args.get('page', default=1, type=int)
    return f"url_page{page}"


# 渲染html模板
@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/blog/<blog_id>')
def blog(blog_id):
    return render_template('blog.html', blog_id=blog_id)

# 过滤器
@app.route('/filter')
def filterer():
    user = {'uname': 'ljk11', 'email': '123@qq.com'}
    return render_template('filter.html', user=user)

# 控制语句

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8888')
