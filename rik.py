import time
from datetime import datetime, timedelta

# Function to read account IDs from data.txt
def read_account_ids(filename):
    with open(filename, 'r') as file:
        account_ids = [line.strip() for line in file if line.strip()]
    return account_ids

# Function to switch account
def switch_account(account_id):
    # Simulating POST request or any switching mechanism
    print(f"Switching to account ID: {account_id}")
    time.sleep(1)  # Simulating the switching process

# Main function to handle account switching and countdown
def handle_account_switching(filename):
    account_ids = read_account_ids(filename)
    total_accounts = len(account_ids)
    print(f"Total accounts to process: {total_accounts}")

    for idx, account_id in enumerate(account_ids, start=1):
        print(f"Processing account {idx}/{total_accounts}: {account_id}")
        switch_account(account_id)
        if idx < total_accounts:
            print("Waiting 5 seconds before switching to the next account...")
            time.sleep(5)
    
    print("All accounts processed.")

    # Countdown for 2 hours after all accounts are processed
    countdown_duration = timedelta(hours=2)
    start_time = datetime.now()
    end_time = start_time + countdown_duration

    while datetime.now() < end_time:
        remaining_time = end_time - datetime.now()
        print(f"Countdown: {remaining_time} remaining...", end="\r")
        time.sleep(1)

    print("\nCountdown finished. Restarting the process.")

# Example usage:
if __name__ == "__main__":
    data_file = 'data.txt'  # Adjust the filename as per your data file
    handle_account_switching(data_file)
