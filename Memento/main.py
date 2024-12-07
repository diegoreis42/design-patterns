from typing import List

class EditorMemento:
    def __init__(self, content: str):
        self._content = content

        def get_content(self) -> str:
            return self._content
        
# o editor que realiza as operações de texto

class TextEditor:
    def __init__(self):
        self._content = ''

    def write(self, text: str):
        self._content += text

    def get_content(self) -> str:
        return self._content
    
    def save(self) -> EditorMemento:
        #cria um memento contendo o estado atual
        return EditorMemento(self._content)
    
    def restore(self, memento: EditorMemento):
        #restaura o estado do editor
        self._content = memento.get_content()

# o caraketerque gerencia os mementos
class History:
    def __init__(self):
        self._mementos: List[EditorMemento] = []

    def save (self, memento: EditorMemento):
        if not self._mementos:
            raise Exception("Nada para desfazer!")
        #retorna o ultimo estado salvo
        return self.mementos.pop()
    
# exemplo de uso 

if __name__ == "__main__":
    editor = TextEditor()
    history = History()

    #escrevendo texto no editor
    editor.write("Olá mundo!")
    history.save(editor.save()) #salva estado

    print("Conteudo atual:", editor.get_content())

    #Desfazer
    editor.restore(history.undo())
    print("Conteúdo após desfazer 1:", editor.get_content())

    editor.restore(history.undo())
    print("Conteúdo após desfazer 2:", editor.get_content())