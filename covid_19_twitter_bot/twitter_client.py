import json

from TwitterAPI import TwitterAPI

from covid_19_twitter_bot import twitter_message


def get_received_messages(last_read=None):
    response = client.request('direct_messages/events/list')
    messages = [twitter_message.Message.from_event(event) for event in response.json()['events']]
    if last_read:
        return _get_unread(messages, last_read)
    else:
        return messages


def write_message(recipient, data):
    message = twitter_message.Message(
        id=None,
        sender=None,
        recipient=recipient,
        data=data)
    event = message.to_event()
    client.request('direct_messages/events/new', json.dumps(event))


def _authenticate():
    return TwitterAPI(
        consumer_key='kDRt54aE0KRusRqgCZbqkIS5X',
        consumer_secret='MNDA1MxmQKuJHAbB271HionhMpJe0tu783kgUB2akmNBDsC82U',
        access_token_key='1394548059636477954-8hnXHARdpf0pZ1u54wperSYyc0EnRH',
        access_token_secret='39Nip5HTEIuH4apA96EVdLKCckBHu5rOSmRjofS0kFzFg')


def _get_unread(messages, last_read_id):
    unread = []
    for message in messages:
        if message.id == last_read_id:
            return unread
        unread.append(message)
    return unread


client = _authenticate()
