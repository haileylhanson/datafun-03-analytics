"""
Process a CSV file on 2020 Happiness ratings by country to analyze the `Ladder score` column and save statistics.
"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import csv
import statistics
import sys

# Ensure project root is in sys.path for local imports
sys.path.append(str(pathlib.Path(__file__).resolve().parent))

# Import local modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

# TODO: Replace with the names of your folders
FETCHED_DATA_DIR: str = "downloaded_data"
PROCESSED_DIR: str = "downloaded_data_processed"

#####################################
# Define Functions
#####################################

# TODO: Add or replace this with a function that reads and processes your CSV file

def analyze_penguin_body_mass(file_path: pathlib.Path) -> dict:
    """Analyze the body mass of the penguins to see which island has the largest and the smallest penguins"""
    try:
        # initialize an empty list to store the body masses
        bm_list = []
        with file_path.open('r') as file:
            # csv.DictReader() methods to read into a DictReader so we can access named columns in the csv file
            dict_reader = csv.DictReader(file)  
            for row in dict_reader:
                try:
                    bm = row["body_mass_g"]
                    if bm == "NA":
                        pass
                    else:
                        bm = float(bm)
                        bm_list.append(bm)
                except ValueError as e:
                    logger.warning(f"Skipping invalid row: {row} ({e})")
        
        '''for val in bm_list:
            print(f"body mass list item = {val}\n")
            print(f"body mass list item type = {type(val)}\n")
        '''
        #print(bm_list)

        # Calculate statistics
        bm_dict = {
            "min": min(bm_list),
            "max": max(bm_list),
            "mean average": statistics.mean(bm_list)
        }
        return bm_dict
    
    except Exception as e:
        logger.error(f"Error processing CSV file: {e}")
        return {}

def process_csv_file():
    """Read a CSV file, analyze Body Mass in grams and save the results."""
    
    input_file = pathlib.Path(FETCHED_DATA_DIR, "penguins.csv")
    output_file = pathlib.Path(PROCESSED_DIR, "penguins_body_mass.txt")
    
    penguin_body_mass = analyze_penguin_body_mass(input_file)
    #print("returned with penguin_body_mass_dict\n")
    #print(penguin_body_mass)

    # Create the output directory if it doesn't exist
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Open the output file in write mode and write the results
    with output_file.open('w') as file:
        file.write(f"Minimum Penguin Body Mass: {penguin_body_mass["min"]:.2f}\n")
        file.write(f"Maximum Penguin Body Mass: {penguin_body_mass["max"]:.2f}\n")
        file.write(f"Average (mean) Penguin Body Mass: {penguin_body_mass["mean average"]:.2f}\n")
        
    # Log the processing of the CSV file
    logger.info(f"Processed CSV file: {input_file}, Statistics saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting CSV processing...")
    process_csv_file()
    logger.info("CSV processing complete.")