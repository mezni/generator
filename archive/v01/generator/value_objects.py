class CallType:
    VOICE_OUTGOING = "Voice"
    VOICE_INCOMING = "Voice"
    SMS_MO = "SMS"
    SMS_MT = "SMS"
    DATA_SESSION = "Data"
    INTERNATIONAL_VOICE = "Voice"
    ROAMING_VOICE_OUTGOING = "Voice"
    ROAMING_VOICE_INCOMING = "Voice"
    EMERGENCY_CALL = "Emergency Call"
    TOLL_FREE = "Toll-Free Call"

    @staticmethod
    def list_types():
        return [
            attr
            for attr in dir(CallType)
            if not callable(getattr(CallType, attr)) and not attr.startswith("__")
        ]
