from Google  import Create_Service
import os

API_NAME = 'photoslibrary'
API_VERSION = 'v1'
CLIENT_SECRET_FILE = 'clientGooglePhotos.json'
SCOPES = ['https://www.googleapis.com/auth/photoslibrary',
          'https://www.googleapis.com/auth/photoslibrary.sharing']

service = Create_Service(CLIENT_SECRET_FILE,API_NAME, API_VERSION, SCOPES)          
alb = service.albums()
media = service.mediaItems()