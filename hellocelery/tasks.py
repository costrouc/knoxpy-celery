from hellocelery.celery import app

@app.task
def hello_celery():
    return "Hello Celery!"