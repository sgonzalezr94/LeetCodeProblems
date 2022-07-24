from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        numbers_dict = dict()
        units_in_truck = 0
        for box in boxTypes:
            numbers_dict[box[1]] = box[0]
        while truckSize != 0 and numbers_dict:
            max_units = max(numbers_dict)
            boxes_per_unit = numbers_dict[max_units]
            if truckSize >= 0:
                if truckSize - boxes_per_unit < 0:
                    boxes_per_unit -= boxes_per_unit - truckSize
                    units_in_truck += max_units * boxes_per_unit
                    truckSize = 0
                    del numbers_dict[max_units]
                else:
                    units_in_truck += max_units * boxes_per_unit
                    truckSize -= boxes_per_unit
                    del numbers_dict[max_units]
            print(f"(max units,boxes per unit) = ({boxes_per_unit},{max_units})")

            # units_in_truck += max_units * boxes_per_unit
        print(units_in_truck)
        return units_in_truck


sol = Solution()
sol.maximumUnits(boxTypes=[[1, 3], [2, 2], [3, 1]], truckSize=4)
sol.maximumUnits(boxTypes=[[5, 10], [2, 5], [4, 7], [3, 9]], truckSize=10)
sol.maximumUnits(
    boxTypes=[
        [2, 1],
        [4, 4],
        [3, 1],
        [4, 1],
        [2, 4],
        [3, 4],
        [1, 3],
        [4, 3],
        [5, 3],
        [5, 3],
    ],
    truckSize=13,
)
