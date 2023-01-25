import string
from telethon import TelegramClient, events
from telethon.tl.types import PeerUser, PeerChannel, PeerChat
import asyncio
import threading

# Use your own values from my.telegram.org
api_id = 15193518
api_hash = '504ab7ab95614155f137244e819b5e91'

phone_number = "+18655004689"
phone_number = "+998901558090"
passw = "@dragon$"

client = TelegramClient('session', api_id, api_hash)

@client.on(events.NewMessage()) # chats=myChannelIDs
async def my_event_handler(event): 
    #print(event)
    print("################################")
    print()

    if type(event.peer_id) == PeerUser:
        print("from user: ", event.peer_id.user_id)

    if type(event.peer_id) == PeerChannel:
        print("from group: ", event.peer_id.channel_id)

    print("message: ", event.message.message)

    await event.message.forward_to(992519627)
    
    print()


# custom login instead of .start()
async def main():
    print("######")
    await client.connect()
    print("######")
    auth = await client.is_user_authorized()
    if not auth:
        await client.send_code_request(phone_number)
        me = await client.sign_in(phone_number, input('Enter code: '), password=passw) # , password="@dragon$"


#t1 = threading.Thread(target=asyncio.run, args=(main(), ))
#t1.start()
#t1.join()

################


#client.start(phone_number)
client.start()
client.run_until_disconnected()



# print(event.peer_id.channel_id)  #qaysi kanaldan keldi?
    # print('######', event)
    # if event.from_id != None:
        # print(event.from_id.user_id)     #.user_id   kim jo'natdi?

    # print(event.message.id)          #msg id 'si
    # print(event.date + datetime.timedelta(hours=5))  #jo'natilgan vaqt Toshkent vaqti
    # print(event.text)                #matn
    # print('********************************************************')

    #data.append(Fish(currend_id, event.peer_id.channel_id, event.message.id, event.date + datetime.timedelta(hours=5), event.text))
    #currend_id += 1
    #print(len(data))
    # print(event)



#bir sutka davomida chiqqan yuklarni hammasini DIV qilib olsin, 
#kerSSak bo'lganlarini, search qilib bersin. Type qilishi bilan filtrlanaversin.



# async def main():
#     for c in myChannelIDs:
#         ch = await client.get_entity(c)
#         print('channel ID: ', ch.id)
#         print('channel tutle: ', ch.title)
#         print('channel username: ', ch.username)
#         print()

# with client:
#     client.loop.run_until_complete(main())
