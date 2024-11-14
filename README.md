# FacebookMessengerE2EE_JSON_Convertor
After Facebook swapped to the End-to-end encrypted chats.  The data is now stored in JSON format.  Previous we would be able to download our messages from our account and it would be organized as easy to read HTML.

Now we can download the E2E message storage from Facebook, then click on Messenger Icon-> Privacy & Safety-> End-to-end encrypted chats -> Download secured storage data -> Download file

This will give you a zip file with all your E2E messages and media.

Make sure install beautifulsoup4

#How to run
python FacebookMessengerE2EE_JSON_Convertor.py [path_to_json] [path_to_media] [output_location]

