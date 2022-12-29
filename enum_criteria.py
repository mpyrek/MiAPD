from enum import Enum

class Criteria(Enum):
    PRICE = 0
    DISTANCE = 1
    ALTITUDE = 2
    PISTE = 3
    LIFTS = 4
    GONDOLAS = 5

    def get_name(self):
        criteria = ["price (£)", "distance from lift (m)", "altitude (m)", "total piste distance (km)", "total lifts", "total gondolas"]
        return criteria[self.value]
    def get_origin_name(self):
        criteria = ["price (£)", "distance_from_lift_(m)", "altitude (m)", "totalPiste (km)", "totalLifts", "gondolas"]
        return criteria[self.value]

# print(Criteria.PRICE.get_name())
