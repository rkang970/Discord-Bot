import discord
import random
from discord.ext import commands
import time
import asyncio
import econ
import os

description = "test bot...!?!??! huhhhh..!??!?!?"
bot = commands.Bot(command_prefix = "?", descrption = description, intents = discord.Intents.all())
discord.Intents.all

def fakeip():
    num1 = random.randint(1, 255)
    num2 = random.randint(1, 255)
    num3 = random.randint(1, 255)
    num4 = random.randint(1, 255)
    num1 = str(num1)
    num2 = str(num2)
    num3 = str(num3)
    num4 = str(num4)
    message = "User IP Address: " + num1 + "." + num2 + "." + num3+ "." + num4
    return message

@bot.command(name = "bal")
async def bal(self, member:discord.Member = None):
    if member is None:
        member = self.message.author
    money = econ.get_balance(user_id=member.id)
    await self.send("%s has %s "%(member.name, money))
@bot.event

async def on_ready():
    print("logged in as")
    print(bot.user.name)
    print("-----------")
    game = discord.Game("with your balls")
    await bot.change_presence(status=discord.Status.online, activity = game)

@bot.command(name = "give", description = "Give money to the specified user")
async def give(self, amount: int, member:discord.Member = None):
    if member is None:
        member = self.message.author
    econ.give_money(member.id, amount)
    await self.send(f"i give {amount} money")

@bot.command(name = "work", description = "works lol")
async def work(self):
    wow = econ.work(self.message.author.id)
    await self.send(wow)


@bot.command(name = "transfer", description = "Takes money from the specified user")
async def transfer(self, amount: int, member:discord.Member = None):
    giver = self.message.author.id
    taker = member.id
    result = econ.take_money(giver, amount)
    if result == True:
        econ.give_money(taker, amount)
        await self.send("lmao ur poor now")
    else:
        await self.send("lol broke you cant afford")

@bot.command()
async def ipgrab(self, who:discord.Member):
    if "ipThings.txt" not in os.listdir():
        with open("ipThings.txt", "x"):
            pass
    with open("ipThings.txt", "r") as ips:
        lines = ips.readlines()
        res = ""
        for line in lines:
            a = line.split()
            if str(who.id) == a[0]:
                res = a[1]
        
    if res == "":
        with open("ipThings.txt", "a") as ips:
            res = "%s.%s.%s.%s"%(random.randint(10,255),random.randint(10,255),random.randint(10,255),random.randint(10,255),)
            msg = "%s %s\n"%(who.id, res)
            ips.write(msg)

    await self.send(res)
    await self.send("meomwewomoewm get doxxed :3")

@bot.command()
async def test(self):
    await self.send("GET OUT OF MY HEAD GET OUT OF MY HEAD")

@bot.command()
async def storedips(self):
    
    stored = ""
    with open("ipThings.txt", "r") as ips:
        lines = ips.readlines()
        for line in lines:
            a = line.split()
            stored += a[0]
            stored += " "
            stored += a[1]
            stored += "\n"
    await self.send(f"``` {stored} ```")

@bot.command()
async def game(self):
    num = random.randint(0,200)
    print(num)
    await self.send("guess a number")
    def check(msg):
        return msg.author == self.message.author 
    try:
        while True:
            message = await bot.wait_for("message", check = check, timeout=10)
            guess = int(message.content)
            if guess == num:
                await self.send("you won")
                break
            elif guess < num:
                await self.send("guess higher")
            elif guess > num:
                await self.send("guess lower")

    except asyncio.TimeoutError:
        await self.send("haha took to long to respond loser")

@bot.command()
async def sum(self):
    await self.send("what are you adding (pls separate with spaces)")
    def check(msg):
        return msg.author == self.message.author
    try:
        message = await bot.wait_for("message", check = check, timeout = 10)
        nums = message.content.split()
        sum = 0
        for i in range(len(nums)):
            sum += int(nums[i])
        print(sum)
        await self.send(sum)
    except asyncio.TimeoutError:
        await self.send("ran out of time bozo")

@bot.command()
async def 赌博(self, number: int=1):
    slot_result = econ.slot_machine(user_id=self.author.id, rolls=number)
    await self.send(slot_result)

'''@bot.command()
async def getuser_id(self, who:discord.Member):
    await self.send(who.user_id)

@bot.command()
async def getip(self):
    trolled = fakeip()
    embed = discord.Embed(
        title = "USER IP LOGGED:",
        description = trolled,
        colour = discord.Colour.blue()
    )

    await self.send(embed=embed)'''

@bot.command()
async def tsundere(self):
    await self.send("<@616808215908450305> be like: Hmph! 💢 💢 💢 Stop calling me a tsundere! Just because I show Alex just a little bit more attention than usual and really pay attention to him when he's online and love his voice doesn't mean im Tsun Tsun!! 😠 😠 😠 We're just really good friends okay?? We aren't dating or anything... n-not th-that I wouldn't mind going out with him.... 🥺 🥺 🥺 I-I-I mean it's not like i like him or anything!!! 😵‍💫 😵‍💫 😵‍💫")

@bot.command()
async def chineseman(self):
    embed = discord.Embed(
        title = "epic test",
        description = "人和恶魔有什么区别",
        colour = discord.Colour.blue()
    )
    embed.set_footer(text = "中国第一 I LOVE CHINA....!!!")
    embed.set_image(url = "https://cdn.discordapp.com/attachments/896181920076038154/963948721148678155/202201012055YCLjo0GX1i.jpg")
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/896181920076038154/963621680155086858/202201162150JuK3KsoFbpSh_1.jpg")
    embed.set_author(name = "Table Bot", icon_url = "https://cdn.discordapp.com/attachments/985653621276418051/998776465728483348/ralsei_blunt.jpg")

    await self.send(embed=embed)

bot.run("")
#put token here