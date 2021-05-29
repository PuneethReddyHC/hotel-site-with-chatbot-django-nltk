import nltk
import numpy
import random
import string
from django.conf import settings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests, json
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('words')
nltk.download('punkt')
nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.corpus import words


def greeting(sentence):
    for word in sentence.split(" "):
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

def find_response(response):
    chatbots_file = open(r'' + settings.BASE_DIR + '/HotelChatbot/chatbot.txt','r',errors = 'ignore')
    # chatbots_file = open(r'chatbot.txt','r',errors = 'ignore')
    info_data = chatbots_file.read()
    info_data = info_data.lower()

    sentence_tokens = nltk.sent_tokenize(info_data)
    word_tokens = nltk.word_tokenize(info_data)
    
    bot_response = ''
    sentence_tokens.append(response)
    TfidfVec = TfidfVectorizer(tokenizer = normalize, stop_words = 'english')
    tfidf = TfidfVec.fit_transform(sentence_tokens)
    
    values = cosine_similarity(tfidf[-1],tfidf)
    idx = values.argsort()[0][-2]
    flat = values.flatten()
    flat.sort()
    
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        bot_response = bot_response + "I am sorry! I don't understand you"
    else:
        bot_response = bot_response + sentence_tokens[idx]
    return bot_response
 
    
remove_punct = {}    
GREETING_INPUTS = ("hello","hi","what's up","sup","hey")
GREETING_RESPONSES = ("hi","hey","hi there","hello","I am glad! You are talking to me")



def find_weather(city):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=ae9512f4de94ef9415b53d6a357bd78a'
    response = requests.get(url.format(city))
    
    return response

def give_response(input_given):
    input_given = input_given.lower()
    if 'weather' in input_given:
        text_tokens = word_tokenize(input_given)

        tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
        
        city =   tokens_without_sw[1] if tokens_without_sw[0] == "weather" else tokens_without_sw[0]
        
        print(tokens_without_sw)
        response = find_weather(city)
        if response.status_code == 200:
            weather_data = response.json()
            main = weather_data['main']
            weather = {
                'city' : city,
                'temperature' : main['temp'],
                'description' :weather_data['weather'][0]['description'],
                'icon' : weather_data['weather'][0]['icon']
            }
        else:
            # showing the error message
            setofwords = set(words.words())
            for word in tokens_without_sw:
                if word not in setofwords:
                    response = find_weather(word)
                    if response.status_code == 200:
                        weather_data = response.json()
                        main = weather_data['main']
                        weather = {
                            'city' : word,
                            'temperature' : main['temp'],
                            'description' :weather_data['weather'][0]['description'],
                            'icon' : weather_data['weather'][0]['icon']
                        }
                    else:
                        weather = "Can't find city name. Try this format(eg: weather CITY)"
        return weather
        
    elif(input_given != 'bye'):
        if(input_given=='thanks' or input_given=='thank you'):
            flag = False
            return('You are welcome!')
        else:
            if(greeting(input_given)!=None):
                return greeting(input_given) + ', How can I help You?'
            else:
                
                response = '<div class="cont">I am sorry! I don\'t understand you<br>Checkout below'
                response+= '<ul class="nested_lu">'
                response+= '<li class="input__nested-list"><a href="/HotelApp/#search_layout">Book a Hotel </a></li>'
                response+= '<li class="input__nested-list"><a href="/Reservations/mybookings/">Your Bookings</a></li>'
                response+= '<li class="input__nested-list"><a href="#" class="list_hotels">List Hotels</a></li>'
                response+= '<li class="input__nested-list"><a href="#" class="price_hotels">Hotels Price</a></li>'
                response+= '<li class="input__nested-list"><a href="#" class="weather_info">Weather Info </a></li>'
                response+= '</ul>'
                response+= 'Thanks</div>'
                # return find_response(input_given)
                return response
                sentence_tokens.remove(input_given)
    else:
        flag = False
        return ('Bye!')
