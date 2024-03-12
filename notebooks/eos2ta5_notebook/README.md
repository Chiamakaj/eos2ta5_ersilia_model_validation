# Model Evaluation Summary for eos2ta5 (cardiotoxnet-herg)
# (Ligand-based prediction of hERG blockade)


## Model Description

- The model predicts hERG channel blockade based on an ensemble of five deep learning models.
- The model classifies small drug-like molecules as hERG blockers and hERG non blockers.
- The model generates probability score.
- Probability greater than or equal to 0.5 declares the molecule to be hERG blocker. 


## Environment setup

Ubuntu 20.04 with Python 3.7

1. Install miniconda3

2. Install GitHub CLI

3. Install and activate Git LFS from Conda using:

	conda install git-lfs -c conda-forge
	git-lfs install
 
4. Install Ersilia using:

	conda create -n ersilia python=3.7
	conda activate ersilia
	python -m pip install isaura==0.1
	git clone https://github.com/ersilia-os/ersilia.git
	cd ersilia
	pip install -e .

5. Test the selected model to be sure it works.

	ersilia -v fetch model_name
	ersilia serve model_name
	ersilia -v api run -i "CCCC"


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

The distribution of the probability shows that a large number of the molecules are below 0.5. According to the model's publication, this means that a larger number of molecules in the dataset selected are hERG non blockers while the rest that are 0.5 and above are hERG blockers. 


## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a None license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.
_______

**Author:** Chiamaka Ohaji
