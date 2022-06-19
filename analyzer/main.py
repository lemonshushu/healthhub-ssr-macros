# https://www.notion.so/wl7788/be806f3eba77430ea5b01bf8e6e6da1e
import csv
import os


def process_log(logfile, outfile):
    print("Processing log file:", logfile)
    entries = []
    with open(logfile, "r") as f:
        for line in f:
            if "[BENCHMARK]" not in line:
                continue
            # print(line)
            location, marker, timestamp_method = line.strip().split(" ")
            # timestamp: ms
            timestamp, method = timestamp_method.split(",")
            # print(location, marker, timestamp, method)
            entries.append((timestamp, method))
    with open(outfile, "w") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "method"])
        writer.writerows(entries)


def main(datadir: str):
    dir_list = os.scandir(datadir)
    for item in dir_list:
        if item.is_dir():
            print(f"{item.name} is a directory")
            continue
        elif item.is_file():
            pass
            # print(f"{item.name} is a file")
        name, ext = os.path.splitext(item.name)
        if ext != ".log":
            print("Not a log file")
            continue
        modality, network_speed, situation, *method = name.split("-")
        if len(method) > 0:
            method = "original"
        else:
            method = "improved"
        print(modality, network_speed, situation, method)
        process_log(item.path, f"../csvs/{modality}-{network_speed}-{situation}-{method}.csv")


if __name__ == '__main__':
    main("../logs/")
