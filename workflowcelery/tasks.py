from workflowcelery.celery import app

@app.task
def add_task(*args):
    return sum(args)

@app.task
def multiply_task(*args):
    value = 1
    for arg in args:
        value = value * arg
    return value

@app.task
def add_group_task(tasks):
    return sum(tasks)