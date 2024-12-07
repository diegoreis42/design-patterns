from abc import ABC, abstractmethod

# classe base abstrata

class DataMiner(ABC):
    def mine (self, file_path: str):
        #esqueleto algoritimo
        data = self.open_file(file_path)
        raw_data = self.extract_data(data)
        structured_data = self.process_data(raw_data)
        self.analize_dat(structured_data)
        self.close_file(data)

    @abstractmethod
    def open_file(self, file_path: str):
        pass

    @abstractmethod
    def extract_data(sel, file):
        pass

    def process_dat(self, raw_data)  :
        #codigo comun para processar dados
        print(f"Processando dados: {raw_data}") 
        return {"structured_data":raw_data  }
    def analyze_data(self, structured_data):
        print(f"Analisando dados estruturados: {structured_data}")   

    def close_file(self, file):
        print(f"Fechando arquivo:{file}")

#subclasses para formato especificos

class DocMiner(DataMiner):
    def open_file(self, file_path: str):
        print(f"Abrindo arquivo DOC: {file_path}")
        return f"DOC content of {file_path}"
    
    def extract_data(sel, file):
        print (f"EXtraindo dados do DOC : {file}")
        return {"doc_data": "dados extraidos DOC"}
    
class CsvMiner(DataMiner):
    def open_file(self, file_path: str):
        print(f"Abrindo arquivo CSV: {file_path}")
        return f"CSV content of {file_path}"
    
    def extract_data(sel, file):
        print (f"EXtraindo dados do CSV : {file}")
        return {"doc_data": "dados extraidos CSV"}
    
class PdfMiner(DataMiner):
    def open_file(self, file_path: str):
        print(f"Abrindo arquivo PDF: {file_path}")
        return f"PDF content of {file_path}"
    
    def extract_data(sel, file):
        print (f"EXtraindo dados do PDF : {file}")
        return {"doc_data": "dados extraidos PDF"}
    
def main():
    file_processors = {
        "doc": DocMiner(),
        "csv": CsvMiner(),
        "pdf": PdfMiner(),
    }

    files = [
        ("doc","documento.doc"),
        ("csv","dados.csv"),
        ("pdf","relatorio.pdf"),
    ]

    for file_type, file_path in files:
        processor = file_processors[file_type]
        print(f"Processando arquivo: {file_path}")
        processor.mine(file_path)
        print(" _ " * 40)

if __name__ == " __main__":
    main()