
from getfile import getFileNames
from commandLinearg import destinationAlbum
from commandLinearg import sourceDir
from getAlbum import getalbumID
from init import media
import pickle
import requests
import os


def uploder():
    print('Uploader Started...')
    photo_file_list = getFileNames(sourceDir)
    for photo_file_name in photo_file_list:
        img_dir = sourceDir
        upload_url = 'https://photoslibrary.googleapis.com/v1/uploads'
        token = pickle.load(open('token_photoslibrary_v1.pickle', 'rb'))

        header = {
            'Authorization': 'Bearer ' + token.token,
            'Content-type': 'application/octet-stream',
            'X-Goog-Upload-Protocol': 'raw'
        }

        img_file = os.path.join(img_dir, photo_file_name)
        # header['']='img_Upload.png'

        img = open(img_file, 'rb').read()
        respons = requests.post(upload_url, data=img, headers=header)

        # print(userInput)
        # Namespace(a='ok', d=None, mk=None)

        requests_body = {
            "albumId": getalbumID(),
            "newMediaItems": [
                {
                    "description": "Upload via API Call",
                    "simpleMediaItem": {
                        "fileName": photo_file_name,
                        "uploadToken": respons.content.decode('utf-8')
                    }
                }
            ]
        }

        upload_rp = media.batchCreate(body=requests_body).execute()
    return respons.content
