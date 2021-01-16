# coding=utf-8

import discord, asyncio, os, math, ast, datetime, json, dotenv, random, traceback

dotenv.load_dotenv(verbose=True)
token = os.getenv("TOKEN")
intents = discord.Intents.all()

client = discord.AutoShardedClient(intents=intents)

# 변수
prefix = "m?"
owner = [726350177601978438]
guildpass = [700331611165687838]
botlog = 777845388673548298
nameprefix = ['📡ㅣ메잌애드', '메잌애드', '📡메잌애드', '🤝메잌애드']
cooltime2 = []

def get_category(guild):
    members = len(list(filter(lambda x: not x.bot, guild.members)))
    target_category = None
    if members >= 1 and members <= 50:
        target_category = client.get_channel(774894654964760586)
    elif members >= 51 and members <= 100:
        target_category = client.get_channel(774894653794811915)
    elif members >= 101 and members <= 200:
        target_category = client.get_channel(774894652452372511)
    elif members >= 201 and members <= 300:
        target_category = client.get_channel(774894651613118494)
    elif members >= 301 and members <= 400:
        target_category = client.get_channel(774894650456670219)
    elif members >= 401 and members <= 500:
        target_category = client.get_channel(774894649487261706)
    elif members >= 501 and members <= 600:
        target_category = client.get_channel(774894648392941568)
    elif members >= 601 and members <= 700:
        target_category = client.get_channel(774894647192977429)
    elif members >= 701 and members <= 800:
        target_category = client.get_channel(774894645976104992)
    elif members >= 801 and members <= 900:
        target_category = client.get_channel(774894644978122804)
    elif members >= 901 and members <= 1000:
        target_category = client.get_channel(774894643481542658)
    elif members >= 1001:
        target_category = client.get_channel(774894642675712000)
    return target_category

@client.event
async def bg_change_playing():
    while True:
        await client.change_presence(status=discord.Status.online, activity=discord.Game(name=f"2021/01/16에 서비스 지원을 종료합니다."))
        await client.get_channel(777844769740947476).edit(name=f"서버 : {len(client.guilds)}개")
        await client.get_channel(777844805085560833).edit(name=f"유저 : {len(client.users)}명")
        await client.get_channel(777844853073379338).edit(name=f"멤버(서버) : {len(list(filter(lambda x: not x.bot, client.get_guild(700331611165687838).members)))}명")
        await client.get_channel(774894654964760586).edit(name=f"👥 1~50명 ({len(client.get_channel(774894654964760586).channels)}개 서버 홍보중)")
        await client.get_channel(774894653794811915).edit(name=f"👥 51~100명 ({len(client.get_channel(774894653794811915).channels)}개 서버 홍보중)")
        await client.get_channel(774894652452372511).edit(name=f"👥 101~200명 ({len(client.get_channel(774894652452372511).channels)}개 서버 홍보중)")
        await client.get_channel(774894651613118494).edit(name=f"👥 201~300명 ({len(client.get_channel(774894651613118494).channels)}개 서버 홍보중)")
        await client.get_channel(774894650456670219).edit(name=f"👥 301~400명 ({len(client.get_channel(774894650456670219).channels)}개 서버 홍보중)")
        await client.get_channel(774894649487261706).edit(name=f"👥 401~500명 ({len(client.get_channel(774894649487261706).channels)}개 서버 홍보중)")
        await client.get_channel(774894648392941568).edit(name=f"👥 501~600명 ({len(client.get_channel(774894648392941568).channels)}개 서버 홍보중)")
        await client.get_channel(774894647192977429).edit(name=f"👥 601~700명 ({len(client.get_channel(774894647192977429).channels)}개 서버 홍보중)")
        await client.get_channel(774894645976104992).edit(name=f"👥 701~800명 ({len(client.get_channel(774894645976104992).channels)}개 서버 홍보중)")
        await client.get_channel(774894644978122804).edit(name=f"👥 801~900명 ({len(client.get_channel(774894644978122804).channels)}개 서버 홍보중)")
        await client.get_channel(774894643481542658).edit(name=f"👥 901~1000명 ({len(client.get_channel(774894643481542658).channels)}개 서버 홍보중)")
        await client.get_channel(774894642675712000).edit(name=f"👥 1001명 이상 ({len(client.get_channel(774894642675712000).channels)}개 서버 홍보중)")
        await asyncio.sleep(300)
    client.loop.create_task(bg_change_playing())

@client.event
async def on_ready():
    print(f"{client.user.name}이 준비됨!")
    embed = discord.Embed(colour=discord.Colour.purple(), title="🚦 봇 켜짐 🚦")
    embed.add_field(name="전체 서버 수", value=f"`{len(client.guilds)}개`", inline=False)
    embed.add_field(name="전체 인원 수", value=f"`{len(client.users)}명`", inline=False)
    embed.set_footer(text=client.user, icon_url=client.user.avatar_url)
    await client.get_channel(int(botlog)).send(embed=embed)
    client.loop.create_task(bg_change_playing())
    client.loop.create_task(synchronization())

