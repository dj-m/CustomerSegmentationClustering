from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description=' implement the K-Means clustering algorithm, find the value for K using the Elbow method, the Silhouette method, and the Gap statistic, and visualize the clusters with Principal Components Analysis (PCA).',
    author='Domingo Moronta',
    license='MIT',
)
