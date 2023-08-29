import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    filename = "example.txt"
    logging.info(f"Opening file: {filename}")
    with open(filename, 'r') as file:
        content = file.read()
    logging.info("File content:\n" + content)
except FileNotFoundError:
    logging.error("File not found.")

# output
# 2023-08-29 11:10:24,590 - INFO - Opening file: example.txt
# 2023-08-29 11:10:24,592 - ERROR - File not found.