from abc import ABC, abstractmethod


class RWStream(ABC):
    @abstractmethod
    def readline(self) -> str:
        pass
    
    @abstractmethod
    def writeline(self, line: str):
        pass
