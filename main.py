from telegram.ext import *
import requests
import json

Token="5782637638:AAH1cEoISqUyLEzP2RCx6Td2v8JZoQIjoWs"
#/dashboard - To access the dashboard making the interface easier

updater = Updater(Token,use_context=True)
dispatcher = updater.dispatcher

def start(update,context):
    update.message.reply_text('''Hello   ¡Hola!  Bonjour  Ciao    你好(nǐ hǎo)    Dia     Olá  नमस्ते (namaste)  Здравствуйте (Zdravstvuyte) こんにちは (Kon’nichiwa)    Χαίρετε (Chaírete)

Hey, This is InforNation , I'm a countrybot and I'm here to help you find the country you are looking for.
InforNation will also provide you some basic Information about that particular Nation.

You can search country you want by name,code, region,sub-region,currency,capital city,language.


You can use the following commands:
/name- To search the country by name.
/capital - To search the country by name.
/language - To search the country by language.
/currency - To search the country by currency.
/countrycode - To search the country by countrycode.(Search by cca2, ccn3, cca3 or cioc country code)
/searchbyreg - To see the list of all countries in a region.
/searchbysubreg - To see the list of all countries in a region.

Use the /help command for more instructions and information regarding the bot.
'''
)   
    
    

def sendinfo(data ,i,update,context):
    update.message.reply_text(f"""Common Name: {data[i]['name']['common']}

Official Name: {data[i]['name']['official']}

Currency used: {list(data[i]['currencies'])[0]}

Capital: {(data[i]['capital'])}

Languages used: {list(data[i]['languages'].values())}
""")      


# in help add dash board
def help(update,context):
    update.message.reply_text('''   
Hey This is InforNation , I'm a countrybot and I'm here to provide you information and intresting facts about any country in the world.
I'm always here to help you.


You can use the following commands:
/help - To access this message containing the basic information and instructions
/name - Use this command to activate the country bot and follow up by entering the name of any country and
/capital - To get to know Capital of a country
/language - To get to know the Languages used in the country
/currency - To get to know the currency used in the country(use loer)
/countrycode - To see the codes of the country(Search by cca2, ccn3, cca3 or cioc country code)
/searchbyreg - To see the list of all countries in a region
/searchbysubreg - To see the list of all countries in a region

''')

def name(update,context):
    update.message.reply_text("Please enter the Name of a country to get some Information about it.")
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, readbyname ))

    

def capital(update,context):
    update.message.reply_text("Please enter the capital of a country to get some Information about it.")
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, readbycapital))

def language(update,context):
    update.message.reply_text("Please enter the language of a country to get some Information about it.")
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, readbylanguage))

def currency(update,context):
    update.message.reply_text("Please enter the currency of a country to get some Information about it.")
    dispatcher.add_handler(CommandHandler('currency',currency))
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, readbycurrency))
    


def countrycode(update,context):
    update.message.reply_text("Please enter the countrycode of a country to get some Information about it.")
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, readbycountrycode))
    



def readbyname(update,context):
    response = requests.get(f'https://restcountries.com/v3.1/name/{update.message.text}')
    if(response.status_code==200):
        data=response.json()
        for i in range (len(data)):
            if(data[i]['name']['common']==update.message.text):
                update.message.reply_photo(data[i]['flags']['png'])
                sendinfo(data,i,update,context)          
                break
        else:
            update.message.reply_text("These are closest possible guesses I have for the country name you entered")
            for i in range (len(data)):
                update.message.reply_photo(data[i]['flags']['png'])
                sendinfo(data,i,update,context)
        
    else:
        update.message.reply_text('Error , No such country is found. Please check the spelling once.')

    
def readbycurrency(update,context):
    update.message.reply_text("Please enter the name of the currency to get information about the country")
    response1 = requests.get(f'https://restcountries.com/v3.1/currency/{update.message.text}')

    if(response1.status_code==200):
        data=response1.json()
        for i in range (len(data)):
            update.message.reply_photo(data[i]['flags']['png'])
            sendinfo(data,i,update,context)          
    else:
        update.message.reply_text(response1.status_code)
        update.message.reply_text('Error , No such country is found. Please check the spelling once.')



def readbycapital(update,context):
    response = requests.get(f'https://restcountries.com/v3.1/capital/{update.message.text}')
    if(response.status_code==200):
        data=response.json()
        for i in range (len(data)):
            update.message.reply_photo(data[i]['flags']['png'])
            sendinfo(data,i,update,context)          
    else:
        update.message.reply_text('Error , No such country is found. Please check the spelling once.')

def readbylanguage(update,context):
    response = requests.get(f'https://restcountries.com/v3.1/language/{update.message.text}')
    if(response.status_code==200):
        data=response.json()
        for i in range (len(data)):
            update.message.reply_photo(data[i]['flags']['png'])
            sendinfo(data,i,update,context)          
    else:
        update.message.reply_text('Error , No such country is found. Please check the spelling once.')


def readbycountrycode(update,context):
    response = requests.get(f'https://restcountries.com/v3.1/alpha/{update.message.text}')
    if(response.status_code==200):
        data=response.json()
        for i in range (len(data)):
            update.message.reply_photo(data[i]['flags']['png'])
            sendinfo(data,i,update,context)          
    else:
        update.message.reply_text('Error , No such country is found. Please check the spelling once.')

dispatcher.add_handler(CommandHandler('start',start))
dispatcher.add_handler(CommandHandler('help',help))
dispatcher.add_handler(CommandHandler('name',name))
dispatcher.add_handler(CommandHandler('currency',currency))
dispatcher.add_handler(CommandHandler('language',language))
dispatcher.add_handler(CommandHandler('capital',capital))
dispatcher.add_handler(CommandHandler('countrycode',countrycode))



updater.start_polling()
updater.idle()