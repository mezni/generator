# entities.py
class Location:
    def __init__(
        self,
        Location_id: int,
        name: str,
        network_type: str,
        latitude_min: float,
        latitude_max: float,
        longitude_min: float,
        longitude_max: float,
    ):
        self.Location_id = Location_id
        self.name = name
        self.network_type = network_type
        self.latitude_min = latitude_min
        self.latitude_max = latitude_max
        self.longitude_min = longitude_min
        self.longitude_max = longitude_max

        # Validate the geographic boundaries
        self._validate_coordinates()

    def _validate_coordinates(self):
        # Validate latitude boundaries
        if not (-90 <= self.latitude_min <= 90) or not (-90 <= self.latitude_max <= 90):
            raise ValueError("Latitude must be between -90 and 90 degrees.")
        if self.latitude_min > self.latitude_max:
            raise ValueError("latitude_min cannot be greater than latitude_max.")

        # Validate longitude boundaries
        if not (-180 <= self.longitude_min <= 180) or not (
            -180 <= self.longitude_max <= 180
        ):
            raise ValueError("Longitude must be between -180 and 180 degrees.")
        if self.longitude_min > self.longitude_max:
            raise ValueError("longitude_min cannot be greater than longitude_max.")

    def contains_point(self, latitude: float, longitude: float) -> bool:
        """Check if a given point is within the geographical boundaries of the location."""
        return (self.latitude_min <= latitude <= self.latitude_max) and (
            self.longitude_min <= longitude <= self.longitude_max
        )

    def __repr__(self):
        """Representation for better debugging and visualization."""
        return (
            f"Location({self.Location_id}, {self.name}, {self.network_type}, "
            f"Latitude: {self.latitude_min} to {self.latitude_max}, "
            f"Longitude: {self.longitude_min} to {self.longitude_max})"
        )


class NetworkElement:
    def __init__(
        self,
        element_id: int,
        element_name: str,
        network_type: str,
        ip_address: str,
        status: str,
        function: str,
        location_id: int,
        cell_id: int = None,
        lac: int = None,
        tac: int = None,
    ):
        self.element_id = element_id
        self.element_name = element_name
        self.network_type = network_type
        self.ip_address = ip_address
        self.status = status
        self.function = function
        self.location_id = location_id
        self.cell_id = cell_id
        self.lac = lac
        self.tac = tac

    def __repr__(self):
        return f"NetworkElement(ID: {self.element_id}, Name: {self.element_name}, Type: {self.network_type}, IP: {self.ip_address}, Status: {self.status}, Function: {self.function}, Location ID: {self.location_id}, Cell ID: {self.cell_id}, LAC: {self.lac}, TAC: {self.tac})"
