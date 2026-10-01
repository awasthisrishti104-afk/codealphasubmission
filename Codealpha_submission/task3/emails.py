import os
import re
def extract_emails(input_file_path, output_file_path):
    """
    Extracts all email addresses from a specified text file and 
    saves the unique results to an output file.
    """
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    if not os.path.exists(input_file_path):
        print(f"Error: The file '{input_file_path}' does not exist.")
        return
    try:
        with open(input_file_path, 'r', encoding='utf-8') as infile:
            content = infile.read()
        found_emails = re.findall(email_pattern, content)
        unique_emails = list(dict.fromkeys(found_emails))
        with open(output_file_path, 'w', encoding='utf-8') as outfile:
            for email in unique_emails:
                outfile.write(email + '\n')
        print(f"Success! Extracted {len(unique_emails)} email(s) into '{output_file_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    input_file = "sample.txt"      
    output_file = "emails.txt"     
    if not os.path.exists(input_file):
        with open(input_file, 'w', encoding='utf-8') as f:
            f.write("Hello, contact us at info@example.com or support@company.org. "
                    "For sales, reach out to sales@example.com.")
    extract_emails(input_file, output_file)