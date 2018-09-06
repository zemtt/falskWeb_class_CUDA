#coding:utf-8

from flask import Flask, render_template, request
from classData import search_class, add_class, del_class, change
app = Flask(__name__)

# 主页
@app.route('/search')
@app.route('/')
def index():
    return render_template('index.html')

# 前端课程搜索展示页面
@app.route('/search',methods = ['POST'])
def search():
    try:
        school = request.form['school']
    except:
        school = ''
    try:
        name = request.form['class']
    except:
        name = ''
    class_data = search_class(school, name)
    return render_template('search.html', class_data=class_data)

# 课程添加接口
@app.route('/add',methods = ['GET', 'POST'])
def add():
    try:
        if request.method == 'GET':
            return render_template('add.html')
        else:
            if not(request.form['school'] and request.form['class'] and request.form['date']):
                raise EOFError
            add_class(request.form['school'], request.form['class'], request.form['date'])
            return render_template('warning.html',info=u'添加成功!', back='add')
    except:
        return render_template('warning.html',info=u'信息不全!', back='add')

# 课程处理接口
@app.route('/operator',methods = ['POST'])
def operator():
    # 接受课程更改信息，实现课程更改
    if request.form['oper'] == 'change':
        change(request.form['oschool'],request.form['oclass'],request.form['odate'],
            request.form['school'],request.form['class'],request.form['date']
        )
        return render_template('warning.html',info=u'修改成功!', back='search')
    
    # 接受课程更改信息，返回更改页面
    if request.form['oper'] == u'修改':
        class_data = [request.form['school'], request.form['class'], request.form['date']]
        return render_template('change.html', class_data=class_data)
    
    # 接受课程删除信息，实现课程删除
    if request.form['oper'] == u'删除':
        del_class(request.form['school'], request.form['class'], request.form['date'])
        return render_template('warning.html',info=u'删除成功!', back='search')

# 其他信息
@app.route('/info')
def info():
    return render_template('info.html')

if __name__ == '__main__':
    app.run(debug=True,port=80,host='0.0.0.0')
