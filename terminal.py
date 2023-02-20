import os
def upload():
    title=input("Enter the video title : ")
    description=input("Enter the vide description : ")
    os.system('cmd /k"python upload.py --file="final.mp4" --title="{t} #shorts" --description="{d} #shorts" --keywords="family guy petergriffin meg griffin" --privacyStatus="public" "'.format(t=title,d=description))

upload()