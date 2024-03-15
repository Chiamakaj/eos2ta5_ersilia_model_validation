# Model Evaluation Summary for eos2ta5 (cardiotoxnet-herg)
# Ligand-based prediction of hERG blockade

## Repository organisation
The repository is organised in folders:
- **notebooks** folder contains the jupyter notebooks where most of the work is being developed
- **data** folder contains all the .csv files. Model predictions are obtained outside this repository and saved in this folder.
- **figures** contains the plots I have produced during the model validation process
- 'requirements.txt' lists all the required packages to run the notebooks in this repository and the version of the package.


## Process
![image](https://github.com/Chiamakaj/Ersilia_model_validation/assets/88968378/cb45db4d-f19b-4eab-b3f1-a82f63c88241)


## Model Summary

hERG is the human ether-à-go-go gene that is responsible for encoding a voltage dependent ion that regulates the electrical activities of the heart. Some molecules found in drugs have been observed to inhibit the activities of this gene resulting in scientists and pharmaceuticals working out ways to factor out these molecules during drug production. The cardiotoxnet-herg model is one of the computational models that have been designed to detect these harmful molecules before drug production.

## Model Description

- The model predicts hERG channel blockade based on an ensemble of five deep learning models.
- The model classifies small drug-like molecules as hERG blockers and hERG non blockers.
- The model generates probability score.
- Probability greater than or equal to 0.5 declares the molecule to be hERG blocker.

## Ersilia environment setup

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
	- ersilia -v fetch model_name
	- ersilia serve model_name
	- ersilia -v api run -i "CCCC"

## Steps

- Select dataset of 1000 molecules from ChEMBL database and extract the SMILES.
- Load this dataset into the model bias python notebook.
- Convert the SMILES to standard SMILES using the function in src folder.
- Use the RDKIT package to get the Inchikey representation of the molecules.
- Export the file containing Inchikey and SMILES and save in a CSV file.
- Select a model and run predictions via google colab on (https://github.com/ersilia-os/ersilia/blob/master/notebooks/ersilia-on-colab.ipynb).
- Create a scatter plot of the predictions (probability) gotten from the step above to show the model bias.

# Findings

## Model bias evaluation

- The initial prediction was carried out using 1000 SMILEs. After prediction, 752 SMILEs where categorized as hERG non-blocker while 248 were categorized as hERG blocker as their probability fall above 0.5.
- The distribution of the probability shows that a large number of the molecules are below 0.5. According to the model's publication, this means that a larger number of molecules in the dataset selected are hERG non blockers while the rest that are 0.5 and above are hERG blockers.

	![image](https://github.com/Chiamakaj/Ersilia_model_validation/assets/88968378/8d7f44ba-b9b1-4e81-8869-6b95bff33ebc)

  
- The histogram also shows the frequency of the probability values which is seen to have a majority value between 0.1 and 0.2.

	![image](https://github.com/Chiamakaj/Ersilia_model_validation/assets/88968378/c3678c1b-2de2-4dec-8354-54cbd9229c69)

   


## Model Reproducibility

- The data set used to reproduce the figures from the publication of the model can be found [here](https://github.com/Abdulk084/CardioTox/tree/master/data). This repository contains 

	|  Dataset   | Total | hERG blockers | hERG non-blockers |
	|------------|-------|---------------|-------------------|
	|Train       | 12620 |     6643      |      5977         |
	|Test set I  |   44  |       30      |        14         |
	|Test set II |   41  |       11      |        30         |
	|Test set III|   740 |       30      |       710         |

- The original modle was used to carry out this task. This model implementation can be found [here](https://github.com/Abdulk084/CardioTox/blob/master/README.md)

- The implemetation was carried out on Ubuntu 20.04 and python 3.8. The initial implementation by the original authors was don on Ubuntu 20.04 and python 3.7.7

- These are the steps followed to setup the environment for cardiotox using Ubuntu 20.04 and python 3.8
	- download environment.yml file at [here](https://github.com/Abdulk084/CardioTox/blob/master/environment.yml)
	- conda env create -f environment.yml
	- conda activate cardiotox
	- git clone https://github.com/Abdulk084/CardioTox.git
	- cd Cardiotox 
	- cd PyBioMed
	- python setup.py install
	- cd ..
   	- Test the model with "python test.py"
   	  You should get an output like this

	![image](https://github.com/Chiamakaj/Ersilia_model_validation/assets/88968378/84ec6920-8e11-420e-9fe0-c45aa33e82ab)


	Issues faced while setting up the environment
	-  TypeError for protobuf 
		- Solution: Downgraded protobut by using "pip install protobuf==3.20.0"
	- Numpy version upgrade required
		- Solution: Upgraded numpy by using "pip install numpy==1.19.5"


**Reproducibility Summary**

- **All images/figures can be found in /figures folder**

- From the publication, Tanimoto similarity was done on the training set and all three test sets to show that the data sets were all different and had no hint of similarity. During this reproducibility evaluation, I used the authors' data set to reproduce the similarity plots as can be found in the **/figures** folder.

  ![image](https://github.com/Chiamakaj/Ersilia_model_validation/assets/88968378/1522f7e3-d43b-48a7-8823-3e48d3460ac4)


- The publication also contains a scatter plot showing the space diversity which was definded using t-SNE components for all the data set which was also successfully reproduced. This shows diverse space distribution of the SMILEs as well as some overlap in the dataset. Even though there is a similarity between the plots from the original authors and the evaluation done here, some outliers were noticed which was not mentioned in the publication.

  ![image](https://github.com/Chiamakaj/Ersilia_model_validation/assets/88968378/afc91291-303d-487d-8098-9fdbe38f4af4)


- Three tests sets were used by the authors to test the final model and some metrics like specificity, sensitivity, negative predictive value, positive predictive value, accuracy, Mathews correlation coefficient were used to evaluate the model's performance. This value was also reproduced in this work. The model performed well based on the sensitivity showing that it has a hogh chnage of predicting true positive values. It also performed well basen on the negative predictive value which tell that it has a high chance of predicting non-blokers correctly.

	| Evaluation data |   Method  |  MCC  |  NPV  |  ACC  |  PPV  |  SPE  |  SEN  | B-ACC |
	|-----------------|-----------|-------|-------|-------|-------|-------|-------|-------|
	|    Test set-I   | Cardiotox | 0.599 | 0.688 |  0.81 | 0.893 | 0.786 | 0.833 |  0.81 |
	|   Test set-II   | Cardiotox | 0.452 | 0.947 | 0.755 | 0.455 |  0.6  | 0.909 | 0.755 |
	|   Test set-III  | Cardiotox |  0.22 | 0.986 | 0.746 | 0.112 | 0.698 | 0.794 | 0.746 |


- Test set I was run using eos2ta5 model from Ersilia Model Hub and predictions were extracted. These predictions were used to analyse the model performance using the same metrics mentioned above that were used by the authors and Ersilia model produced the same results.

	| Evaluation data |  Method |  MCC  |  NPV  | ACC  |  PPV  |  SPE  |  SEN  | B-ACC |
	|-----------------|---------|-------|-------|------|-------|-------|-------|-------|
	|    Test set-I   | eos2ta5 | 0.599 | 0.688 | 0.81 | 0.893 | 0.786 | 0.833 |  0.81 |




## Model Performace using external validation

External dataset was used to check the model performance. The dataset was gotten from ChEMBL and it contains 499 molecules. To avoid bias, no molecues used during the training was included in this validation set. The SMILEs obtained were converted to standard form and Inchikey also processed.

External validation summary
- As done during the reproducibility process, specificity, sensitivity, negative predictive value, positive predictive value, accuracy, Mathews correlation coefficient were used to evaluate the model's performance as seen in the table below. Ersilia model had about the same SPE and NPV score as when performed on test set-I. The model could perform better as it has an accuracy performace of 66% . The specificity and NPV seems to have a better score. The model could be tested on more dataset to get a better evaluation of its performance.

	| Evaluation data  |  Method |  AUC  |  MCC  |  NPV  |  ACC  |  PPV  |  SPE  |  SEN  | B-ACC |
	|------------------|---------|-------|-------|-------|-------|-------|-------|-------|-------|
	| External dataset | eos2ta5 | 0.683 | 0.321 | 0.631 | 0.659 | 0.693 | 0.727 | 0.592 | 0.659 |

- AUC of the model is o.683 which is above 0.5 of a random classifier. From the ROC curve, it is oberserved that the model is able to discriminate between the positive and negative classes of the molecules. The model achieves higher TPR while keeping FPR low.

![image](https://github.com/Chiamakaj/Ersilia_model_validation/assets/88968378/49f2b76d-5f4b-4407-b6f0-801aa0f0c562)



## Reference
- [Github](https://github.com/Abdulk084/CardioTox)
- [Publication](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-021-00541-z)
- [Ersilia Model Page](https://github.com/ersilia-os/eos2ta5/tree/main)

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a None license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.
_______
