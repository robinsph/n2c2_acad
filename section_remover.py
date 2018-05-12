import re
import os
#This collects all of the xml files in the directory and not any files you have already filtered. 
files = [file for file in os.listdir() if (file[-3:] == 'xml' and file[0] != 'f')]

#Put in one file here if you need to examine the sections for one particular file. The code will give you the results for the sections and what was tagged for removal automatically 
#files = ['397.xml']


#flist =['ADMISSION MEDS', 'ALLERGIES', 'ALLERGIES/ADVERSE REACTIONS', 'Admission Meds', 'Admission meds', 'Allergies', 'Allergies/adverse Reactions', 'Allergies/adverse reactions', 'CCU COURSE + PLAN', 'CCU course + plan', 'CT-A HEAD/NECK', 'CT-A head/neck', 'CV', 'Ccu Course + Plan', 'Ccu course + plan', 'Ct-a Head/neck', 'Ct-a head/neck', 'Cv', 'DISPOSITION', 'Disposition', 'EKG', 'Ekg', 'FAMILY', 'FAMILY HISTORY', 'FAMILY HX', 'FATHER', 'FH', 'FINAL DIAGNOSIS', 'FOLLOW-UP', 'Family', 'Family History', 'Family Hx', 'Family history', 'Family hx', 'Father', 'Fh', 'Final Diagnosis', 'Final diagnosis', 'Follow-up', 'HEENT EXAMINATION', 'HISTORY OF PRESENT ILLNESS', 'HPI', 'Heent Examination', 'Heent examination', 'History Of Present Illness', 'History of Present Illness', 'History of present illness', 'Hpi', 'IMPRESSION', 'IMPRESSION BY PROBLEM', 'INPATIENT MEDS', 'Impression', 'Impression By Problem', 'Impression by problem', 'Inpatient Meds', 'Inpatient meds', 'LABS', 'LABS + PE', 'LABS/STUDIES', 'Labs', 'Labs + Pe', 'Labs + pe', 'Labs/studies', 'MEDICATIONS', 'MEDICATIONS ON ADMISSION', 'MEDS', 'MEDS ON TRANSFER', 'MICROBIOLOGY', 'MOTHER', 'MRI BRAIN', 'MRI L/S SPINE', 'MRI L/S spine', 'MRI brain', 'Medications', 'Medications On Admission', 'Medications on admission', 'Meds', 'Meds On Transfer', 'Meds on Transfer', 'Meds on transfer', 'Microbiology', 'Mother', 'Mri Brain', 'Mri L/s Spine', 'Mri brain', 'Mri l/s spine', 'PAST MEDICAL HISTORY', 'PE', 'PHYSICAL EXAM', 'PHYSICAL EXAMINATION', 'PLAN', 'PMH', 'PROBLEMS', 'PSH', 'Past Medical History', 'Past medical history', 'Pe', 'Physical Exam', 'Physical Examination', 'Physical exam', 'Physical examination', 'Plan', 'Pmh', 'Problems', 'Psh', 'REASON FOR CONSULT', 'REASON FOR VISIT', 'RECS', 'REVIEW OF SYSTEMS', 'Reason For Consult', 'Reason For Visit', 'Reason for Consult', 'Reason for consult', 'Reason for visit', 'Recs', 'Review Of Systems', 'Review of Systems', 'Review of systems', 'SIBLINGS', 'SOCIAL HISTORY', 'SOCIAL HISTORY AND FAMILY HISTORY', 'STUDIES', 'Siblings', 'Social History', 'Social History And Family History', 'Social history', 'Social history and family history', 'Studies', 'TESTS', 'THERAPY RENDERED/COURSE IN ED', 'Tests', 'Therapy Rendered/course In Ed', 'Therapy rendered/course in ed', '\\*+', 'admission meds', 'allergies', 'allergies/adverse reactions', 'ccu course + plan', 'ct-a head/neck', 'cv', 'disposition', 'ekg', 'family', 'family history', 'family hx', 'father', 'fh', 'final diagnosis', 'follow-up', 'heent examination', 'history of present illness', 'hpi', 'impression', 'impression by problem', 'inpatient meds', 'labs', 'labs + pe', 'labs/studies', 'medications', 'medications on admission', 'meds', 'meds on transfer', 'microbiology', 'mother', 'mri brain', 'mri l/s spine', 'past medical history', 'pe', 'physical exam', 'physical examination', 'plan', 'pmh', 'problems', 'psh', 'reason for consult', 'reason for visit', 'recs', 'review of systems', 'siblings', 'social history', 'social history and family history', 'studies', 'tests', 'therapy rendered/course in ed']



