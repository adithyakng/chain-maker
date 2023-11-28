import csv
import json
import hashlib

index_protocol = 1
index_standard = 3
index_devices = 4
index_requ_hardware = 6
index_paper_name = 10
index_prior_state = 14
index_prior_knowledge = 15
index_post_state = 16
index_post_knowledge = 17


with open('attacks.csv') as file:
    #read in the attacks csv file
    csv_reader = csv.reader(file)

    #skip the heading line
    next(csv_reader)

    #convert all of the attacks into dictionaries and store them in a list
    attack_dict_list = []
    for attack in csv_reader:
        temp_dict = {}

        #keep a space open for an id to be saved since we want this to be the first val for asthetics
        temp_dict['_id'] = {'$oid': 0}

        #save the attack name
        temp_dict['name'] = attack[index_paper_name]

        #save prior state 
        prior_state_dict = {}
        for state in attack[index_prior_state].split(';'):
            prior_state_dict[state] = state
        temp_dict['initState'] = prior_state_dict

        #save post state 
        post_state_dict = {}
        for state in attack[index_post_state].split(';'):
            post_state_dict[state] = state
        temp_dict['endState'] = post_state_dict

        #save prior knowledge
        temp_dict['initKnowledge'] = attack[index_prior_knowledge].split(';')

        #save post knowledge
        temp_dict['endKnowledge'] = attack[index_post_knowledge].split(';')

        #save hardware requirements
        temp_dict['hardwareRequirements'] = attack[index_requ_hardware].split(';')
            
        #update the id with a hash of temp_dict
        #dump it to a json first to ensure stability
        temp_dict['_id'] = {'$oid': hex(abs(hash(json.dumps(temp_dict, sort_keys=True))))[2::]+'ffffffff'}

        #save the temp dict in the list
        attack_dict_list.append(temp_dict)

with open('attackDB.json','w') as output_file:
    json.dump(attack_dict_list,fp=output_file,indent=4)
    
