import speech_recognition as sr

video_file=input("please enter the audio file: ")

# obtain path to "english.wav" in the same folder as this script
from os import path
#AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "testaudio.wav")
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), video_file)


# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file


# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    transcript=r.recognize_google(audio)
    print(transcript)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
#file = open(“testfile.txt”,”w”) 
#file.write(transcript) 
#file.close() 

#will be required in order to remove punctuation
import string
#function made in order to remove punctuation and make the string lowercase
def format_string(s):
  for x in string.punctuation:
    s=s.replace(x,"")
    s=s.lower()
  return s

KEYWORDS=open('keywords.txt','r')
#lists that store the keywords co-orespoding to their values
rating_1=[]
rating_2=[]
rating_3=[]
rating_4=[]
rating_5=[]
rating_6=[]
rating_7=[]
rating_8=[]
rating_9=[]
rating_10=[]

for line in KEYWORDS.readlines():
    word=line.split(",")
    if int(word[1]) == 1:
        rating_1.append(word[0])
    elif int(word[1]) == 2:
        rating_2.append(word[0])
    elif int(word[1]) == 3:
        rating_3.append(word[0])
    elif int(word[1]) == 4:
        rating_4.append(word[0])
    elif int(word[1]) == 5:
        rating_5.append(word[0])
    elif int(word[1]) == 6:
        rating_6.append(word[0])
    elif int(word[1]) == 7:
        rating_7.append(word[0])
    elif int(word[1]) == 8:
        rating_8.append(word[0])
    elif int(word[1]) == 9:
        rating_9.append(word[0])
    elif int(word[1]) == 10:
        rating_10.append(word[0])

#function created in order to measure the happiness score of each tweet
#this makes sure that if there is a key file inserted with keys having values from anywhere between 1-10 it'd still be able to calculate it
def happiness_score(tweet):
    no_of_positive_words=0
    value_of_tweet=0
    for x in tweet:
        if x in rating_1:
            no_of_positive_words+=1
            value_of_tweet+=1
        elif x in rating_2:
            no_of_positive_words+=1
            value_of_tweet+=2
        elif x in rating_3:
            no_of_positive_words+=1
            value_of_tweet+=3
        elif x in rating_4:
            no_of_positive_words+=1
            value_of_tweet+=4
        elif x in rating_5:
            no_of_positive_words+=1
            value_of_tweet+=5
        elif x in rating_6:
            no_of_positive_words+=1
            value_of_tweet+=6
        elif x in rating_7:
            no_of_positive_words+=1
            value_of_tweet+=7
        elif x in rating_8:
            no_of_positive_words+=1
            value_of_tweet+=8
        elif x in rating_9:
            no_of_positive_words+=1
            value_of_tweet+=9
        elif x in rating_10:
            no_of_positive_words+=1
            value_of_tweet+=10
        try:
            score=value_of_tweet/no_of_positive_words
        except ZeroDivisionError:
            score=5
    return (score)

list_of_words=[]
for word in transcript:
    formated_item=format_string(word)
    list_of_words.append(formated_item)
    happiness_per_tweet=happiness_score(list_of_words)

print(happiness_per_tweet)
