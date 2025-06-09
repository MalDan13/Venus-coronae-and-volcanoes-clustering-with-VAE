# Venus coronae and volcanoes clustering with VAE
## Annotation:
More than 30 years have passed since the Magellan mission, yet the classification of large and medium-sized volcanic edifices on Venus remains unresolved. This study employs machine learning techniques to identify new classes of coronae, as well as large and medium-sized volcanoes. Unlike existing approaches based on manual analysis of radar images, topographic profiles, and diameters, we propose using a variational autoencoder (VAE) to extract features from satellite images for subsequent clustering. The methodology includes the collection and preprocessing of radar image data from the Magellan mission, training a VAE, and applying clustering algorithms (KMeans, DBSCAN, hierarchical clustering) to identify subclasses of geological structures. The results of this study can contribute to the automation of Venusian surface analysis, the expansion of volcanic edifice classification, and preparations for future missions.
## Contents
This project has 4 folders: data, model_train, model_test and latent_dim_clustering.
* The data folder contains some examples of synthetic-aperture radar (SAR) images and topographic maps of the studied structures: two coronaes, large volcanoes and intermidiate volcanoes.
* 
