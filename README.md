# Python git uploader

## What's this?

This script was written to ease the uploading of recently committed files to git.
It will read the single latest commit and upload the changed files to the provided server.

## Usage

Copy & paste the uploader.ini and uploader.py files to the root directory you want to upload the latest git changes for.
Then enter your details in the uploader.ini file.

After you've made your git commit you can execute the uploader.py and you'll be given a list of the recent changes.
once you confirm the files to be uploaded are correct the uploading will start.

## TODO's

* Show progress of individual file uploads
* Aks user if they want to overwrite the file on server if it exists
* Adding/removing files to be uploaded
* Change certain paths, f.e. /web/ to /public_html/
* ...