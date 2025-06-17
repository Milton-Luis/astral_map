from app.models.planet_phala_model import PlanetPhala


class AstroHouse:
    house_number = [
        (1, "1ª Casa: A Casa do Eu (Tanu Bhava)"),
        (2, "2ª Casa: Riqueza e Família (Dhana Bhava)"),
        (3, "3ª Casa: Comunicação e Coragem (Sahaja Bhava)"),
        (4, "4ª Casa: Lar e Felicidade (Sukha Bhava)"),
        (5, "5ª Casa: Criatividade e Filhos (Putra Bhava)"),
        (6, "6ª Casa: Trabalho e Saúde (Shatru Bhava)"),
        (7, "7ª Casa: Parcerias e Casamento (Kalatra Bhava)"),
        (8, "8ª Casa: Transformação e Segredos (Ayur Bhava)"),
        (9, "9ª Casa: Sabedoria e Espiritualidade (Dharma Bhava)"),
        (10, "10ª Casa: Carreira e Reputação (Karma Bhava)"),
        (11, "11ª Casa: Ganhos e Desejos (Labha Bhava)"),
        (12, "12ª Casa: Perdas e Liberação (Vyaya Bhava)"),
    ]

    def __init__(self, house, strengths, planet: PlanetPhala):
        self._house = house
        self._strengths = strengths
        self._planet = planet

    def _show_house(self):
        for number, description in self.house_number:
            if number == self._house:
                return description
        return "Casa desconhecida"

    def check_strengths(self, strength: float):
        if strength > 1:
            return self._show_house()
        elif self._strengths > 2 and self._strengths < 4:
            ...
        else:
            ...

    def check_house_and_planet(self):
        """
        SE A CASA FOR 1
                SE A CASA TIVER FORÇA X>
                        COLOCAR PLANETAS DA RESPECTIVA CASA

        """
        match self._house:
            case 1:
                ...
            case 2:
                return self._show_house()
