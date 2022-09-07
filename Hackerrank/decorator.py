import operator

def person_lister(f):
    def inner(people):
        return map(f,sorted([*people],key=lambda lista:int(lista[2])))        
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    #people = [input().split() for i in range(int(input()))]
    people = [['Mike', 'Thomson', '20', 'M'], ['Robert', 'Bustle', '32', 'M'], ['Andria', 'Bustle', '30', 'F']]
    print(*name_format(people), sep='\n')