import click
import configuration_loader
import configuration
import twitter_client


@click.command()
@click.option("--configuration", 'configuration_file', required=True, type=click.Path(
    exists=True,
    file_okay=True,
    dir_okay=False,
    resolve_path=True))
def run(configuration_file):
    configurationObj = configuration_loader.load_configuration(configuration_file)
    # TODO: Implement script
    #twitterClient = twitter_client.TwitterClient(configurationObj.twitter.consumer_key, configurationObj.twitter.consumer_secret, configurationObj.twitter.access_token_key, configurationObj.twitter.access_token_secret)
    #messages = twitterClient.get_received_messages()
    #print(messages)

if __name__ == '__main__':
    run()
