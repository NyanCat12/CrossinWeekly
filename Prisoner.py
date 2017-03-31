#Crossin 2017/03/31
def Start_behavior(strategy):
    if strategy == 'nice':
        return 0
    elif strategy == 'rat':
        return 1
    elif strategy == 'tit_for_tat':
        return 0
    elif strategy == 'my_strategy':
        return 0

def Update_behavior(strategy, behavior1, behavior2):
    if strategy == 'nice':
        return 0
    elif strategy == 'rat':
        return 1
    elif strategy == 'tit_for_tat':
        return behavior2
    elif strategy == 'my_strategy':
        return 0

def Step_result(behavior1, behavior2):
    if [behavior1, behavior2] == [0,1]:
        return [5,0]
    elif [behavior1, behavior2] == [1,0]:
        return [0,5]
    elif [behavior1, behavior2] == [1,1]:
        return [2,2]
    elif [behavior1, behavior2] == [0,0]:
        return [1,1]

def prisoner_delimma(N, strategy1, strategy2):
    result = [0, 0]
    behavior = [Start_behavior(strategy1),Start_behavior(strategy2)]
    for step in range(N):
        result[0] += Step_result(behavior[0], behavior[1])[0]
        result[1] += Step_result(behavior[0], behavior[1])[1]
        behavior = [Update_behavior(strategy1, behavior[0], behavior[1]), Update_behavior(strategy2, behavior[1], behavior[0])]
    return (result[0], result[1])

if __name__ == '__main__':
    print (prisoner_delimma(4,'nice', 'nice'))
    print (prisoner_delimma(5,'rat', 'rat'))
    print (prisoner_delimma(6,'nice', 'rat'))
    print (prisoner_delimma(4,'rat', 'tit_for_tat'))
    print (prisoner_delimma(7,'tit_for_tat', 'tit_for_tat'))
