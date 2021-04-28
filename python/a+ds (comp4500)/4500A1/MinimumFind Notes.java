MinimumFind Notes

Design notes/questions: 
	-recursive?
	-adjacency list/matrix
		-how will i implement it?
	-would doing a topological sort help?
		-could use this to remove all deliveries that act as sinks
		- keep doing so for anything that leads to it
	-do I need to start from source? are there other ways of doing this?
	-are there other ways of representing a vertex and an edge? 
		-i feel like my way might be cumbersome?
	-how else could i traverse the graph instead of start location, then cost, then time
	-do i have any way of dealing with duplicates? sinks? loops? selfloops?

	-loops
		-i should remove the location the delivery departs from the locations list 
		-this will avoid returning to a location ive already been

	-selfloops
		-check that for any delivery, Pu != Pv 

	-TreeMap/hashMap
		-adding a delivery as a key will automatically remove that delivery from being reconsidered

	-sinks
		-might not be STRICTLY necessary, but could be a big runtime sink

	-if i have an empty loop over all elements, e, of a list, is that running time then O(e)?
		-i guess if no constant runtime operations than its 0 time?

	-currently this is a dfs, will this find me the shortest path?
		-why does dijkstras guarantee shortest path?
		-purely the priority queue? 
		-whereas using dfs is a stack based search, dijkstras is a priority-queue based 
		-but why wouldnt this find all the possible paths?
		-dfs colours shit in, so this is doing much more work than dfs


	-SOURCE might be really close, really far away or in the opposite numerical order to DESTINATION
		-i remember something about finding the edge of a graph given any two verticies? 


	-improvements
		-avoid ever moving backwards by removing locations already visited
		-order LOCATIONS
		-order DELIVERIES
		-remove locations already visited
		-remove deliveries already visited
		-remove deliveries that are equivalent to the current delivery
		-remove deliveries with locations already visited 
			-remove deliveries where its source has already been visited
			-remove deliveries where its destination has already be visited
			-only allow deliveries with destination NOT visited
			-only allow deliveries with source that matches CURRENT source 
			-whats right here
		-change to non-recursive?