import json

class SatData:

    def __init__(self, name_of_file):
        self._name_of_file = name_of_file
        self._sat_json_data = ''
        
        with open(name_of_file, 'r') as infile:
            self._sat_json_data = json.load(infile)
    
    def save_as_csv(self, dbn_list):
        rows = [] 

        with open('output.csv', 'w') as outfile:
            outfile.write('DBN, School Name, Number of Test Takers, Critical Reading Mean, Mathematics Mean, Writing Mean')
            for school_row in self._sat_json_data['data']:
                dbn = school_row[8]
                if dbn in dbn_list:
                    rows.append(school_row)
            
            for row in rows:
                outfile.write(','.join(row[8:]))
                outfile.write('\n')

sd = SatData('sat.json')
dbns = ["02M303", "02M294", "01M450", "02M418"]
sd.save_as_csv(dbns)