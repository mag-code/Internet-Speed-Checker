import requests
import time
import os
import logging

# constant variables
url = "https://download.thinkbroadband.com/5MB.zip"
file_size = 5000000
file_path = "C:\\Users\\Setup\\Downloads\\5MB.zip"


# Setting up logging to display download/upload speeds and latency times
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s- %(message)s')
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
logging.getLogger('').addHandler(console_handler)

# this is the test for speed of internet
def test_speed(url, file_size):
    try:
        session, start_time= requests.Session(), time.time()
#here we create the session and the timer for the session 
#we make a get request to the website to install the zip file
        response = session.get(url, stream=True)
#this calculates the time 
        download_time = time.time() - start_time
#this calculates the speed we installed the zip file by dividing file size by time
        download_speed = ((file_size / download_time) / 1000000)
#this creates the log for 
        logging.info(f'Download speed: {download_speed:.2f} Mbps')
    except requests.exceptions.RequestException as e:
        logging.error(f'Error testing download speed: {e}')
        raise

#this is the test for upload speed of internet
def test_upload_speed(url, file_path):
    try:
#this creates the session and receives the file size through the given file path
        session, file_size = requests.Session(), os.path.getsize(file_path)
        with open(file_path, "rb") as f:
#this creates the started time
            start_time, response  = time.time(),session.post(url, data=f)
#we create the upload time by subtracting the measured time with start time
            upload_time = time.time() - start_time
#we measure the upload speed by file size, upload time, and 1000000
            upload_speed = file_size / upload_time / 1000000
#this logs the upload speed
            logging.info(f'Upload speed: {upload_speed:.2f} Mbps')
    except (IOError, requests.exceptions.RequestException) as e:
        logging.error(f'Error testing upload speed: {e}')
        raise

#this is the test for latency of internet
def test_latency(url):
    try:
#we create the session and time
        session, start_time = requests.Session(),time.time()
        response = session.head(url)
#we measure latency by time - start time * 1000
        latency = (time.time() - start_time) * 1000
#we log latency 
        logging.info(f'Latency: {latency:.2f} ms')
    except requests.exceptions.RequestException as e:
        logging.error(f'Error testing latency: {e}')
        raise
#main function for error message when user interrupts
if __name__ == "__main__":
    try:
        test_speed(url, file_size)
        test_upload_speed(url, file_path)
        test_latency(url)
    except KeyboardInterrupt:
        print("Interrupted by user")
        logging.error(f'Interrupted by User.')