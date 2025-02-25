from dataclasses import dataclass

@dataclass
class Register:
    address: int
    value: int
