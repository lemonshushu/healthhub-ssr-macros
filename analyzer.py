import os

import matplotlib.pyplot as plt
import pandas as pd
from scipy import integrate


class BenchmarkResult:
    def __init__(self, network, dataseq, alg, time, mean_score):
        self.network = network
        self.dataseq = dataseq
        self.alg = alg
        self.time = time
        self.mean_score = mean_score

    def __str__(self):
        return "{}-{}-{}, time: {}, mean_score: {}".format(self.network, self.dataseq, self.alg, self.time,
                                                           self.mean_score)

    def __repr__(self):
        return self.__str__()


def process_one_csv(csv_path, size, dataseq, alg) -> BenchmarkResult:
    df = pd.read_csv(csv_path)
    # print(df.head())
    # print(df[df["timestamp"] > 100000])
    df.drop(df[df["timestamp"] < 100000].index, inplace=True)
    df.loc[df["timestamp"] > 100000, "timestamp"] -= df["timestamp"][0]
    maxtim = df["timestamp"].max()
    print("Maxtim in ms:", maxtim)
    df["score"] = 0
    df.loc[df["method"] == "X", "score"] = 0
    df.loc[df["method"] == "CSR", "score"] = 5  # TODO: consider modality
    df.loc[df["method"] == "SSR", "score"] = 3
    total_score = integrate.trapezoid(df.score, x=df.timestamp)
    print("total score:", total_score, "mean score:", total_score / maxtim)
    # df = df.cumsum()
    plt.figure()
    df.plot(x="timestamp", y="score")
    plt.show()
    # print(df)
    return BenchmarkResult(size, dataseq, alg, maxtim, total_score / maxtim)


def main(datadir):
    dir_list = os.scandir(datadir)
    bench_results = pd.DataFrame(columns=["network", "dataseq", "alg", "time", "mean_score"])
    for item in dir_list:
        name = os.path.splitext(item.name)[0]
        network, dataseq, alg = name.split("-")
        print(network, dataseq, alg)
        bench_result = process_one_csv(item.path, network, dataseq, alg)
        bench_results = bench_results.append(
            {
                "network": bench_result.network, "dataseq": bench_result.dataseq, "alg": bench_result.alg,
                "time": bench_result.time, "mean_score": bench_result.mean_score
            },
            ignore_index=True
        )
        # bench_results[(network, dataseq, alg)] = bench_result
    bench_results["label"] = bench_results["network"] + "-" + bench_results["dataseq"]
    bench_results["alg"] = pd.Categorical(bench_results["alg"], categories=["before", "after"])
    # bench_results.sort_values(by=["alg"], inplace=True, ascending=[False])
    print(bench_results)
    bench_results.pivot("label", "alg", "mean_score").plot(kind="bar")
    # bench_results.groupby("label").plot(x="label", y=["mean_score"], kind="bar")
    plt.show()

    # labels = bench_results.keys()
    # labels = sorted(labels, key=lambda x: x[0] + x[1])
    # scores = bench_results[labels].mean_score


if __name__ == "__main__":
    main("./medium-ct-csv")
