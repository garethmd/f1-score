import pandas as pd


def create_results_file():
    df = pd.read_csv("data/raw-monash-mase.csv")
    metric = df.set_index("Dataset")
    metric_long = pd.melt(metric, value_vars=metric.columns, ignore_index=False).rename(
        columns={"variable": "model", "value": "metric"}
    )
    rankings = df.set_index("Dataset").rank(axis=1)
    rankings_long = pd.melt(
        rankings, value_vars=rankings.columns, ignore_index=False
    ).rename(columns={"variable": "model", "value": "position"})
    rankings_long["position"] = rankings_long["position"].astype(int)
    scores = pd.read_csv("data/scores.csv")
    results = rankings_long.reset_index().merge(scores, on="position")
    results = results.merge(metric_long.reset_index(), on=["Dataset", "model"])
    results.to_csv("data/results.csv", index=False)


if __name__ == "__main__":
    create_results_file()
