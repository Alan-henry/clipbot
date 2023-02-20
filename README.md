# clipbot
A bot that grabs clips from YouTube, cuts them down to the given time stamps (in seconds) and posts them as shorts on YouTube 

**STEPS TO GET YOU STARTED**

STEP 1 : You will first need to get your "client id" and "client secret" from https://console.cloud.google.com/

if you dont know how to do that here's a documentation on how to do that : https://www.askdata.com/docs/dataset-google-analytics-how-to-get-google-client-id-and-client-secret

STEP 2 : Paste your "client id" and "client secret" in client_secrets.json in the given manner          

          "client_id":"YOUR CLIENT ID"
          "client_secret":"YOUR CLIENT SECRET"

STEP 3: Run "python main.py" 
NOTE: YOU MIGHT HAVE TO RUN THE "main.py" FILE IN THE TERMINAL AS AN ADMIN

STEP 4: On select option 2 i.e press 2 for : "1 for vertically stacked 2 for normal : " as the first option is still under beta testing

STEP 5: Enter the required details

STEP 6: Give authentication.
NOTE : The api used for the uploading of the videos is take from this website so you can check these documents for any queries : https://developers.google.com/youtube/v3/guides/uploading_a_video
