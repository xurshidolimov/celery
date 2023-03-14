from config.celery import app

@app.task()
def slow(num):
    for i in range(num):
        print(i)
