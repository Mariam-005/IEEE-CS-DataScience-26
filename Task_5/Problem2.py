class Solution:
    def sampleStats(self, count):
        minimum= -1
        maximum= -1
        mode =0
        max_count =0
        total_sum =0
        total_elements =0

        for i in range(len(count)):
            freq = count[i]
            if freq > 0:
                if minimum == -1: minimum = i
                maximum = i
                if freq > max_count:
                    max_count = freq
                    mode = i
                total_sum += i*freq
                total_elements+= freq

        mean = total_sum/total_elements
        mid1 = (total_elements + 1) // 2
        mid2 = (total_elements // 2) + 1
        current = 0
        median_low = 0
        median_high = 0

        for i in range(len(count)):
            freq = count[i]
            current += freq
            if current >= mid1 and median_low == 0:
                median_low = i
            if current >= mid2:
                median_high = i
                break

        median = (median_low +median_high) / 2.0

        return [float(minimum), float(maximum), mean, median, float(mode)]