from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class SpaceStation(BaseModel):

    station_id: str = Field(min_length=3, max_length=10)
    name : str = Field(min_length=1, max_length=50)
    crew_size : int = Field(ge=1, le=20)
    power_level : float = Field(ge=0.0, le=100.0)
    oxygen_level : float = Field(ge=0.0, le=100.0)
    last_maintenance : datetime
    is_operational : bool = Field(default=True)
    notes : Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    space_station_1 = SpaceStation(
        station_id = "ISS001",
        name = "International Space Station",
        crew_size = 6,
        power_level = 0.855,
        oxygen_level = 0.923,
        last_maintenance = "2035-12-02 00:47:21"
    )