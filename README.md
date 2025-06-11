# Clustering of volcanoes and coronae on Venus based on neural network processing
## Annotation
More than thirty years have passed since the Magellan mission. However, the classification of volcanic features on Venus is still unresolved. In this study, we use machine learning techniques to classify new types of coronas and large and intermediate-sized volcanoes on the planet. Unlike previous approaches that relied on manual analysis of satellite images, radar data, and topographic profiles to determine the size of volcanoes, we employ a variational autoencoder to extract features directly from satellite imagery. We then use clustering algorithms such as K-means, DBSCAN and hierarchical clustering to identify different types of geological features. The results from this study could contribute to automated analysis of the Venusian surface, expansion of our understanding of volcanic activity, and preparation for future exploration missions.

## Contents:
This project consists of four folders: "data", "model_train", "model_test", and "latent_dim_clustering".
* The "data" directory contains CSV files with information about volcanic structures: unique IDs, names, coordinates, and diameters. That data was collected and revised from publushed lists (Stofan et al., 1992, 1997; Hahn and Byrne, 2023; Ivanov and Head, 2025). It also includes examples of SAR images and topographical maps of the structures studied. You can find and download Venus maps and surface images on the website of Lunar and planetary cartographic catalog (https://astrogeology.usgs.gov/search?target=&system=&p=1&accscope=&searchBar=).
* "model_train" contains notebooks for training autoencoders to recognize volcanic structures on Venus using satellite imagery and topography.
* In the "model_test" folder, there are notebooks for testing the trained models.
* Finally, the "latent_dim_clustering" folder includes two notebooks. The first notebook extracts features from the latent space of autoencoders and the second one performs clustering using K-means and other algorithms such as hierarchical clustering and Gaussian mixture models.
* The results of SAR images and topographic maps reconstructions are presented in "SAR_reconstructions_120epochs_LD512.png" and "topo_reconstructions_50epochs_LD16.png" files respectively.
## Pipeline
1) Before training, each image and topographic map is cut into 64 tiles of 512x512 pixel size with overlap using "Cut_tiles_folder.py".
2) These tiles are used for further two separate autoencoders for SAR images and topography maps training.
3) The results are then validated on the entire images after training.
4) Latent space features from the trained models are extracted and combined with other data (coordinates, diameters) to create a new dataset "latent_features_expended_with_types.csv".
5) "latent_features_expended_with_types.csv" dataset is also processed via PCA to reduce its dimension; and further utilized for volcanoes and coronae clustering.
## Acknowledgments:
The autoencoders used in this work were adopted from the VanillaVAE (https://github.com/AntixK/PyTorch-VAE). Thanks a lot to https://github.com/Nikita-Belyakov for immense help and support.
