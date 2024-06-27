import os
import discord
from discord.ext import commands
from discord import app_commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())




# ///////////////////////////// Bot Event ///////////////////////////////////////////////
# คำสั่ง bot พร้อมใช้งานแล้ว
@bot.event
async def on_ready():
    print("Bot Online!")
    synced = await bot.tree.sync()
    print(f"{len(synced)} command(s)")




#แจ้งคนเข้า-ออก

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1255647657477542021) # ID ห้อง log
    text = f"Welcome To The Server, {member.mention}!" # ข้อความที่อยากใส่

    emmbed = discord.Embed(title = 'User นี้ได้ทำการเข้าร่วม Server!',
                           description = text,
                           color = 0x05FF00)


    await channel.send(text) # ส่งข้อความไปที่ห้อง log
    await channel.send(embed = emmbed) # ส่ง Embed ไปที่ห้อง log
    await member.send(text) # ส่งข้อความไปที่แชทส่วนตัว member


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1255647657477542021) # ID ห้อง bye
    text = f"{member.name} Bye!" # ข้อความที่อยากใส่

    emmbed = discord.Embed(title = ' User นี้ได้ทำการออกจาก Server!',
                           description = text,
                           color = 0xFF0000)
    

    await channel.send(text) # ส่งข้อความไปที่ห้อง bye
    await channel.send(embed = emmbed) # ส่ง Embed ไปที่ห้อง log




# -----------------------------------------------------------------------------------------------------------------------------

# คำสั่ง ChatBot
@ bot.event
async def on_message(message):
    mes = message.content # ดึงข้อความที่ถูกส่งมา
    if mes == 'hello':
        await message.channel.send("Hello It's me") # ข้อความส่งกลับไปที่ห้องนั้น

    elif mes == 'hi bot':
        await message.channel.send("Hello, " + str(message.author.name))

    await bot.process_commands(message)
    # ทำคำสั่ง event แล้วไปทำคำสั่ง bot command ต่อ




# ///////////////////////// Commands /////////////////////////
# กำหนดคำสั่งให้บอท

@bot.command()
async def hello(ctx):
    await ctx.send(f"hello {ctx. author.name} !")



@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)






# Slash Commands
@bot.tree.command(name='hellobot', description='Replies with Hello')
async def hellocommand(interaction):
    await interaction.response.send_message("Hello It's me Bot DISCORD")


@bot.tree.command(name='name')
@app_commands.describe(name = "What's your name?")
async def namecommand(interaction, name : str):
    await interaction.response.send_message(f"Hello {name}")



# Embeds

@bot.tree.command(name='help', description='Bot Command')
async def helpcommand(interaction):
    emmbed = discord.Embed(title='Help Me! - Bot Commands',
                           description='Bot Commands',
                           color=0x66FFFF,
                           timestamp= discord.utils.utcnow())
    

    emmbed.add_field(name='/hello1', value='Hello Command', inline=False) # ข้อความ 1
    emmbed.add_field(name='/hello2', value='Hello Command', inline=False) # ข้อความ 2
    emmbed.add_field(name='/hello3', value='Hello Command', inline=False) # ข้อความ 3

    emmbed.set_author(name='Author', url='https://youtu.be/MFtfIpt7DfY?si=psfocVtv-xKpSAzX', icon_url='https://cdn.discordapp.com/attachments/1020003545229041725/1255791913257140314/Test-log.png?ex=667e6adb&is=667d195b&hm=00b9a82d4d8c88ab6b644f3d62e7197daa2418096955556227da62fba12c3d13&')

    # ใส่รูปเล็ก-ใหญ่
    emmbed.set_thumbnail(url='https://cdn.discordapp.com/attachments/1020003545229041725/1255791913257140314/Test-log.png?ex=667e6adb&is=667d195b&hm=00b9a82d4d8c88ab6b644f3d62e7197daa2418096955556227da62fba12c3d13&')
    emmbed.set_image(url='https://cdn.discordapp.com/attachments/1020003545229041725/1255791913257140314/Test-log.png?ex=667e6adb&is=667d195b&hm=00b9a82d4d8c88ab6b644f3d62e7197daa2418096955556227da62fba12c3d13&')

    #Footer เนื้อหาส่วนสุดท้าย
    emmbed.set_footer(text='Footer',icon_url='https://cdn.discordapp.com/attachments/1020003545229041725/1255791913257140314/Test-log.png?ex=667e6adb&is=667d195b&hm=00b9a82d4d8c88ab6b644f3d62e7197daa2418096955556227da62fba12c3d13&')



    await interaction.response.send_message(embed = emmbed)




bot.run(os.getenv('TOKEN'))