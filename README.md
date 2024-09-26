# Dynamic IP Watcher

`Dynamic IP Watcher` is a Python-based application that monitors your public IP address. It checks for changes in the IP address at regular intervals (every 10 seconds by default) and sends an email notification if the IP address has changed. The IP address is stored in a file and updated whenever a change is detected.

## Features

- **Fetch Public IP:** Retrieves your public IP address using the https://api.ipify.org service.
- **Track IP Changes:** Compares the current IP with the previously stored IP.
- **Update IP in File:** Stores the IP in a text file and updates it upon change.
- **Email Notification:** Sends an email notification if the public IP has changed.
- **Customizable Schedule:** The script is scheduled to run every 10 seconds, but this can be modified.


## Prerequisites

- Python 3.x
- Internet connection (to check the public IP)
- Email account (to send notifications)

## Installation
- Clone or download the project.

    ```bash
        git clone https://github.com/your-username/dynamic-ip-watcher.git
        cd dynamic-ip-watcher
    ```

- Install the required dependencies:

    ```bash
        pip install requests schedule
    ```