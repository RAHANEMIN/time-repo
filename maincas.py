import logging
import random
import re
import time
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, Dispatcher, executor, types
#from aiocryptopay import AioCryptoPay, Networks
from aiocryptopay import AioCryptoPay, Networks
from aiogram.types import InputFile 









crypto = AioCryptoPay(token="193107:AA8gtf92CTb7j8FeVEQLIgOJxt0DKokKmE5", network=Networks.MAIN_NET) #токен криптобот
API_TOKEN = '7032782299:AAGVVWCkKsbMU7xUbs8JZBnROdpCEHRHijM' #токен бота
kazik = -1002048436909
news = -1002095366591 #айди канала с казом
button = InlineKeyboardButton("Сделать ставку", url="http://t.me/send?start=IVwlfCGk2t1W")

kb = InlineKeyboardMarkup().add(button)
log = "@kehdhdnennejd"
#ВСЕ НУЖНОЕ









# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

global action
action = 0


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


@dp.message_handler(commands=['kazna'])
async def kazna(message: types.Message):

	check = await crypto.get_balance()
	await message.answer(check)



@dp.message_handler(commands=['t'])
async def act(message: types.Message):
	act = open("act.txt", "r")
	action = act.read()
	if action == "1":
		print(10*1.1)

@dp.message_handler(commands=['actionset'])
async def act(message: types.Message):
	act = open("act.txt", "r")
	action = act.read()
	if action == "0":
		act.close()
		act = open("act.txt", "w")
		act.write("1")
		await message.answer("Акция включена")
		await bot.send_message(kazik, """
<b>❗️АКЦИЯ❗️
Все ваши ставки после начала акции будут умножены на "1.1"

👇Участвуйте в акции, нажав на кнопку ниже!</b>""", parse_mode='HTML', reply_markup=kb)
		await bot.send_message(news, """
<b>❗️АКЦИЯ❗️
Все ваши ставки после начала акции будут умножены на "1.1"

👇Участвуйте в акции, нажав на кнопку ниже!</b>""", reply_markup=kb, parse_mode='HTML')
	elif action == "1":
		act.close()
		act = open("act.txt", "w")
		act.write("0")
		await message.answer("Акция отключена")
		await bot.send_message(kazik, """
<b>❗️АКЦИЯ БЫЛА ЗАВЕРШЕНА❗️
Желаем вам сочных заносов и без акции!

👇Во всех верим, держем кулачки!</b>""", parse_mode='HTML', reply_markup=kb)
		await bot.send_message(news, """
<b>❗️АКЦИЯ БЫЛА ЗАВЕРШЕНА❗️
Желаем вам сочных заносов и без акции!

👇Во всех верим, держем кулачки!</b>""", reply_markup=kb, parse_mode='HTML')

kd = 2.7


@dp.message_handler(commands=['dcheck'])
async def donate(message: types.Message):
	allchecks = await crypto.get_checks()
	print(allchecks)
	await crypto.delete_check(int(message.text.split()[1]))
@dp.message_handler(commands=['donate'])
async def donate(message: types.Message):
	sum = message.text.split()[1]
	check = await crypto.create_invoice(asset="USDT", amount = sum)
	await message.answer(check)

@dp.message_handler(commands=['limset'])
async def setlimit(message: types.Message):
	sum = message.text.split()[1]
	await message.answer("Установлен лимит ставки: " + str(sum) + "$")
	lim = open("limit.txt", "w")
	lim.write(sum)
	
	
	
	

	
	

