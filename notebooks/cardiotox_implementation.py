import cardiotox

import pandas as pd
import csv
#from cardiotox import DescModel, SVModel, FVModel,  FingerprintModel

#import numpy as np

model = cardiotox.load_ensemble()

test_set_pos = pd.read_csv("data/external_test_set_pos.csv")
test_set_neg = pd.read_csv("data/external_test_set_neg.csv")
test_set_new = pd.read_csv("data/external_test_set_new.csv")

pos_smiles = list(test_set_pos["smiles"])
y_test_ex_fp_pos = test_set_pos["ACTIVITY"]

neg_smiles = list(test_set_neg["smiles"])
y_test_ex_fp_neg = test_set_neg["ACTIVITY"]

new_smiles = list(test_set_new["smiles"])
y_test_ex_fp_new = test_set_new["ACTIVITY"]

###################### Stack ensemble for POSITIVELY BIASED TEST DATA ########################################

pred_test_external_stack_pos = model.predict(pos_smiles)

# Write the data to the CSV file
pred_test_external_stack_pos_pred_data = list(zip(test_set_pos["smiles"], pred_test_external_stack_pos))


csv_output1 = "pred_test_external_stack_pos_pred_file.csv"

with open(csv_output1, 'w', newline='') as file:
    writer = csv.writer(file)

    for row in pred_test_external_stack_pos_pred_data:
        writer.writerow(row)

print("First file outputted")


###################### Stack ensemble for NEGATIVELY BIASED TEST DATA ########################################

pred_test_external_stack_neg = model.predict(neg_smiles)

pred_test_external_stack_neg_pred_data = list(zip(test_set_neg["smiles"], pred_test_external_stack_neg))

csv_output2 = "pred_test_external_stack_neg_pred_file.csv"

with open(csv_output2, 'w', newline='') as file1:
    writer1 = csv.writer(file1)

    for row1 in pred_test_external_stack_neg_pred_data:
        writer1.writerow(row1)

print("Second file outputted")


###################### Stack ensemble for NEW BIASED TEST DATA ########################################

pred_test_external_stack_new = model.predict(new_smiles)

pred_test_external_stack_new_pred_data = list(zip(test_set_new["smiles"], pred_test_external_stack_new))

csv_output3 = "pred_test_external_stack_new_pred_file.csv"

with open(csv_output3, 'w', newline='') as file3:
    writer3 = csv.writer(file3)

    for row3 in pred_test_external_stack_new_pred_data:
        writer3.writerow(row3)

print("Third file outputted")
