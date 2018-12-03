def chronal_calibration_part1(frequency_list):
    return sum(frequency_list)

def chronal_calibration_part2(frequency_list):
    diff_set = set()
    counter = 0
    len_feq = len(frequency_list)
    current_freq = 0
    diff_set.add(0)
    while True:
        current_freq += frequency_list[counter % len_feq]
        if current_freq in diff_set:
            return current_freq
        else:
            diff_set.add(current_freq)
            counter += 1