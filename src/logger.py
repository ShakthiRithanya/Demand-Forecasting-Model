import logging
import sys
import os

def setup_logger(name, log_file, level=logging.INFO):
    """Function setup as many loggers as you want"""
    
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s: %(message)s')

    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    logger.addHandler(console_handler)

    return logger

# Create logs directory
os.makedirs('logs', exist_ok=True)

# Main project logger
logger = setup_logger('demand_forecasting', 'logs/project.log')
