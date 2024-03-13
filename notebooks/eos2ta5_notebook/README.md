# Model Evaluation Summary for eos2ta5 (cardiotoxnet-herg)
# Ligand-based prediction of hERG blockade


## Model Description

- The model predicts hERG channel blockade based on an ensemble of five deep learning models.
- The model classifies small drug-like molecules as hERG blockers and hERG non blockers.
- The model generates probability score.
- Probability greater than or equal to 0.5 declares the molecule to be hERG blocker. 


## Model Summary

hERG stands for human ether-à-go-go-related gene. This gene plays a role in regulating the heart's electrical activity. There are drugs that could interfere with the activity of the hERG gene and Pharmaceuticals try to identify compunds that could interfere even before the drug is produced. This is where the cardiotoxnet-herg model comes in. It uses computational method to predict the probability of a compound to cause hERG bolckage or not.

## Environment setup

Ubuntu 20.04 with Python 3.7

1. Install miniconda3

2. Install GitHub CLI

3. Install and activate Git LFS from Conda using:

	- conda install git-lfs -c conda-forge
	- git-lfs install
 
4. Install Ersilia using:

	- conda create -n ersilia python=3.7
	- conda activate ersilia
	- python -m pip install isaura==0.1
	- git clone https://github.com/ersilia-os/ersilia.git
	- cd ersilia
	- pip install -e .

5. Test the selected model to be sure it works.

	- ersilia -v fetch eos2ta5
	- ersilia serve eos2ta5
	- ersilia -v api run -i "CCCC"


## Steps

- Select dataset of 1000 molecules from ChEMBL database and extract the SMILES.
- Load this dataset into the model bias python notebook.
- Convert the SMILES to standard SMILES using the function in src folder.
- Use the RDKIT package to get the Inchikey representation of the molecules.
- Export the file containing Inchikey and SMILES and save in a CSV file.
- Select a model and run predictions via google colab on (https://github.com/ersilia-os/ersilia/blob/master/notebooks/ersilia-on-colab.ipynb).
- Create a scatter plot of the predictions (probability) gotten from the step above to show the model bias. 


## Findings

Model bias evaluation:
- The histogram distribution of the probability shows that a large number of the molecules are below 0.5 when we look at the frequency at which each probabilty occured. According to the model's publication, this means that a larger number of molecules in the dataset selected are hERG non blockers while the rest that are 0.5 and above could be hERG blockers.
- From the 1000 SMILEs used in this evaluation, 752 molecules were classified as hERG non-blocker and 248 hERG blockers.

Model Reproducibility:



External Validation:



## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a None license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.
_______

**Author:** Chiamaka Ohaji
