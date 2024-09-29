from instabot import Bot
bot=Bot()

bot.login(username=input("Enter your user ID"),password=input("Enter your password"),use_cookie=False)
'''bot.follow(input("Enter the user_id of account you want to follow"))
bot.upload_photo(input("Enter the path of the file you need to upload as a post"),caption=input("Enter the caption for your post"))
bot.unfollow(input("Enter the user_id of account you want to unfollow"))
bot.send_message(input("type your message here"),[input("enetr id's of people you wanna send messages to")])

follower=bot.get_user_followers(input("Enter your user ID"))

for f in follower:
    print(bot.get_user_info(f),'\n')'''


following=bot.get_user_following(input("Enter user id"))

for j in following:
    print(bot.get_user_info(j),'\n')
