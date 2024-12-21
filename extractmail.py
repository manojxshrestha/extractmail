import re

input_file = input("Enter the file path: ").strip()
output_file = "spreadmail.txt" 

try:
    with open(input_file, "r") as file:
        lines = file.readlines()
      
    email_regex = r"[a-zA-Z0-9._%+-]+@(gmail\.com|yahoo\.com|hotmail\.com)"

    emails = []
    for line in lines:
        match = re.search(email_regex, line)
        if match:
            emails.append(match.group())  

    with open(output_file, "w") as file:
        for email in emails:
            file.write(email + "\n")

    print(f"Extracted email addresses have been saved to {output_file}.")

except FileNotFoundError:
    print("Error: The input file was not found. Please check the path and try again.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