#This code creates 4 different variations of sections for a section. For example, if we have the section 'social history and family history', it will create:
#'SOCIAL HISTORY AND FAMILY HISTORY', 'Social History And Family History', 'Social history and family history', 'social history and family history']
#If you need to add a new section to the section list, uncomment lines 11-36, comment out the rest of the code, and then copy/paste the returned list back into the list on line 10

# new_list = []
# for sec in flist:
# 	if sec.upper() not in new_list:
# 		new_list.append(sec.upper())
# 	if sec.lower() not in new_list:
# 		new_list.append(sec.lower())
# 	if sec[0].upper() + sec[1:].lower() not in new_list:
# 		new_list.append(sec[0].upper() + sec[1:].lower())
# 	if sec not in new_list:
# 		new_list.append(sec)
# 	z = sec.split()
# 	if len(z) > 1:
# 		y = ''
# 		for thing in z:
# 			y += thing[0].upper() + thing[1:].lower() + ' '
# 		if y.strip() not in new_list:
# 			new_list.append(y.strip())
# print(sorted(new_list))


# # \\*+ is a regular expression for the ************************************ between documents
flist =['ADMISSION MEDS', 'ALLERGIES', 'ALLERGIES/ADVERSE REACTIONS', 'Admission Meds', 'Admission meds', 'Allergies', 'Allergies/adverse Reactions', 'Allergies/adverse reactions', 'CCU COURSE + PLAN', 'CCU course + plan', 'CT-A HEAD/NECK', 'CT-A head/neck', 'CV', 'Ccu Course + Plan', 'Ccu course + plan', 'Ct-a Head/neck', 'Ct-a head/neck', 'Cv', 'DISPOSITION', 'Disposition', 'EKG', 'Ekg', 'FAMILY', 'FAMILY HISTORY', 'FAMILY HX', 'FATHER', 'FH', 'FINAL DIAGNOSIS', 'FOLLOW-UP', 'Family', 'Family History', 'Family Hx', 'Family history', 'Family hx', 'Father', 'Fh', 'Final Diagnosis', 'Final diagnosis', 'Follow-up', 'HEENT EXAMINATION', 'HISTORY OF PRESENT ILLNESS', 'HPI', 'Heent Examination', 'Heent examination', 'History Of Present Illness', 'History of Present Illness', 'History of present illness', 'Hpi', 'IMPRESSION', 'IMPRESSION BY PROBLEM', 'INPATIENT MEDS', 'Impression', 'Impression By Problem', 'Impression by problem', 'Inpatient Meds', 'Inpatient meds', 'LABS', 'LABS + PE', 'LABS/STUDIES', 'Labs', 'Labs + Pe', 'Labs + pe', 'Labs/studies', 'MEDICATIONS', 'MEDICATIONS ON ADMISSION', 'MEDS', 'MEDS ON TRANSFER', 'MICROBIOLOGY', 'MOTHER', 'MRI BRAIN', 'MRI L/S SPINE', 'MRI L/S spine', 'MRI brain', 'Medications', 'Medications On Admission', 'Medications on admission', 'Meds', 'Meds On Transfer', 'Meds on Transfer', 'Meds on transfer', 'Microbiology', 'Mother', 'Mri Brain', 'Mri L/s Spine', 'Mri brain', 'Mri l/s spine', 'PAST MEDICAL HISTORY', 'PE', 'PHYSICAL EXAM', 'PHYSICAL EXAMINATION', 'PLAN', 'PMH', 'PSH', 'Past Medical History', 'Past medical history', 'Pe', 'Physical Exam', 'Physical Examination', 'Physical exam', 'Physical examination', 'Plan', 'Pmh', 'Psh', 'REASON FOR CONSULT', 'REASON FOR VISIT', 'RECS', 'REVIEW OF SYSTEMS', 'Reason For Consult', 'Reason For Visit', 'Reason for Consult', 'Reason for consult', 'Reason for visit', 'Recs', 'Review Of Systems', 'Review of Systems', 'Review of systems', 'SIBLINGS', 'SOCIAL HISTORY', 'SOCIAL HISTORY AND FAMILY HISTORY', 'STUDIES', 'Siblings', 'Social History', 'Social History And Family History', 'Social history', 'Social history and family history', 'Studies', 'TESTS', 'THERAPY RENDERED/COURSE IN ED', 'Tests', 'Therapy Rendered/course In Ed', 'Therapy rendered/course in ed', '\\*+', 'admission meds', 'allergies', 'allergies/adverse reactions', 'ccu course + plan', 'ct-a head/neck', 'cv', 'disposition', 'ekg', 'family', 'family history', 'family hx', 'father', 'fh', 'final diagnosis', 'follow-up', 'heent examination', 'history of present illness', 'hpi', 'impression', 'impression by problem', 'inpatient meds', 'labs', 'labs + pe', 'labs/studies', 'medications', 'medications on admission', 'meds', 'meds on transfer', 'microbiology', 'mother', 'mri brain', 'mri l/s spine', 'past medical history', 'pe', 'physical exam', 'physical examination', 'plan', 'pmh', 'psh', 'reason for consult', 'reason for visit', 'recs', 'review of systems', 'siblings', 'social history', 'social history and family history', 'studies', 'tests', 'therapy rendered/course in ed', 'Problems']







