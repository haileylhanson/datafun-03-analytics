"""
This file fetches a CSV file from a url and saves it to a local file named penguins.csv in a folder named downloaded_data.
"""

#####################################
# Imported Modules
#####################################

# Import from Python Standard Library
import pathlib
import sys

# Import from external packages
import requests

# Ensure project root is in sys.path for local imports
sys.path.append(str(pathlib.Path(__file__).resolve().parent))

# Import local modules
from utils_logger import logger

#####################################
# Global Variables
#####################################

FETCHED_DATA_DIR = "downloaded_data"

#####################################
# Functions
#####################################

def fetch_csv_file(folder_name: str, filename: str, url: str) -> None:
    #Fetch CSV data from the given URL and write it to a file.
    
    try:
        logger.info(f"Fetching CSV data from {url}...")
        response = requests.get(url)
        response.raise_for_status()
        write_csv_file(folder_name, filename, response.text)
        logger.info(f"SUCCESS: CSV file fetched and saved as {filename}")
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        logger.error(f"Request error occurred: {req_err}")

def write_csv_file(folder_name: str, filename: str, string_data: str) -> None:
    #Write CSV data to a file.
    
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        logger.info(f"Writing CSV data to {file_path}...")
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open('w') as file:
            file.write(string_data)
        logger.info(f"SUCCESS: CSV data written to {file_path}")
    except IOError as io_err:
        logger.error(f"Error writing CSV data to {file_path}: {io_err}")

#####################################
# main() function
#####################################

def main():
    """
    Main function to demonstrate fetching CSV data showing size measurements of penguins on 3 different islands in Palmer Archipelago, Antarctica 
    """
    csv_url = 'https://raw.githubusercontent.com/MainakRepositor/Datasets/refs/heads/master/penguins_size.csv'
    logger.info("Starting CSV fetch demonstration...")
    fetch_csv_file(FETCHED_DATA_DIR, "penguins.csv", csv_url)

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()