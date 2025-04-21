

def activity_selection(start_times, finish_times):
    """
    Solve the activity selection problem using greedy approach.
    Returns the maximum number of activities that can be performed.
    """
    # Create a list of tuples containing start time, finish time, and index
    activities = [(start_times[i], finish_times[i], i) for i in range(len(start_times))]
    # Sort activities by finish time
    activities.sort(key=lambda x: x[1])
    
    selected_activities = []
    last_finish_time = 0
    
    for start, finish, index in activities:
        if start >= last_finish_time:
            selected_activities.append(index)
            last_finish_time = finish
    
    return selected_activities


    """
    Solve the coin change problem using greedy approach.
    Returns the minimum number of coins needed to make the amount.
    Note: This works only for certain coin denominations.
    """
    # Sort coins in descending order
    coins.sort(reverse=True)
    
    result = []
    remaining_amount = amount
    
    for coin in coins:
        while remaining_amount >= coin:
            result.append(coin)
            remaining_amount -= coin
    
    return result if remaining_amount == 0 else []

# Example usage
if __name__ == "__main__":
 
    # Example 2: Activity Selection
    start_times = [1, 3, 0, 5, 8, 5]
    finish_times = [2, 4, 6, 7, 9, 9]
    print("Activity Selection Result:", activity_selection(start_times, finish_times))
    
    