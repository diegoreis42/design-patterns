from abc import ABC, abstractmethod

class EstrategiaRoteamento(ABC):
    @abstractmethod
    def calcular_rota(self, origem, destino):
        pass
class RotaRodovia(EstrategiaRoteamento):
    def calcular_rota(self, origem, destino):
        return f"Calculando a rota mais rapida de {origem} para {destino} via rodovias."
    
class RotaCaminhada(EstrategiaRoteamento):
    def calcular_rota(self, origem, destino):
        return f"Calculando a rota mais rapida de {origem} para {destino} para caminhada."
    
class RotaTransportePublico(EstrategiaRoteamento):
    def calcular_rota(self, origem, destino):
        return f"Calculando a rota mais rapida de {origem} para {destino} Utilizando transporte publico."
     
class RotaCiclista(EstrategiaRoteamento):
    def calcular_rota(self, origem, destino):
        return f"Calculando a rota mais rapida de {origem} para {destino}."

class RotaTuristica(EstrategiaRoteamento):
    def calcular_rota(self, origem, destino):
        return f"Calculando a rota mais rapida de {origem} para {destino} Passando por pontos turisticos."

class Navegador:
    def __init__(self, estrategia: EstrategiaRoteamento) :
        self.estrategia = estrategia

    def definir_estrategia(self, nova_estrategia: EstrategiaRoteamento):
        self.estrategia = nova_estrategia   

    def calcular_rota(self, origem, destino):
        return self.estrategia.calcular_rota(origem, destino)
    
    #definindo pontos de origem e destino

    origem = " Praça Central"

    destino = " Museu de Artes "

    # criando um navegador com a estrategia inicial

    navegador = Navegador(RotaRodovia())
    print(navegador.calcular_rota(origem, destino))

    #Alterando para estrategia de caminhada
    navegador.definir_estrategia(RotaCaminhada())
    print(navegador.calcular_rota(origem, destino))


    #Alterando para trasnporte publico
    navegador.definir_estrategia(RotaTransportePublico())
    print(navegador.calcular_rota(origem, destino))
    
    #Alterando para ciclista
    navegador.definir_estrategia(RotaCiclista())
    print(navegador.calcular_rota(origem, destino))
    
    #Alterando para rota turistica
    navegador.definir_estrategia(RotaTuristica())
    print(navegador.calcular_rota(origem, destino))
    