#####################################
# Imported Modules
#####################################
from utils_logger import logger

import haileyhanson_get_csv
import haileyhanson_process_csv

import haileyhanson_get_excel
import haileyhanson_process_excel

import haileyhanson_get_json
import haileyhanson_process_json

import haileyhanson_get_text
import haileyhanson_process_text

#####################################
# main() function
#####################################

def main():
    """
    Main function to control conditional logic of project
    """
    logger.info("Starting Main Script of Get&Process Data Project...")
    user_choice = int(input("Enter 1 to get&process CSV data\nEnter 2 to get&process excel data\nEnter 3 to get&process json data\nEnter 4 to get&process text data\n"))
    if user_choice == 1:
        haileyhanson_get_csv.main()
        haileyhanson_process_csv.process_csv_file()
    elif user_choice == 2:
        haileyhanson_get_excel.main()
        haileyhanson_process_excel.process_excel_file()
    elif user_choice == 3:
        haileyhanson_get_json.main()
        haileyhanson_process_json.process_json_file()
    elif user_choice == 4:
        haileyhanson_get_text.main()
        haileyhanson_process_text.process_text_file()
    else:
        print("please start again choossing a valid number 1, 2, 3, or 4")
        exit



#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()