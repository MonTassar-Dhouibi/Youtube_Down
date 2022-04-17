
from __future__ import unicode_literals
import yt_dlp as youtube_dl
import sys, os


os.system("termux-wake-lock")
def main():
	try :
		if len(sys.argv)>1:
 	     	  link = sys.argv[1]
		else:
        		print("Insert the link")
        		link = input ("")

		ydl_opts = {
    'format': 'bestaudio/best',
    'writethumbnail': True,
    'add-metadata':True,
     'outtmpl': '/storage/emulated/0/PMusic/%(title)s.%(ext)s',
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
	except:
 	   print("[+] 0 :EXIT\n[+] 1 :RETRY ")
 	   c = int(input())
 	   if c ==0:
 	   	sys.exit()
 	   else :
 	   	main()   
 	   
 	   
if __name__ == "__main__":
	main();sys.exit()
