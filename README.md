# Internet-Speed-Checker
This is an internet speed checker that measures the download speed, upload speed, and latency of your wifi. The process of this was for the program to install a zipfile from download.thinkbroadband.com and to measure the internet speed.
The script imports the requests, time, os, and logging modules. It defines several constants, including a URL for a 5 MB zip file, the size of the file, and the file path to where the zip file will be downloaded.
The script sets up logging to display download/upload speeds and latency times. It creates a console handler and adds it to the root logger.
There are three functions defined: test_speed(), test_upload_speed(), and test_latency().
test_speed() function tests the download speed of the internet connection by making a GET request to the URL where the 5 MB zip file is located. It measures the time taken to download the file, calculates the download speed, and logs the result using the logging module.
test_upload_speed() function tests the upload speed of the internet connection by making a POST request to the same URL and uploading the downloaded 5 MB zip file. It measures the time taken to upload the file, calculates the upload speed, and logs the result using the logging module.
test_latency() function tests the latency of the internet connection by making a HEAD request to the URL and measuring the time taken for the response to be received. It calculates the latency and logs the result using the logging module.
The main block of the script calls the three functions defined above and catches a keyboard interrupt error in case the user wants to exit the script prematurely.
Thank You!
