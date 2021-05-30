import discord
import os
#import pynacl
#import dnspython
import server
import requests
from discord.ext import commands
import random

client = commands.Bot(command_prefix='?/')
memberlist = []

def Convert(lst):
  res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
  return res_dct

def listToString(s):	
  str1 = ""
  for ele in s:
    str1 += ele
  return str1
a = 1
role_allowed = []
@client.event
async def on_ready():
  print("Project is ready")


  


@client.command()
async def warn(ctx, member: discord.Member, *, reason):
  yes = 0
  role1 = discord.utils.get(ctx.guild.roles, name='Head Administrator')
  role2 = discord.utils.get(ctx.guild.roles, name='Assistant Sheriff')
  role3 = discord.utils.get(ctx.guild.roles, name='Undersheriff')
  role4 = discord.utils.get(ctx.guild.roles, name='Sheriff')
  role5 = discord.utils.get(ctx.guild.roles, name='Co Founder')
  role6 = discord.utils.get(ctx.guild.roles, name='Founder')
  role9 = discord.utils.get(ctx.guild.roles, name='Developer')
  if role1 not in role_allowed:
    role_allowed.append(role1)
  if role2 not in role_allowed:
    role_allowed.append(role2)
  if role3 not in role_allowed:
    role_allowed.append(role3)
  if role4 not in role_allowed:
    role_allowed.append(role4)
  if role5 not in role_allowed:
    role_allowed.append(role5)
  if role6 not in role_allowed:
    role_allowed.append(role6) 
  if role9 not in role_allowed:
    role_allowed.append(role9)
  yes = 0
  for i in role_allowed:
    if i in ctx.author.roles:
      key1 = str(member)
      #db[key1] = db[key1] + 1
      embed = discord.Embed(title=f'Warning from {ctx.author}',
      description= f'Warning for {reason}', color=0x34eb3d)
      await member.create_dm()
      await member.dm_channel.send(embed=embed)
      await ctx.send("Warning sent!")
      yes = 1
      break
  if yes == 0:
    embed = discord.Embed(title="Permission Denied.",description= "You are missing these role(s): Head Administrator, Assistant Sheriff, Undersheriff, Sheriff, Co Founder, Founder, Administrator, Head administrator, or Developer", color=0xf54242)
    await ctx.send(embed=embed)
    print("Permission Denied.")
		


@client.command()
async def clearwarnings(ctx, member: discord.Member):
  yes = 0
  role1 = discord.utils.get(ctx.guild.roles, name='Head Administrator')
  role2 = discord.utils.get(ctx.guild.roles, name='Assistant Sheriff')
  role3 = discord.utils.get(ctx.guild.roles, name='Undersheriff')
  role4 = discord.utils.get(ctx.guild.roles, name='Sheriff')
  role5 = discord.utils.get(ctx.guild.roles, name='Co Founder')
  role6 = discord.utils.get(ctx.guild.roles, name='Founder')
  role9 = discord.utils.get(ctx.guild.roles, name='Developer')
  if role1 not in role_allowed:
    role_allowed.append(role1)
  if role2 not in role_allowed:
    role_allowed.append(role2)
  if role3 not in role_allowed:
    role_allowed.append(role3)
  if role4 not in role_allowed:
    role_allowed.append(role4)
  if role5 not in role_allowed:
    role_allowed.append(role5)
  if role6 not in role_allowed:
    role_allowed.append(role6) 
  if role9 not in role_allowed:
    role_allowed.append(role9)
  for i in role_allowed:
    if i in ctx.author.roles:
      key1 = str(member)
      #db[key1] = 0
      await member.create_dm()
      await member.dm_channel.send('Your warnings has been cleared!')
      await ctx.send(f'Warnings cleared for {key1}')
      yes = 1
      break
    if yes == 0:
      embed = discord.Embed(
		    title="Permission Denied.", description=
		  "You are missing these role(s): Head Administrator, Assistant Sheriff, Undersheriff, Sheriff, Co Founder, Founder, Administrator, Head administrator, or Developer",
		  color=0xf54242)
      await ctx.send(embed=embed)


@client.command()
async def checkwarnings(ctx, member: discord.Member):
  key1 = str(member)
  value = db[key1]
  embed = discord.Embed(description=f'This member has {value} warnings',
  color = 0xf54242)
  await ctx.send(embed=embed)

