import os

import matplotlib.pyplot as plt
import pandas as pd
from scipy import integrate

durations = {  # situation ->
    'normal': 60,
    'fastscroll': 10
}


class BenchmarkResult:
    def __init__(self, modality, network, situation, algorithm, cum_scores, full_load_time):
        self.modality = modality
        self.network = network
        self.situation = situation
        self.alg = algorithm
        self.time = durations[situation]
        self.cum_scores = cum_scores
        self.full_load_time = full_load_time

    def __str__(self):
        return "{}-{}-{}-{}, time: {}, mean_score: {}, full_load_time: {}".format(
            self.modality,
            self.network,
            self.situation,
            self.alg,
            self.time,
            self.cum_scores.iloc[-1],
            self.full_load_time
        )

    def __repr__(self):
        return self.__str__()


def process_one_csv(csv_path, modality, network, situation, algorithm) -> BenchmarkResult:
    df = pd.read_csv(csv_path)
    firstRenderIndex = df.index[df["method"] == "firstRender"][0]
    # print("FirstRender index:", firstRenderIndex)
    df.drop(df[:firstRenderIndex].index, inplace=True)
    df.reset_index(drop=True, inplace=True)
    # print("after drop:", df.to_string())
    df["score"] = 0
    df.loc[df["method"] == "X", "score"] = -5
    df.loc[df["method"] == "CSR", "score"] = 0
    df.loc[df["method"] == "SSR", "score"] = -2

    mintime = df["timestamp"].iloc[0]
    df["elapsedTime"] = (df["timestamp"] - mintime) / 1000
    # df.loc[fullLoadIndex:, "score"] = 0
    df["cumint"] = 100 + integrate.cumulative_trapezoid(df.score, x=df.elapsedTime, initial=0)
    df["cumsum"] = df["score"].cumsum()
    try:
        fullLoadIndex = df.index[df["method"] == "fullLoad"][0]
    except:
        fullLoadIndex = None
    # print("fullLoad index:", fullLoadIndex)
    if fullLoadIndex is not None:
        # print("Length: ", len(df["elapsedTime"]))
        fullLoadTime = df["elapsedTime"].iloc[fullLoadIndex]
    else:
        fullLoadTime = durations[situation] + 10  # default value
    # difft = df["timestamp"][fullLoadIndex] - df["timestamp"].iloc[0]
    # firstRender와 Full load 의 시간 차이 구함. in milliseconds
    # print(f"Total time: {difft}ms")
    # df["cumscore"] = 100 + df["cumsum"] / difft * 1000
    # plt.figure()
    # df.plot(x="elapsedTime", y="cumint", title=f"{network}-{modality}-{situation}-{algorithm}", ylim=(0, 100),
    #         legend=True)
    # plt.show()
    return BenchmarkResult(modality, network, situation, algorithm, df[["elapsedTime", "cumint"]], fullLoadTime)
    # print(df.to_string())
    # return BenchmarkResult(size, dataseq, alg, maxtim, total_score / maxtim)


