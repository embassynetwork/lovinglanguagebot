#!/usr/bin/env python

import os, sys, time, re, datetime
from slackclient import SlackClient

# get these tokens from slack or ask someone to give them to you. 
# then `export LOVING_LANGUAGE_SLACK_TOKEN='xoxb-xxxxxxxxxxxxxxxxxxxxx'`
token = os.environ.get('LOVING_LANGUAGE_SLACK_TOKEN')
bot_id = os.environ.get('LOVING_LANGUAGE_BOT_ID')

if not token:
    print('No token was set. Please set the environment variable LOVING_LANGUAGE_SLACK_TOKEN')
    sys.exit()

client = SlackClient(token)

class LanguageBot: 

    class BotMode:
        def __init__(self, name, method):
            self.name = name
            self.enabled = False
            self.method = method

    def __init__(self, client=None):
        self.client = client

        # TODO this would ideally be a queue of some kind
        self.current_event = None

        # all modes are initialized to False
        self.modes = {
            'posessional': self.BotMode(name='posessional', method=self.posessional),
            'gender': self.BotMode(name='gender', method=self.gender),
            'conditional': self.BotMode(name='conditional', method=self.conditional),
            'eprime': self.BotMode(name='eprime', method=self.eprime)
        }

        self.bot_info()

    def bot_info(self):
        # show some basic bot info
        # bot started at xxxx
        # bot name
        # bot channel membership
        print('Bot started at %s' % datetime.datetime.now())

    def enable(self, mode):
        if self.modes.get(mode, None):
            self.modes[mode].enabled = True
            print('Bot mode \'%s\' was enabled' % mode)
            return True
        else:
            return False

    def new_incoming(self, incoming):
        print('Received event:')
        print(incoming)
        for event in incoming:
            self.current_event = event
            if event.get('type', None) and event['type'] == 'message':
                message = event.get('text', None)
                if message:
                    self.process(message)
                else:
                    print('there was no text in the message')
            else:
                print('--> event was not a message')
        print('')

    def process(self, message):
        for name, mode in self.modes.items():
            if mode.enabled:
                mode.method(message)

    def reply(self, response):
        self.client.api_call(
            "chat.postMessage",
            channel=self.current_event['channel'],
            text=response,
            thread_ts=self.current_event['ts']
        )

    def posessional(self, message):
        print('Mode "posessional" not yet implemented')

    def gender(self, message):
        print('gender mode: processing message')
        # this regex looks for the keywords at the beginning or end of the
        # text, or after or before any non-alphanumeric characters. 
        gender_terms = re.compile(r'(\W|^)(guys|dude|his|her|hers|she|he)(\W|$)')
        if gender_terms.search(message):
            # construct responses to gendered terms here
            response = "Hello! I'm the loving language bot. We are conducting an experiment in non-gendered language. This bot will periodically suggest that you consider using alternate phrasing that is less gender-specific. This is one of those times. "
            self.reply(response)

    def conditional(self, message):
        print('Mode "conditional" not yet implemented')

    def eprime(self, message):
        print('Mode "eprime" not yet implemented')



if client.rtm_connect():
    langbot = LanguageBot(client)
    langbot.enable('gender')

    while True:
        incoming = client.rtm_read()
        if incoming:
            langbot.new_incoming(incoming)
        time.sleep(1)
else:
    print("Connection Failed")

