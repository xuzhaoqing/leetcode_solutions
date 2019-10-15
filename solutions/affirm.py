
#
# Complete the 'amounts_to_return_users' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY transaction_activities as parameter.
#
from datetime import datetime

def amounts_to_return_users(transaction_activities):
    # Write your code here
    users = {}   # {funds, loads + funds, if purchased}

    # Since it's not chronlogical, we should firstly find all the creation and purchase step
    for transaction in transaction_activities:
        uid, activity, amount, timestamp = transaction.split(',')
        amount = int(amount)
        if activity == 'Creation':
            if uid not in users:
                users[uid] = {'credit':amount, 'fund':amount,'load':0, 'purchased_time':None}
            else:
                users[uid]['credit'] = amount
                users[uid]['fund'] += amount
                if users[uid]['fund'] < 0:
                    users[uid]['load'] = users[uid]['fund']
                    users[uid]['fund'] = 0

        elif activity == 'Purchase':
            timestamp = datetime.strptime(timestamp,"%Y-%m-%d %H:%M:%S")
            if uid not in users:
                users[uid] = {'credit':0, 'fund':-amount, 'load': 0, 'purchased_time':timestamp} 
            else:
                users[uid]['fund'] -= amount
                if users[uid]['fund'] < 0:
                    users[uid]['load'] = users[uid]['fund']
                    users[uid]['fund'] = 0
                users[uid]['purchased_time'] = timestamp

    

    for transaction in transaction_activities:
        uid, activity, amount, timestamp = transaction.split(',')
        
        if activity == 'Load':
            amount = int(amount)
            timestamp = datetime.strptime(timestamp,"%Y-%m-%d %H:%M:%S")
            if uid not in users or not users[uid]['purchased_time']:
                continue
            else:
                if users[uid]['purchased_time'] > timestamp:  # It's a Load by the user
                    users[uid]['load'] += amount
                else: # It's a return
                    if users[uid]['credit'] - users[uid]['fund'] >= amount:
                        users[uid]['fund'] += amount
                    else:
                        users[uid]['load'] += (amount - users[uid]['credit'] + users[uid]['fund'])
                        users[uid]['fund'] = users[uid]['credit']

    
    return_list = [uid + '**' + str(user['load']) for uid,user in users.items() if user['load'] > 0 and user['purchased_time'] ]

    return return_list

    