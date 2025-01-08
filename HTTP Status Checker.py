# ===================================================================================
# Created By     : x_4rch4n63l_x
# Created On     : 10/18/2024 - 7:16AM
# Script Purpose : Check HTTP status of multiple URLs
# Description    : This script takes a list of URLs from the user, checks their HTTP
#                  status codes, and prints the status codes to the console.
# Features       : 
#                  - Fetches HTTP status codes for multiple URLs
#                  - Handles exceptions and prints error messages
#                  - Simple user input and output
# Usage Note     : Run the script and enter URLs separated by commas when prompted.
# ===================================================================================
import requests

def check_http_status(urls):
    status_codes = {}
    for url in urls:
        try:
            response = requests.get(url)
            status_codes[url] = response.status_code
        except requests.RequestException as e:
            status_codes[url] = f"Error: {str(e)}"
    return status_codes

def main():
    user_input = input("Enter URLs to check (comma-separated): ")
    urls = [url.strip() for url in user_input.split(",")]

    status_codes = check_http_status(urls)

    for url, status in status_codes.items():
        print(f"{url}: {status}")

if __name__ == '__main__':
    main()
