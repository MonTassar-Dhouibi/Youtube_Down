from __future__ import unicode_literals
import yt_dlp as youtube_dl
import sys
import glob, os
from mutagen.id3 import ID3, APIC, error,TALB
import shutil ,random

#path = "/storage/emulated/0/PMusic3/.tmp/"


def CImg():
	aFile = glob.glob(("*.mp3"))[0]
	tags = ID3(aFile)
	try :
		Name = aFile.split("-")[1].replace(".mp3","")
		id = "YDown | " +Name+ str(random.randint(1,99))
	except:
		id = "YDown | "+ aFile.replace(".mp3","") +str(random.randint(1,99))
	tags.add(TALB(encoding=3, text=id))
	tags.save()
	

	
	shutil.move(aFile,"/storage/emulated/0/PMusic3/"+aFile)

	

def main():
	i= 0
	path = "/storage/emulated/0/PMusic3/.tmp/"
	try :
		if len(sys.argv)>1:
 	     	  link = sys.argv[1]
		else:
        		print("Insert the link")
        		link = input ("")
		while os.path.isdir(path) :
			i+=1 
			path = "/storage/emulated/0/PMusic3/.tmp"+str(i) +"/"
		ydl_opts = {
    'format': 'bestaudio/best',
    '%(title)s': "gt",
    'writethumbnail': True,
    'add-metadata':True,
     'outtmpl': path+'%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    },
        {'key': 'EmbedThumbnail'},
        {'key': 'FFmpegMetadata'},
        ],
	}

		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			   	ydl.download([link])
			   	
			   	os.chdir(path)
			   	CImg()
			   	os.rmdir(path)
 		   	
	except Exception as e:
 	   print(e,"\n[+] 0 :EXIT\n[+] 1 :RETRY ")
 	   c = int(input("-->  "))
 	   if c ==0:
 	   	sys.exit()
 	   else :
 	   	main()   
 	   
 	   
if __name__ == "__main__":
	main()
