from abc import ABC, abstractmethod
from gol import GOL

class Brush(ABC):
    @abstractmethod
    def apply(self, gol: GOL, row, col):
        pass

class BaseBrush(Brush):
    def apply(self, gol, row, col):
        gol.set_cell(row,col)

class GliderBrush(Brush):
    def apply(self, gol, row, col):
        pattern = [
            (0, 1), (1, 2), (2, 0), (2, 1), (2, 2)
        ]

        for dr, dc in pattern:
            gol.set_cell(row + dr, col + dc)

class BlinkerBrush(Brush):
    def apply(self,gol,row,col):
        pattern = [
            (0, 0), (0, 1), (0, 2)
        ]
        for dr, dc in pattern:
            gol.set_cell(row + dr, col + dc)

class PulsarBrush(Brush):
    def apply(self, gol, row, col):
        pattern = [
            (2, 4), (2, 5), (2, 6), (2, 10), (2, 11), (2, 12),
            (4, 2), (5, 2), (6, 2), (10, 2), (11, 2), (12, 2),
            (4, 7), (5, 7), (6, 7), (10, 7), (11, 7), (12, 7),
            (4, 9), (5, 9), (6, 9), (10, 9), (11, 9), (12, 9),
            (4, 14), (5, 14), (6, 14), (10, 14), (11, 14), (12, 14),
            (7, 4), (7, 5), (7, 6), (7, 10), (7, 11), (7, 12),
            (9, 4), (9, 5), (9, 6), (9, 10), (9, 11), (9, 12),
            (14, 4), (14, 5), (14, 6), (14, 10), (14, 11), (14, 12),
        ]
        for dr, dc in pattern:
            gol.set_cell(row + dr, col + dc)

if __name__ == "__main__":
    gol = GOL(20,20)
    brush = PulsarBrush()
    brush.apply(gol,2,2)
    print(gol)