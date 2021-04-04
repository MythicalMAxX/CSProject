from discord.ext import commands
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="**********", database="mydb")

mycursor = mydb.cursor()

TOKEN = "*******************************************"
client = commands.Bot(command_prefix="$")

@client.event
async def on_ready():
    print("bot is ready to takeoff")

@client.command(aliases=['INTRO'])
async def Intro(ctx):
    await ctx.send("hi i am memer dog")

@client.command(aliases=['mysqledit'])
async def Mysqledit(ctx, *, data):
    sql = data
    mycursor.execute(sql)
    mydb.commit()
    await ctx.send("Commit succesfull")

@client.command(aliases=['mysql'])
async def Mysql(ctx, *, data):
    sql = data
    mycursor.execute(sql)
    try:
        myresult = mycursor.fetchall()
    except:
        myresult = mycursor.fetchone()
    await ctx.send("Commit succesfull")
    await ctx.send(myresult)


client.run(TOKEN)