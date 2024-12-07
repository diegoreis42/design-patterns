# Interface para Jogadores
class Jogador:
    def exibir_detalhes(self):
        pass


# Interface para Uniformes
class Uniforme:
    def exibir_detalhes(self):
        pass


# Interface para Estádios
class Estadio:
    def exibir_detalhes(self):
        pass


# Jogadores de Palmeiras
class JogadorPalmeiras(Jogador):
    def exibir_detalhes(self):
        return "Jogador do Palmeiras"


# Jogadores de São Paulo
class JogadorSaoPaulo(Jogador):
    def exibir_detalhes(self):
        return "Jogador do São Paulo"


# Uniforme de Palmeiras
class UniformePalmeiras(Uniforme):
    def exibir_detalhes(self):
        return "Uniforme verde do Palmeiras"


# Uniforme de São Paulo
class UniformeSaoPaulo(Uniforme):
    def exibir_detalhes(self):
        return "Uniforme tricolor do São Paulo"


# Estádio do Palmeiras
class EstadioPalmeiras(Estadio):
    def exibir_detalhes(self):
        return "Estádio Allianz Parque (Palmeiras)"


# Estádio do São Paulo
class EstadioSaoPaulo(Estadio):
    def exibir_detalhes(self):
        return "Estádio Morumbi (São Paulo)"


# Fábrica Abstrata
class TimeFactory:
    def criar_jogador(self):
        pass

    def criar_uniforme(self):
        pass

    def criar_estadio(self):
        pass


# Fábrica de Palmeiras
class PalmeirasFactory(TimeFactory):
    def criar_jogador(self):
        return JogadorPalmeiras()

    def criar_uniforme(self):
        return UniformePalmeiras()

    def criar_estadio(self):
        return EstadioPalmeiras()


# Fábrica de São Paulo
class SaoPauloFactory(TimeFactory):
    def criar_jogador(self):
        return JogadorSaoPaulo()

    def criar_uniforme(self):
        return UniformeSaoPaulo()

    def criar_estadio(self):
        return EstadioSaoPaulo()


# Cliente Utilizando a Fábrica Abstrata
def criar_time(factory: TimeFactory):
    jogador = factory.criar_jogador()
    uniforme = factory.criar_uniforme()
    estadio = factory.criar_estadio()

    print(jogador.exibir_detalhes())
    print(uniforme.exibir_detalhes())
    print(estadio.exibir_detalhes())


# Criando um time do Palmeiras
print("Detalhes do time Palmeiras:")
palmeiras_factory = PalmeirasFactory()
criar_time(palmeiras_factory)

# Criando um time do São Paulo
print("\nDetalhes do time São Paulo:")
sao_paulo_factory = SaoPauloFactory()
criar_time(sao_paulo_factory)
