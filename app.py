from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Todo.db"
db = SQLAlchemy(app)


class Todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


@app.get("/")
def todos():
    todos_list = []
    todos = Todos.query.order_by(Todos.date_created).all()

    for h in todos:
        todos_list.append(Todos.as_dict(h))

    return todos_list


@app.post("/")
def index():
    content = request.get_json()["content"]

    new_hist = Todos(content=content)
    db.session.add(new_hist)
    db.session.commit()

    return "todo added"


@app.delete("/delete/<int:id>")
def delete(id):
    task_to_delete = Todos.query.get_or_404(int(id))
    print(task_to_delete)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return "todo deleted"
    except:
        return "There was a problem deleting that Todo"


@app.delete("/clear")
def clear():
    hist = Todos.query.all()
    for h in hist:
        db.session.delete(h)
    db.session.commit()
    return "all clear"
