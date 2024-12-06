from abc import ABC, abstractmethod


# Handler - Interface comum para todos os manipuladores
class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: 'Handler') -> 'Handler':
        pass

    @abstractmethod
    def handle(self, package: dict) -> None:
        pass


# Base Handler - Implementação padrão
class BaseHandler(Handler):
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def handle(self, package: dict) -> None:
        if self._next_handler:
            self._next_handler.handle(package)
        else:
            print("Encomenda não pode ser tratada.")


# Concrete Handlers - Manipuladores específicos
class LocalPostOfficeHandler(BaseHandler):
    def handle(self, package: dict) -> None:
        if package["size"] == "small":
            print("Correio Local: Processando encomenda pequena.")
        else:
            super().handle(package)


class RegionalDistributionCenterHandler(BaseHandler):
    def handle(self, package: dict) -> None:
        if package["size"] == "medium":
            print("Centro Regional: Processando encomenda média.")
        else:
            super().handle(package)


class NationalTransportHandler(BaseHandler):
    def handle(self, package: dict) -> None:
        if package["size"] == "large" or package["international"]:
            print("Transportadora Nacional: Processando encomenda grande ou internacional.")
        else:
            super().handle(package)


# Client - Configurando a cadeia e enviando a solicitação
if __name__ == "__main__":
    # Criando os manipuladores
    local_post_office = LocalPostOfficeHandler()
    regional_center = RegionalDistributionCenterHandler()
    national_transport = NationalTransportHandler()

    # Configurando a cadeia
    local_post_office.set_next(regional_center).set_next(national_transport)

    # Criando pacotes para teste
    packages = [
        {"size": "small", "international": False},
        {"size": "medium", "international": False},
        {"size": "large", "international": False},
        {"size": "small", "international": True},
        {"size": "unknown", "international": False},
    ]

    # Processando as encomendas
    for package in packages:
        print(f"\nProcessando pacote: {package}")
        local_post_office.handle(package)
