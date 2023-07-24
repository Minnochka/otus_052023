"""
create dataclass `Engine`
"""
from dataclasses import dataclass

@dataclass
class Engine:
    __slots__ = ("volume", "pistons")
    volume: int
    pistons: int

