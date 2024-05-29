import logging
import random
import re
import time
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, Dispatcher, executor, types
#from aiocryptopay import AioCryptoPay, Networks
from pyCryptoPayAPI import pyCryptoPayAPI








crypto = pyCryptoPayAPI(api_token="191421:AAvLNNXm0tcambnOBWGzekh05VXtEUcWDal") #токен криптобот
API_TOKEN = '7008453328:AAGE8ZfeYokpafkuQvntTcucAerMW1CdIZo' #токен бота
kazik = -1002174696005 #айди канала с казом
button = InlineKeyboardButton("Сделать ставку", url="http://t.me/send?start=IVOe4HBAETPG")

kb = InlineKeyboardMarkup().add(button)
log = -1002229270028
#ВСЕ НУЖНОЕ









# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)





global full
def passgen():
	global full
	full = ""
	alfawit = ["a", "#", "@", "b", "c", "d", "e", "h", "g", "k", "&", "A", "N", "n", "M", "m", "2", "1", "3", "9", "4", "5", "6", "7", "8", "Q", "Z", "X", "z", "x", "$", "!", "?", "(", ")"]
	i = 0
	while i < 16:
		r = random.randint(0,34)
		full = f"{alfawit[r]}" + full
		i+=1
	print(full)
	return full




@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
	id = message.from_user.id
	try:
		regcheck = open(str(id)+".ref.txt", "r")
	except:
		regbalance = open(str(id)+".ref.txt", "w")
		regbalance.write("0")
	basec = open("RefBase.txt", "r")
	if str(id) in basec.read():
		return
		basec.close()
	else:
		basec.close()
		refid = message.text.split()[1]
		basereg = open("RefBase.txt", "a")
		basereg.write(str(refid) + "|" + str(id) + "\n")
	basereg.close()

@dp.message_handler(commands=['donate'])
async def donate(message: types.Message):
	checkk = await crypto.createC(asset="USDT", amount=0.01)
	print(checkk)
	sum = message.text.split()[1]
	await message.answer("Задонать нам /donate сумма")
	check = await crypto.create_invoice(asset="USDT", amount = sum)
	await message.answer(check)

@dp.message_handler(commands=['limset'])
async def setlimit(message: types.Message):
	sum = message.text.split()[1]
	await message.answer("Установлен лимит ставки: " + str(sum) + "$")
	lim = open("limit.txt", "w")
	lim.write(sum)
	
	
	
	
@dp.message_handler(commands=['kazna'])
async def setlimit(message: types.Message):
	kazna = await crypto.get_balance()
	await message.answer(kazna)
	
	
	

global summ
global id
id=0
summ = 0.0
async def bolshe(message):
	await bot.delete_message(kazik,message.message_id)
	time.sleep(0.3)
	global summ
	global id
	i=0
	limitcheck = open("limit.txt", "r")
	if message.entities[0].user:
		user = message.entities[0].user
		username = f"@{user.username}"
		name = user.full_name
		id = int(user.id)
		asset = message.text.split("отправил(а)")[1].split()[1]
		summ = float(message.text.split("отправил(а)")[1].split()[0].replace(',', ""))
		#summ = float(message.text.split("отправил(а)")[1].split()[0])
		if summ <= float(limitcheck.read()):
			if "💬 " in message.text:
				comment = message.text.split("💬 ")[1]
				await bot.send_message(kazik, f"""
🔑 Игрок: {name}
💵 Сумма ставки: {summ}$
💬 Комментарий: {comment}""", reply_markup=kb)
			winx = summ * 1.8
			cube = await bot.send_dice(kazik, "🎲")
			value = cube.dice.value
			#balkazna = await crypto.get_balance()
			
			if value > 3:
				try:
					await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
					await bot.send_message(kazik, f"""🎉 Поздравляем, вы выиграли {winx} USDT\n\n🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥 Удачи в следующих ставках!""")
				except:
					await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")
					await bot.send_message(kazik, f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!""")
			else:
		
				await bot.send_message(kazik, "❌ Твоя ставка не сыграла. Повезёт в следующий раз!",reply_markup=kb)




async def menshe(message):
	await bot.delete_message(kazik,message.message_id)
	time.sleep(0.3)
	global summ
	global id
	i=0
	limitcheck = open("limit.txt", "r")
	if message.entities[0].user:
		user = message.entities[0].user
		username = f"@{user.username}"
		name = user.full_name
		id = int(user.id)
		asset = message.text.split("отправил(а)")[1].split()[1]
		summ = float(message.text.split("отправил(а)")[1].split()[0].replace(',', ""))
		#summ = float(message.text.split("отправил(а)")[1].split()[0])
		if summ <= float(limitcheck.read()):
			if "💬 " in message.text:
				comment = message.text.split("💬 ")[1]
				await bot.send_message(kazik, f"""
🔑 Игрок: {name}
💵 Сумма ставки: {summ}$
💬 Комментарий: {comment}""", reply_markup=kb)
			winx = summ * 1.8
			cube = await bot.send_dice(kazik, "🎲")
			value = cube.dice.value
			#balkazna = await crypto.get_balance()
			
			if value < 4:
				try:
					await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
					await bot.send_message(kazik, f"""🎉 Поздравляем, вы выиграли {winx} USDT\n\n🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥 Удачи в следующих ставках!""")
				except:
					await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")
					await bot.send_message(kazik, f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!""")
			else:
				await bot.send_message(kazik, "❌ Твоя ставка не сыграла. Повезёт в следующий раз!",reply_markup=kb)





