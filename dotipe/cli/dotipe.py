from importlib.metadata import version

from typer import Exit

from dotipe.core.config_handler import DotipeConfigHandler
from dotipe.core.consts import TEMP_DIR
from dotipe.core.files_handler import compare_files, extract_compared_files_metadata
from dotipe.core.retriever import Retriever
from dotipe.facade.dotipe import DotipeFacade


def get_version(value: bool):
    if value:
        print(f"Dotipe Version: {version("dotipe")}")
        raise Exit(code=0)


class DotipeCli(DotipeFacade):
    def __init__(self, dotipe_config: DotipeConfigHandler, retriever: Retriever):
        super().__init__(dotipe_config)
        self.retriever = retriever

    def retrieve_to_tmp(self, session):
        self.retriever.retrieve_data(session, TEMP_DIR)

    def compare(self, session):
        url, name, file_path_name = self.retriever.get_session_data(session)
        raw_path = f"{TEMP_DIR}/{name}"
        diffs = compare_files(f"{file_path_name}", raw_path)
        metadata = extract_compared_files_metadata(diffs, name)
        # TODO Fazer as diferenças usando uma tabela, pra cada diferença adicionar uma linha
        # Nao esquecer de fazer uns testes para CLI como um todo,
        # Não esquecer de testar essa função extract_compared_files_metadata
        print(metadata)
