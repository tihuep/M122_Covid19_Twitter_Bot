import click
import configuration_loader


@click.command()
@click.option("--configuration", 'configuration_file', required=True, type=click.Path(
    exists=True,
    file_okay=True,
    dir_okay=False,
    resolve_path=True))
def run(configuration_file):
    configuration = configuration_loader.load_configuration(configuration_file)
    # TODO: Implement script


if __name__ == '__main__':
    run()
