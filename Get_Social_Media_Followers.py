from selenium import webdriver
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account
import time


#gets tikok followers of url
def getTikTokFollowers(driver):

    # get url and check for the request
    URL = '#TIK TOK PAGE URL'

    driver.get(URL)
    time.sleep(4)
    followers_tiktok = driver.find_element_by_xpath('#XPATH FOR TIKTOK PAGE')

    return int(followers_tiktok.text)

def getInstaFollowers(driver):

    # get url and check for the request
    URL2 = '#INSTAGRAM PAGE URL'

    driver.get(URL2)
    time.sleep(4)
    followers_insta = driver.find_element_by_xpath('#XPATH FOR INSTAGRAM PAGE')

    return int(followers_insta.text)

def getTwitterFollowers(driver):

    # get url and check for the request
    URL3 = '#Twitter PAGE URL'

    driver.get(URL3)
    time.sleep(4)

    followers_twitter = driver.find_element_by_xpath('#XPATH FOR TWITTER PAGE')

    followers_value_twitter = followers_twitter.text
    followers_value_twitter_new = followers_value_twitter.replace(',','')

    return int(followers_value_twitter_new)


def main():

    file_path = r"#ABSOLUTE PATH OF CHROMIUM DRIVER"
    driver = webdriver.Chrome(file_path)

    followers_list =[]

    followers_list.append([getTwitterFollowers(driver)])
    followers_list.append([getInstaFollowers(driver)])
    followers_list.append([getTikTokFollowers(driver)])

    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SERVICE_ACCOUNT_FILE = r'#ABSOLUTE PATH OF KEYS(SERVICE ACCOUNT KEY).JSON FILE'

    # set the creds and create the creds for the service acc
    creds = None
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # The ID and range of a sample spreadsheet.
    SAMPLE_SPREADSHEET_ID = '#CAN BE FOUND IN BETWEEN /d AND /edit#gid=0 IN URL OF WEB BROWSER'
    SAMPLE_RANGE_NAME = '#SHEETNAME!(CELL):(CELL)'

    # create the build for the spreadsheeet
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                   range=SAMPLE_RANGE_NAME, valueInputOption="USER_ENTERED",
                                   body={"values": followers_list}).execute()
    print(result)
    driver.close()
    driver.quit()

if __name__ == '__main__':
    main()
