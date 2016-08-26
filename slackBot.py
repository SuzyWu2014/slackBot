from slacker import Slacker
import json


config_file = open("configure.json")
config_data = json.load(config_file)
token = config_data["token"]

slack = Slacker(token)
slack.chat.post_message('#slack_bot_test', 'Hello, you can find me at https://github.com/SuzyWu2014/slackBot')
