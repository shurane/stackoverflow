# https://stackoverflow.com/questions/67015308/turning-multiple-dictionary-values-into-single-output/67015642
list_of_dictionaries = [
    [{'key1': {'subkey1': 1.0},'key2': {'subkey2': 1.0},'key3': 'abc'},
     {'key1': {'subkey1': 1.1},'key2': {'subkey2': 1.1},'key3': 'def'},
     {'key1': {'subkey1': 1.2},'key2': {'subkey2': 1.2},'key3': 'ghi'},
     {'key5': 5.0, 'key6': 6.0}],
    [{'key1': {'subkey1': 2.0},'key2': {'subkey2': 2.0},'key3': 'abc'},
     {'key1': {'subkey1': 2.1},'key2': {'subkey2': 2.1},'key3': 'def'},
     {'key1': {'subkey1': 2.2},'key2': {'subkey2': 2.2},'key3': 'ghi'},
     {'key5': 7.0, 'key6': 8.0}]
]

for list_of_metrics in list_of_dictionaries:
    extra = next((d for d in list_of_metrics if 'key5' in d), None)
    print('extra', extra)
    for dictionary in list_of_metrics:
        if 'key1' in dictionary:
            subkey1 = dictionary['key1']['subkey1']
            print('Key1, Subkey1 value:', subkey1, 'Key5 value:', extra['key5'], 'Key6 value:', extra['key6'])
        # if 'key5' in dictionary:
        #     key5 = dictionary['key5']
        #     key6 = dictionary['key6']
        #     print('Key5 value: ' + str(key5) + ', Key6 value: ' + str(key6))