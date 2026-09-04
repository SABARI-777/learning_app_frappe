import click

@click.command("hello-app")
def hello_app():
    click.echo("Hello from learning_app")

commands = [hello_app]