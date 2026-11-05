# Week 1.7, Session 2: Task 2 - logging

import logging

def calculate_average(scores):
    # add logging configuration    
    logging.basicConfig(filename='log.txt', filemode='w', level=logging.DEBUG)
    
    # you can turn the logging off
    # logging.disable(logging.CRITICAL)
    
    logger = logging.getLogger()
    logger.info(f"calculate_average(): started")
    
    total_score = sum(scores)
    total_assignments = len(scores)
    
    # add debug logging here
    
    average = total_score // total_assignments
    
    # add a debug logging here
    
    return round(average,2)

print(calculate_average([85, 90, 88]))
# Expected Output: 87.67
# Actual Output:   87.0