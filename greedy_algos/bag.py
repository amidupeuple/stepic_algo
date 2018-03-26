import heapq

def get_max_cost(pieces, capacity):
	sorted_pieces = sorted(pieces, key=lambda p: p[0]/p[1], reverse=True)
	result_cost = []
	i = 0
	while capacity and i < len(sorted_pieces):
		if capacity <= sorted_pieces[i][1]:
			new_c = (sorted_pieces[i][0]/sorted_pieces[i][1]) * capacity
			result_cost.append(new_c)
			capacity = 0
		else:
			result_cost.append(sorted_pieces[i][0])
			capacity = capacity - sorted_pieces[i][1]
		i += 1
	return sum(result_cost)


def fractional_knapsack(capacity, values_and_weights):
	order = [(-v / w, w) for v, w in values_and_weights]
	heapq.heapify(order)
    acc = 0
    while order and capacity:
        v_per_w, w = heapq.heappop(order)
        can_take = min(w, capacity)
        acc -= v_per_w * can_take
        capacity -= can_take

    return acc



def main():
	n, w = map(int, input().split())
	
	pieces = [tuple(map(int, input().split())) for _ in range(n)]
	
	'''n = 3
	w = 50
	pieces = [(60, 20), (100, 50), (120, 30)]'''

	print("{0:.3f}".format(get_max_cost(pieces, w)))

if __name__ == "__main__":
	main()
