import re


class Subscriber:
    def __init__(
        self,
        subscriber_id: int,
        msisdn: str,
        imsi: str,
        imei: str,
        sim_id: str,
        subscriber_type: str,  # home. national, international
        account_type: str,  # prepaid, postpaid
        account_status: str,
    ):
        self.subscriber_id = subscriber_id
        self.msisdn = msisdn
        self.imsi = imsi
        self.imei = imei
        self.sim_id = sim_id
        self.subscriber_type = subscriber_type
        self.account_type = account_type
        self.account_status = account_status

        self._validate_msisdn()
        self._validate_imsi()
        self._validate_imei()

    def _validate_msisdn(self):
        """Validates the MSISDN format (example: 10 digits)."""
        if not re.match(r"^\d{10}$", self.msisdn):
            raise ValueError(f"Invalid MSISDN: {self.msisdn}")

    def _validate_imsi(self):
        """Validates the IMSI format (example: 15 digits)."""
        if not re.match(r"^\d{15}$", self.imsi):
            raise ValueError(f"Invalid IMSI: {self.imsi}")

    def _validate_imei(self):
        """Validates the IMEI format (example: 15 digits)."""
        if not re.match(r"^\d{15}$", self.imei):
            raise ValueError(f"Invalid IMEI: {self.imei}")

    def to_dict(self):
        return {
            "subscriber_id": self.subscriber_id,
            "msisdn": self.msisdn,
            "imsi": self.imsi,
            "imei": self.imei,
            "sim_id": self.sim_id,
            "subscriber_type": self.subscriber_type,
            "account_type": self.account_type,
            "account_status": self.account_status,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            subscriber_id=data["subscriber_id"],
            msisdn=data["msisdn"],
            imsi=data["imsi"],
            imei=data["imei"],
            sim_id=data["sim_id"],
            subscriber_type=data["subscriber_type"],
            account_type=data["account_type"],
            account_status=data["account_status"],
        )


class Location:
    def __init__(
        self,
        location_id: int,
        name: str,
        network_type: str,
        latitude_min: float,
        latitude_max: float,
        longitude_min: float,
        longitude_max: float,
    ):
        self.location_id = location_id
        self.name = name
        self.network_type = network_type
        self.latitude_min = latitude_min
        self.latitude_max = latitude_max
        self.longitude_min = longitude_min
        self.longitude_max = longitude_max

        # Validate the geographic boundaries
        self._validate_coordinates()

    def _validate_coordinates(self):
        """Validates latitude and longitude boundaries."""
        if not (-90 <= self.latitude_min <= 90) or not (-90 <= self.latitude_max <= 90):
            raise ValueError("Latitude must be between -90 and 90 degrees.")
        if self.latitude_min > self.latitude_max:
            raise ValueError("latitude_min cannot be greater than latitude_max.")

        if not (-180 <= self.longitude_min <= 180) or not (
            -180 <= self.longitude_max <= 180
        ):
            raise ValueError("Longitude must be between -180 and 180 degrees.")
        if self.longitude_min > self.longitude_max:
            raise ValueError("longitude_min cannot be greater than longitude_max.")

    def __repr__(self):
        return (
            f"Location(location_id={self.location_id}, name={self.name}, "
            f"network_type={self.network_type}, lat_min={self.latitude_min}, lat_max={self.latitude_max}, "
            f"lon_min={self.lon_min}, longitude_max={self.longitude_max})"
        )

    def __str__(self):
        return f"Location: {self.name} ({self.network_type}) - Lat: {self.latitude_min}-{self.latitude_max}, Lon: {self.longitude_min}-{self.longitude_max}"

    def to_dict(self):
        return {
            "location_id": self.location_id,
            "name": self.name,
            "network_type": self.network_type,
            "latitude_min": self.latitude_min,
            "latitude_max": self.latitude_max,
            "longitude_min": self.longitude_min,
            "longitude_max": self.longitude_max,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            location_id=data["location_id"],
            name=data["name"],
            network_type=data["network_type"],
            latitude_min=data["latitude_min"],
            latitude_max=data["latitude_max"],
            longitude_min=data["longitude_min"],
            longitude_max=data["longitude_max"],
        )


class NetworkElement:
    VALID_STATUSES = {"Active", "Inactive"}

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

        # Validate attributes
        self._validate_ip_address()
        self._validate_status()
        self._validate_cell_id()
        self._validate_lac()
        self._validate_tac()

    def _validate_ip_address(self):
        """Validates the IP address format."""
        ip_pattern = (
            r"^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\."
            r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\."
            r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\."
            r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$"
        )
        if not re.match(ip_pattern, self.ip_address):
            raise ValueError(f"Invalid IP address: {self.ip_address}")

    def _validate_status(self):
        """Validates that the status is one of the predefined valid values."""
        if self.status not in self.VALID_STATUSES:
            raise ValueError(
                f"Invalid status: {self.status}. Valid statuses are: {self.VALID_STATUSES}"
            )

    def _validate_cell_id(self):
        """Validates that cell_id is a positive integer."""
        if self.cell_id and not isinstance(self.cell_id, int):
            raise ValueError(f"Invalid cell_id: {self.cell_id}. Must be an integer.")

    def _validate_lac(self):
        """Validates that lac is a positive integer."""
        if self.lac and not isinstance(self.lac, int):
            raise ValueError(f"Invalid LAC: {self.lac}. Must be an integer.")

    def _validate_tac(self):
        """Validates that tac is a positive integer."""
        if self.tac and not isinstance(self.tac, int):
            raise ValueError(f"Invalid TAC: {self.tac}. Must be an integer.")

    def __repr__(self):
        return (
            f"NetworkElement(element_id={self.element_id}, element_name={self.element_name}, "
            f"network_type={self.network_type}, ip_address={self.ip_address}, location_id={self.location_id}, "
            f"status={self.status}, function={self.function}, cell_id={self.cell_id}, "
            f"lac={self.lac}, tac={self.tac})"
        )

    def __str__(self):
        return f"Network Element: {self.element_name} ({self.network_type}), IP: {self.ip_address}, Location: {self.location_id}, Status: {self.status}"

    def to_dict(self):
        return {
            "element_id": self.element_id,
            "element_name": self.element_name,
            "network_type": self.network_type,
            "ip_address": self.ip_address,
            "status": self.status,
            "function": self.function,
            "location_id": self.location_id,
            "cell_id": self.cell_id,
            "lac": self.lac,
            "tac": self.tac,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            element_id=data["element_id"],
            element_name=data["element_name"],
            network_type=data["network_type"],
            ip_address=data["ip_address"],
            status=data["status"],
            function=data["function"],
            location_id=data["location_id"],
            cell_id=data.get("cell_id"),
            lac=data.get("lac"),
            tac=data.get("tac"),
        )