def main(datadir, compare_score=False):
    dir_list = os.scandir(datadir)
    # bench_results = pd.DataFrame(columns=["network", "dataseq", "alg", "time", "mean_score"])
    bench_results = {}
    for item in dir_list:
        name = os.path.splitext(item.name)[0]
        modality, network, situation, alg = name.split("-")
        # print(modality, network, situation, alg)
        bench_result = process_one_csv(item.path, modality, network, situation, alg)
        if (modality, network, situation) not in bench_results:
            bench_results[(modality, network, situation)] = {}
        bench_results[(modality, network, situation)][alg] = bench_result
        # bench_results = bench_results.append(
        #     {
        #         "modality": bench_result.modality,
        #         "network": bench_result.network,
        #         "situation": bench_result.situation,
        #         "algorithm": bench_result.alg,
        #         "time": bench_result.time,
        #         "cum_scores": bench_result.cum_scores
        #     },
        #     ignore_index=True
        # )
        # bench_results[(network, dataseq, alg)] = bench_result
    # 점수 비교
    if compare_score:
        for condition, bench_result in bench_results.items():
            print(condition, bench_result)
            # 그림 그리기
            orignal_df = bench_result["original"].cum_scores
            improved_df = bench_result["improved"].cum_scores
            # ax = orignal_df.plot(x="elapsedTime", y="cumint", label="original", color="red")
            # improved_df.plot(ax=ax, x="elapsedTime", y="cumint", label="improved", color="blue")
            fig = plt.figure()
            plot1, = plt.plot(orignal_df["elapsedTime"], orignal_df["cumint"], label="original", color="red")
            plot2, = plt.plot(improved_df["elapsedTime"], improved_df["cumint"], label="our", color="blue")
            plt.ylim(0, 100)
            plt.xlim(0, durations[condition[2]])  # situation
            plt.legend([plot1, plot2], ["original", "ours"])
            plt.title("{}-{}-{}".format(condition[0], condition[1], condition[2]))
            original_full_load_time = bench_result["original"].full_load_time
            improved_full_load_time = bench_result["improved"].full_load_time
            original_final_score = bench_result["original"].cum_scores.iloc[-1][1]
            improved_final_score = bench_result["improved"].cum_scores.iloc[-1][1]

            original_indicator = f'original algorithm full load ({original_full_load_time:.2f}s, {original_final_score:.2f}pt)'
            improved_indicator = f'our algorithm full load ({improved_full_load_time:.2f}s, {improved_final_score:.2f}pt)'
            # print(original_indicator, improved_indicator)
            plt.annotate(original_indicator,
                         xy=(original_full_load_time, original_final_score),
                         xytext=(original_full_load_time, original_final_score - 30),
                         arrowprops=dict(facecolor='red', shrink=0.05))
            plt.annotate(improved_indicator,
                         xy=(improved_full_load_time, improved_final_score),
                         xytext=(improved_full_load_time, improved_final_score - 15),
                         arrowprops=dict(facecolor='blue', shrink=0.05))
            plt.xlabel("time (s)")
            plt.ylabel("score")
            plt.tight_layout()
            # plt.show()
            plt.savefig(f"../result-figs/{condition[0]}-{condition[1]}-{condition[2]}.png")
            # fig.close()

    network_speeds = {}
    for condition, bench_result in bench_results.items():
        modality, network, situation = condition
        if (modality, situation) not in network_speeds:
            network_speeds[(modality, situation)] = {}
        network_speeds[(modality, situation)][network] = (
            bench_result["original"].full_load_time, bench_result["improved"].full_load_time
        )

    for condition, network_speeds in network_speeds.items():
        modality, situation = condition
        # print(modality, situation)
        network_analysis_result = pd.DataFrame(columns=["network", "alg", "full_load_time"])
        for network_speed, result in network_speeds.items():
            network_analysis_result = network_analysis_result.append(
                {
                    "network": int(network_speed),
                    "alg": "original",
                    "full_load_time": result[0]
                },
                ignore_index=True
            )
            network_analysis_result = network_analysis_result.append(
                {
                    "network": int(network_speed),
                    "alg": "improved",
                    "full_load_time": result[1]
                },
                ignore_index=True
            )
        # print(network_analysis_result.to_string())
        mapping = {speed: i for i, speed in enumerate(sorted(map(int, network_speeds.keys())))}
        # print(mapping)
        network_analysis_result["alg"] = pd.Categorical(network_analysis_result["alg"],
                                                        categories=["original", "improved"])
        network_analysis_result.pivot("network", "alg", "full_load_time").plot(kind="bar")
        plt.title("{}-{}".format(modality, situation))
        plt.xlabel("network speed (Mbps)")
        plt.ylabel("full load time (s)")
        plt.tight_layout()
        plt.savefig(f"../load_time_figs/{modality}-{situation}.png")
        # plt.show()
    return bench_results

    # bench_results["label"] = bench_results["network"] + "-" + bench_results["dataseq"]
    # bench_results["alg"] = pd.Categorical(bench_results["alg"], categories=["before", "after"])
    # # bench_results.sort_values(by=["alg"], inplace=True, ascending=[False])
    # print(bench_results)
    # bench_results.pivot("label", "alg", "mean_score").plot(kind="bar")
    # # bench_results.groupby("label").plot(x="label", y=["mean_score"], kind="bar")
    # plt.show()

    # labels = bench_results.keys()
    # labels = sorted(labels, key=lambda x: x[0] + x[1])
    # scores = bench_results[labels].mean_score


def tex_title(modality, situation):
    return r"& \multicolumn{2}{|c|}{" + modality + "-" + situation + r"}"


if __name__ == "__main__":
    bench_results = main("../csvs/", compare_score=True)
    print(bench_results)
    print("Tex===========")
    print(r"\begin{tabular}{ | c | c | c | c | c | c | c | c | c | c | c | c | c |}")
    print(r"\hline")
    modalities = ["ct", "mr", "us"]
    situations = ["fastscroll", "normal"]
    for modality in modalities:
        for situation in situations:
            print(tex_title(modality, situation), end='')
    print(r" \\ \hline")
    print("network speed(Mbps)", end='')
    for i in range(len(modalities) * len(situations)):
        print("& original & new ", end='')
    print(r"\\ \hline")
    for network_speed in [40, 80, 120, 160, 200]:
        print(network_speed, end='')
        print(r" & ", end='')
        for modality in modalities:
            for situation in situations:
                print(
                    f"""{bench_results[(modality, str(network_speed), situation)]["original"].cum_scores.iloc[-1][1]:.2f}""",
                    end='')
                print(r" & ", end='')
                print(
                    f"""{bench_results[(modality, str(network_speed), situation)]["improved"].cum_scores.iloc[-1][1]:.2f}""",
                    end='')
                print(r" & ", end='')
        print(r" \\ \hline")

    print(r"\end{tabular}")
