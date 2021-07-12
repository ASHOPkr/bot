import discord
import asyncio

from discord.ext.commands.core import command

client = discord.Client()



cid = 864077720963383366
tid = 864077720963383366
gid = 864077714578866186
dii = 864077720119017472
aid = 822437655957995552
gtid = 864077728109166633
lid = 864077727345410068
token = "ODYzMzkyNDEzOTQxNDk3ODY3.YOmO2A.xkb36fdQNcZKNhZ2ZScAQ97QMss"

@client.event
async def on_message(message):
    if message.content.startswith("!출근"):
        if message.author.id == aid:
            if message.channel.id == dii:
                embed = discord.Embed(title=f"{message.author.name}님이 출근하셨습니다.", color=0x00ff00)
                await client.get_channel(int(cid)).send (embed=embed)

    if message.content.startswith("!퇴근"):
        if message.author.id == aid:
            if message.channel.id == dii:
                embed = discord.Embed(title=f"{message.author.name}님이 퇴근하셨습니다.", color=0x00ff00)
                await client.get_channel(int(tid)).send (embed=embed)

    if message.content.startswith("!제품추가"):
        if message.author.id == aid:
            if message.channel.id == dii:
                await message.channel.send("제품 이름을 입력해주세요.")
                name = await client.wait_for('message', check=lambda message: message.author == message.author)
                name = name.content
                await message.channel.send("제품 가격을 입력해주세요.")
                k = await client.wait_for('message', check=lambda message: message.author == message.author)
                k = k.content
                await message.channel.send("제품 설명을 입력해주세요.")
                s = await client.wait_for('message', check=lambda message: message.author == message.author)
                s = s.content
                await message.channel.send("사진 URL을 입력해주세요.")
                url = await client.wait_for('message', check=lambda message: message.author == message.author)
                url = url.content
                await message.channel.send("제품 채널 ID를 입력해주세요.")
                id = await client.wait_for('message', check=lambda message: message.author == message.author)
                id = id.content
                await message.channel.send("제품추가가 완료되었습니다.")
                embed = discord.Embed(title=name, color=0x000000)
                embed.add_field(name="가격", value=str(k), inline=False)
                embed.add_field(name="기능", value=str(s))
                embed.set_image(url=f"{url}")
                await client.get_channel(int(id)).send (embed=embed)

    if message.content.startswith("!공지"):
        if message.author.id == aid:
            if message.channel.id == dii:
                msg = message.content[4:]
                embed = discord.Embed(title="공지사항", color=0x000000)
                embed.set_footer(text=msg)
                await client.get_channel(int(gid)).send (embed=embed)

    if message.content.startswith('!블랙리스트'):
        if message.author.guild_permissions.ban_members:
            try:
                target = message.mentions[0]
            except:
                await message.channel.send('유저가 지정되지 않았습니다')
                return

            j = message.content.split(" ")
            try:
                reason = j[2]
            except IndexError:
                reason = 'None'
            embed = discord.Embed(title='블랙리스트',
                                  description=f'{target}님이 {message.guild.name} 블랙리스트에 추가되었습니다.\n사유: {reason}',
                                  colour=discord.Colour.red())
            try:
                await target.send(embed=embed)
            except:
                pass
            embed = discord.Embed(title="블랙리스트 추가", color=0x000000)
            embed.add_field(name="닉네임", value=str(target), inline=False)
            embed.add_field(name="아이디", value=str(target.id), inline=False)
            embed.add_field(name="사유", value=str(reason), inline=False)
            await client.get_channel(int(gtid)).send(embed=embed)
            await target.ban(reason=reason)


    if message.content.startswith ("!청소"):
        i = (message.author.guild_permissions.administrator)

        if i is True:
            amount = message.content[4:]
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="메시지 삭제 알림", description="최근 디스코드 채팅 {}개가\n관리자 {}님의 요청으로 인해 정상 삭제 조치 되었습니다".format(amount, message.author), color=0x000000)
            embed.set_footer(text="Bot Made by. 정복자#8867", icon_url="https://discordapp.com/channels/691615852620939274/703908401381376000/711859989177958410")
            await message.channel.send(embed=embed)
        
        if i is False:
            await message.channel.purge(limit=1)
            await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))

client.run(token)

