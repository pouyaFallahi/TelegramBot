from telegram.ext import *
import logging


PAI_KEY='enter your PAI_KEY bot'
updater = Updater(PAI_KEY, update_queue= True)
logging.basicConfig(filename='logging.log', format='%(process)d-%(levelname)s-%(message)s-%(asctime)s')


print('bot start')
async def start(update, context):
    await update.message.reply_text('سلام من یه رباط هستم برای رمزی حرف زدن کار کردن با من خیلی آسون \n\n تو یه متن برای من بفرست تا من تبدیلش کنم \n\n\n روی /help بزن تا ببینی ')

async def help(update, context):
    await update.message.reply_text('برای تبدیل به کد مورس از دستور \n/convert_to_morse بعد کلمه که میخوای البته به اینگلیسی\n\n/decoding_morse اینم برای دیکود کردن ')
    await update.message.reply_text('برای تبدیل به کد سزار هم \n/convert_to_sezar با یه فاصله متن مورد نظر تو تایپ کن\n\n/decod_sezar اینم برای دیکود کردن\nاگه متوجه نشدی مثل این پیام پایین متن هاتو بفرست ')
    await update.message.reply_text('/convert_to_morse\nslm')
    await update.message.reply_text('/decoding_morse\nslm')
    await update.message.reply_text('/convert_to_sezar\nslm')
    await update.message.reply_text('/decod_sezar\nslm')
    
async def ConvertToSezareCode(update , context):
    update.message.reply_text('oky let\'s go')
    tXt = str(update.message.text)        
    result=''
    s = 4
    for i in tXt:
        if i.isupper():
            result=result+chr((ord(i)+s-65)% 26 + 65)
        elif i.islower():
            result = result + chr((ord(i)+ s -97) % 26 + 97)
        else:
            result = result + i

    logging.error(tXt)

    
    await update.message.reply_text(result)

async def convertTo_Decoding_Sezar(update , context):
    update.message.reply_text('oky let\'s go')
    tXt = str(update.message.text)
    result=''
    s = -4
    for i in tXt:
        if i.isupper():
                result=result+chr((ord(i)+s-65)% 26 + 65)
        elif i.islower():
                result = result + chr((ord(i)+ s -97) % 26 + 97)
        else:
                result = result + i

    logging.error(tXt)
    await update.message.reply_text(result)

async def convertToMorseCod(update , context):
    data={"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---", "K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-",
          "U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..","0":"-----","1":".----","2":"..---", "3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.",".":".-.-.-",",":"--..--", "?":"..--..","-":"-....-",'_':' ','\n':'\n','/n':'\n',"/":"-..-."}
    await update.message.reply_text('convert to morse code')
    txt = str(update.message.text).upper()
    
    code=''
    for i in txt:
        if i != ' ' and i !='/n':
            code = code +data[i]+' '
        else:
            code+=' '

    logging.error(txt)
    await update.message.reply_text(code)


async def decoding_mors(update , context):
    data={"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---", "K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-",
          "U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..","0":"-----","1":".----","2":"..---", "3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.",".":".-.-.-",",":"--..--", "?":"..--..","-":"-....-",'_':' ','\n':'\n','/n':'\n',"/":"-..-.",'/DECODING_MORS\n\n':' ','/decoding_mors\n\n':' ',' ':'/DECODING_MORSE\n\n','':'/DECODING_MORSE\n'}     
    x=''
    code=''
    v=list(data.values())
    k=list(data.keys())
    text = str(update.message.text).upper()
    text += ' '
    for i in text:
        if i != ' ':
            n=0
            x=x+i
        else:
            n=n+1
            if n==2:
                code=code+' '
            else:
                m=v.index(x)
                s=k[m]
                code+=s
                x=''

    logging.error(text)
    await update.message.reply_text(code)

async def masseag(update, context):

    InputText,TypeConvert =''
    txt = str(update.message.text).upper()
    if txt == 'convert':
        logging.error(txt)
        await update.message.reply_text(text=input('matn morde nazr'))
        #inputText(txt=InputText)
        #typeConvert(txt=TypeConvert)
        #ConvertToMorseCode(txt= InputText, typeConvert=TypeConvert)



def main():
    dp = Application.builder().token(PAI_KEY).build()
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler('convert_to_sezar', ConvertToSezareCode))
    dp.add_handler(CommandHandler('decod_sezar', convertTo_Decoding_Sezar))
    dp.add_handler(CommandHandler('convert_to_morse', convertToMorseCod ))
    dp.add_handler(CommandHandler('decoding_morse', decoding_mors ))
    dp.add_handler(CommandHandler('help', help ))
    # updater.start_polling(5)
    # updater.idle()
    dp.run_polling(5)
main()
