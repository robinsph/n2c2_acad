import re
import os
import requests
import json
from dc import HEART_MEDICATIONS


CACHE_FNAME = "meds.json"
try:
    openx = open('meds.json')
    readx = openx.read()
    CACHE_DICTION = json.loads(readx)
    openx.close()
except:
    CACHE_DICTION = {}

def params_unique_combination(baseurl, params_d, private_keys=["api_key"]):
     alphabetized_keys = sorted(params_d.keys())
     res = []
     for k in alphabetized_keys:
         if k not in private_keys:
             res.append("{}-{}".format(k, params_d[k]))
     return baseurl + "_".join(res) 

def get_drug_data(drug):
	base_url = 'https://rxnav.nlm.nih.gov/REST/rxclass/class/byDrugName.json?'
	params_d = {}
	params_d['drugName'] = drug
	unique_identifier = params_unique_combination(base_url, params_d)
	if unique_identifier in CACHE_DICTION:
	    return CACHE_DICTION[unique_identifier]
	else:
	    resp = requests.get(base_url, params = params_d)
	    resp_text = resp.text
	    CACHE_DICTION[unique_identifier] = json.loads(resp.text)
	    dumped_json_cache = json.dumps(CACHE_DICTION)
	    outfile = open (CACHE_FNAME, 'w')
	    outfile.write(dumped_json_cache)
	    outfile.close()
	    return CACHE_DICTION[unique_identifier]

drug_class_list = [drug.lower() for drug in HEART_MEDICATIONS]
#files = [file for file in os.listdir() if file[-3:] == 'txt']
files = ['397.txt']
drug_csv = open('drug_csv.csv','w')
drug_csv.write('{},{}\n'.format('file','two_or_more_cardiac_drugs'))
for file in files:
	open_file = open(file,'r')
	read_file = open_file.read()
	drugs = read_file.split()
	file_drugs = {}
	for drug in drugs:
		try:
			res_obj = get_drug_data(drug)

			total_bool_list = []
			for drug_instance in res_obj['rxclassDrugInfoList']['rxclassDrugInfo']:
				drug_class = drug_instance['rxclassMinConceptItem']['className'].lower()


				if len(drugs) == 1:
					print(drug_class)

				check = [drug_class.find(drug_check) for drug_check in drug_class_list]

				check_vales = [True if i >= 0 else False for i in check]

				drug_val = False
				if True in check_vales:
					drug_val = True

					if len(drugs) == 1:
						print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
				total_bool_list.append(drug_val)

			#print(drug,(total_bool_list.count(True))/(len(total_bool_list)))
			file_drugs[drug] = (total_bool_list.count(True))/(len(total_bool_list))

		except:
			continue 
	sorted_drugs = sorted(file_drugs, key = lambda drug_probability: file_drugs[drug_probability], reverse = True)
	#file_cardiac_drugs = [drug if file_drugs[drug] >=.2 else  for drug in sorted_drugs]
	file_cardiac_drugs = [drug for drug in sorted_drugs if file_drugs[drug] >=.2]
	print(file[:-4], file_cardiac_drugs)
	state = len(file_cardiac_drugs) >= 2
	state_num = 0
	if state == True:
		state_num = 1
	drug_csv.write('{},{}\n'.format(file[:-4], state_num))
drug_csv.close()
