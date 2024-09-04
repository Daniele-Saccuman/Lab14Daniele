from dataclasses import dataclass

@dataclass
class Gene:
    GeneID: str
    Function: str
    Essential: str
    Chromosome: int


    def __str__(self):
        return self.GeneID

    def __hash__(self):
        return hash(self.GeneID)