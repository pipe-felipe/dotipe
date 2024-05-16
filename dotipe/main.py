from typer import run

from dotipe.facade.dotipe_facade import Dotipe

if __name__ == "__main__":
    dotipe = Dotipe()
    run(dotipe.start)
