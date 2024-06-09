Instructions to Run the Script:/n
Save the Script: Save the above script to a file, for example, file_sorter.py.
Run the Script: Open a terminal or command prompt and navigate to the directory where file_sorter.py is located.
Execute the Script: Run the script using the command:
sh
Copy code
python file_sorter.py
Provide Inputs: When prompted, enter the source directory (where the files are currently located), the destination directory (where you want the sorted files to be moved to), and the naming format.
Example Naming Format:
To rename files to include the original name and type: {original_name}_{file_type}
To rename files to include a sequential number: {file_type}_{original_name}_001
This script will organize your files into subdirectories within the destination directory based on their type and rename them according to your specified format. Adjust the file_types dictionary in the script to include any additional file extensions as needed.
