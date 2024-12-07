from abc import ABC, abstractmethod

# 1. Interface/Classe abstrata para Transporte

class Transporte(ABC):
    @abstractmethod
    def entregar(self) -> None:
        pass

# 2. Subclasses concretas de Transporte

class Caminhao(Transporte):
    def entregar(self):
        print("Entrega realizada por Caminhão.")

class Navio(Transporte):
    def entregar(self):
        print("Entrega realizada por Navio.")

# 3. Classe abstrata para Logística (Fábrica)
class Logistica(ABC):
    @abstractmethod
    def criar_transporte(self):
        pass

    def realizar_entrega(self):
        transporte = self.criar_transporte()
        transporte.entregar()

# 4. Fábricas concretas

class LogisticaCaminhao(Logistica):
    def criar_transporte(self):
        return Caminhao()

class LogisticaNavio(Logistica):
    def criar_transporte(self):
        return Navio()

# 5. Código cliente

def cliente(logistica):
    logistica.realizar_entrega()


# Testando a aplicação
if __name__ == "__main__":
    print("=== Logística com Caminhão ===")
    logistica_caminhao = LogisticaCaminhao()
    cliente(logistica_caminhao)

    print("\n=== Logística com Navio ===")
    logistica_navio = LogisticaNavio()
    cliente(logistica_navio)

