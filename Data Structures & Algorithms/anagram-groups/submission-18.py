class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collection = {}
        for string in strs:
            sum = 0
            for char in string:
                sum += ord(char)
            if not collection:
                collection[sum] = [string]
            elif sum in collection and all(set(collection[sum][j]) == set(string) for j in range(len(collection[sum]))):
                collection[sum].append(string)
            elif sum not in collection:
                collection[sum] = [string]
            elif sum in collection and not all(set(collection[sum][j]) == set(string) for j in range(len(collection[sum]))):
                collection["outliers"] = [string] if "outliers" not in collection else collection["outliers"].append(string)

        return [collection[i] for i in collection]
            
        
        # seen = {}
        # key = 0
        # result = []

        # for string in strs:
        #     for char in string:
        #         key += ord(char)
        #         if not seen:
        #             seen[key] = [{}, []]

                
        #         if char in seen[key][0]:
        #             seen[key][0][char] -= 1
        #         if not seen[key][0]:
        #             seen[key][0][char] = 1
        #         if char in seen[key][0]:
        #             seen[key][0][char] += 1
        #     if all(value == 0 for value in seen[key].values()):
        #         seen[key][1].append(string)

        # for index, string in enumerate(strs):
        #     sub_seen = {}
        #     sub_result = []
        #     for char in string:
        #         for j in seen:
        #             if char in seen[j]:
        #                 sub[char] -= 1
        #         if all(value == 0 for value in seen[j].values()):
        #             sub_result.append([string])

        #         sub[char] = 1 if char not in sub else sub[char] += 1
        #     seen[index] = sub
