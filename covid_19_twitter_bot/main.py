import click
import configuration_loader
import twitter_client
from pathlib import Path
import last_read
import covid_data_request_parser
import covid_client
import message_generator
import logging
import datetime

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('Main')


@click.command()
@click.option("--configuration", 'configuration_file', required=True, type=click.Path(
    exists=True,
    file_okay=True,
    dir_okay=False,
    resolve_path=True))
def run(configuration_file):
    log.info(f'Starting processing of Covid-19 Twitter Bot at {datetime.datetime.now()}')
    configuration = configuration_loader.load_configuration(configuration_file)
    twitter = twitter_client.TwitterClient(
        consumer_key=configuration.twitter.consumer_key,
        consumer_secret=configuration.twitter.consumer_secret,
        access_token_key=configuration.twitter.access_token_key,
        access_token_secret=configuration.twitter.access_token_secret)
    covid = covid_client.CovidClient()
    last_read_store = last_read.LastReadStore((Path(configuration.output_directory) / 'last_read').absolute())
    last_read_id = last_read_store.get_last_read()
    log.info(f'Loaded last read id {last_read_id}')
    unread_messages = twitter.get_received_messages(last_read_id)
    if unread_messages:
        for message in unread_messages:
            _process_message(message, twitter, covid)
        log.info(f'Set last read id: {unread_messages[0].id}')
        last_read_store.set_last_read(unread_messages[0].id)


def _process_message(message, twitter, covid):
    request = covid_data_request_parser.parse(message.data)
    if request:
        covid_data = covid.get_covid_data(request)
        twitter.write_message(message.sender, message_generator.generate_response_message(covid_data))
    else:
        print(message_generator.wrong_syntax())
        twitter.write_message(message.sender, message_generator.wrong_syntax())


if __name__ == '__main__':
    run()