@client.command(pass_context=True)
async def report(ctx, member: discord.Member, *, reason):
  def check(msg):
    return msg.author == ctx.author and msg.channel == name.dm_channel
  yes = 0
  role1 = discord.utils.get(ctx.guild.roles, name='Head Administrator')
  role2 = discord.utils.get(ctx.guild.roles, name='Assistant Sheriff')
  role3 = discord.utils.get(ctx.guild.roles, name='Undersheriff')
  role4 = discord.utils.get(ctx.guild.roles, name='Sheriff')
  role5 = discord.utils.get(ctx.guild.roles, name='Co Founder')
  role6 = discord.utils.get(ctx.guild.roles, name='Founder')
  role9 = discord.utils.get(ctx.guild.roles, name='Developer')
  if role1 not in role_allowed:
    role_allowed.append(role1)
  if role2 not in role_allowed:
    role_allowed.append(role2)
  if role3 not in role_allowed:
    role_allowed.append(role3)
  if role4 not in role_allowed:
    role_allowed.append(role4)
  if role5 not in role_allowed:
    role_allowed.append(role5)
  if role6 not in role_allowed:
    role_allowed.append(role6) 
  if role9 not in role_allowed:
    role_allowed.append(role9)
  for i in role_allowed:
    if i in ctx.author.roles:
      user = await client.fetch_user(723483241075572769)
      await user.create_dm()
      await user.dm_channel.send(f'{ctx.author} reported {member} for {reason}. Do you Accept or Deny it?(A/D)')
      msg = await client.wait_for("message", check=check)
      answer = str(msg.content)
      await user.create_dm()
      if answer == "A":
        await user.dm_channel.send("The report was accepted")
      else:
        await user.dm_channel.send("The report was denied")
      yes = 1
      break

  if yes == 0:
      embed = discord.Embed(
		    title="Permission Denied.", description=
		  "You are missing these role(s): Head Administrator, Assistant Sheriff, Undersheriff, Sheriff, Co Founder, Founder, Administrator, Head administrator, or Developer",
		  color=0xf54242)
      await ctx.send(embed=embed)
  



@client.command()
async def kill(ctx):
	await ctx.send("Mention someone to kill:")

	def check(msg):
		return msg.author == ctx.author and msg.channel == ctx.channel

	msg = await client.wait_for("message", check=check)
	msg = str(msg.content)
	await ctx.channel.send(f'{msg} Died Imao wat a looser')


@client.command(pass_context=True)
async def kick(ctx, member: discord.Member):
  yes = 0
  role1 = discord.utils.get(ctx.guild.roles, name='Head Administrator')
  role2 = discord.utils.get(ctx.guild.roles, name='Assistant Sheriff')
  role3 = discord.utils.get(ctx.guild.roles, name='Undersheriff')
  role4 = discord.utils.get(ctx.guild.roles, name='Sheriff')
  role5 = discord.utils.get(ctx.guild.roles, name='Co Founder')
  role6 = discord.utils.get(ctx.guild.roles, name='Founder')
  role9 = discord.utils.get(ctx.guild.roles, name='Developer')
  if role1 not in role_allowed:
    role_allowed.append(role1)
  if role2 not in role_allowed:
    role_allowed.append(role2)
  if role3 not in role_allowed:
    role_allowed.append(role3)
  if role4 not in role_allowed:
    role_allowed.append(role4)
  if role5 not in role_allowed:
    role_allowed.append(role5)
  if role6 not in role_allowed:
    role_allowed.append(role6) 
  if role9 not in role_allowed:
    role_allowed.append(role9)
  for i in role_allowed:
    if i in ctx.author.roles:
      await member.kick()
      await ctx.send(f'User {member} has kicked the bucket.')
      yes = 1
      break
    elif yes == 0:
      embed = discord.Embed(
        title="Permission Denied.",
        description=
		  "You are missing these role(s): Head Administrator, Assistant Sheriff, Undersheriff, Sheriff, Co Founder, Founder, Administrator, Head administrator, or Developer", color=0xf54242)
      await ctx.send(embed=embed)


@client.command(pass_context=True)
async def ban(ctx, member: discord.Member):
  yes = 0
  role1 = discord.utils.get(ctx.guild.roles, name='Head Administrator')
  role2 = discord.utils.get(ctx.guild.roles, name='Assistant Sheriff')
  role3 = discord.utils.get(ctx.guild.roles, name='Undersheriff')
  role4 = discord.utils.get(ctx.guild.roles, name='Sheriff')
  role5 = discord.utils.get(ctx.guild.roles, name='Co Founder')
  role6 = discord.utils.get(ctx.guild.roles, name='Founder')
  role9 = discord.utils.get(ctx.guild.roles, name='Developer')
  if role1 not in role_allowed:
    role_allowed.append(role1)
  if role2 not in role_allowed:
    role_allowed.append(role2)
  if role3 not in role_allowed:
    role_allowed.append(role3)
  if role4 not in role_allowed:
    role_allowed.append(role4)
  if role5 not in role_allowed:
    role_allowed.append(role5)
  if role6 not in role_allowed:
    role_allowed.append(role6) 
  if role9 not in role_allowed:
    role_allowed.append(role9)
  for i in role_allowed:
    if i in ctx.author.roles:
      reason = None
      await member.ban(reason=reason)
      await ctx.send(f'User {member} has been banned')
      yes = 1
      break
  if yes == 0:
    embed = discord.Embed(
		  title="Permission Denied.",
		  description=
		  "You are missing these role(s): Head Administrator, Assistant Sheriff, Undersheriff, Sheriff, Co Founder, Founder, Administrator, Head administrator, or Developer",
		  color=0xf54242)
    await ctx.send(embed=embed)