@client.event
async def synchronization():
    c = [774894643481542658, 774894644978122804, 774894645976104992, 774894647192977429, 774894648392941568, 774894649487261706, 774894650456670219, 774894651613118494, 774894652452372511, 774894653794811915, 774894654964760586]
    number = 0
    ab = []
    for a in c:
        for i in client.get_channel(int(a)).channels:
            try:
                guild = client.get_guild(int(i.topic.split(" ")[0]))
                members = len(list(filter(lambda x: not x.bot,guild.members)))
                try:
                    if not str(client.get_channel(int(i.topic.split(" ")[2]))) == "None":
                        try:
                            if guild.me.guild_permissions >= discord.Permissions(permissions=8) == False:
                                await guild.owner.send(embed=discord.Embed(color=0x7289DA, title="퇴장 안내", description=f"{guild.name} 서버에 권한이 부족해 퇴장하였습니다."))
                                await guild.leave()
                            else:
                                asdf = client.get_channel(int(i.topic.split(" ")[2]))
                                tg = await asdf.fetch_message(int(asdf.topic.split(" ")[0]))
                                await tg.edit(content=f"<a:loading:774533173722873856> `{client.get_guild(700331611165687838).name}` 서버와 동기화중입니다.", embed=None)
                                await asyncio.sleep(1)
                                embed=discord.Embed(timestamp=tg.edited_at, color=discord.Colour.green(), title=f"{client.user.name} 사용법", description=f"{client.user.mention}은 홍보를 할 수 있는 디스코드 봇입니다.\n\nSTEP 1. 봇을 초대합니다. [봇 초대링크](https://discord.com/oauth2/authorize?client_id=774520032864108575&permissions=8&scope=bot)\nSTEP 2. `{client.get_guild(700331611165687838).name}`에 채널이 생성됩니다.\nSTEP 3. `{prefix}등록` 명령어로 서버 명령어를 등록합니다.")
                                embed.set_footer(text="마지막 동기화")
                                await tg.edit(content="https://discord.gg/k8dbkSdZRZ",embed=embed)
                                if members >= 1 and members <= 50:
                                    target_category = client.get_channel(774894654964760586)
                                elif members >= 51 and members <= 100:
                                    target_category = client.get_channel(774894653794811915)
                                elif members >= 101 and members <= 200:
                                    target_category = client.get_channel(774894652452372511)
                                elif members >= 201 and members <= 300:
                                    target_category = client.get_channel(774894651613118494)
                                elif members >= 301 and members <= 400:
                                    target_category = client.get_channel(774894650456670219)
                                elif members >= 401 and members <= 500:
                                    target_category = client.get_channel(774894649487261706)
                                elif members >= 501 and members <= 600:
                                    target_category = client.get_channel(774894648392941568)
                                elif members >= 601 and members <= 700:
                                    target_category = client.get_channel(774894647192977429)
                                elif members >= 701 and members <= 800:
                                    target_category = client.get_channel(774894645976104992)
                                elif members >= 801 and members <= 900:
                                    target_category = client.get_channel(774894644978122804)
                                elif members >= 901 and members <= 1000:
                                    target_category = client.get_channel(774894643481542658)
                                elif members >= 1001:
                                    target_category = client.get_channel(774894642675712000)
                                await i.edit(name=guild.name, category=target_category)
                                number += 1
                                ab.append(guild.id)
                        except: await client.get_channel(int(botlog)).send(embed=discord.Embed(title="동기화 오류 발생.", colour=discord.Colour.red(), description=f"{guild.name} / {guild.owner} / {guild.id}").set_footer(text=guild.name, icon_url=guild.icon_url))
                except: await client.get_channel(int(botlog)).send(embed=discord.Embed(title="동기화 오류 발생.", colour=discord.Colour.red(), description=f"{guild.name} / {guild.owner} / {guild.id}").set_footer(text=guild.name, icon_url=guild.icon_url))
            except:
                await i.delete()
    abc = []
    for i in client.guilds:
        if not i.id in ab:
            if not i.id in guildpass:
                abc.append(i.id)
    await client.get_channel(int(botlog)).send(embed=discord.Embed(color=0x7289DA, title="🔁 동기화 알림", description=f"{client.user.name} 봇이 접속한 {len(client.guilds)-len(guildpass)}개의 서버 중 {number}개의 서버에 동기화를 완료했으며, {len(client.guilds)-len(guildpass)-number}개의 서버에 동기화를 실패하였습니다."))
    if not len(abc) == 0:
        await client.get_channel(int(botlog)).send(embed=discord.Embed(colour=discord.Colour.red(), title="🔁 동기화 실패 서버 안내", description=f"{abc}"))
        for i in abc:
            guild = client.get_guild(i)
            embed=discord.Embed(color=0x7289DA, title="퇴장 알림", description=f"안녕하세요? `{guild.name}` 서버장님! 메잌애드에서 안내드립니다.\n메잌애드에서는 1시간에 1번 동기화를 진행하고 있습니다!\n하지만 동기화 중, `{guild.name}` 서버의 동기화가 실패되어 퇴장하였습니다.\n봇이 퇴장한 후에도 아래의 링크로 봇을 다시 초대하실 수 있습니다!")
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            embed.add_field(name="봇 초대 링크", value=f"[봇 초대하기](https://discord.com/oauth2/authorize?client_id=774520032864108575&permissions=8&scope=bot)", inline=False)
            embed.add_field(name="서버 초대 링크", value=f"[https://discord.gg/k8dbkSdZRZ](https://discord.gg/k8dbkSdZRZ)", inline=False)
            try: await guild.owner.send(embed=embed)
            except: pass
            await guild.leave()
    await asyncio.sleep(3600)
    client.loop.create_task(synchronization())

