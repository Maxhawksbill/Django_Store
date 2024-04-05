"""gunicorn WSGI server configuration."""
from multiprocessing import cpu_count


def max_workers():
    return 2 * cpu_count() + 1


# bind = '0.0.0.0:' + environ.get('PORT', '8000')
max_requests = 5
workers = 1
threads = 2 * cpu_count()

# Max parallel requests per worker
worker_connections = 1000

# Worker type gevent
worker_class = 'gevent'
