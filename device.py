class Device:
    """Device description"""
    def __init__(self, device_info):
        self.ip = device_info[0]  #Device IP
        self.device_type_and_location = device_info[1].replace("Devices\\", "")  # Remove folder name
        self.device_id = device_info[2]  # device ID (number of string)

    def get_all_information(self):
        all_info = [self.ip, self.device_type_and_location, self.device_id]
        return all_info
