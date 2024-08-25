# SQL_inj_-time_delays-information_retrieval-_Tool
Python Script for SQL injection with time delays and information retrieval

warning!!!
This software is provided for educational and informational purposes only. The author is not responsible for any illegal or unauthorized use of this software. Use it at your own risk.



Instructions for Using the Code

1. Clone the Repository:
   - First, you need to clone the repository to your local machine. Open a terminal and run:
     ```bash
     git clone https://github.com/FAQ10/SQL_inj_-time_delays-information_retrieval-_Tool.git
     ```
   - Navigate to the project directory:
     ```bash
     cd SQL_inj_-time_delays-information_retrieval-_Tool
     ```

2. Install Dependencies:
   - Make sure you have Python installed on your system.
   - Install the required Python libraries by running:
     ```bash
     pip install -r requirements.txt
     ```
   - This will install the `requests` library and any other dependencies needed to run the script.

3. Prepare the Inputs:
   - **Page URL**: Enter the URL of the target web page you want to attack.
   - **Cookie Value**: If the target requires a session or authentication, input the value of the `TrackingId` cookie when prompted.

4. Run the Script:
   - Execute the Python script:
     ```bash
     python main.py
     ```
   - When prompted, enter the URL of the target page and the cookie value (if applicable).

5. Monitor Output:
   - The script will attempt to guess each character of the password using timing-based SQL injection. It will print the characters as it finds them.
   - Once all characters are found, the full password will be displayed.

6. Modify for Your Use Case:
   - You can modify the `username`, `cookie_name`, or adjust the character set in the script (`main.py`) to fit the needs of your specific target.
   - The script is currently set to work with lowercase letters (`a-z`) and digits (`0-9`). If your target uses uppercase letters or special characters, you can update the `character_set` variable accordingly.

7. Disclaimer:
   - This code is provided for educational and informational purposes only. The author is not responsible for any illegal or unauthorized use of this software. Use it at your own risk.

