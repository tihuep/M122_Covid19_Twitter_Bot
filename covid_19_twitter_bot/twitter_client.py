import json

from TwitterAPI import TwitterAPI

from covid_19_twitter_bot import twitter_message


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

    def get_received_messages(self, last_read=None):
        response = self.client.request('direct_messages/events/list')
        messages = [twitter_message.Message.from_event(event) for event in response.json()['events']]
        if last_read:
            return self._get_unread(messages, last_read)
        else:
            return messages

    def write_message(self, recipient, data):
        message = twitter_message.Message(
            id=None,
            sender=None,
            recipient=recipient,
            data=data)
        event = message.to_event()
        self.client.request('direct_messages/events/new', json.dumps(event))

    @staticmethod
    def _get_unread(messages, last_read_id):
        unread = []
        for message in messages:
            if message.id == last_read_id:
                return unread
            unread.append(message)
        return unread
