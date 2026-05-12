class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_dict = {position[i]: speed[i] for i in range(len(position))}
        car_dict = dict(sorted(car_dict.items(), reverse=True))
        s = []
        for i in car_dict:
            time = (target - i) / car_dict[i]
            if not s or time > s[-1]:
                s.append(time)
        return len(s)