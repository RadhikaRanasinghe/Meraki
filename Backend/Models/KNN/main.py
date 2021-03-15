import methods


# Loading Data
# path = "/content/drive/MyDrive/Colab Notebooks/detect_pd"
path = ""

x, y = methods.preprocessing_columns(path)

# methods.initialise_save(path, x, y)

methods.building_models(path, x, y)

methods.print_results(path)
