from .celery_app import celery_app
import time
import logging

logger = logging.getLogger(__name__)

@celery_app.task(name='process_message')
def process_message(message):
    """
    Process a message from the queue
    """
    logger.info(f"Processing message: {message}")
    # Simulate some work
    time.sleep(2)
    logger.info(f"Completed processing message: {message}")
    return f"Processed: {message}"

@celery_app.task(name='handle_error')
def handle_error(message, error):
    """
    Handle error messages from the queue
    """
    logger.error(f"Error processing message: {message}, Error: {error}")
    return f"Error handled for: {message}" 