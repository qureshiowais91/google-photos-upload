from init import alb
from commandLinearg import newAlbum

#new album request body
def createNewAlbum():
    albumInfo = {
        "album": {
            "title": (newAlbum),
            "isWriteable": 'true'
        }
    }

    # alb = service.albums()
    
    newAlb = alb.create(body=albumInfo).execute()
    print(newAlb['title'],'Album is Created')
    return newAlb
