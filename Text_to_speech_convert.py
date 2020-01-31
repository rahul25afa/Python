# gtts(google text to speech module) import gTTS library
from gtts import gTTS
#import 'os' module to interact with operating system
import os
# open the text file which you want to convert in speech using open function and assign in the variable 'f'

f=open('Welcome friend.txt')
# Now read the file stored in 'f' and assign the place to file read by os in new variable 'x'
x=f.read()
# select the language for speech, here 'en' means 'english'
language='en'
#using gTTS library convert text into speech by declaring the agruments i.e text file, language and speed of speech, assign the file into variable(here audio)
audio=gTTS(text=x,lang=language,slow=False)
#save the audio file in either of the wav or mp3 format
audio.save("Welcome friend.wav")
#using os play the text converrted into speech
os.system("Welcome friend.wav")

