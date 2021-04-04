import discord
import smtplib
from discord.ext import commands
import mysql.connector


mydb = mysql.connector.connect(host="localhost", user="root", password="************", database="mydb")

mycursor = mydb.cursor()

def schedule(data):
    fil = open("schedule.txt", "a")
    fil.write(data)
    fil.close
    return data


def mailer(data, reciever, subject):
    message = data
    sender = "***************.com"
    password = "****"
    body = 'Subject: {}\n\n{}'.format(subject, message)
    with smtplib.SMTP("smtp.gmail.com", 587) as smtpserver:
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        smtpserver.login(sender, password)
        smtpserver.sendmail(sender, reciever, body)



TOKEN = "*******************************************"
client = commands.Bot(command_prefix="")

@client.event
async def on_ready():
    print("bot is ready to takeoff")



@client.command(aliases=['add_entry', 'Add_entry', 'add', 'Add'])
@commands.has_permissions(kick_members=True)
async def ADD(ctx, *, data):
    string = schedule(data)
    await ctx.send(string)


@client.command(aliases=['Send_mail', 'SEND_MAIL'])
@commands.has_permissions(kick_members=True)
async def send_mail(ctx, data, reciever, subject):
    files = open("editor.txt", "w")
    files.write(data)

    mailer(data, reciever, subject)
    await ctx.send("message sent")


@client.command(aliases=['marks5'])
async def Marks5(ctx, *, data):
    await ctx.send("pending")
    sql = "INSERT INTO Question5Marks (questions) VALUES (%s)"
    val = [data]
    mycursor.execute(sql, val)
    mydb.commit()
    await ctx.send("Question Added")

@client.command(aliases=['marks4'])
async def Marks4(ctx, *, data):
    await ctx.send("pending")
    sql = "INSERT INTO Question4Marks (questions) VALUES (%s)"
    val = [data]
    mycursor.execute(sql, val)
    mydb.commit()
    await ctx.send("Question Added")

@client.command(aliases=['marks3'])
async def Marks3(ctx, *, data):
    await ctx.send("pending")
    sql = "INSERT INTO Question3Marks (questions) VALUES (%s)"
    val = [data]
    mycursor.execute(sql, val)
    mydb.commit()
    await ctx.send("Question Added")

@client.command(aliases=['marks2'])
async def Marks2(ctx, *, data):
    await ctx.send("pending")
    sql = "INSERT INTO Question2Marks (questions) VALUES (%s)"
    val = [data]
    mycursor.execute(sql, val)
    mydb.commit()
    await ctx.send("Question Added")@client.command(aliases=['marks5'])

@client.command(aliases=['marks1'])
async def Marks1(ctx, *, data):
    await ctx.send("pending")
    sql = "INSERT INTO Question1Marks (questions) VALUES (%s)"
    val = [data]
    mycursor.execute(sql, val)
    mydb.commit()
    await ctx.send("Question Added")



@client.command(aliases=['Show_mark5', 'Show_Mark5', 'SHOW_MARK5'])
@commands.has_permissions(kick_members=True)
async def show_mark5(ctx):
    mycursor.execute("SELECT * FROM Question5Marks ORDER BY RAND() LIMIT 1;")
    myresult = mycursor.fetchone()
    await ctx.send(myresult)

@client.command(aliases=['Show_mark4', 'Show_Mark4', 'SHOW_MARK4'])
@commands.has_permissions(kick_members=True)
async def show_mark4(ctx):
    mycursor.execute("SELECT * FROM Question4Marks ORDER BY RAND() LIMIT 1;")
    myresult = mycursor.fetchone()
    await ctx.send(myresult)

@client.command(aliases=['Show_mark3', 'Show_Mark3', 'SHOW_MARK3'])
@commands.has_permissions(kick_members=True)
async def show_mark3(ctx):
    mycursor.execute("SELECT * FROM Question3Marks ORDER BY RAND() LIMIT 1;")
    myresult = mycursor.fetchone()
    await ctx.send(myresult)

@client.command(aliases=['Show_mark2', 'Show_Mark2', 'SHOW_MARK2'])
@commands.has_permissions(kick_members=True)
async def show_mark2(ctx):
    mycursor.execute("SELECT * FROM Question2Marks ORDER BY RAND() LIMIT 1;")
    myresult = mycursor.fetchone()
    await ctx.send(myresult)

@client.command(aliases=['Show_mark1', 'Show_Mark1', 'SHOW_MARK1'])
@commands.has_permissions(kick_members=True)
async def show_mark1(ctx):
    mycursor.execute("SELECT * FROM Question1Marks ORDER BY RAND() LIMIT 1;")
    myresult = mycursor.fetchone()
    await ctx.send(myresult)


@client.command(aliases=['Showall_mark5', 'Showall_Mark5', 'SHOWALL_MARK5'])
@commands.has_permissions(kick_members=True)
async def showall_mark5(ctx):
    mycursor.execute("SELECT * FROM Question5Marks;")
    myresult = mycursor.fetchall()
    await ctx.send(myresult)

@client.command(aliases=['Showall_mark4', 'Showall_Mark4', 'SHOWALL_MARK4'])
@commands.has_permissions(kick_members=True)
async def showall_mark4(ctx):
    mycursor.execute("SELECT * FROM Question4Marks;")
    myresult = mycursor.fetchall()
    await ctx.send(myresult)

@client.command(aliases=['Showall_mark3', 'Showall_Mark3', 'SHOWALL_MARK3'])
@commands.has_permissions(kick_members=True)
async def showall_mark3(ctx):
    mycursor.execute("SELECT * FROM Question3Marks;")
    myresult = mycursor.fetchall()
    await ctx.send(myresult)

@client.command(aliases=['Showall_mark2', 'Showall_Mark2', 'SHOWALL_MARK2'])
@commands.has_permissions(kick_members=True)
async def showall_mark2(ctx):
    mycursor.execute("SELECT * FROM Question2Marks;")
    myresult = mycursor.fetchall()
    await ctx.send(myresult)

@client.command(aliases=['Showall_mark1', 'Showall_Mark1', 'SHOWALL_MARK1'])
@commands.has_permissions(kick_members=True)
async def showall_mark1(ctx):
    mycursor.execute("SELECT * FROM Question1Marks;")
    myresult = mycursor.fetchall()
    await ctx.send(myresult)





@client.command(aliases=['Kick'])
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="You have been kicked for bot testing"):
    try:
        await member.send("you have been kicked for testing purpose try rejoining with this link: https://discord.gg/w6Atau")
    except:
        await ctx.send("dm is closed")
    await member.kick(reason=reason)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Kripya Aukaat Ansusaar Commands Ka Prayog Kare")

    async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Incomplete Command")
            await ctx.message.deleat()


@client.command(aliases=['d'])
@commands.has_permissions(manage_guild=True)
async def deleat(ctx, amount=2):
    await ctx.channel.purge(limit=amount)


client.run(TOKEN)
