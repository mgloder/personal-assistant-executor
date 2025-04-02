from celery import Celery
import os
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=os.getenv('LOG_LEVEL', 'INFO'),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Celery with environment variables
celery_app = Celery(
    'worker',
    broker=os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0'),
    backend=os.getenv('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')
)

# Celery configuration from environment variables
celery_app.conf.update(
    task_serializer=os.getenv('CELERY_TASK_SERIALIZER', 'json'),
    accept_content=[os.getenv('CELERY_ACCEPT_CONTENT', 'json')],
    result_serializer=os.getenv('CELERY_RESULT_SERIALIZER', 'json'),
    timezone=os.getenv('CELERY_TIMEZONE', 'UTC'),
    enable_utc=os.getenv('CELERY_ENABLE_UTC', 'True').lower() == 'true',
    task_track_started=os.getenv('CELERY_TASK_TRACK_STARTED', 'True').lower() == 'true',
    task_time_limit=int(os.getenv('CELERY_TASK_TIME_LIMIT', '1800')),
    worker_max_tasks_per_child=int(os.getenv('CELERY_WORKER_MAX_TASKS_PER_CHILD', '100')),
    worker_prefetch_multiplier=int(os.getenv('CELERY_WORKER_PREFETCH_MULTIPLIER', '1'))
)

# Log configuration
logger.info("Celery configuration loaded:")
logger.info(f"Broker URL: {celery_app.conf.broker_url}")
logger.info(f"Result Backend: {celery_app.conf.result_backend}")
logger.info(f"Timezone: {celery_app.conf.timezone}") 