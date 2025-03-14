def count_errors_in_log(file_path):
    try:
        with open(file_path, 'r') as log_file:
            error_count = 0
            
            # Read the log file line by line
            for line in log_file:
                # Count occurrences of "ERROR" in the current line
                error_count += line.count("ERROR")
        
        # Print the total count of "ERROR"
        print(f'Total occurrences of "ERROR": {error_count}')
    
    except FileNotFoundError:
        print(f'Error: The file "{file_path}" was not found.')
    except Exception as e:
        print(f'An error occurred: {e}')

# Specify the path to the log file
log_file_path = 'server.log'

# Call the function to count errors
count_errors_in_log(log_file_path)