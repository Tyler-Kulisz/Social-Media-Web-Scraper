# Social-Media-Web-Scraper
Scrapes followers from Tik Tok, Twitter, and Instagram. It updates a Google Sheet with all the follower numbers to track growth over time.

In order for this script to work you need to create a Project and a Service Account in a Google Cloud Account. The Service Account is meant to act like an actual person is updating the cell values in the Google Sheet. After creating the Service Account we need to give it the Editor role for the Project which will then allow us to share the Google Sheet with the Account. Once the Service Account is successfully created we need to download the Service Account key in JSON and put that into the same folder as our .py file and also putting the latest Chromium Driver version that syncs with your current Google Chrome build. Just make sure the Xpaths of the social media accounts are correct and that's it.

The libraries used in this script are Selenium for Xpath scrapping and Automation and the Google-Api-Python-Client for verifying Credentials, Creating the build for the spreadsheet, and the Service Account.
