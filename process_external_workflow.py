

# converts a string of the form "M:SS" to number of seconds
def time_string_to_seconds(time_string):
    minutes, seconds = map(int, time_string.split(':'))
    total_seconds = minutes * 60 + seconds
    return total_seconds

def main():
    file = "external_workflow_data.csv"
    all_total_time_old = []
    all_total_time_new = []
    all_saved_time = []
    with open(file, "r") as f:
        data = f.read().split("\n")[1:]
        for line in data:
            action_id = line.split(", ")[0]
            times = line.split(", ")[1:]
            total_time_old = sum(map(time_string_to_seconds, times[:3]))
            build_time_old = sum(map(time_string_to_seconds, times[3:]))
            build_time_new = build_time_old / 3
            total_time_new = (total_time_old - build_time_old) + build_time_new
            saved_time = total_time_old - total_time_new

            all_total_time_old.append(total_time_old)
            all_total_time_new.append(total_time_new)
            all_saved_time.append(saved_time)
        
    print("Average Total Time (s)", sum(all_total_time_old) / len(all_total_time_old))
    print("Average Total Time with Build Reuse (s)", sum(all_total_time_new) / len(all_total_time_new))
    print("Average Saved Time (s)", sum(all_saved_time) / len(all_saved_time))


if __name__ == "__main__":
    main()