#!/usr/bin/env bash

# Set the path where you want to download the dataset
download_path="package/classification/classification/dataset/"

# Download the Kaggle dataset to the specified path
kaggle competitions download -c playground-series-s3e24 -p "$download_path"

# Unzip the downloaded file
unzip -o "${download_path}playground-series-s3e24.zip" -d "$download_path"
