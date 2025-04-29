from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

# Görevleri yükleme veya yeni dosya oluşturma
def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            return json.load(file)
    return []

# Görevleri kaydetme
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

@app.route("/")
def index():
    tasks = load_tasks()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    tasks = load_tasks()
    task = request.form.get("task")
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    return redirect(url_for("index"))

@app.route("/complete/<int:task_id>")
def complete(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks[task_id]["completed"] = True
        save_tasks(tasks)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)