# google-sync-photos

## Upload your Photo to Google photos

Create Your Project on Google Cloud https://redirect.is/o0i61kz

## Command

-mk make new album in your account
-a  destination album 
-d  source dir of photos


## File Description

Google.py           : uses client_id.json and authenticate user.

init.py             : init uses Create_service funtion and create service from Google.py.

createAlbum.py      : Create Album ( -mk option use this file)

getfile.py          : small function that return list of file.

getAlbum.py         : return album_id( -a option use this file)

commandLinearg.py   : command line arg

uploadMedia.py      : upload img file to album
