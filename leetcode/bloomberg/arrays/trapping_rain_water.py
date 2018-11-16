class WaterUtils(object):
    """
    instead of trying to solve the problem in one efficient algo
    try separating it into smaller parts and put the pieces together

    [0,1,0,2,1,0,1,3,2,1,2,1]
    """
    def trap_water(self, elevations):
        def find_right_h(start_h):
            print(f'start_h:{start_h}')
            next_biggest = start_h+1
            for i in range(start_h+2, len(elevations)):
                if elevations[i] >= elevations[start_h]:
                    right_h = i
                    return right_h
                elif elevations[i] > elevations[next_biggest]:
                    next_biggest = i

            right_h = next_biggest
            return right_h

        def get_water_area(A, l, r):
            for i in range(l+1, r):
                A-=elevations[i]
            print(f'[DEBUG]: water_area={A}')
            return A

        rainwater_area = 0
        if len(elevations) < 2:
            return rainwater_area
        start_h = 0
        while start_h < len(elevations):
            right_h = None
            while start_h < len(elevations):
                right_h = find_right_h(start_h)
                if right_h:
                    break
                else:
                    start_h += 1
            if start_h < len(elevations):
                print(f'[DEBUG]: start_h={start_h} right_h={right_h}')
                total_area = (right_h-start_h-1)*elevations[start_h]
                print(f'[DEBUG]: total_area={total_area}')
                water_area = get_water_area(total_area, start_h, right_h)
                rainwater_area += water_area
                print(f'[DEBUG]: rainwater_area={rainwater_area}')
                start_h = right_h

        return rainwater_area

    """
    algo:
    for each point (i) in the elevations graph
    search for a point to the left inclusive that is the biggest
    search for a point to the right inclusive that is biggest
    water_area += min(left, right) - height[i]
    --> the reasoning here is we are always bounded by the shorter side for 
    area calculations. it's ok to use the biggest non-bounded side because
    there is a side below the non-bounded biggest that is actually
    bounding the water
    --> it is - height[i] b/c the bottom bound is the height of the 
    point that we're at 
    
    in the case where there isn't a bigger edge for either side
    --> the water area here is 0 because there isn't a "hole" for water
    to fill in 
    """
    def trap1(self, height):
        ans = 0
        size = len(height)
        for i in range(1, size-1):
            max_left = max_right = 0
            for j in range(i, -1, -1):
                max_left = max(max_left, height[j])
            for j in range(i, size):
                max_right = max(max_right, height[j])
            ans += min(max_left, max_right) - height[i]
        return ans

    def trap2(self, height):
        if height is None:
            return 0
        ans = 0
        size = len(height)
        left_max = [None for i in range(size)]
        right_max = [None for i in range(size)]
        left_max[0] = height[0]
        for i in range(1, size):
            left_max[i] = max(height[i], left_max[i-1])
        right_max[size-1] = height[size-1]
        for i in range(size-1, -1, -1):
            right_max[i] = max(height[i], right_max[i+1])
        for i in range(1, size-1):
            ans += min(left_max[i], right_max[i])-height[i]
        return ans

    def trap3(self, height):
        

if __name__ == '__main__':
    sol = WaterUtils()
    elevations = [4,2,3]
    print(sol.trap_water(elevations))