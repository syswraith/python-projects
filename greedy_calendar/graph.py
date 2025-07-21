number_of_days = 31
graph = {}


# Generate graph/days in the month
for day in range(1, number_of_days):
    for adjacent_days in range(day + 1, number_of_days + 1):
        distance = adjacent_days - day
        graph.setdefault(f"Day {day}", []).append((f"Day {adjacent_days}", distance))


def greedy_path(at_day, goto_day):
    '''
    As long as the at_day isn't greater than goto_day
    Get the edges of at_day and sort them with respect to minimum distance from each other
    Get the first element of the sorted edges and go to that day
    Repeat the process
    '''
    if at_day > goto_day:
        print("Cannot go back to date")
        return

    current = at_day
    while current < goto_day:
        edges = graph[f"Day {current}"] # Get all the edges
        edges.sort(key=lambda x: x[1]) # Sort all the edges w.r.t their distance
        next_day = int(edges[0][0].split()[1]) # Get the first day which has the most minimum distance, split and get its number (its initially a string)
        print(f"Day {current} -> ", end="") # Print the current day
        current = next_day # Set the current day to the next day
    print(f"Day {goto_day}")


greedy_path(int(input('Current day: ')), int(input('Goto day: ')))
