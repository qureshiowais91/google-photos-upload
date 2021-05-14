# google-sync-photos

## Upload your Photo to Google photos

## Setup

1. Install requirements: `pip install -r requirements.txt`
2. Signup for an Google Photos API here: https://developers.google.com/photos/
3. Create Your Project on Google Cloud https://redirect.is/o0i61kz  
4. Download the `Client_id.json` file and place it in this directory


## Commands
  
  ### To Upload
  
    python3 runMe.py -d dir -a 'name of album'
  
  #### Create New Album
  
     python3 runMe.py -mk "new album name"
  
   
   ```
   usage: runMe.py [-h] [-d D] [-a A] [-mk MK]

optional arguments:
  -h, --help  show this help message and exit
  -d D        Enter Source directory
  -a A        Enter Name of Destination Album
  -mk MK      Create Album in Google Photo
   ```
   

## File Description

1. Google.py           : uses client_id.json and authenticate user.
2.  init.py             : init uses Create_service funtion and create service from Google.py.
3.  createAlbum.py      : Create Album ( -mk option use this file)
4.  getfile.py          : small function that return list of file.
5.  getAlbum.py         : return album_id( -a option use this file)
6.  commandLinearg.py   : command line arg
7.  uploadMedia.py      : upload img file to album


