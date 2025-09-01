import os
import eel 

eel.init("www") 

os.system('start local.exe --app="http://localhost:800/index.html"') 
eel.start('index.html',mode=None,host='localhost',block=True)eel.start('index.html', mode="chrome", host='localhost', block=True)eel.start('index.html', mode="chrome", host='localhost', block=True)