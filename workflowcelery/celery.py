from celery import Celery

import workflowcelery.config as CeleryConfig  

app = Celery()
app.config_from_object(CeleryConfig) # Can be class or module

if __name__ == '__main__':
    app.start()