from init import service
from commandLinearg import destinationAlbum
from commandLinearg import newAlbum
import pandas as pd


def getalbumID():
    respons = service.albums().list(
        pageSize=10,
        excludeNonAppCreatedData=False
    ).execute()

    lstrespons = respons.get('albums')
    nextPageToken = respons.get('nextPageToken')

    while nextPageToken:
        respons = service.albums().list(
            pageSize=50,
            excludeNonAppCreatedData=False,
            pageToken=nextPageToken
        )
        lstrespons.append(respons.get('albums'))
        nextPageToken = respons.get('nextPageToken')

    df = pd.DataFrame(lstrespons)

    index = 0
    for i, row in df.iterrows():
        if row.title == destinationAlbum:
            album_id = row.id
        else:
            index += 1
    return album_id

