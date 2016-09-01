BROKER_URL = 'amqp://celery:xBWsncGUD414@172.17.0.1:5672/celerydemo'
CELERY_BACKEND = 'db+postgresql://celery:S96Pf0TdVz4g@172.17.0.1:5432/celerydemo'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_IMPORTS = (
    'workflowcelery.tasks'
)