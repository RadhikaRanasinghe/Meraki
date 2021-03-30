import methods


# Loading Data
# path = "/content/drive/MyDrive/Colab Notebooks/detect_pd"
path = ""
# dataset_type = "_SMOTE"
# dataset_type = "_RandomOverSampler"
dataset_type = "_ADASYN"

# preprocessing dataset
x, y = methods.preprocessing_columns(path, dataset_type)

# Save initial saves.
methods.initialise_save(path, x, y, dataset_type)

# Build the model
methods.building_models(path, x, y, dataset_type)

# Print the results.
methods.print_results(path, dataset_type)
