from rich.pretty import pprint as pprint

number_of_days = 31
graph = {}


# Generate graph/days in the month
for day in range(1, number_of_days):
    for adjacent_days in range(day + 1, number_of_days + 1):  # +1 to include 31
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
        edges = graph[f"Day {current}"]
        edges.sort(key=lambda x: x[1])
        next_day = int(edges[0][0].split()[1])
        print(f"Day {current} -> ", end="")
        current = next_day
    print(f"Day {goto_day}")

greedy_path(int(input('Current day: ')), int(input('Goto day: ')))
