""" Basic logging setup for the application """
import os
import logging

logging.basicConfig(
    level=os.environ.get("LOGLEVEL", "INFO"),
    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s'
)
