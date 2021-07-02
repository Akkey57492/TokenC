import requests
import pprint

token = input("Token: ")
res = requests.get("https://discordapp.com/api/v6/users/@me", headers={"authorization": f"{token}"})
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
	adu = "18歳以下"

if doubleauth == True:
	dauth = "有効"
else:
	dauth = "無効"

message = f"=== Token Checker ===\nユーザーネーム: {username}\nユーザーID: {client_id}\nメールアドレス: {email}\n電話番号: {phone_number}\n年齢: {adu}\n二段階認証: {dauth}"

print(message)
input("Enterキーを押すことで閉じます")
exit()