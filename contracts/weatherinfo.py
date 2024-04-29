from dataclasses import dataclass, asdict


@dataclass
class WeatherInfo:
    temperature: str
    humidity: str
    description: str
    wind_speed: str

    def serialize(self):
        return asdict(self)
