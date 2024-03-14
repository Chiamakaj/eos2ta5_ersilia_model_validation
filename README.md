# Ersilia_model_validation
This repository contains modle validation for eos2t15 model gotten from Ersilia hub which tells the probability of a molecule being a  hERG blocker. **The summary for the model can be found in the readmefile contained in its notebook folder**. This contribution is part of the Outreachy 2024 internship selection process.

## Repository organisation
The repository is organised in folders:
- **notebooks** folder contains the jupyter notebooks where most of the work is being developed
- **data** folder contains all the .csv files. Model predictions are obtained outside this repository and saved in this folder.
- **figures** contains the plots I have produced during the model validation process
- 'requirements.txt' lists all the required packages to run the notebooks in this repository and the version of the package.

## How to use this repository
- The model used here was gotten from Ersilia Model Hub.
- The model has a readme file to help replicate the process.
- Load the model into the jupyter notebook
- Use the python file to standardize SMILEs and run the model
- The data folder contains the dataset used to test the model
- The findings from the model performance can be found in the figures folder

## Process
![image](https://github.com/Chiamakaj/Ersilia_model_validation/assets/88968378/cb45db4d-f19b-4eab-b3f1-a82f63c88241)


## License
All the code in this repository is licensed under a GPLv3 License.
