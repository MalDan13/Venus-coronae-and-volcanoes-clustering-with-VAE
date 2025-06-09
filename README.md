# Venus coronae and volcanic clusters with VAEs
## Annotation
More than thirty years have passed since the Magellan mission. However, the classification of volcanic features on Venus is still unresolved. In this study, we use machine learning techniques to classify new types of coronas and large and intermediate-sized volcanoes on the planet. Unlike previous approaches that relied on manual analysis of satellite images, radar data, and topographic profiles to determine the size of volcanoes, we employ a variational autoencoder to extract features directly from satellite imagery. We then use clustering algorithms such as K-means, DBSCAN and hierarchical clustering to identify different types of geological features. The results from this study could contribute to automated analysis of the Venusian surface, expansion of our understanding of volcanic activity, and preparation for future exploration missions.

## Contents:
This project consists of four folders: "data", "model_train", "model_test", and "latent_dim_clustering".
* The "data" directory contains CSV files with information about volcanic structures: unique IDs, names, coordinates, and diameters. It also includes examples of SAR images and topographical maps of the structures studied.
* "model_train" contains notebooks for training autoencoders to recognize volcanic structures on Venus using satellite imagery and topography.
* In the "model_test" folder, there are notebooks for testing the trained models.
* Finally, the "latent_dim_clustering" folder includes two notebooks. The first notebook extracts features from the latent space of autoencoders, combines them with additional data, and creates a new dataset called "latent dim concat.ipynb". The second notebook uses PCA to reduce the number of dimensions in the latent features, then performs clustering using K-means and other algorithms such as hierarchical clustering and Gaussian mixture models.
## Pipeline
1) We cut 