@client.command()
async def test(ctx):
	await ctx.channel.send("Test Failed! Bot deactivated!")


@client.command()
async def name(ctx):
	nicknames = [
	  "dumbass", "shithead", "asshole", "cunt", "nigger", "dildo",
	  "pink dildo"
	]
	await ctx.channel.send(f"${random.choice(nicknames)} is your new name!")


@client.command()
async def fun_commands(ctx):
	await ctx.channel.send(
	  "**The Fun commands are**``:\n\Redmonkeybet, West, and ?/kill!``")


@client.event
async def on_message(message):
	mescon = str(message.content)
	mescon = mescon.lower()
	auth = str(message.author)
	if auth not in memberlist:
		memberlist.append(auth)
		#db[auth] = 0

	if mescon == "redmonkeybet":
		await message.channel.send(
		  "hes gay :flushed: :flushed: :flushed: :flushed: :flushed: :flushed::flushed: :flushed: :flushed::flushed:"
		)
	elif mescon == "west":
		await message.channel.send("Needs robux :tired_face:")
	elif mescon == "commands":
		await message.channel.send(
		  "**The commands are**``:\n\kick, name, report, and test! These commands are case sensative."
		)
	elif mescon.startswith("@West..!#3179"):
		await message.channel.send("Do not ping West!")
	await client.process_commands(message)


@client.command()
async def prefix():
	await ctx.channel.send("The current prefix is: `?/`")


@client.command(aliases=['ManoHelp'])
async def help_bot(ctx):
	embed = discord.Embed(title="What do you need help with?",
	   description="Commands, Fun commands!",
	   color=000000)
	embed.set_footer(
	  text=
	  "ban(member), unban(put members name here(real name for discord not specific server nickname) kick(member), fun_commands, name, kill, report(member), warn(member)(message to send), checkwarnings(member), clearwarnings(member)"
	)
	await ctx.channel.send(embed=embed)


@client.command()
async def unban(ctx, *, member):
	role1 = discord.utils.get(ctx.guild.roles, name='Head Administrator')
	role2 = discord.utils.get(ctx.guild.roles, name='Assistant Sheriff')
	role3 = discord.utils.get(ctx.guild.roles, name='Undersheriff')
	role4 = discord.utils.get(ctx.guild.roles, name='Sheriff')
	role5 = discord.utils.get(ctx.guild.roles, name='Co Founder')
	role6 = discord.utils.get(ctx.guild.roles, name='Founder')
	role7 = discord.utils.get(ctx.guild.roles, name='Administrator')
	role8 = discord.utils.get(ctx.guild.roles, name='Head administrator')
	role9 = discord.utils.get(ctx.guild.roles, name='Developer')
	if role1 in ctx.author.roles or role2 in ctx.author.roles or role3 in ctx.author.roles or role4 in ctx.author.roles or role5 in ctx.author.roles or role6 or role7 in ctx.author.roles or role8 in ctx.author.roles or role9 in ctx.author.roles:
		banned_users = await ctx.guild.bans()
		member = str(member)
		member_name, member_discriminator = member.split('#')
		for ban_entry in banned_users:
			user = ban_entry.user
			if (user.name, user.discriminator) == (member_name,
			  member_discriminator):
				await ctx.guild.unban(user)
				await ctx.send(f'Unbanned {user.mention}')
				return

		await ctx.send(
		  "This member was never banned to begin with. You can't unban someone who isn't banned!"
		)
	else:
		embed = discord.Embed(
		  title="Permission Denied.",
		  description=
		  "You are missing these rank(s): Developer, Head Administrator, Assistant Undersheriff, Undersheriff, Sheriff, Co Founder, Founder",
		  color=0xff00f6)
		await ctx.send(embed=embed)


@client.event
async def on_member_join(member: discord.Member):
	await member.create_dm()
	await member.dm_channel.send(f'Hi {member.name}, Welcome to Mano County!')


@client.event
async def on_member_remove(member: discord.Member):
	print(f'{member} has left a server.')



server.server()
bot.run(TOKEN)
