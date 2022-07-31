from instabot import Bot
bot = Bot()
bot.login(username='jkurianza', password='_82$TiQ<)s')

######  upload a picture #######
#bot.upload_photo("yoda.jpg", caption="biscuit eating baby")

######  follow someone #######
#bot.follow("elonrmuskk")

######  send a message #######
#bot.send_message("Hello from Dhaval", ['user1','user2'])

######  get follower info #######
my_followers = bot.get_user_followers('urianza_amanda')
pass

#for follower in my_followers:
    #print(follower)

#bot.unfollow_everyone()