import pandas as pd


def create_results_file():
    df = pd.read_csv("data/raw-monash-mase.csv")
    metric = df.set_index("Dataset")
    metric_long = pd.melt(metric, value_vars=metric.columns, ignore_index=False).rename(
        columns={"variable": "model", "value": "MASE"}
    )
    rankings = df.fillna(99).set_index("Dataset").rank(axis=1)
    rankings_long = pd.melt(
        rankings, value_vars=rankings.columns, ignore_index=False
    ).rename(columns={"variable": "model", "value": "position"})
    rankings_long["position"] = rankings_long["position"].astype(int)
    scores = pd.read_csv("data/scores.csv")
    results = rankings_long.reset_index().merge(scores, on="position")
    results = results.merge(metric_long.reset_index(), on=["Dataset", "model"])
    results.to_csv("data/results.csv", index=False)

    # leaderboard
    models_df = pd.read_csv("data/models.csv").set_index("Model")
    leaderboard_ranks = results.groupby("model")["points"].sum().rank(ascending=False)
    leaderboard_points = results.groupby("model")["points"].sum()
    leaderboard_df = pd.DataFrame(
        {"Position": leaderboard_ranks, "Points": leaderboard_points}
    )
    leaderboard_df = leaderboard_df.join(models_df)
    leaderboard_df.index.name = "Model"
    leaderboard_df.to_csv("data/leaderboard.csv")

    # dataset
    dataset_df = pd.read_csv("data/datasets.csv").set_index("Dataset")
    dataset_ranks = results[results["position"] == 1].set_index("Dataset")
    dataset_ranks = dataset_ranks.merge(models_df, left_on="model", right_index=True)
    dataset_df = dataset_df.join(dataset_ranks[["model", "Type", "MASE"]])
    dataset_df.rename(columns={"model": "Leader"}, inplace=True)
    dataset_df.to_csv("data/datasets_leader.csv")


if __name__ == "__main__":
    create_results_file()
