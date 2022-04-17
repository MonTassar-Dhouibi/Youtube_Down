import os
print("#"*20,"\n\n")
print("{}^20".format("InSTTALLER"))
print("\n\n","#"*20)
print("Installing ....")
os.system("pkg install -y ffmpeg")
os.system("pip install -y youtube_dl")
os.system("python setup.py install")
input("Installation finished .....")