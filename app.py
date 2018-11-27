# encoding: utf-8


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)


db.create_all()


@app.route('/')
def hello_world():
    # # 增加:
    # article1 = Article(title='article1', content='there is content')
    # db.session.add(article1)
    # # 事务:
    # db.session.commit()

    # 查
    # select * from article where title = 'article1';
    # result = Article.query.filter(Article.title == 'article1').first()
    # print 'tittle %s' % result.title
    # print 'content %s' % result.content

    # # 改
    # # 1. 先把你要更改的数据查找出来
    # article = Article.query.filter(Article.title == 'article1').first()
    # # 2. 把这条数据你要修改的地方进行修改
    # article.title = 'new title'
    # # 3. 做事务提交
    # db.session.commit()

    # # 删
    # # 1. 把需要删除的数据找出来
    # article = Article.query.filter(Article.title == 'new title').first()
    # # 2. 把这条数据删除
    # db.session.delete(article)
    # # 3. 做事务提交
    # db.session.commit()

    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
