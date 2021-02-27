import discord
import urllib
import asyncio
import random
from bs4 import BeautifulSoup


class aClient(discord.Client):

    player      = None
    when        = None
    ended       = None
    pedalique   = None
    duration    = None
    reason      = None

    channel     = None

    async def on_ready(self):
        print('[Банхаммер-трап] Я открыла глаза, хозяин.')

        while True:

            statuses = ['Клуб романтики', 'Space Station 13', 'The Sims 4', 'Life Is Strange', 'Candy Crush Saga', 'Stardew Valley', 'Just Dance 2021', 'Забань их всех!', 'Разработка с Natrium11']

            await self.change_presence(activity=discord.Game(name=statuses[random.randint(0, len(statuses) - 1)]))

            f = urllib.request.urlopen('https://hub.ss13.ru/11/bans')
            page = f.read()
            print('[Банхаммер-трап] Я зашла на хаб, хозяин.')

            soup = BeautifulSoup(page, 'lxml')
            tds = soup.findAll('td')
            print('[Банхаммер-трап] Я нашла на странице баны, хозяин.')

            self.channel = client.get_channel(796729758724653077)
            print('[Банхаммер-трап] Я получила доступ к текстовому каналу, хозяин. Напишем что-нибудь милое?')

            if (self.when != tds[1].text):
                print('[Банхаммер-трап] Я нашла новый бан, хозяин.')

                self.player     = tds[0].text
                self.when       = tds[1].text
                self.ended      = tds[2].text
                self.pedalique  = tds[3].text
                self.duration   = tds[5].text
                self.reason     = tds[6].text
                print('[Банхаммер-трап] Я занесла сведения о бане в блокнотик, хозяин.')

                if (self.ended == 'Permaban'):
                    print('[Банхаммер-трап] Я поняла, что это пермабан, хозяин.')

                    if ('Job' in self.duration):
                        print('[Банхаммер-трап] Я поняла, что это джоббан, хозяин.')

                        jobs = []
                        i = 0
                        print('[Банхаммер-трап] Я создала список с рольками, хозяин, и присвоила счётчику нулик.')

                        while tds[7*i].text == self.player and ('job' in tds[5+7*i]):

                            index = tds[5+7*i].text.index(':') + 1
                            print(f'[Банхаммер-трап] Хозяин, а вы знали, что index = {index}, i = {i}?')

                            jobs.append(tds[5+7*i].text[index+1:])
                            print(f'[Банхаммер-трап] Списочек в моём блокнотике выглядит так, хозяин: {jobs}.')

                            i += 1

                        print('[Банхаммер-трап] Я всё посчитала, хозяин, и готова открыть всем сведения о бане.')

                        print(F'Игрок {self.player} был забанен {self.pedalique} навсегда на следующие роли: ' + ', '.join(jobs) + f'\n {self.reason}')
                        await self.channel.send(f'Игрок `{self.player}` был забанен `{self.pedalique}` навсегда на следующие роли: ' + '\`' + ', '.join(jobs) + '\`' + f'.\n> {self.reason}')

                    else:
                        print('[Банхаммер-трап] Я поняла, что это НЕ джоббан, хозяин.')

                        print(f'[Банхаммер-трап] Игрок {self.player} был забанен {self.pedalique} навсегда.\n{self.reason}')
                        await self.channel.send(f'Игрок `{self.player}` был забанен `{self.pedalique}` навсегда.\n> {self.reason}')

                else:
                    print('[Банхаммер-трап] Я поняла, что это НЕ пермабан, хозяин.')

                    if ('job' in self.duration):
                        print('[Банхаммер-трап] Я поняла, что это джоббан, хозяин.')

                        jobs = ['Smth']
                        i = 0
                        print('[Банхаммер-трап] Я создала список с рольками, хозяин, и присвоила счётчику нулик.')

                        while (tds[7*i].text == self.player) and ('job' in tds[5+7*i].text):

                            index = tds[5+7*i].text.index(':') + 1
                            print(f'[Банхаммер-трап] Хозяин, а вы знали, что index = {index}, i = {i}?')

                            if (jobs[-1] != tds[5+7*i].text[index+1:]):
                                if 'Smth' in jobs:
                                    jobs.remove('Smth')
                                jobs.append(tds[5+7*i].text[index+1:])
                                print(f'[Банхаммер-трап] Списочек в моём блокнотике выглядит так, хозяин: {jobs}.')

                            i += 1

                        print('[Банхаммер-трап] Хозяин, тут времечко надо переделать.')
                        new_duration = []
                        for g in self.duration:
                            if g != ',':
                                new_duration.append(g)
                                print(f'[Банхаммер-трап] Я добавила ко времени {g} и теперь оно выглядит так {new_duration}')
                            else:

                                print(f'[Банхаммер-трап] Времечко вроде получилось, хозяин')
                                self.duration = ''.join(new_duration)
                                break

                        print('[Банхаммер-трап] Я готова вам открыться, хозяин.')

                        print(f'Игрок {self.player} был забанен {self.pedalique} на {self.duration} на следующие роли: ' + ', '.join(jobs) + f'\n {self.reason}')
                        await self.channel.send(f'Игрок `{self.player}` был забанен `{self.pedalique}` на `{self.duration}` на следующие роли: `' + ', '.join(jobs) + f'`.\n> {self.reason}')

                    else:
                        print('[Банхаммер-трап] Я поняла, что это НЕ джоббан, хозяин.')
                        print('[Банхаммер-трап] Я всё посчитала, хозяин, и готова открыть всем сведения о бане.')

                        print(f'Игрок {self.player} был забанен {self.pedalique} на {self.duration}.\n{self.reason}')
                        await self.channel.send(f'Игрок `{self.player}` был забанен `{self.pedalique}` на `{self.duration}`.\n> {self.reason}')

            else:

                print('[Банхаммер-трап] :( Ничего нового, хозяин.')
                await asyncio.sleep(11)

client = aClient()
client.run('Nzk2NDU0OTExNjIwNjc3NjUz.X_YKcA.OW0FLzsifA5iX2boke6aYOC1Wy8')
