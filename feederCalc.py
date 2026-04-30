import sys

feeders = None
start = None
end = None

def get_feeders(rank, start=1):
    ## Calculates the number of feeders to get to a rank from another
    number_needed = 0
    for i in range(0,rank):
        if rank == start+1:
            number_needed += 1
        else:
            number_needed += get_feeders(rank-1, start)
    # print(F"End Rank: {rank}, Start Rank: {start}, Number Needed: {number_needed}")
    return number_needed
if len(sys.argv) == 1:
    print(F"Usage {sys.argv[0]} [flags], end_level")
    sys.exit()
for (i, c) in enumerate(sys.argv):
    if ~c.find('-f') or ~c.find('--feeders'):
        feeders = int(sys.argv[i+1])
    if ~c.find('-s') or ~c.find('--start'):
        start = int(sys.argv[i+1])
    if ~c.find('-e') or ~c.find('--end'):
        end = int(sys.argv[i+1])
feeders = feeders if feeders is not None else 1
end = end if end is not None else int(sys.argv[len(sys.argv)-1])
start = start if start is not None else 1

# Check if feeders are higher rank the the target champion and exit if so.
if feeders > start:
    print(F"Feeders are higher ranked then the starting rank of the champion,"
          F"or champion start level not specifed with feeder level specfied.")
    sys.exit(1)


total_feeders = get_feeders(end, feeders)
final_feeders = total_feeders - get_feeders(start,feeders) - 1
print(f"It takes {final_feeders} feeders of rank {feeders} to get to rank {end} from {start}")
