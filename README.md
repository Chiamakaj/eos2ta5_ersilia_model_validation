# eos2ta5_ersilia_model_validation
This is a model validation repository for eos2ta5 model (Outreachy contributors 2024).

## Repository organisation
The repository is organised in folders:
- '/notebooks' contains the jupyter notebooks where most of the work is being developed
- '/data' contains all the .csv files. Model predictions are obtained outside this repository and saved in this folder. Subfolders might be created if needed
- '/src' contains important functions I will re-use throughout the repository, to avoid typing them each time
- '/figures' contains the plots I have produced during the model validation process
- 'requirements.txt' lists all the required packages to run the notebooks in this repository. If possible I also specify the version of the package I am using.

## How to use this repository
This repository is just a guideline, it does not contain any real example, hence some folders might not be existing yet. There are mostly placeholders to inspire you.

Use the notebooks as they have been defined, there is a code block with instructions of what step should be done there. Remember to install and import all the necessayr packages. Do not use installs from the Notebook directly, create a conda environment and install the packages in that environment. 

## License
All the code in this repository is licensed under a GPLv3 License.