async def chet(message):
	await bot.delete_message(kazik,message.message_id)
	time.sleep(0.3)
	global summ
	global id
	i=0
	limitcheck = open("limit.txt", "r")
	if message.entities[0].user:
		user = message.entities[0].user
		username = f"@{user.username}"
		name = user.full_name
		id = int(user.id)
		asset = message.text.split("отправил(а)")[1].split()[1]
		summ = float(message.text.split("отправил(а)")[1].split()[0].replace(',', ""))
		#summ = float(message.text.split("отправил(а)")[1].split()[0])
		if summ <= float(limitcheck.read()):
			if "💬 " in message.text:
				comment = message.text.split("💬 ")[1]
				await bot.send_message(kazik, f"""
🔑 Игрок: {name}
💵 Сумма ставки: {summ}$
💬 Комментарий: {comment}""", reply_markup=kb)
			winx = summ * 1.8
			cube = await bot.send_dice(kazik, "🎲")
			value = cube.dice.value
			#balkazna = await crypto.get_balance()
			
			if value == 2:
				try:
					await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
					await bot.send_message(kazik, f"""🎉 Поздравляем, вы выиграли {winx} USDT\n\n🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥 Удачи в следующих ставках!""")
				except:
					await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")
					await bot.send_message(kazik, f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!""")
			elif value == 4:
					try:
						await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
						await bot.send_message(kazik, f"""🎉 Поздравляем, вы выиграли {winx} USDT\n\n🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥 Удачи в следующих ставках!""")
					except:
						await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")
					await bot.send_message(kazik, f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!""")
			elif value == 6:
					try:
						await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
						await bot.send_message(kazik, f"""🎉 Поздравляем, вы выиграли {winx} USDT\n\n🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥 Удачи в следующих ставках!""")
					except:
						await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")
						await bot.send_message(kazik, f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!""")
			else:
				await bot.send_message(kazik, "❌ Твоя ставка не сыграла. Повезёт в следующий раз!",reply_markup=kb)



async def nechet(message):
	await bot.delete_message(kazik,message.message_id)
	time.sleep(0.3)
	global summ
	global id
	i=0
	limitcheck = open("limit.txt", "r")
	if message.entities[0].user:
		user = message.entities[0].user
		username = f"@{user.username}"
		name = user.full_name
		id = int(user.id)
		asset = message.text.split("отправил(а)")[1].split()[1]
		summ = float(message.text.split("отправил(а)")[1].split()[0].replace(',', ""))
		#summ = float(message.text.split("отправил(а)")[1].split()[0])
		if summ <= float(limitcheck.read()):
			if "💬 " in message.text:
				comment = message.text.split("💬 ")[1]
				await bot.send_message(kazik, f"""
🔑 Игрок: {name}
💵 Сумма ставки: {summ}$
💬 Комментарий: {comment}""", reply_markup=kb)
			winx = summ * 1.8
			cube = await bot.send_dice(kazik, "🎲")
			value = cube.dice.value
			#balkazna = await crypto.get_balance()
			
			if value == 1:
				try:
					await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
					await bot.send_message(kazik, f"""🎉 Поздравляем, вы выиграли {winx} USDT\n\n🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥 Удачи в следующих ставках!""")
				except:
					await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")
					await bot.send_message(kazik, f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!""")
			elif value == 3:
					try:
						await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
						await bot.send_message(kazik, f"""🎉 Поздравляем, вы выиграли {winx} USDT\n\n🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥 Удачи в следующих ставках!""")
					except:
						await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")
					await bot.send_message(kazik, f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!""")
			elif value == 5:
					try:
						await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
						await bot.send_message(kazik, f"""🎉 Поздравляем, вы выиграли {winx} USDT\n\n🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥 Удачи в следующих ставках!""")
					except:
						await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")
						await bot.send_message(kazik, f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!""")
			else:
				await bot.send_message(kazik, "❌ Твоя ставка не сыграла. Повезёт в следующий раз!",reply_markup=kb)


def getproc(a, b):
	return a/b




global comment
@dp.channel_post_handler(chat_id=kazik)
async def echo(message: types.Message):
    global comment
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    #await message.answer("true")
    #comment = message.text.split("💬 ")[1]
    
    if message.entities[0].user:
    	user = message.entities[0].user
    	username = f"@{user.username}"
    	name = user.full_name
    	id = int(user.id)
    	asset = message.text.split("отправил(а)")[1].split()[1]
    	summ = float(message.text.split("отправил(а)")[1].split()[0].replace(',', ""))
    try:
    	comment = message.text.split("💬 ")[1]
    except:
    	await bot.delete_message(kazik, message.message_id)
    	finalback = summ - getproc(summ, 10)
    	await bot.send_message(kazik, f"""
❌ Ошибка для пользователя "{name}"

Такая команда не найдена.
Заберите обратно свои деньги с комиссей 10%""")
    	await crypto.transfer(user_id=id, asset="USDT", amount = finalback, spend_id=passgen())
   	
    if "больше" in comment.lower():
    	await bolshe(message)
    elif "меньше" in comment.lower():
    	await menshe(message)
    elif "нечет" in comment.lower():
    	await nechet(message)
    elif "чет" in comment.lower():
    	await chet(message)
    else:
    	await bot.delete_message(kazik, message.message_id)
    	finalback = summ - getproc(summ, 10)
    	await bot.send_message(kazik, f"""
❌ Ошибка для пользователя "{name}"

Такая команда не найдена.
Заберите обратно свои деньги с комиссей 10%""")
    	await crypto.transfer(user_id=id, asset="USDT", amount = finalback, spend_id=passgen())  
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
