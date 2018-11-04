class StatisticsCalculator:
    #dummy k-v
    cust_traveled = {'': 0}
    city_miles = {'': 0}

    total_dist = 0
    curr_most_traveled = ''
    curr_busiest = ''


    def process(self, line: str) -> str:
        parts = line.split(':')

        self.total_dist += int(parts[3])

        self.get_most_traveled(parts[0], int(parts[3]))

        self.get_busiest(parts[1], parts[2], int(parts[3]))

        return str(self.total_dist) + ':' + self.curr_most_traveled + ':' + self.curr_busiest

    def get_most_traveled(self, cust, miles):
        print(cust)
        if cust not in self.cust_traveled:
            self.cust_traveled[cust] = miles
        else:
            self.cust_traveled[cust] += miles

        curr = self.cust_traveled[self.curr_most_traveled]
        temp = self.cust_traveled[cust]
        # print(temp)
        # print(self.curr_most_traveled == '')
        self.curr_most_traveled = cust if curr >= temp else cust

    def get_busiest(self, depart, dest, miles):
        dep_flag = depart not in self.city_miles
        dest_flag = dest not in self.city_miles
        if dep_flag:
            self.city_miles[depart] = miles
        else:
            self.city_miles[depart] += miles
        if dest_flag:
            self.city_miles[dest] = miles
        else:
            self.city_miles[dest] += miles

        equal = self.city_miles[depart] == self.city_miles[dest]
        curr = self.city_miles[self.curr_busiest]
        res = curr
        if self.city_miles[depart] > curr and equal:
            res = depart if ord(depart[0]) > ord(dest[0]) else dest
        elif self.city_miles[depart] > curr:
            res = depart
        elif self.city_miles[dest] > curr:
            res = dest

        self.curr_busiest = res

if __name__ == '__main__':
    sol = StatisticsCalculator()
    print(sol.process('C0FFEE1C:CHI:NYC:714'))
    # sol.process('0FF1CE18:LA:SEATTLE:961')
    # sol.process('C0FFEE1C:NYC:LA:2448')