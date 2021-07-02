import requests
import discord
import time

from discord.ext import commands

bot = commands.Bot(command_prefix="!")

def check(token):
	res = requests.get("https://discordapp.com/api/v6/users/@me", headers={"Authorization": f"{token}"})
	response = res.json()
	location = response["locale"]
	name = response["username"]
	tag = response["discriminator"]
	username = f"{name}#{tag}"
	client_id = response["id"]
	email = response["email"]
	phone_number = response["phone"]
	adult = response["nsfw_allowed"]
	doubleauth = response["mfa_enabled"]
	if adult == True:
		adu = "18歳以上"
	else:
		adu = "18歳以上"

	if doubleauth == True:
		dauth = "有効"
	else:
		dauth = "無効"

	message = f"=== Token Checker ===\n国: {location}\nユーザーネーム: {username}\nユーザーID: {client_id}\nメールアドレス: {email}\n電話番号: {phone_number}\n年齢: {adu}\n二段階認証: {dauth}"
	return message

@bot.event
async def on_ready():
	print("Success")

@bot.command()
async def tokenc(tokenc, t=None):
	if t == None:
		await tokenc.send("Tokenを指定してください。")
	response = check(t)
	await tokenc.send(response)

try:
	bot.run("token")
except:
	print("Failed")
	time.sleep(10)
	exit()