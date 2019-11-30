import sys
import discord
import asyncio
import praw


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.seen = []
        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.my_background_task())

    async def on_ready(self):
        print('Logged in as', self.user.name, self.user.id)

    async def my_background_task(self):
        await self.wait_until_ready()
        channel = self.get_channel(621059740797239367)
        count = 0
        while not self.is_closed():
            count += 1
            print(count)
            for submission in bapc.new(limit=10):
                if sys.argv[1].upper() in submission.title.upper():
                    if submission.id not in self.seen:
                        self.seen.append(submission.id)
                        await channel.send(submission.title[submission.title.find("]") + 1:])
            await asyncio.sleep(60)


client = MyClient()
reddit = praw.Reddit(client_id='OcQcLKfDRQs9cw',
                     client_secret="_5UhtnXwXJARxSUHNG-Tz6tfxv8",
                     user_agent='taurus')

bapc = reddit.subreddit('buildapcsales')
client.run('NjIxMDMzNjIyNjQ3OTk2NDM3.XXfg5A.We7JNmyuE9ouGeh0bgDIzfQBK5o')
