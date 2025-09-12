"""
Process a JSON file to count astronauts by spacecraft and save the result.

JSON file is in the format where people is a list of dictionaries with keys "craft" and "name".

{
    "people": [
        {
            "craft": "ISS",
            "name": "Oleg Kononenko"
        },
        {
            "craft": "ISS",
            "name": "Nikolai Chub"
        }
    ],
    "number": 2,
    "message": "success"
}

"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import json
import pathlib
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

# TODO: Add or replace this with a function that reads and processes your JSON file

def countries_and_populations(file_path: pathlib.Path) -> dict:
    """Count the number of astronauts on each spacecraft from a JSON file."""
    try:
        # Open the JSON file using the file_path passed in as an argument
        with file_path.open('r') as file:
            
            # Use the json module load() function 
            # to read data file into a Python dictionary
            country_data_list = json.load(file) #comes from file as list
            country_data_dictionary = {}
            #print(country_data_list)
            #print("***********************\n")

            population_list = []
            country_list = []
            iter = 0
            #convert incoming data into dictionary
            for item in country_data_list:
                if type(item) == 'NoneType':
                    pass
                population_list.append(item['population'])
                country_list.append(item['country'])
                country_data_dictionary = dict(zip(population_list, country_list))
                iter = iter+1
            return country_data_dictionary
    except Exception as e:
        logger.error(f"Error reading or processing JSON file: {e}")
        return {} # return an empty dictionary in case of error

def process_json_file():
    """Read a JSON file, count astronauts by spacecraft, and save the result."""

    input_file: pathlib.Path = pathlib.Path(FETCHED_DATA_DIR, "countries_data.json")

    output_file: pathlib.Path = pathlib.Path(PROCESSED_DIR, "countries_populations.txt")
    
    countries_with_pop = countries_and_populations(input_file)


    # Create the output directory if it doesn't exist
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Open the output file in write mode and write the results
    with output_file.open('w') as file:
        file.write("All Countries by Population:\n")
        for country, pop in countries_with_pop.items():
            file.write(f"{country}: {pop}\n")

        
    
    # Log the processing of the JSON file
    logger.info(f"Processed JSON file: {input_file}, Results saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting JSON processing...")
    process_json_file()
    logger.info("JSON processing complete.")