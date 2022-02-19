import csv
import argparse



def Main(search):

    reader = csv.reader(open('Phrases.csv'))
    runes = {}
    phrases = {}
    counter = {}
    result = []
    count = 0

    for row in reader:
        rune = row[1]
        phrase = row[0]
        
        # if rune in runes:
        #     runes[rune].append(phrase)
        # else:
        #     runes[rune] = [phrase]
            
        if phrase in phrases:
            phrases[phrase].append(rune)
        else:
            phrases[phrase] = [rune]
            counter[phrase] = 0
        
    
    for i in search:
        for key,value in phrases.items():
            if i in value:
                counter[key] += 1
            
    for key,value in counter.items():
        if value == len(search):
            result.append(key)
            

    print(result)                
 
    
    

def Arguments():
    parser = argparse.ArgumentParser(description="Search List of Hive Rune Phrases")
    parser.add_argument("search", nargs='+', help="Name of the biugplanet input file")
    
    args = parser.parse_args()
    Main(args.search)


if __name__ == "__main__":
    Arguments()