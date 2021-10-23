class InvalidDataError(Exception):
    """ Error raised when an invalid data type is requested
    """
    def __init__(self, data_type, message):
        self.data_type = data_type
        if len(message) > 0:
            message += " "
        message += f"Requsted data type is {data_type.name}"
        super().__init__(message)
