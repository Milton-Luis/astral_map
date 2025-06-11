from typing import List


class PlanetPhala:
    planet_list = [
        "SOL",
        "LUA",
        "MARTE",
        "MERCURIO",
        "JUPITER",
        "VENUS",
        "SATURNO",
        "NENHUM",
    ]

    def __init__(self, planet: List[str], ishtaphala: str, kashtaphala: str, strenghts: str):
        self._planet = planet
        self._ishtaphala = self._parse_value(ishtaphala)
        self._kashtaphala = self._parse_value(kashtaphala)
        self._strenghts = self._parse_value(strenghts)
        self._description = None

    def _parse_value(self, value: str) -> float:
        try:
            return float(str(value.replace(",", ".")))
        except ValueError:
            raise ValueError(f"Valor Invalido {value}")

    def _read_planet_file(self):
        if self._planet in self.planet_list:
            ...

planet = "Sol"
# value_1 = "None"
value_2 = "201.43"