global summ
global id
id=0
summ = 0.0
async def bolshe(message):
	act = open("act.txt", "r")
	action = act.read()
	await bot.delete_message(kazik,message.message_id)
	losejpg = InputFile("lose.jpg")
	winjpg = InputFile("win.jpg")
	time.sleep(0.6)
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
				if action == "0":
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				else:
					summ = summ * 1.1
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу во время акции</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<b>[🎉] Акция: каждая ставка умножается на 1.1x! Успейте воспользоваться выгодой!</b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')

			cube = await bot.send_dice(kazik, "🎲")
			value = cube.dice.value

			
			if value > 3:
				winx = summ * 1.8
				time.sleep(kd)
				if winx < 1:
					check = await crypto.create_check(asset="USDT", amount=winx, pin_to_user_id=id)
					ch = str(check)
					chf = ch.split("hash=")[1]
					chf = chf.replace("\'", "")
					chff = chf
					ur = f"https://t.me/send?start={chff[:12]}"
					button = InlineKeyboardButton("Забрать чек", url=ur)
					kbb = InlineKeyboardMarkup().add(button)
					await bot.send_photo(kazik, photo=winjpg, caption=f"""
<b>💸 Поздравляем! Вы выиграли {winx} USD

<blockquote>👇 Получите свой приз, по кнопке ниже.</blockquote></b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kbb, parse_mode="HTML")
				else:
					try:
						await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
						await bot.send_photo(kazik, photo=winjpg, caption=f'''<b> 🎉 Поздравляем, вы выиграли {winx} USD! </b>

<blockquote> 🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥Желаем вам удачи в новых ставках!</blockquote>

<a href="https://t.me/c/2048436909/49">Как сделать ставку</a> | <a href="https://t.me/+S_G66vEv8y0zNjky">Новостной канал</a>''', parse_mode='HTML')
					except:
						await bot.send_photo(kazik, photo=winjpg, caption=f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
						await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")

			else:
				time.sleep(2.5)
				await bot.send_photo(kazik, photo=losejpg, caption=f"""
❌ <b> <i> Твоя ставка не сыграла. Повезёт в следующий раз!</i> </b>

<blockquote> Фортуна дружит с отважными. - Драйден </blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')









async def b2b(message):
	act = open("act.txt", "r")
	action = act.read()
	await bot.delete_message(kazik,message.message_id)
	losejpg = InputFile("lose.jpg")
	winjpg = InputFile("win.jpg")
	time.sleep(0.6)
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
				if action == "0":
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				else:
					summ = summ * 1.1
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу во время акции</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<b>[🎉] Акция: каждая ставка умножается на 1.1x! Успейте воспользоваться выгодой!</b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')

			
			cube = await bot.send_dice(kazik, "🎲")
			cube2 = await bot.send_dice(kazik, "🎲")
			value = cube.dice.value
			value2 = cube2.dice.value
			finalv = value + value2
			if value > 3 and value2 > 3:
				winx = summ * 2.8
			else:
				winx = 0

			if winx > 0:
				time.sleep(kd)
				if winx < 1:
					check = await crypto.create_check(asset="USDT", amount=winx, pin_to_user_id=id)
					ch = str(check)
					chf = ch.split("hash=")[1]
					chf = chf.replace("\'", "")
					chff = chf
					ur = f"https://t.me/send?start={chff[:12]}"
					button = InlineKeyboardButton("Забрать чек", url=ur)
					kbb = InlineKeyboardMarkup().add(button)
					await bot.send_photo(kazik, photo=winjpg, caption=f"""
<b>💸 Поздравляем! Вы выиграли {winx} USD

<blockquote>👇 Получите свой приз, по кнопке ниже.</blockquote></b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kbb, parse_mode="HTML")
				else:
					try:
						await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
						await bot.send_photo(kazik, photo=winjpg, caption=f"""<b> 🎉 Поздравляем, вы выиграли {winx} USD! </b>

<blockquote> 🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥Желаем вам удачи в новых ставках!</blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
					except:
						await bot.send_photo(kazik, photo=winjpg, caption=f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
						await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")			
			else:
				time.sleep(kd)
				await bot.send_photo(kazik, photo=losejpg, caption=f"""
❌ <b> <i> Твоя ставка не сыграла. Повезёт в следующий раз!</i> </b>

<blockquote> Фортуна дружит с отважными. - Драйден </blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')















async def b2m(message):
	act = open("act.txt", "r")
	action = act.read()
	await bot.delete_message(kazik,message.message_id)
	losejpg = InputFile("lose.jpg")
	winjpg = InputFile("win.jpg")
	time.sleep(0.6)
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
				if action == "0":
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				else:
					summ = summ * 1.1
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу во время акции</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<b>[🎉] Акция: каждая ставка умножается на 1.1x! Успейте воспользоваться выгодой!</b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
	
			cube = await bot.send_dice(kazik, "🎲")
			cube2 = await bot.send_dice(kazik, "🎲")
			value = cube.dice.value
			value2 = cube2.dice.value
			finalv = value + value2
			if value < 4 and value2 < 4:
				winx = summ * 2.8
			else:
				winx = 0

			if winx > 0:
				time.sleep(kd)
				if winx < 1:
					check = await crypto.create_check(asset="USDT", amount=winx, pin_to_user_id=id)
					ch = str(check)
					chf = ch.split("hash=")[1]
					chf = chf.replace("\'", "")
					chff = chf
					ur = f"https://t.me/send?start={chff[:12]}"
					button = InlineKeyboardButton("Забрать чек", url=ur)
					kbb = InlineKeyboardMarkup().add(button)
					await bot.send_photo(kazik, photo=winjpg, caption=f"""
<b>💸 Поздравляем! Вы выиграли {winx} USD

<blockquote>👇 Получите свой приз, по кнопке ниже.</blockquote></b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kbb, parse_mode="HTML")
				else:
					try:
						await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
						await bot.send_photo(kazik, photo=winjpg, caption=f"""<b> 🎉 Поздравляем, вы выиграли {winx} USD! </b>

<blockquote> 🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥Желаем вам удачи в новых ставках!</blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
					except:
						await bot.send_photo(kazik, photo=winjpg, caption=f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
						await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")			

			else:
				time.sleep(kd)
				await bot.send_photo(kazik, photo=losejpg, caption=f"""
❌ <b> <i> Твоя ставка не сыграла. Повезёт в следующий раз!</i> </b>

<blockquote> Фортуна дружит с отважными. - Драйден </blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')













async def menshe(message):
	act = open("act.txt", "r")
	action = act.read()
	await bot.delete_message(kazik,message.message_id)
	losejpg = InputFile("lose.jpg")
	winjpg = InputFile("win.jpg")
	time.sleep(0.6)
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
				if action == "0":
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				else:
					summ = summ * 1.1
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу во время акции</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<b>[🎉] Акция: каждая ставка умножается на 1.1x! Успейте воспользоваться выгодой!</b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
		
			cube = await bot.send_dice(kazik, "🎲")
			value = cube.dice.value

			
			if value < 4:
				winx = summ * 1.8
				time.sleep(kd)
				if winx < 1:
					check = await crypto.create_check(asset="USDT", amount=winx, pin_to_user_id=id)
					ch = str(check)
					chf = ch.split("hash=")[1]
					chf = chf.replace("\'", "")
					chff = chf
					ur = f"https://t.me/send?start={chff[:12]}"
					button = InlineKeyboardButton("Забрать чек", url=ur)
					kbb = InlineKeyboardMarkup().add(button)
					await bot.send_photo(kazik, photo=winjpg, caption=f"""
<b>💸 Поздравляем! Вы выиграли {winx} USD

<blockquote>👇 Получите свой приз, по кнопке ниже.</blockquote></b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kbb, parse_mode="HTML")
				else:
					try:
						await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
						await bot.send_photo(kazik, photo=winjpg, caption=f"""<b> 🎉 Поздравляем, вы выиграли {winx} USD! </b>

<blockquote> 🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥Желаем вам удачи в новых ставках!</blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
					except:
						await bot.send_photo(kazik, photo=winjpg, caption=f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
						await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")

			else:
				time.sleep(kd)
				await bot.send_photo(kazik, photo=losejpg, caption=f"""
❌ <b> <i> Твоя ставка не сыграла. Повезёт в следующий раз!</i> </b>

<blockquote> Фортуна дружит с отважными. - Драйден </blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')





async def chet(message):
	act = open("act.txt", "r")
	action = act.read()
	await bot.delete_message(kazik,message.message_id)
	losejpg = InputFile("lose.jpg")
	winjpg = InputFile("win.jpg")
	time.sleep(0.6)
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
				if action == "0":
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				else:
					summ = summ * 1.1
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу во время акции</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<b>[🎉] Акция: каждая ставка умножается на 1.1x! Успейте воспользоваться выгодой!</b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
			
			cube = await bot.send_dice(kazik, "🎲")
			value = cube.dice.value

			
			if value == 2:
				winx = summ * 1.8
				time.sleep(kd)
				if winx < 1:
					check = await crypto.create_check(asset="USDT", amount=winx, pin_to_user_id=id)
					ch = str(check)
					chf = ch.split("hash=")[1]
					chf = chf.replace("\'", "")
					chff = chf
					ur = f"https://t.me/send?start={chff[:12]}"
					button = InlineKeyboardButton("Забрать чек", url=ur)
					kbb = InlineKeyboardMarkup().add(button)
					await bot.send_photo(kazik, photo=winjpg, caption=f"""
<b>💸 Поздравляем! Вы выиграли {winx} USD

<blockquote>👇 Получите свой приз, по кнопке ниже.</blockquote></b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kbb, parse_mode="HTML")
				else:
					try:
						await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
						await bot.send_photo(kazik, photo=winjpg, caption=f"""<b> 🎉 Поздравляем, вы выиграли {winx} USD! </b>

<blockquote> 🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥Желаем вам удачи в новых ставках!</blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
					except:
						await bot.send_photo(kazik, photo=winjpg, caption=f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
						await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")

			elif value == 4:
				winx = summ * 1.8
				time.sleep(kd)
				if winx < 1:
					check = await crypto.create_check(asset="USDT", amount=winx, pin_to_user_id=id)
					ch = str(check)
					chf = ch.split("hash=")[1]
					chf = chf.replace("\'", "")
					chff = chf
					ur = f"https://t.me/send?start={chff[:12]}"
					button = InlineKeyboardButton("Забрать чек", url=ur)
					kbb = InlineKeyboardMarkup().add(button)
					await bot.send_photo(kazik, photo=winjpg, caption=f"""
<b>💸 Поздравляем! Вы выиграли {winx} USD

<blockquote>👇 Получите свой приз, по кнопке ниже.</blockquote></b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kbb, parse_mode="HTML")
				else:
					try:
						await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
						await bot.send_photo(kazik, photo=winjpg, caption=f"""<b> 🎉 Поздравляем, вы выиграли {winx} USD! </b>

<blockquote> 🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥Желаем вам удачи в новых ставках!</blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
					except:
						await bot.send_photo(kazik, photo=winjpg, caption=f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
						await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")


			elif value == 6:
				winx = summ * 1.8
				time.sleep(kd)
				if winx < 1:
					check = await crypto.create_check(asset="USDT", amount=winx, pin_to_user_id=id)
					ch = str(check)
					chf = ch.split("hash=")[1]
					chf = chf.replace("\'", "")
					chff = chf
					ur = f"https://t.me/send?start={chff[:12]}"
					button = InlineKeyboardButton("Забрать чек", url=ur)
					kbb = InlineKeyboardMarkup().add(button)
					await bot.send_photo(kazik, photo=winjpg, caption=f"""
<b>💸 Поздравляем! Вы выиграли {winx} USD

<blockquote>👇 Получите свой приз, по кнопке ниже.</blockquote></b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kbb, parse_mode="HTML")
				else:
					try:
						await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
						await bot.send_photo(kazik, photo=winjpg, caption=f"""<b> 🎉 Поздравляем, вы выиграли {winx} USD! </b>

<blockquote> 🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥Желаем вам удачи в новых ставках!</blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
					except:
						await bot.send_photo(kazik, photo=winjpg, caption=f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
						await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")



			else:
				time.sleep(2.5)
				await bot.send_photo(kazik, photo=losejpg, caption=f"""
❌ <b> <i> Твоя ставка не сыграла. Повезёт в следующий раз!</i> </b>

<blockquote> Фортуна дружит с отважными. - Драйден </blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')




async def nechet(message):
	act = open("act.txt", "r")
	action = act.read()
	await bot.delete_message(kazik,message.message_id)
	losejpg = InputFile("lose.jpg")
	winjpg = InputFile("win.jpg")
	time.sleep(0.6)
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
				if action == "0":
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				else:
					summ = summ * 1.1
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу во время акции</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<b>[🎉] Акция: каждая ставка умножается на 1.1x! Успейте воспользоваться выгодой!</b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
			
			cube = await bot.send_dice(kazik, "🎲")
			value = cube.dice.value

			
			if value == 1:
				winx = summ * 1.8
				time.sleep(kd)
				if winx < 1:
					check = await crypto.create_check(asset="USDT", amount=winx, pin_to_user_id=id)
					ch = str(check)
					chf = ch.split("hash=")[1]
					chf = chf.replace("\'", "")
					chff = chf
					ur = f"https://t.me/send?start={chff[:12]}"
					button = InlineKeyboardButton("Забрать чек", url=ur)
					kbb = InlineKeyboardMarkup().add(button)
					await bot.send_photo(kazik, photo=winjpg, caption=f"""
<b>💸 Поздравляем! Вы выиграли {winx} USD

<blockquote>👇 Получите свой приз, по кнопке ниже.</blockquote></b>""", reply_markup=kbb, parse_mode="HTML")
				else:
					try:
						await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
						await bot.send_photo(kazik, photo=winjpg, caption=f"""<b> 🎉 Поздравляем, вы выиграли {winx} USD! </b>

<blockquote> 🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥Желаем вам удачи в новых ставках!</blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
					except:
						await bot.send_photo(kazik, photo=winjpg, caption=f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
						await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")

			elif value == 3:
				winx = summ * 1.8
				time.sleep(kd)
				if winx < 1:
					check = await crypto.create_check(asset="USDT", amount=winx, pin_to_user_id=id)
					ch = str(check)
					chf = ch.split("hash=")[1]
					chf = chf.replace("\'", "")
					chff = chf
					ur = f"https://t.me/send?start={chff[:12]}"
					button = InlineKeyboardButton("Забрать чек", url=ur)
					kbb = InlineKeyboardMarkup().add(button)
					await bot.send_photo(kazik, photo=winjpg, caption=f"""
<b>💸 Поздравляем! Вы выиграли {winx} USD

<blockquote>👇 Получите свой приз, по кнопке ниже.</blockquote></b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kbb, parse_mode="HTML")
				else:
					try:
						await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
						await bot.send_photo(kazik, photo=winjpg, caption=f"""<b> 🎉 Поздравляем, вы выиграли {winx} USD! </b>

<blockquote> 🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥Желаем вам удачи в новых ставках!</blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
					except:
						await bot.send_photo(kazik, photo=winjpg, caption=f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
						await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")


			elif value == 5:
				winx = summ * 1.8
				time.sleep(kd)
				if winx < 1:
					check = await crypto.create_check(asset="USDT", amount=winx, pin_to_user_id=id)
					ch = str(check)
					chf = ch.split("hash=")[1]
					chf = chf.replace("\'", "")
					chff = chf
					ur = f"https://t.me/send?start={chff[:12]}"
					button = InlineKeyboardButton("Забрать чек", url=ur)
					kbb = InlineKeyboardMarkup().add(button)
					await bot.send_photo(kazik, photo=winjpg, caption=f"""
<b>💸 Поздравляем! Вы выиграли {winx} USD

<blockquote>👇 Получите свой приз, по кнопке ниже.</blockquote></b>""", reply_markup=kbb, parse_mode="HTML")
				else:
					try:
						await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
						await bot.send_photo(kazik, photo=winjpg, caption=f"""<b> 🎉 Поздравляем, вы выиграли {winx} USD! </b>

<blockquote> 🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥Желаем вам удачи в новых ставках!</blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
					except:
						await bot.send_photo(kazik, photo=winjpg, caption=f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
						await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")



			else:
				time.sleep(kd)
				await bot.send_photo(kazik, photo=losejpg, caption=f"""
❌ <b> <i> Твоя ставка не сыграла. Повезёт в следующий раз!</i> </b>

<blockquote> Фортуна дружит с отважными. - Драйден </blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')










async def basketpopal(message):
	act = open("act.txt", "r")
	action = act.read()
	await bot.delete_message(kazik,message.message_id)
	losejpg = InputFile("lose.jpg")
	winjpg = InputFile("win.jpg")
	time.sleep(0.5)
	global summ
	global id
	global typeb
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
				if action == "0":
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				else:
					summ = summ * 1.1
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу во время акции</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<b>[🎉] Акция: каждая ставка умножается на 1.1x! Успейте воспользоваться выгодой!</b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				time.sleep(0.6)
				bask = await bot.send_dice(kazik,emoji = "🏀")
				v = bask.dice.value
				winx = summ*1.8
				if v == 4 or v == 5:
					time.sleep(kd)
					if winx<1:
						check = await crypto.create_check(asset="USDT", amount=winx, pin_to_user_id=id)
						ch = str(check)
						chf = ch.split("hash=")[1]
						chf = chf.replace("\'", "")
						chff = chf
						ur = f"https://t.me/send?start={chff[:12]}"
						button = InlineKeyboardButton("Забрать чек", url=ur)
						kbb = InlineKeyboardMarkup().add(button)
						await bot.send_photo(kazik, photo=winjpg, caption=f"""
<b>💸 Поздравляем! Вы выиграли {winx} USD

<blockquote>👇 Получите свой приз, по кнопке ниже.</blockquote></b>""", reply_markup=kbb, parse_mode="HTML")
					else:
						try:
							await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
							await bot.send_photo(kazik, photo=winjpg, caption=f"""<b> 🎉 Поздравляем, вы выиграли {winx} USD! </b>

<blockquote> 🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥Желаем вам удачи в новых ставках!</blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
						except:
							await bot.send_photo(kazik, photo=winjpg, caption=f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
							await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")
				else:
					time.sleep(kd)
					await bot.send_photo(kazik, photo=losejpg, caption=f"""
❌ <b> <i> Твоя ставка не сыграла. Повезёт в следующий раз!</i> </b>

<blockquote> Фортуна дружит с отважными. - Драйден </blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')




async def basketmimo(message):
	act = open("act.txt", "r")
	action = act.read()
	await bot.delete_message(kazik,message.message_id)
	losejpg = InputFile("lose.jpg")
	winjpg = InputFile("win.jpg")
	time.sleep(0.5)
	global summ
	global id
	global typeb
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
				if action == "0":
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				else:
					summ = summ * 1.1
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу во время акции</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<b>[🎉] Акция: каждая ставка умножается на 1.1x! Успейте воспользоваться выгодой!</b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')

				time.sleep(0.6)
				bask = await bot.send_dice(kazik,emoji = "🏀")
				v = bask.dice.value
				winx = summ*1.3
				print(v)
				if v == 3 or v == 1 or v == 2:
					time.sleep(kd)
					if winx < 1:
						check = await crypto.create_check(asset="USDT", amount=winx, pin_to_user_id=id)
						ch = str(check)
						chf = ch.split("hash=")[1]
						chf = chf.replace("\'", "")
						chff = chf
						ur = f"https://t.me/send?start={chff[:12]}"
						button = InlineKeyboardButton("Забрать чек", url=ur)
						kbb = InlineKeyboardMarkup().add(button)
						await bot.send_photo(kazik, photo=winjpg, caption=f"""
<b>💸 Поздравляем! Вы выиграли {winx} USD

<blockquote>👇 Получите свой приз, по кнопке ниже.</blockquote></b>""", reply_markup=kbb, parse_mode="HTML")
					else:
						try:
							await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
							await bot.send_photo(kazik, photo=winjpg, caption=f"""<b> 🎉 Поздравляем, вы выиграли {winx} USD! </b>

<blockquote> 🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥Желаем вам удачи в новых ставках!</blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
						except:
							await bot.send_photo(kazik, photo=winjpg, caption=f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
								
							await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")
				else:
					time.sleep(kd)
					await bot.send_photo(kazik, photo=losejpg, caption=f"""
❌ <b> <i> Твоя ставка не сыграла. Повезёт в следующий раз!</i> </b>

<blockquote> Фортуна дружит с отважными. - Драйден </blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')










async def footpopal(message):
	act = open("act.txt", "r")
	action = act.read()
	await bot.delete_message(kazik,message.message_id)
	losejpg = InputFile("lose.jpg")
	winjpg = InputFile("win.jpg")
	time.sleep(0.5)
	global summ
	global id
	global typeb
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
				if action == "0":
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				else:
					summ = summ * 1.1
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу во время акции</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<b>[🎉] Акция: каждая ставка умножается на 1.1x! Успейте воспользоваться выгодой!</b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				time.sleep(0.6)
				bask = await bot.send_dice(kazik,emoji = "⚽")
				v = bask.dice.value
				winx = summ*1.3
				if v == 4 or v == 5 or v == 3:
					time.sleep(kd)
					if winx < 1:
						check = await crypto.create_check(asset="USDT", amount=winx, pin_to_user_id=id)
						ch = str(check)
						chf = ch.split("hash=")[1]
						chf = chf.replace("\'", "")
						chff = chf
						ur = f"https://t.me/send?start={chff[:12]}"
						button = InlineKeyboardButton("Забрать чек", url=ur)
						kbb = InlineKeyboardMarkup().add(button)
						await bot.send_photo(kazik, photo=winjpg, caption=f"""
<b>💸 Поздравляем! Вы выиграли {winx} USD

<blockquote>👇 Получите свой приз, по кнопке ниже.</blockquote></b>""", reply_markup=kbb, parse_mode="HTML")
					else:
						try:
							await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
							await bot.send_photo(kazik, photo=winjpg, caption=f"""<b> 🎉 Поздравляем, вы выиграли {winx} USD! </b>

<blockquote> 🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥Желаем вам удачи в новых ставках!</blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
						except:
							await bot.send_photo(kazik, photo=winjpg, caption=f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
							await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")
				else:
					time.sleep(kd)
					await bot.send_photo(kazik, photo=losejpg, caption=f"""
❌ <b> <i> Твоя ставка не сыграла. Повезёт в следующий раз!</i> </b>

<blockquote> Фортуна дружит с отважными. - Драйден </blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')









async def footmimo(message):
	act = open("act.txt", "r")
	action = act.read()
	await bot.delete_message(kazik,message.message_id)
	losejpg = InputFile("lose.jpg")
	winjpg = InputFile("win.jpg")
	time.sleep(0.5)
	global summ
	global id
	global typeb
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
				if action == "0":
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				else:
					summ = summ * 1.1
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу во время акции</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<b>[🎉] Акция: каждая ставка умножается на 1.1x! Успейте воспользоваться выгодой!</b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				time.sleep(0.6)
				bask = await bot.send_dice(kazik,emoji = "⚽")
				v = bask.dice.value
				winx = summ*1.8
				if v == 1 or v == 2:
					time.sleep(kd)
					if winx < 1:
						check = await crypto.create_check(asset="USDT", amount=winx, pin_to_user_id=id)
						ch = str(check)
						chf = ch.split("hash=")[1]
						chf = chf.replace("\'", "")
						chff = chf
						ur = f"https://t.me/send?start={chff[:12]}"
						button = InlineKeyboardButton("Забрать чек", url=ur)
						kbb = InlineKeyboardMarkup().add(button)
						await bot.send_photo(kazik, photo=winjpg, caption=f"""
<b>💸 Поздравляем! Вы выиграли {winx} USD

<blockquote>👇 Получите свой приз, по кнопке ниже.</blockquote></b>""", reply_markup=kbb, parse_mode="HTML")
					else:
						try:
							await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
							await bot.send_photo(kazik, photo=winjpg, caption=f"""<b> 🎉 Поздравляем, вы выиграли {winx} USD! </b>

<blockquote> 🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥Желаем вам удачи в новых ставках!</blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
						except:
							await bot.send_photo(kazik, photo=winjpg, caption=f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
							await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")
				else:
					time.sleep(kd)
					await bot.send_photo(kazik, photo=losejpg, caption=f"""
❌ <b> <i> Твоя ставка не сыграла. Повезёт в следующий раз!</i> </b>

<blockquote> Фортуна дружит с отважными. - Драйден </blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
				







async def pvp(message):
	act = open("act.txt", "r")
	action = act.read()
	await bot.delete_message(kazik,message.message_id)
	losejpg = InputFile("lose.jpg")
	winjpg = InputFile("win.jpg")
	time.sleep(0.5)
	global summ
	global id
	global typeb
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
				if action == "0":
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				else:
					summ = summ * 1.1
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу во время акции</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<b>[🎉] Акция: каждая ставка умножается на 1.1x! Успейте воспользоваться выгодой!</b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				time.sleep(0.6)
				cubep = await bot.send_dice(kazik, "🎲")
				cubeb = await bot.send_dice(kazik, "🎲")
				winx = summ*1.8
				playerv = cubep.dice.value
				botv = cubeb.dice.value
				
				if playerv > botv:
					time.sleep(kd)
					if winx < 1:
						check = await crypto.create_check(asset="USDT", amount=winx, pin_to_user_id=id)
						ch = str(check)
						chf = ch.split("hash=")[1]
						chf = chf.replace("\'", "")
						chff = chf
						ur = f"https://t.me/send?start={chff[:12]}"
						button = InlineKeyboardButton("Забрать чек", url=ur)
						kbb = InlineKeyboardMarkup().add(button)
						await bot.send_photo(kazik, photo=winjpg, caption=f"""
<b>💸 Поздравляем! Вы выиграли {winx} USD

<blockquote>👇 Получите свой приз, по кнопке ниже.</blockquote></b>""", reply_markup=kbb, parse_mode="HTML")
					else:
						try:
							await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
							await bot.send_photo(kazik, photo=winjpg, caption=f"""<b> 🎉 Поздравляем, вы выиграли {winx} USD! </b>

<blockquote> 🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥Желаем вам удачи в новых ставках!</blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
						except:
							await bot.send_photo(kazik, photo=winjpg, caption=f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
							await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")
				else:
					time.sleep(kd)
					await bot.send_photo(kazik, photo=losejpg, caption=f"""
❌ <b> <i> Твоя ставка не сыграла. Повезёт в следующий раз!</i> </b>

<blockquote> Фортуна дружит с отважными. - Драйден </blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
				if playerv == botv:
					time.sleep(kd)
					await bot.send_photo(kazik, photo=losejpg, caption=f"""
❌ <b> <i> Твоя ставка не сыграла. Повезёт в следующий раз!</i> </b>

<blockquote> Фортуна дружит с отважными. - Драйден </blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
				
				








async def cub1(message):
	act = open("act.txt", "r")
	action = act.read()
	await bot.delete_message(kazik,message.message_id)
	losejpg = InputFile("lose.jpg")
	winjpg = InputFile("win.jpg")
	time.sleep(0.5)
	global summ
	global id
	global typeb
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
				if action == "0":
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				else:
					summ = summ * 1.1
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу во время акции</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<b>[🎉] Акция: каждая ставка умножается на 1.1x! Успейте воспользоваться выгодой!</b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				time.sleep(0.6)
				winx = summ*3.0
				#typeb = comment.split("куб")[1]
				
				cubik = await bot.send_dice(kazik, "🎲")
				if cubik.dice.value == 1:
					time.sleep(kd)
					if winx < 1:

						check = await crypto.create_check(asset="USDT", amount=winx, pin_to_user_id=id)
						ch = str(check)
						chf = ch.split("hash=")[1]
						chf = chf.replace("\'", "")
						chff = chf
						ur = f"https://t.me/send?start={chff[:12]}"
						button = InlineKeyboardButton("Забрать чек", url=ur)
						kbb = InlineKeyboardMarkup().add(button)
						await bot.send_photo(kazik, photo=winjpg, caption=f"""
<b>💸 Поздравляем! Вы выиграли {winx} USD

<blockquote>👇 Получите свой приз, по кнопке ниже.</blockquote></b>""", reply_markup=kbb, parse_mode="HTML")
						
					else:
						try:
							await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
							await bot.send_photo(kazik, photo=winjpg, caption=f"""<b> 🎉 Поздравляем, вы выиграли {winx} USD! </b>

<blockquote> 🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥Желаем вам удачи в новых ставках!</blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
						except:
							await bot.send_photo(kazik, photo=winjpg, caption=f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
							await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")
				else:
					time.sleep(kd)
					await bot.send_photo(kazik, photo=losejpg, caption=f"""
❌ <b> <i> Твоя ставка не сыграла. Повезёт в следующий раз!</i> </b>

<blockquote> Фортуна дружит с отважными. - Драйден </blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')





async def cub2(message):
	act = open("act.txt", "r")
	action = act.read()
	await bot.delete_message(kazik,message.message_id)
	losejpg = InputFile("lose.jpg")
	winjpg = InputFile("win.jpg")
	time.sleep(0.5)
	global summ
	global id
	global typeb
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
				if action == "0":
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				else:
					summ = summ * 1.1
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу во время акции</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<b>[🎉] Акция: каждая ставка умножается на 1.1x! Успейте воспользоваться выгодой!</b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				time.sleep(0.6)
				winx = summ*3.0
				#typeb = comment.split("куб")[1]
				
				cubik = await bot.send_dice(kazik, "🎲")
				if cubik.dice.value == 2:
					time.sleep(kd)
					if winx < 1:

						check = await crypto.create_check(asset="USDT", amount=winx, pin_to_user_id=id)
						ch = str(check)
						chf = ch.split("hash=")[1]
						chf = chf.replace("\'", "")
						chff = chf
						ur = f"https://t.me/send?start={chff[:12]}"
						button = InlineKeyboardButton("Забрать чек", url=ur)
						kbb = InlineKeyboardMarkup().add(button)
						await bot.send_photo(kazik, photo=winjpg, caption=f"""
<b>💸 Поздравляем! Вы выиграли {winx} USD

<blockquote>👇 Получите свой приз, по кнопке ниже.</blockquote></b>""", reply_markup=kbb, parse_mode="HTML")
						
					else:
						try:
							await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
							await bot.send_photo(kazik, photo=winjpg, caption=f"""<b> 🎉 Поздравляем, вы выиграли {winx} USD! </b>

<blockquote> 🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥Желаем вам удачи в новых ставках!</blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
						except:
							await bot.send_photo(kazik, photo=winjpg, caption=f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
							await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")
				else:
					time.sleep(kd)
					await bot.send_photo(kazik, photo=losejpg, caption=f"""
❌ <b> <i> Твоя ставка не сыграла. Повезёт в следующий раз!</i> </b>

<blockquote> Фортуна дружит с отважными. - Драйден </blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')


async def cub3(message):
	act = open("act.txt", "r")
	action = act.read()
	await bot.delete_message(kazik,message.message_id)
	losejpg = InputFile("lose.jpg")
	winjpg = InputFile("win.jpg")
	time.sleep(0.5)
	global summ
	global id
	global typeb
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
				if action == "0":
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				else:
					summ = summ * 1.1
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу во время акции</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<b>[🎉] Акция: каждая ставка умножается на 1.1x! Успейте воспользоваться выгодой!</b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				time.sleep(0.6)
				winx = summ*3.0
				#typeb = comment.split("куб")[1]
				
				cubik = await bot.send_dice(kazik, "🎲")
				if cubik.dice.value == 3:
					time.sleep(kd)
					if winx < 1:

						check = await crypto.create_check(asset="USDT", amount=winx, pin_to_user_id=id)
						ch = str(check)
						chf = ch.split("hash=")[1]
						chf = chf.replace("\'", "")
						chff = chf
						ur = f"https://t.me/send?start={chff[:12]}"
						button = InlineKeyboardButton("Забрать чек", url=ur)
						kbb = InlineKeyboardMarkup().add(button)
						await bot.send_photo(kazik, photo=winjpg, caption=f"""
<b>💸 Поздравляем! Вы выиграли {winx} USD

<blockquote>👇 Получите свой приз, по кнопке ниже.</blockquote></b>""", reply_markup=kbb, parse_mode="HTML")
						
					else:
						try:
							await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
							await bot.send_photo(kazik, photo=winjpg, caption=f"""<b> 🎉 Поздравляем, вы выиграли {winx} USD! </b>

<blockquote> 🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥Желаем вам удачи в новых ставках!</blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
						except:
							await bot.send_photo(kazik, photo=winjpg, caption=f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
							await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")
				else:
					time.sleep(kd)
					await bot.send_photo(kazik, photo=losejpg, caption=f"""
❌ <b> <i> Твоя ставка не сыграла. Повезёт в следующий раз!</i> </b>

<blockquote> Фортуна дружит с отважными. - Драйден </blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')



async def cub4(message):
	act = open("act.txt", "r")
	action = act.read()
	await bot.delete_message(kazik,message.message_id)
	losejpg = InputFile("lose.jpg")
	winjpg = InputFile("win.jpg")
	time.sleep(0.5)
	global summ
	global id
	global typeb
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
				if action == "0":
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				else:
					summ = summ * 1.1
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу во время акции</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<b>[🎉] Акция: каждая ставка умножается на 1.1x! Успейте воспользоваться выгодой!</b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				time.sleep(0.6)
				winx = summ*3.0
				#typeb = comment.split("куб")[1]
				
				cubik = await bot.send_dice(kazik, "🎲")
				if cubik.dice.value == 4:
					time.sleep(kd)
					if winx < 1:

						check = await crypto.create_check(asset="USDT", amount=winx, pin_to_user_id=id)
						ch = str(check)
						chf = ch.split("hash=")[1]
						chf = chf.replace("\'", "")
						chff = chf
						ur = f"https://t.me/send?start={chff[:12]}"
						button = InlineKeyboardButton("Забрать чек", url=ur)
						kbb = InlineKeyboardMarkup().add(button)
						await bot.send_photo(kazik, photo=winjpg, caption=f"""
<b>💸 Поздравляем! Вы выиграли {winx} USD

<blockquote>👇 Получите свой приз, по кнопке ниже.</blockquote></b>""", reply_markup=kbb, parse_mode="HTML")
						
					else:
						try:
							await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
							await bot.send_photo(kazik, photo=winjpg, caption=f"""<b> 🎉 Поздравляем, вы выиграли {winx} USD! </b>

<blockquote> 🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥Желаем вам удачи в новых ставках!</blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
						except:
							await bot.send_photo(kazik, photo=winjpg, caption=f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
							await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")
				else:
					time.sleep(kd)
					await bot.send_photo(kazik, photo=losejpg, caption=f"""
❌ <b> <i> Твоя ставка не сыграла. Повезёт в следующий раз!</i> </b>

<blockquote> Фортуна дружит с отважными. - Драйден </blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')






async def cub5(message):
	act = open("act.txt", "r")
	action = act.read()
	await bot.delete_message(kazik,message.message_id)
	losejpg = InputFile("lose.jpg")
	winjpg = InputFile("win.jpg")
	time.sleep(0.5)
	global summ
	global id
	global typeb
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
				if action == "0":
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				else:
					summ = summ * 1.1
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу во время акции</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<b>[🎉] Акция: каждая ставка умножается на 1.1x! Успейте воспользоваться выгодой!</b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				time.sleep(0.6)
				winx = summ*3.0
				#typeb = comment.split("куб")[1]
				
				cubik = await bot.send_dice(kazik, "🎲")
				if cubik.dice.value == 5:
					time.sleep(kd)
					if winx < 1:

						check = await crypto.create_check(asset="USDT", amount=winx, pin_to_user_id=id)
						ch = str(check)
						chf = ch.split("hash=")[1]
						chf = chf.replace("\'", "")
						chff = chf
						ur = f"https://t.me/send?start={chff[:12]}"
						button = InlineKeyboardButton("Забрать чек", url=ur)
						kbb = InlineKeyboardMarkup().add(button)
						await bot.send_photo(kazik, photo=winjpg, caption=f"""
<b>💸 Поздравляем! Вы выиграли {winx} USD

<blockquote>👇 Получите свой приз, по кнопке ниже.</blockquote></b>""", reply_markup=kbb, parse_mode="HTML")
						
					else:
						try:
							await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
							await bot.send_photo(kazik, photo=winjpg, caption=f"""<b> 🎉 Поздравляем, вы выиграли {winx} USD! </b>

<blockquote> 🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥Желаем вам удачи в новых ставках!</blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
						except:
							await bot.send_photo(kazik, photo=winjpg, caption=f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
							await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")
				else:
					time.sleep(kd)
					await bot.send_photo(kazik, photo=losejpg, caption=f"""
❌ <b> <i> Твоя ставка не сыграла. Повезёт в следующий раз!</i> </b>

<blockquote> Фортуна дружит с отважными. - Драйден </blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')



async def cub6(message):
	act = open("act.txt", "r")
	action = act.read()
	await bot.delete_message(kazik,message.message_id)
	losejpg = InputFile("lose.jpg")
	winjpg = InputFile("win.jpg")
	time.sleep(0.5)
	global summ
	global id
	global typeb
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
				if action == "0":
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				else:
					summ = summ * 1.1
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу во время акции</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<b>[🎉] Акция: каждая ставка умножается на 1.1x! Успейте воспользоваться выгодой!</b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				time.sleep(0.6)
				winx = summ*3.0
				#typeb = comment.split("куб")[1]
				
				cubik = await bot.send_dice(kazik, "🎲")
				if cubik.dice.value == 1:
					time.sleep(kd)
					if winx < 1:

						check = await crypto.create_check(asset="USDT", amount=winx, pin_to_user_id=id)
						ch = str(check)
						chf = ch.split("hash=")[1]
						chf = chf.replace("\'", "")
						chff = chf
						ur = f"https://t.me/send?start={chff[:12]}"
						button = InlineKeyboardButton("Забрать чек", url=ur)
						kbb = InlineKeyboardMarkup().add(button)
						await bot.send_photo(kazik, photo=winjpg, caption=f"""
<b>💸 Поздравляем! Вы выиграли {winx} USD

<blockquote>👇 Получите свой приз, по кнопке ниже.</blockquote></b>""", reply_markup=kbb, parse_mode="HTML")
						
					else:
						try:
							await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
							await bot.send_photo(kazik, photo=winjpg, caption=f"""<b> 🎉 Поздравляем, вы выиграли {winx} USD! </b>

<blockquote> 🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥Желаем вам удачи в новых ставках!</blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
						except:
							await bot.send_photo(kazik, photo=winjpg, caption=f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
							await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")
				else:
					time.sleep(kd)
					await bot.send_photo(kazik, photo=losejpg, caption=f"""
❌ <b> <i> Твоя ставка не сыграла. Повезёт в следующий раз!</i> </b>

<blockquote> Фортуна дружит с отважными. - Драйден </blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')




async def plinko(message):
	act = open("act.txt", "r")
	action = act.read()
	await bot.delete_message(kazik,message.message_id)
	losejpg = InputFile("lose.jpg")
	winjpg = InputFile("win.jpg")
	time.sleep(0.3)
	global summ
	global id
	global typeb
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
				if action == "0":
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				else:
					summ = summ * 1.1
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу во время акции</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<b>[🎉] Акция: каждая ставка умножается на 1.1x! Успейте воспользоваться выгодой!</b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				time.sleep(0.6)
				dice = await bot.send_dice(kazik)
				v = dice.dice.value
				if v == 1:
					winx = 0
				elif v == 2:
					winx = summ*0.3
				elif v == 3:
					winx = summ*0.9
				elif v == 4:
					winx = summ*1.1
				elif v == 5:
					winx = summ*1.3
				elif v == 6:
					winx = summ*1.9

				if winx > 0:
					time.sleep(kd)
					if winx < 1:
						check = await crypto.create_check(asset="USDT", amount=winx, pin_to_user_id=id)
						ch = str(check)
						chf = ch.split("hash=")[1]
						chf = chf.replace("\'", "")
						chff = chf
						ur = f"https://t.me/send?start={chff[:12]}"
						button = InlineKeyboardButton("Забрать чек", url=ur)
						kbb = InlineKeyboardMarkup().add(button)
						await bot.send_photo(kazik, photo=winjpg, caption=f"""
<b>💸 Поздравляем! Вы выиграли {winx} USD

<blockquote>👇 Получите свой приз, по кнопке ниже.</blockquote></b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kbb, parse_mode="HTML")
					else:
						try:
							await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
							await bot.send_photo(kazik, photo=winjpg, caption=f"""<b> 🎉 Поздравляем, вы выиграли {winx} USD! </b>

<blockquote> 🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥Желаем вам удачи в новых ставках!</blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
						except:
							await bot.send_photo(kazik, photo=winjpg, caption=f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
							await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")
				else:
					time.sleep(kd)
					await bot.send_photo(kazik, photo=losejpg, caption=f"""
❌ <b> <i> Твоя ставка не сыграла. Повезёт в следующий раз!</i> </b>

<blockquote> Фортуна дружит с отважными. - Драйден </blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')									





async def krasnoe(message):
	act = open("act.txt", "r")
	action = act.read()
	await bot.delete_message(kazik,message.message_id)
	losejpg = InputFile("lose.jpg")
	winjpg = InputFile("win.jpg")
	time.sleep(0.5)
	global summ
	global id
	global typeb
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
				if action == "0":
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				else:
					summ = summ * 1.1
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу во время акции</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<b>[🎉] Акция: каждая ставка умножается на 1.1x! Успейте воспользоваться выгодой!</b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				time.sleep(0.4)
				dart = await bot.send_dice(kazik,emoji = "🎯")
				v = dart.dice.value
				if v == 2 or v == 4:
					time.sleep(kd)
					winx = summ*1.8
					if winx < 1:
						check = await crypto.create_check(asset="USDT", amount=winx, pin_to_user_id=id)
						ch = str(check)
						chf = ch.split("hash=")[1]
						chf = chf.replace("\'", "")
						chff = chf
						ur = f"https://t.me/send?start={chff[:12]}"
						button = InlineKeyboardButton("Забрать чек", url=ur)
						kbb = InlineKeyboardMarkup().add(button)
						await bot.send_photo(kazik, photo=winjpg, caption=f"""
<b>💸 Поздравляем! Вы выиграли {winx} USD

<blockquote>👇 Получите свой приз, по кнопке ниже.</blockquote></b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kbb, parse_mode="HTML")
					else:
						try:
							await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
							await bot.send_photo(kazik, photo=winjpg, caption=f"""<b> 🎉 Поздравляем, вы выиграли {winx} USD! </b>

<blockquote> 🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥Желаем вам удачи в новых ставках!</blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
						except:
							await bot.send_photo(kazik, photo=winjpg, caption=f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
							await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")
				else:
					time.sleep(2.5)
					winx=0
					await bot.send_photo(kazik, photo=losejpg, caption=f"""
❌ <b> <i> Твоя ставка не сыграла. Повезёт в следующий раз!</i> </b>

<blockquote> Фортуна дружит с отважными. - Драйден </blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')









async def beloe(message):
	act = open("act.txt", "r")
	action = act.read()
	await bot.delete_message(kazik,message.message_id)
	losejpg = InputFile("lose.jpg")
	winjpg = InputFile("win.jpg")
	time.sleep(0.5)
	global summ
	global id
	global typeb
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
				if action == "0":
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				else:
					summ = summ * 1.1
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу во время акции</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<b>[🎉] Акция: каждая ставка умножается на 1.1x! Успейте воспользоваться выгодой!</b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				time.sleep(0.6)
				dart = await bot.send_dice(kazik,emoji = "🎯")
				v = dart.dice.value
				if v == 3 or v == 5:
					time.sleep(3)
					winx = summ*1.8
					if winx < 1:
						check = await crypto.create_check(asset="USDT", amount=winx, pin_to_user_id=id)
						ch = str(check)
						chf = ch.split("hash=")[1]
						chf = chf.replace("\'", "")
						chff = chf
						ur = f"https://t.me/send?start={chff[:12]}"
						button = InlineKeyboardButton("Забрать чек", url=ur)
						kbb = InlineKeyboardMarkup().add(button)
						await bot.send_photo(kazik, photo=winjpg, caption=f"""
<b>💸 Поздравляем! Вы выиграли {winx} USD

<blockquote>👇 Получите свой приз, по кнопке ниже.</blockquote></b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kbb, parse_mode="HTML")
					else:
						try:
							await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
							await bot.send_photo(kazik, photo=winjpg, caption=f"""<b> 🎉 Поздравляем, вы выиграли {winx} USD! </b>

<blockquote> 🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥Желаем вам удачи в новых ставках!</blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
						except:
							await bot.send_photo(kazik, photo=winjpg, caption=f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!""", parse_mode='HTML')
							await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")
				else:
					time.sleep(kd)
					winx=0
					await bot.send_photo(kazik, photo=losejpg, caption=f"""
❌ <b> <i> Твоя ставка не сыграла. Повезёт в следующий раз!</i> </b>

<blockquote> Фортуна дружит с отважными. - Драйден </blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')







async def krasnoe(message):
	act = open("act.txt", "r")
	action = act.read()
	await bot.delete_message(kazik,message.message_id)
	losejpg = InputFile("lose.jpg")
	winjpg = InputFile("win.jpg")
	time.sleep(0.5)
	global summ
	global id
	global typeb
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
				if action == "0":
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				else:
					summ = summ * 1.1
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу во время акции</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<b>[🎉] Акция: каждая ставка умножается на 1.1x! Успейте воспользоваться выгодой!</b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				time.sleep(0.6)
				dart = await bot.send_dice(kazik,emoji = "🎯")
				v = dart.dice.value
				if v == 6:
					time.sleep(kd)
					winx = summ*1.8
					if winx < 1:
						check = await crypto.create_check(asset="USDT", amount=winx, pin_to_user_id=id)
						ch = str(check)
						chf = ch.split("hash=")[1]
						chf = chf.replace("\'", "")
						chff = chf
						ur = f"https://t.me/send?start={chff[:12]}"
						button = InlineKeyboardButton("Забрать чек", url=ur)
						kbb = InlineKeyboardMarkup().add(button)
						await bot.send_photo(kazik, photo=winjpg, caption=f"""
<b>💸 Поздравляем! Вы выиграли {winx} USD

<blockquote>👇 Получите свой приз, по кнопке ниже.</blockquote></b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kbb, parse_mode="HTML")
					else:
						try:
							await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
							await bot.send_photo(kazik, photo=winjpg, caption=f"""<b> 🎉 Поздравляем, вы выиграли {winx} USD! </b>

<blockquote> 🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥Желаем вам удачи в новых ставках!</blockquote>""", parse_mode='HTML')
						except:
							await bot.send_photo(kazik, photo=winjpg, caption=f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
							await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")
				else:
					time.sleep(kd)
					winx=0
					await bot.send_photo(kazik, photo=losejpg, caption=f"""
❌ <b> <i> Твоя ставка не сыграла. Повезёт в следующий раз!</i> </b>

<blockquote> Фортуна дружит с отважными. - Драйден </blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')










async def miss(message):
	act = open("act.txt", "r")
	action = act.read()
	await bot.delete_message(kazik,message.message_id)
	losejpg = InputFile("lose.jpg")
	winjpg = InputFile("win.jpg")
	time.sleep(0.3)
	global summ
	global id
	global typeb
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
				if action == "0":
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				else:
					summ = summ * 1.1
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу во время акции</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<b>[🎉] Акция: каждая ставка умножается на 1.1x! Успейте воспользоваться выгодой!</b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				time.sleep(0.4)
				dart = await bot.send_dice(kazik,emoji = "🎯")
				v = dart.dice.value
				if v == 1:
					time.sleep(kd)
					winx = summ*1.8
					if winx < 1:
						check = await crypto.create_check(asset="USDT", amount=winx, pin_to_user_id=id)
						ch = str(check)
						chf = ch.split("hash=")[1]
						chf = chf.replace("\'", "")
						chff = chf
						ur = f"https://t.me/send?start={chff[:12]}"
						button = InlineKeyboardButton("Забрать чек", url=ur)
						kbb = InlineKeyboardMarkup().add(button)
						await bot.send_photo(kazik, photo=winjpg, caption=f"""
<b>💸 Поздравляем! Вы выиграли {winx} USD

<blockquote>👇 Получите свой приз, по кнопке ниже.</blockquote></b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kbb, parse_mode="HTML")
					else:
						try:
							await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
							await bot.send_photo(kazik, photo=winjpg, caption=f"""<b> 🎉 Поздравляем, вы выиграли {winx} USD! </b>

<blockquote> 🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥Желаем вам удачи в новых ставках!</blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
						except:
							await bot.send_photo(kazik, photo=winjpg, caption=f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
							await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")
				else:
					time.sleep(kd)
					winx=0
					await bot.send_photo(kazik, photo=losejpg, caption=f"""
❌ <b> <i> Твоя ставка не сыграла. Повезёт в следующий раз!</i> </b>

<blockquote> Фортуна дружит с отважными. - Драйден </blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')




















async def slot(message):
	act = open("act.txt", "r")
	action = act.read()
	await bot.delete_message(kazik,message.message_id)
	losejpg = InputFile("lose.jpg")
	winjpg = InputFile("win.jpg")
	time.sleep(0.5)
	global summ
	global id
	global typeb
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
				if action == "0":
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				else:
					summ = summ * 1.1
					await bot.send_message(kazik, f"""
<b><blockquote>[✅] Ваша ставка принята в работу во время акции</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>

<b>[🎉] Акция: каждая ставка умножается на 1.1x! Успейте воспользоваться выгодой!</b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kb, parse_mode='HTML')
				time.sleep(0.6)
				slot = await bot.send_dice(kazik, emoji = "🎰")
				slotv = slot.dice.value
				
				if slotv == 64:
					winx=summ*13 #777
				elif slotv == 1:
					winx=summ*5 #bar
				elif slotv == 43:
					winx=summ*3 #limon
				elif slotv == 22:
					winx=summ*5 #yagodi
				else:
						time.sleep(kd)
						winx=0
						await bot.send_photo(kazik, photo=losejpg, caption=f"""
❌ <b> <i> Твоя ставка не сыграла. Повезёт в следующий раз!</i> </b>

<blockquote> Фортуна дружит с отважными. - Драйден </blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
				if winx > 0:
					time.sleep(kd)
					if winx<1:
						check = await crypto.create_check(asset="USDT", amount=winx, pin_to_user_id=id)
						ch = str(check)
						chf = ch.split("hash=")[1]
						chf = chf.replace("\'", "")
						chff = chf
						ur = f"https://t.me/send?start={chff[:12]}"
						button = InlineKeyboardButton("Забрать чек", url=ur)
						kbb = InlineKeyboardMarkup().add(button)
						await bot.send_photo(kazik, photo=winjpg, caption=f"""
<b>💸 Поздравляем! Вы выиграли {winx} USD

<blockquote>👇 Получите свой приз, по кнопке ниже.</blockquote></b>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", reply_markup=kbb, parse_mode="HTML")
					else:
						try:
							await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
							await bot.send_photo(kazik, photo=winjpg, caption=f"""<b> 🎉 Поздравляем, вы выиграли {winx} USD! </b>

<blockquote> 🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥Желаем вам удачи в новых ставках!</blockquote>

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
						except:
							await bot.send_photo(kazik, photo=winjpg, caption=f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!

<a href='https://t.me/c/2048436909/49'>Как сделать ставку</a> | <a href='https://t.me/+S_G66vEv8y0zNjky'>Новостной канал</a>""", parse_mode='HTML')
							await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")












async def knb(message, typ):
	await bot.delete_message(kazik,message.message_id)
	losejpg = InputFile("lose.jpg")
	winjpg = InputFile("win.jpg")
	time.sleep(0.3)
	global summ
	global id
	global hodt
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
<b><blockquote>[✅] Ваша ставка принята в работу</blockquote>

<blockquote>[👾] Никнейм игрока: {name}</blockquote>

<blockquote>[💰] Сумма ставки: {summ}</blockquote>

<blockquote>[💬] Комментарий: {comment}</blockquote> </b>""", reply_markup=kb, parse_mode='HTML')
				time.sleep(0.4)
				rnd = ["✊", "✌️", "🖐"]
				import random
				bothod = rnd[random.randint(0,2)]
				winx=summ*2.5
				if typ == "ножницы":
					hodt = "✌️"
				if typ == "камень":
					hodt = "✊"
				if typ == "бумага":
					hodt = "🖐"
				await bot.send_message(hodt)
				time.sleep(0.2)
				await bot.send_message(bothod)
				if bothod == 1:
					res = "✌️"
				if bothod == 0:
					res = "✊"
				if bothod == 2:
					res = "🖐"
				if typ == "ножницы":
					if bothod == 0:
						time.sleep(kd)
						await bot.send_photo(kazik, photo=losejpg, caption=f"""
❌ <b> <i> Твоя ставка не сыграла. Повезёт в следующий раз!</i> </b>

<blockquote> Фортуна дружит с отважными. - Драйден </blockquote>""", parse_mode='HTML')
				if typ == "ножницы":
					if bothod == 2:
						time.sleep(kd)

						try:
							await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
							await bot.send_photo(kazik, photo=winjpg, caption=f"""<b> 🎉 Поздравляем, вы выиграли {winx} USD! </b>

<blockquote> 🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥Желаем вам удачи в новых ставках!</blockquote>""", parse_mode='HTML')
						except:
							await bot.send_photo(kazik, photo=winjpg, caption=f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!""", parse_mode='HTML')
						await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")



				if typ == "бумага":
					if bothod == 0:
						time.sleep(kd)
						try:
							await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
							await bot.send_photo(kazik, photo=winjpg, caption=f"""<b> 🎉 Поздравляем, вы выиграли {winx} USD! </b>

<blockquote> 🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥Желаем вам удачи в новых ставках!</blockquote>""", parse_mode='HTML')
						except:
							await bot.send_photo(kazik, photo=winjpg, caption=f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!""", parse_mode='HTML')
						await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")
				if typ == "бумага":
					if bothod == 1:
						time.sleep(kd)
						await bot.send_photo(kazik, photo=losejpg, caption=f"""
❌ <b> <i> Твоя ставка не сыграла. Повезёт в следующий раз!</i> </b>

<blockquote> Фортуна дружит с отважными. - Драйден </blockquote>""", parse_mode='HTML')



				if typ == "камень":
					if bothod == 1:
						time.sleep(kd)
						try:
							await crypto.transfer(user_id=id, asset="USDT", amount=winx, spend_id=passgen())
							await bot.send_photo(kazik, photo=winjpg, caption=f"""<b> 🎉 Поздравляем, вы выиграли {winx} USD! </b>

<blockquote> 🚀 Ваш выигрыш успешно зачислен на ваш CryptoBot кошелёк. 
🔥Желаем вам удачи в новых ставках!</blockquote>""", parse_mode='HTML')
						except:
							await bot.send_photo(kazik, photo=winjpg, caption=f"""
🎉 Поздравляем, вы выиграли {winx}

🕦 Ваш выигрыш будет зачислен администраторами вручную.
🔥 Удачи в следующих ставках!""", parse_mode='HTML')
						await bot.send_message(log, f"Неуспешная выплата, ожидание ручного вывода для {username} ({id}) в размере {winx}")



				if typ == "камень":
					if bothod == 2:
						await bot.send_photo(kazik, photo=losejpg, caption=f"""
❌ <b> <i> Твоя ставка не сыграла. Повезёт в следующий раз!</i> </b>

<blockquote> Фортуна дружит с отважными. - Драйден </blockquote>""", parse_mode='HTML')





def getproc(a, b):
	return a/b




global comment
@dp.channel_post_handler(chat_id=kazik)
async def echo(message: types.Message):
    global comment
    global summ
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    #await message.answer("true")
    #comment = message.text.split("💬 ")[1]
    kd = 2.7
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
    		await crypto.transfer(user_id=id, asset="USDT", amount = finalback, spend_id=passgen())
    		await bot.send_message(kazik, f"""❌ Ошибка для пользователя "{name}"

Такая команда не найдена.
Заберите обратно свои деньги с комиссей 10%""")
    		await bot.send_message(log, f"{username} ({id}) хуй знает! Выпалата обратно так как нет команды: {finalback} (если меньше 1$ начисляем в ручную)")
    	if "больше" in comment.lower():
    		time.sleep(kd)
    		await bolshe(message)
    	elif "меньше" in comment.lower():
    		time.sleep(kd)
    		await menshe(message)
    	elif "нечет" in comment.lower():
    		time.sleep(kd)
    		await nechet(message)
    	elif "чет" in comment.lower():
    		time.sleep(kd)
    		await chet(message)
    	elif "слоты" in comment.lower():
    		time.sleep(kd)
    		await slot(message)
    	elif "баскет попал" in comment.lower():
    		time.sleep(kd)
    		await basketpopal(message)
    	elif "баскет промах" in comment.lower():
    		time.sleep(kd)
    		await basketmimo(message)
    	elif "красное" in comment.lower():
    		time.sleep(kd)
    		await krasnoe(message)
    	elif "белое" in comment.lower():
    		time.sleep(kd)
    		await beloe(message)
    	elif "центр" in comment.lower():
    		time.sleep(kd)
    		await centr(message)
    	elif "мимо" in comment.lower():
    		time.sleep(kd)
    		await miss(message)
    	elif "фут гол" in comment.lower():
    		time.sleep(kd)
    		await footpopal(message)
    	elif "2б" in comment.lower():
    		time.sleep(kd)
    		await b2b(message)
    	elif "2м" in comment.lower():
    		time.sleep(kd)
    		await b2m(message)
    	elif "фут промазал" in comment.lower():
    		time.sleep(kd)
    		await footmimo(message)
    	elif "1" in comment.lower():
    		time.sleep(kd)
    		await cub1(message)
    	elif "2" in comment.lower():
    		time.sleep(kd)
    		await cub2(message)
    	elif "3" in comment.lower():
    		time.sleep(kd)
    		await cub3(message)
    	elif "4" in comment.lower():
    		time.sleep(kd)
    		await cub4(message)
    	elif "5" in comment.lower():
    		time.sleep(kd)
    		await cub5(message)
    	elif "6" in comment.lower():
    		time.sleep(kd)
    		await cub6(message)
    	elif "дуэль" in comment.lower():
    		time.sleep(kd)
    		await pvp(message)
    	elif "плинко" in comment.lower():
    		time.sleep(kd)
    		await plinko(message)
    	else:
    		finalback = summ - getproc(summ, 10)
    		try:
    			await crypto.transfer(user_id=id, asset="USDT", amount = finalback, spend_id=passgen())
    			await bot.send_message(kazik, f"""
❌ Ошибка для пользователя "{name}"

Такая команда не найдена.
Заберите обратно свои деньги с комиссей 10%""")
    		except:
    			check = await crypto.create_check(asset="USDT", amount=finalback, pin_to_user_id=id)
    			ch = str(check)
    			chf = ch.split("hash=")[1]
    			chf = chf.replace("\'", "")
    			chff = chf
    			ur = f"https://t.me/send?start={chff[:12]}"
    			button = InlineKeyboardButton("Забрать чек", url=ur)
    			kbb = InlineKeyboardMarkup().add(button)
    			await bot.send_message(kazik, f"""
❌ Ошибка для пользователя "{name}"

Такая команда не найдена.
Заберите обратно свои деньги с комиссей 10%""", reply_markup=kbb, parse_mode="HTML")
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
