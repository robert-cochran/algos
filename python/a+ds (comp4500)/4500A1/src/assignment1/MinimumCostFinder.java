package assignment1;

import java.util.*;

public class MinimumCostFinder {

    /**
     * @require The set of locations, locations, is not null and each location
     *          in the set of locations is not null and has a unique identifier
     *          in the range [0, locations.size()-1].
     * 
     *          The set of locations contains the source and destination
     *          locations, and those two locations are not equal.
     * 
     *          The earliest time that the package can depart the source
     *          location, ts, is non-negative (i.e. 0 <= ts). The latest time
     *          that the package can arrive at the destination location, td, is
     *          no earlier than ts (i.e. ts <= td).
     *
     *          The list of deliveries, deliveries, is not null, and for each
     *          delivery x in the deliveries, the source and destination of x
     *          are in the set of locations, and ts <= x.departure() <
     *          x.arrival() <= td.
     * 
     * @ensure Returns the minimum cost of any route from source to destination
     *         that departs the source location no earlier than time ts, and
     *         arrives at the destination location no later than time td, if at
     *         least one such route exists. If no such route exists the
     *         algorithm should return the distinguished value -1.
     * 
     *         (See the assignment handout for details.)
     */
	
	/**
	 * 
	 * @param locations
	 * @param source
	 * @param ts
	 * @param destination
	 * @param td
	 * @param deliveries
	 * @return
	 */
	
	/*
	* 
		1. implement A solution
			After it has been established as working, 
			get better idea of the problem
		2. do run-time analysis of the code
			section all loops in the code to make analysis clear
			see where it can be improved
			hopefully see where it would fail
		3. Write more tests
			based on runtime analysis 
			and identifying any case not explicitly stated in the assignment sheet
		4. Check that it still works, fix, improve
		5. write more tests
		6. Check that it still works, fix, improve
		7. repeat
		8. Refine and improve the algorithm so that functionality is first and speed is second 
	*/
	/*
		Rules:
			Ps != Pd
			0 <= ts <= td
			m deliveries (so measuring here in runtime of m)
			for every D, ts <= tu, tv <= td
			0 <= tu < tv
			0 <= cost; for each delivery
	*/
	/*
	 * NEEDED UPGRADES
	 * 		location used it removed from locations
	 * 		use adjacency list instead of matrix (worst case for lookup with list is O(m), in matrix is O(1))
	 * 		have some kind of Q - essentially a topological sort (only possible with DAG???)
	 * 			Can we remove the loops? one way being to remove any delivery that refers back to source
	 * 			remove sinks?
	 * 
	 * 
	 * Can we assume all the requirements in the assignment spec are also requirements for the code? e.g. cost is non negative
	 */
	 public static int findMinimumCost(
			 			Set<Location> locations, 
	 					Location source, int ts, 
	 					Location destination, int td, 
	 					List<Delivery> deliveries) { 
		 					//can deliveries have repeated location? ie self-loop? I cant see anything stating otherwise

		int minimumCostRoute = -1;
		int minimumCurrentRouteCost = -1;
		
		//0<=tu<tv might prevent this from needing checking
		if (td == 0){return minimumCostRoute;} 
		if (ts == td){return minimumCostRoute;}
		
		//look for adjacent routes starting from Source-P
			//currently does not sort deliveries by start route
			//currently does not sort deliveries by cost
		//Time: O(d) - every delivery is checked if it equals source
			//but its recursive so thats no always true
		
		
		
		/**PriorityQ = {};
		add all deliveries that start with source location
			this will stop the program falling into loops I hope
		
		or
		PriorityQ = All;
		remove deliveries that have no continuation as I go
		
		Can i do both?
		send in reduced Q and reduced Locations ?*/
		
		for (Delivery startDelivery: deliveries){
			
			//these checks are almost definitely too slow
			if (startDelivery.source().equals(source)){

				
				//every ts <= tu, tu < tv, tv <= td, 
				//so lowest it could be is ts = 0, td = 0
					//but if it is it can never be executed!
					//because tu < tv for any ACTUAL delivery
				if (startDelivery.destination().equals(destination)){
					minimumCurrentRouteCost = startDelivery.cost();
				}
				else {
						//this will return the cheapest possible route from the graph for the given delivery
							//need to remove SOURCE from locations to avoid looping
							//should probably remove delivery from deliveries
						//returns minimum possible route for given newSOURCE, newTS, DESTINATION, TD
						//from DELIVERIES if APPLICABLE
							//remove location from LOCATIONS
								//remove delivery from DELIVERIES
								//remove duplicate deliveries if they exist
								//reorder deliveries and locations
						minimumCurrentRouteCost = findRoute(locations, startDelivery.destination(), 
								startDelivery.arrival(), destination, td, deliveries, startDelivery.cost());
					System.out.println("Route " + minimumCurrentRouteCost);
				}
					//does this ensure correctness here?
				if (minimumCurrentRouteCost >= 0 && (minimumCurrentRouteCost < minimumCostRoute || minimumCostRoute == -1)){
					minimumCostRoute = minimumCurrentRouteCost;
				}
				
			}

		}
		System.out.println("End");
		//if no adjacent routes, minimumCostRoute will be unchanged
		return minimumCostRoute;
	}
	 
	//how do I make sure I'm not traversing through the graph a needless amount of times
		//i.e. ignoring the neighbour routes i didnt choose earlier, 
	 	//or even just looking at the routes
		//with a starting location that matches mine  

	/**
	Invariant: delivery chosen will never exceed td, never be less than ts, returns -2 if no routes found
	*/

	/*
	Find the shortest route cost between two start and end locations, and two start and end times, 
	Returns the shortest route cost between these two points if it exists, 

	Start and End locations must:
		- be distinct
		- exist in the locations list

	Start and End times must:
		- be non negative such that 
			0 <= ts <= td

	runningCost will be either:
		- non negative if a valid route exists
		- -2 if no route exists from the start, to the end, within the given timeframe

	Returns Int of minimum cost to destination from given source
	*/
	private static int findRoute(Set<Location> locations, //why do i need locations?
				Location source, int ts, 
				Location destination, int td, 
				List<Delivery> deliveries, int currentRouteCost){

		int minimumCostRoute = -1; //we want to return this
		int minimumCurrentRouteCost = -1; //use this as temp to check against current
		
		
		
		//look for adjacent routes starting from Source-P
			//currently does not sort deliveries by start route
			//currently does not sort deliveries by cost
		//every delivery is checked if it equals source, O(d)
		//should check that delivery locations are in LOCATIONS
		//avoid moving backwards
		for (Delivery nextDelivery: deliveries){


			if (nextDelivery.source().equals(source)
					&& ts <= nextDelivery.departure()) {
				
				if (nextDelivery.destination().equals(destination)){
					minimumCurrentRouteCost = currentRouteCost + nextDelivery.cost();
				}
				else {
					//this will return the cheapest possible route from the graph for the given delivery
					minimumCurrentRouteCost = currentRouteCost + nextDelivery.cost();
					minimumCurrentRouteCost = findRoute(locations, nextDelivery.destination(), nextDelivery.arrival(), destination, td, deliveries, minimumCurrentRouteCost);
				}
				
				if (minimumCurrentRouteCost >= 0 && (minimumCurrentRouteCost < minimumCostRoute || minimumCostRoute == -1)){
					minimumCostRoute = minimumCurrentRouteCost;
				}
			}

		}

		//if no adjacent routes, minimumCostRoute will be unchanged
		return minimumCostRoute;
	}
}
