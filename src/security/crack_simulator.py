'''This modules gives the crack time and simulates the crack'''

def crack_time(entropy_bits,guesses_per_second):
    '''This function gives the crack_time 
        from entropy and guesses per sec'''

    total_possible_passcode = pow(2,entropy_bits)
    time = total_possible_passcode / guesses_per_second
    minutes = time /60
    hours = minutes /60
    days = hours /24
    years = days /365
    return {
        "seconds":time,
        "minutes":minutes,
        "hours":hours,
        "days":days,
        "years":years
    }
