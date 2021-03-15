import methods


# Loading Data
# path = "/content/drive/MyDrive/Colab Notebooks/detect_pd"
path = ""
# dataset_type = "_SMOTE"
# dataset_type = "_RandomOverSampler"
dataset_type = "_ADASYN"


x, y = methods.preprocessing_columns(path, dataset_type)

methods.initialise_save(path, x, y, dataset_type)

methods.building_models(path, x, y, dataset_type)

methods.print_results(path, dataset_type)
