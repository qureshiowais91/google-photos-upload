from uploadMedia import uploder
from commandLinearg import newAlbum
from createAlbum import createNewAlbum

import schedule
import time


def job():
    print("I'm working...")
    uploder()

UPLOAD_EVERY_MIN = 1


#create album here
if newAlbum:
    createNewAlbum()
    exit()
else:
    # Script Script Run Every 60 min.
    # Please dont run it too fruquntly.
    # google may block your IP
    schedule.every(UPLOAD_EVERY_MIN).minutes.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
    
