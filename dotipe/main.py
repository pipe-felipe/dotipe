from typer import run

from dotipe.cli.dotipe_cli import DotipeCli

if __name__ == "__main__":
    cli = DotipeCli()
    run(cli.start)
