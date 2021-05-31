import json
import logging

from TwitterAPI import TwitterAPI

import twitter_message


# Simple Tiwtter client
class TwitterClient:
    def __init__(self,
                 consumer_key,
                 consumer_secret,
                 access_token_key,
                 access_token_secret):
        self.client = TwitterAPI(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token_key=access_token_key,
            access_token_secret=access_token_secret)
        self.log = logging.getLogger('TwitterClient')

    def get_received_messages(self, last_read=None):
        response = self.client.request('direct_messages/events/list')
        if response.status_code == 200:
            self.log.info('Fetched received messages')
            messages = [twitter_message.Message.from_event(event) for event in response.json()['events']]
            if last_read:
                return self._get_unread(messages, last_read)
            else:
                return messages
        else:
            self.log.error(f'Could not fetch received messages: {response.text}')
            return None

    def write_message(self, recipient, data):
        message = twitter_message.Message(
            id=None,
            sender=None,
            recipient=recipient,
            data=data)
        event = message.to_event()
        response = self.client.request('direct_messages/events/new', json.dumps(event))
        if response.status_code == 200:
            self.log.info(f'Successfully wrote message to client with id {recipient}')
        else:
            self.log.error(f'Error while writing message to client with id {recipient}: {response.text}')

    @staticmethod
    def _get_unread(messages, last_read_id):
        unread = []
        for message in messages:
            if message.id == last_read_id:
                return unread
            unread.append(message)
        return unread
