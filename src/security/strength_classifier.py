'''This module is for the classification of password
with the respect to the entropy and crack time'''
def classify_strength(entropy,crack_time):
    '''
    Comparision:
    UNACCEPTABLY WEAK == 0
    VERY WEAK == 1
    WEAK ==2
    MODERATE == 3
    STRONG == 4
    VERY STRONG == 5
    - < 28 bits → VERY WEAK
    - < 36 bits → WEAK
    - < 60 bits → MODERATE
    - < 128 bits → STRONG
    - ≥ 128 bits → VERY STRONG
    '''
    entropy_cap = 0
    strength_using_crack_time = 0
    if crack_time['seconds'] < 1:
        strength_using_crack_time = 0
    elif crack_time['minutes'] < 1:
        strength_using_crack_time = 1
    elif crack_time['hours'] < 1:
        strength_using_crack_time = 2
    elif crack_time['days'] < 1:
        strength_using_crack_time = 3
    elif crack_time['years'] < 1:
        strength_using_crack_time = 4
    else:
        strength_using_crack_time = 5
    if entropy < 28:
        entropy_cap = 1
    elif entropy <36:
        entropy_cap = 2
    elif entropy <60:
        entropy_cap = 3
    elif entropy <128:
        entropy_cap = 4
    elif entropy >= 128:
        entropy_cap = 5
    final_rank = min(strength_using_crack_time,entropy_cap)
    if final_rank == 0:
        return "UNACCEPTABLY WEAK"
    elif final_rank == 1:
        return "VERY WEAK"
    elif final_rank == 2:
        return "WEAK"
    elif final_rank == 3:
        return "MODERATE"
    elif final_rank == 4:
        return "STRONG"
    elif final_rank == 5:
        return "VERY STRONG"