def insert_returns(body):
    if isinstance(body[-1], ast.Expr):
        body[-1] = ast.Return(body[-1].value)
        ast.fix_missing_locations(body[-1])
    if isinstance(body[-1], ast.If):
        insert_returns(body[-1].body)
        insert_returns(body[-1].orelse)
    if isinstance(body[-1], ast.With):
        insert_returns(body[-1].body)

@client.event
async def on_guild_join(guild):
    embed = discord.Embed(colour=discord.Colour.green(), title=":inbox_tray: 서버 입장 :inbox_tray:")
    embed.add_field(name="서버 이름", value=f"`{guild.name}`", inline=False)
    embed.add_field(name="서버 아이디", value=f"`{guild.id}`", inline=False)
    embed.add_field(name="서버 주인", value=f"`{guild.owner}`", inline=False)
    embed.add_field(name="서버 순인원수", value=f"`{len(list(filter(lambda x: not x.bot, guild.members)))}명`", inline=False)
    embed.add_field(name="현재 접속한 서버 수", value=f"`{len(client.guilds)}개`", inline=False)
    embed.set_footer(text=guild.name, icon_url=guild.icon_url)
    await client.get_channel(int(botlog)).send(embed=embed)
    if guild.me.guild_permissions >= discord.Permissions(permissions=8) == False:
        await guild.owner.send(embed=discord.Embed(color=0x7289DA, title="퇴장 안내", description=f"{guild.name} 서버에 권한이 부족해 퇴장하였습니다."))
        await guild.leave()
    else:
        text = await guild.create_text_channel("메잌애드")
        omg = await text.send(content="https://discord.gg/k8dbkSdZRZ", embed=discord.Embed(color=discord.Colour.green(), title=f"{client.user.name} 사용법", description=f"{client.user.mention}은 홍보를 할 수 있는 디스코드 봇입니다.\n\nSTEP 1. 봇을 초대합니다. [봇 초대링크](https://discord.com/oauth2/authorize?client_id=774520032864108575&permissions=8&scope=bot)\nSTEP 2. `{client.get_guild(700331611165687838).name}`에 채널이 생성됩니다.\nSTEP 3. `{prefix}등록` 명령어로 서버 명령어를 등록합니다."))
        await text.edit(topic=f'{omg.id}')
        await text.set_permissions(guild.default_role, read_messages = True, send_messages = False, read_message_history = True)
        await text.set_permissions(client.user, read_messages = True, send_messages = True, read_message_history = True)
        target_category = get_category(guild)
        serverchannel = await target_category.create_text_channel(guild.name)
        url = await text.create_invite(reason=f'{client.user.name}')
        m = await serverchannel.send(f"{url}", embed=discord.Embed(colour=discord.Colour.green(), title=guild.name, description=f"서버 설명이 없습니다.\n`{prefix}등록` 명령어로 소개를 등록해주세요."))
        await serverchannel.edit(topic=f'{guild.id} {m.id} {text.id}')

