from typer import run

from dotipe.cli.dotipe_cli import DotipeCli


def main():
    cli = DotipeCli()
    run(cli.start)


if __name__ == "__main__":
    main()
