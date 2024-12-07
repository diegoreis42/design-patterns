from abc import ABC, abstractmethod

# Element base class
class Node(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

# Concrete Node classes
class City(Node):
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def accept(self, visitor):
        return visitor.visit_city(self)

class Industry(Node):
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees

    def accept(self, visitor):
        return visitor.visit_industry(self)

class TouristSpot(Node):
    def __init__(self, name, visitors_per_year):
        self.name = name
        self.visitors_per_year = visitors_per_year

    def accept(self, visitor):
        return visitor.visit_tourist_spot(self)

# Visitor base class
class Visitor(ABC):
    @abstractmethod
    def visit_city(self, city):
        pass

    @abstractmethod
    def visit_industry(self, industry):
        pass

    @abstractmethod
    def visit_tourist_spot(self, tourist_spot):
        pass

# Concrete Visitor: XML Exporter
class XMLExporter(Visitor):
    def visit_city(self, city):
        return f"<City><Name>{city.name}</Name><Population>{city.population}</Population></City>"

    def visit_industry(self, industry):
        return f"<Industry><Name>{industry.name}</Name><Employees>{industry.employees}</Employees></Industry>"

    def visit_tourist_spot(self, tourist_spot):
        return f"<TouristSpot><Name>{tourist_spot.name}</Name><VisitorsPerYear>{tourist_spot.visitors_per_year}</VisitorsPerYear></TouristSpot>"

# Graph class to hold nodes
class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def export_to_xml(self):
        exporter = XMLExporter()
        return "<Graph>" + "".join(node.accept(exporter) for node in self.nodes) + "</Graph>"

# Example usage
graph = Graph()
graph.add_node(City("New York", 8419000))
graph.add_node(Industry("TechCorp", 5000))
graph.add_node(TouristSpot("Statue of Liberty", 4300000))

xml_output = graph.export_to_xml()
print(xml_output)