@client.event
async def on_guild_remove(guild):
    embed = discord.Embed(colour=discord.Colour.red(), title=":outbox_tray: 서버 퇴장 :outbox_tray:")
    embed.add_field(name="서버 이름", value=f"`{guild.name}`", inline=False)
    embed.add_field(name="서버 아이디", value=f"`{guild.id}`", inline=False)
    embed.add_field(name="서버 주인", value=f"`{guild.owner}`", inline=False)
    embed.add_field(name="서버 순인원수", value=f"`{len(list(filter(lambda x: not x.bot, guild.members)))}명`", inline=False)
    embed.add_field(name="현재 접속한 서버 수", value=f"`{len(client.guilds)}개`", inline=False)
    embed.set_footer(text=guild.name, icon_url=guild.icon_url)
    await client.get_channel(int(botlog)).send(embed=embed)
    target_category = get_category(guild)
    for a in target_category.channels:
        if str(guild.id) in a.topic:
            await a.delete()

@client.event
async def on_message(message):
    if message.content.startswith(f"{prefix}eval"):
        if message.author.id in owner:
            try:
                prefix_count=len(prefix)+5
                cmd=message.content[prefix_count:]
                fn_name = "_eval_expr"
                cmd = cmd.strip("` ")
                # add a layer of indentation
                cmd = "\n".join(f"    {i}" for i in cmd.splitlines())
                # wrap in async def body
                body = f"async def {fn_name}():\n{cmd}"
                parsed = ast.parse(body)
                body = parsed.body[0].body
                insert_returns(body)
                env = {
                    'client': client,
                    'discord': discord,
                    'message': message,
                    '__import__': __import__
                }
                exec(compile(parsed, filename="<ast>", mode="exec"), env)
                result = (await eval(f"{fn_name}()", env))
                embed=discord.Embed(title="실행 성공", colour=discord.Colour.green(), timestamp=message.created_at)
                embed.add_field(name="`📥 Input (들어가는 내용) 📥`", value=f"```py\n{cmd}```", inline=False)
                embed.add_field(name="`📤 Output (나오는 내용) 📤`", value=f"```py\n{result}```", inline=False)
                embed.add_field(name="`🔧 Type (타입) 🔧`",value=f"```py\n{type(result)}```", inline=False)
                embed.add_field(name="`🏓 Latency (지연시간) 🏓`",value=f"```py\n{str((datetime.datetime.now()-message.created_at)*1000).split(':')[2]}```", inline=False)
                embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)
            except Exception as e:
                await message.channel.send(f"{message.author.mention}, 실행 중 오류가 발생하였습니다.\n\n```py\n{e}```")
        else:
            await message.channel.send(f"{message.author.mention}, 당신은 권한이 없습니다.")

    if message.content == f"{prefix}가이드":
        await message.channel.send(message.author.mention, embed=discord.Embed(color=0x7289DA, title=f"{client.user.name} 가이드", description=f"{client.user.mention}은 디스코드에서 홍보를 할 수 있는 홍보형 봇입니다!\n당신의 서버를 홍보하시려면 아래의 가이드를 지켜주세요!\n\nSTEP 1. 봇을 초대합니다. [봇 초대링크](https://discord.com/oauth2/authorize?client_id=774520032864108575&permissions=8&scope=bot)\nSTEP 2. `{client.get_guild(700331611165687838).name}`에 채널이 생성됩니다.\nSTEP 3. `{prefix}등록` 명령어로 서버 명령어를 등록합니다."))

    if message.content.startswith(f"{prefix}등록"):
        if message.author.guild_permissions.administrator == True:
            if message.guild.id in cooltime2:
                await message.channel.send(f"{message.author.mention}, 쿨타임이 적용되어 있습니다. 기다려주세요.")
            else:
                cmd = message.content[len(prefix)+3:]
                if cmd == "" or cmd == " ":
                    await message.channel.send(f"{message.author.mention}, 서버 소개 내용 `{prefix}등록` 커맨드와 함께 써주세요.")
                else:
                    msg = await message.channel.send(f"<a:loading:774533173722873856> {message.author.mention}, `{message.guild.name}` 서버의 설명을 포스트중입니다...")
                    target_category = get_category(message.guild)
                    for a in target_category.channels:
                        splits = a.topic.split(" ")
                        if str(message.guild.id) == splits[0]:
                            m = await a.fetch_message(int(splits[1]))
                            embed=discord.Embed(colour=discord.Colour.green(), title=message.guild.name, description=cmd).set_footer(text=message.author, icon_url=message.author.avatar_url)
                            if message.guild.is_icon_animated() is True:
                                a = message.guild.icon_url_as(format="gif", size=2048)
                            elif message.guild.is_icon_animated() is False:
                                a = message.guild.icon_url_as(format="png", size=2048)
                            embed.set_thumbnail(url=a)
                            await m.edit(embed=embed)
                            await msg.edit(content=f"✅ {message.author.mention}, 성공적으로 `{message.guild.name}` 서버의 설명을 포스트하였습니다!")
                            cooltime2.append(message.guild.id)
                            await asyncio.sleep(3600)
                            cooltime2.remove(message.guild.id)
                        else:
                            pass

client.run(token)