#Self explanitory: a type of section that we are trying to remove
what_to_remove = ['family history', 'mother', 'father', 'siblings','family hx','fh'] #make these sections lowercase


for file in files:
	f = open(file, 'r')
	content = f.read()

	#This creates a dictionary of key-value pairs, based on a regular expression of strings from the flist. The key in the key_value pair is the index position in which the string starts, where the value in the key_value pair is the string from the list
	sections = {}
	for tag in flist:
		for m in re.finditer(re.compile(tag +'[ ]?[\t\n:]'),content):
			#print(tag, m.start())
			sections[m.start()] = tag

	#Create a list of the keys in the section dictionary. This puts the indexed positions in positional order (and the section headings, by association)
	sorted_sections = sorted(sections, key = lambda spot: spot)

	if len(files) == 1:
		for section in sorted_sections:
			print(sections[section])


	#I wrote this to remove family history, which is why most of these reference family. We iterate trhough the sorted list of indexed positions. We also ask about what we section we are looking for (as defined by the what_to_remove variable on line 6). For example, it currently is set to 'family', so it will look for the section headings that have 'family' in it. We normalize the section headings here, so don't worry about case sensitivity. We also then ask about the FOLLOWING indexed position following the section we are looking for. We then append these to a list. For this, we are appending sets of indexed positions, where the positions between our indexed positions are for our searched section
	family_span = []
	for i in range(len(sorted_sections)):
		normalize = sections[sorted_sections[i]].lower()
		if len(files) == 1:
			print(sections[sorted_sections[i]])
		for remove in what_to_remove:
			if remove in normalize:
				#When looking at a single file that is causing a section removal problem, print the all the sections, and then print !!!!!!! underneath the sections
				#that are going to be removed
				if len(files) == 1:
					print('!!!!!!!!!!!!!!!!!!!!!!')
				family_span.append(sorted_sections[i])
				family_span.append(sorted_sections[i+1])

	#This is complicated, but in essence, we are creating the string indexers for the positions that need to be removed. This apporpriately handles the data from the start of the document to the first what_to_remove section, leaves in the document that is between what_to_remove sections, keeps the data from the last what_to_remove section to the end of the document
	if len(family_span) > 0:
		count = 0
		out_dictionary = {}
		for tup in range(len(family_span)):
			try:
				count += 1
				if count == 1:
					#print(str(family_span[-count])+': end')
					out_dictionary[count] = content[family_span[-count]:]
				if count == len(family_span):
					out_dictionary[count] = content[:family_span[-count]]
				if count % 2 == 0:
					out_dictionary[count] = content[family_span[-count-1]:family_span[-count]]
			except:
				break

		#Here, we are just putting back the removed sections in order. While document order doesn't matter for all sections, I know that some of you are depending on the document reamaining in order. 
		out_sorted = sorted(out_dictionary.keys(), reverse = True)
		out_string = ''
		for i in range(len(out_sorted)):
			#print(out_dictionary[out_sorted[i]])
			out_string += out_dictionary[out_sorted[i]]

		#Rewrite the new file, filtered out for what sections we are looking for. 
		outfile = open('filtered_'+ file ,'w')
		outfile.write(out_string)
		outfile.close()
	else:
		outfile = open('filtered_'+ file,'w')
		outfile.write(content)
		outfile.close()
