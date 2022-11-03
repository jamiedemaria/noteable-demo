from dagster import asset, file_relative_path, AssetIn, Field, Int
import pandas as pd
from papermill_origami.noteable_dagstermill import define_noteable_dagster_asset
from dagstermill import define_dagstermill_asset

# TODO create an asset from a Jupyter notebook
