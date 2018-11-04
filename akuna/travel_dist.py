from math import floor, acos, sin, cos, radians

RADIUS_MILES = 3963


class DestinationCalculator:
    call_num = 0
    long_diff = 0
    lat1 = 0
    lat2 = 0
    city1 = ''
    city2 = ''

    def process(self, line: str) -> str:
        if self.call_num == 0:
            self.call_num += 1

            parts = line.split(':')
            parts[1] = parts[1].replace('\U00002013', '-')
            parts[2] = parts[2].replace('\U00002013', '-')
            self.long_diff = abs(radians(float(parts[2])) - radians(float(parts[3])))
            self.city1 = parts[1]
            return self.city1

        elif self.call_num == 1:
            self.call_num += 1

            parts = line.split(':')
            self.lat1 = parts[2]
            self.lat2 = parts[3]
            self.city2 = parts[1]
            return self.city2

        else:
            self.call_num = 0
            parts = line.split(':')
            return parts[1] + ':' + parts[2] + ':' + parts[3] + ':' + str(self.spherical_law())


    def spherical_law(self):
        lat1 = radians(float(self.lat1))
        lat2 = radians(float(self.lat2))
        tmp = acos(sin(lat1) * sin(lat2) + cos(lat1)
                   * cos(lat2) * cos(self.long_diff))
        return floor(RADIUS_MILES * tmp)

if __name__ == '__main__':
    sol = DestinationCalculator()
    print(sol.process('LOC:CHI:41.836944:-87.684722'))
    print(sol.process('LOC:NYC:40.7127:-74.0059'))
    print(sol.process('TRIP:C0FFEE1C:CHI:NYC'))

