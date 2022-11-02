from dagster import asset, file_relative_path, AssetIn, AssetKey
import pandas as pd
from papermill_origami import define_noteable_dagster_asset


@asset 
def iris_dataset():
    return pd.read_csv(
        "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", 
        names=['Sepal length (cm)', 'Sepal width (cm)', 'Petal length (cm)', 'Petal width (cm)', 'Species']
    )


notebook_id = "bf560603-5b83-4553-9b85-19625c5501c6"
iris_kmeans_notebook = define_noteable_dagster_asset(
    name="iris_kmeans",
    notebook_id=notebook_id,
    ins={"iris": AssetIn(AssetKey("iris_dataset"))}
)