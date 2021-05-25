class Configuration:
    def __init__(self, twitter, output_directory):
        self.twitter = twitter
        self.output_directory = output_directory

    @staticmethod
    def from_dict(configuration_dict):
        twitter_configuration_dict = configuration_dict['twitter']
        return Configuration(
            twitter=TwitterConfiguration.from_dict(twitter_configuration_dict),
            output_directory=configuration_dict['output-directory'])


class TwitterConfiguration:
    def __init__(self, consumer_key, consumer_secret, access_token_key, access_token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token_key = access_token_key
        self.access_token_secret = access_token_secret

    @staticmethod
    def from_dict(twitter_configuration_dict):
        return TwitterConfiguration(
            consumer_key=twitter_configuration_dict['consumer-key'],
            consumer_secret=twitter_configuration_dict['consumer-secret'],
            access_token_key=twitter_configuration_dict['access-token-key'],
            access_token_secret=twitter_configuration_dict['access-token-secret'])

