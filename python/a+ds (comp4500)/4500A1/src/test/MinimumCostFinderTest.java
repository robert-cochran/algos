package test;

import assignment1.*;
import java.util.*;

import org.junit.Assert;
import org.junit.Test;

/**
 * Basic tests for the {@link MinimumCostFinder} implementation class.
 * 
 * We will use a much more comprehensive test suite to test your code, so you
 * should add your own tests to this test suite to help you to debug your
 * implementation.
 */
public class MinimumCostFinderTest {

    @Test
    public void example1Test() {
        /* Initialise parameters to the test. */

        // number of locations
        int n = 6;
        // create n locations so that location.get(i) has identifier i
        List<Location> locations = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            locations.add(new Location(i));
        }
        Location source = locations.get(0);
        int ts = 2;
        Location destination = locations.get(5);
        int td = 20;
        List<Delivery> deliveries = new ArrayList<>();
        deliveries.add(getDelivery(locations, 0, 1, 3, 4, 10));
        deliveries.add(getDelivery(locations, 0, 1, 5, 7, 2));
        deliveries.add(getDelivery(locations, 0, 1, 10, 11, 1));
        deliveries.add(getDelivery(locations, 0, 3, 8, 9, 0));
        deliveries.add(getDelivery(locations, 1, 2, 5, 6, 2));
        deliveries.add(getDelivery(locations, 1, 2, 7, 9, 3));
        deliveries.add(getDelivery(locations, 1, 4, 8, 10, 1));
        deliveries.add(getDelivery(locations, 1, 5, 12, 13, 9));
        deliveries.add(getDelivery(locations, 2, 5, 4, 6, 1));
        deliveries.add(getDelivery(locations, 2, 5, 11, 15, 3));
        deliveries.add(getDelivery(locations, 4, 0, 11, 12, 2));
        deliveries.add(getDelivery(locations, 4, 5, 9, 10, 1));

        /* Run method on inputs and test result. */

        // the expected minimum cost
        int expectedCost = 8;
        // the actual cost returned
        int actualCost = MinimumCostFinder.findMinimumCost(
                new HashSet<Location>(locations), source, ts, destination, td,
                deliveries);

        // compare the actual and expected outputs
        Assert.assertEquals(expectedCost, actualCost);
    }

    @Test
    public void example2Test() {
        /* Initialise parameters to the test. */

        // number of locations
        int n = 6;
        // create n locations so that location.get(i) has identifier i
        List<Location> locations = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            locations.add(new Location(i));
        }
        Location source = locations.get(0);
        int ts = 2;
        Location destination = locations.get(5);
        int td = 20;
        List<Delivery> deliveries = new ArrayList<>();
        deliveries.add(getDelivery(locations, 0, 1, 15, 16, 1));
        deliveries.add(getDelivery(locations, 0, 3, 8, 9, 0));
        deliveries.add(getDelivery(locations, 1, 2, 5, 6, 2));
        deliveries.add(getDelivery(locations, 1, 2, 7, 9, 3));
        deliveries.add(getDelivery(locations, 1, 4, 8, 10, 1));
        deliveries.add(getDelivery(locations, 1, 5, 12, 13, 9));
        deliveries.add(getDelivery(locations, 2, 5, 4, 6, 1));
        deliveries.add(getDelivery(locations, 2, 5, 11, 15, 3));
        deliveries.add(getDelivery(locations, 4, 0, 11, 12, 2));
        deliveries.add(getDelivery(locations, 4, 5, 9, 10, 1));

        /* Run method on inputs and test result. */

        // the expected minimum cost
        int expectedCost = -1;
        // the actual cost returned
        int actualCost = MinimumCostFinder.findMinimumCost(
                new HashSet<Location>(locations), source, ts, destination, td,
                deliveries);

        // compare the actual and expected outputs
        Assert.assertEquals(expectedCost, actualCost);
    }

    @Test
    public void example3Test() {
        /* Initialise parameters to the test. */

        // number of locations
        int n = 5;
        // create n locations so that location.get(i) has identifier i
        List<Location> locations = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            locations.add(new Location(i));
        }
        Location source = locations.get(0);
        int ts = 2;
        Location destination = locations.get(4);
        int td = 20;
        List<Delivery> deliveries = new ArrayList<>();
        deliveries.add(getDelivery(locations, 0, 1, 2, 3, 1));
        deliveries.add(getDelivery(locations, 1, 2, 4, 5, 1));
        deliveries.add(getDelivery(locations, 2, 3, 6, 7, 1));
        deliveries.add(getDelivery(locations, 3, 4, 8, 9, 1));
        deliveries.add(getDelivery(locations, 0, 4, 2, 9, 3));
        

        /* Run method on inputs and test result. */

        // the expected minimum cost
        int expectedCost = 3;
        // the actual cost returned
        int actualCost = MinimumCostFinder.findMinimumCost(
                new HashSet<Location>(locations), source, ts, destination, td,
                deliveries);

        // compare the actual and expected outputs
        Assert.assertEquals(expectedCost, actualCost);
    }
    
    @Test
    public void twoP2RouteTest() {
        /* Initialise parameters to the test. */

        // number of locations
        int n = 3;
        // create n locations so that location.get(i) has identifier i
        List<Location> locations = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            locations.add(new Location(i));
        }
        Location source = locations.get(0);
        int ts = 2;
        Location destination = locations.get(2);
        int td = 20;
        List<Delivery> deliveries = new ArrayList<>();
        deliveries.add(getDelivery(locations, 0, 1, 2, 3, 1));
        deliveries.add(getDelivery(locations, 1, 2, 4, 5, 1));
        deliveries.add(getDelivery(locations, 0, 2, 2, 5, 3));
        

        /* Run method on inputs and test result. */

        // the expected minimum cost
        int expectedCost = 2;
        // the actual cost returned
        int actualCost = MinimumCostFinder.findMinimumCost(
                new HashSet<Location>(locations), source, ts, destination, td,
                deliveries);

        // compare the actual and expected outputs
        Assert.assertEquals(expectedCost, actualCost);
    }
    
    @Test
    public void selfLoopSourceTest() {
        /* Initialise parameters to the test. */

        // number of locations
        int n = 2;
        // create n locations so that location.get(i) has identifier i
        List<Location> locations = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            locations.add(new Location(i));
        }
        Location source = locations.get(0);
        int ts = 2;
        Location destination = locations.get(n-1);
        int td = 20;
        List<Delivery> deliveries = new ArrayList<>();
        deliveries.add(getDelivery(locations, 0, 0, 2, 3, 1));
        //deliveries.add(getDelivery(locations, 0, 1, 2, 5, 3));
        

        /* Run method on inputs and test result. */

        // the expected minimum cost
        int expectedCost = -1;
        // the actual cost returned
        int actualCost = MinimumCostFinder.findMinimumCost(
                new HashSet<Location>(locations), source, ts, destination, td,
                deliveries);

        // compare the actual and expected outputs
        Assert.assertEquals(expectedCost, actualCost);
    }
    
    @Test
    public void selfLoopDestinationTest() {
        /* Initialise parameters to the test. */

        // number of locations
        int n = 2;
        // create n locations so that location.get(i) has identifier i
        List<Location> locations = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            locations.add(new Location(i));
        }
        Location source = locations.get(0);
        int ts = 2;
        Location destination = locations.get(n-1);
        int td = 20;
        List<Delivery> deliveries = new ArrayList<>();
        deliveries.add(getDelivery(locations, 1, 1, 2, 3, 1));
        //deliveries.add(getDelivery(locations, 0, 1, 2, 5, 3));
        

        /* Run method on inputs and test result. */

        // the expected minimum cost
        int expectedCost = -1;
        // the actual cost returned
        int actualCost = MinimumCostFinder.findMinimumCost(
                new HashSet<Location>(locations), source, ts, destination, td,
                deliveries);

        // compare the actual and expected outputs
        Assert.assertEquals(expectedCost, actualCost);
    }
    
    @Test
    public void ThreeLocationsIncompleteRouteBeforeDestinationTest() {
        /* Initialise parameters to the test. */

        // number of locations
        int n = 3;
        // create n locations so that location.get(i) has identifier i
        List<Location> locations = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            locations.add(new Location(i));
        }
        Location source = locations.get(0);
        int ts = 2;
        Location destination = locations.get(n-1);
        int td = 20;
        List<Delivery> deliveries = new ArrayList<>();
        deliveries.add(getDelivery(locations, 1, 2, 2, 3, 1));
        //deliveries.add(getDelivery(locations, 0, 1, 2, 5, 3));
        

        /* Run method on inputs and test result. */

        // the expected minimum cost
        int expectedCost = -1;
        // the actual cost returned
        int actualCost = MinimumCostFinder.findMinimumCost(
                new HashSet<Location>(locations), source, ts, destination, td,
                deliveries);

        // compare the actual and expected outputs
        Assert.assertEquals(expectedCost, actualCost);
    }
    
    @Test
    public void ThreeLocationsIncompleteRouteAfterSourceTest() {
        /* Initialise parameters to the test. */

        // number of locations
        int n = 3;
        // create n locations so that location.get(i) has identifier i
        List<Location> locations = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            locations.add(new Location(i));
        }
        Location source = locations.get(0);
        int ts = 2;
        Location destination = locations.get(n-1);
        int td = 20;
        List<Delivery> deliveries = new ArrayList<>();
        deliveries.add(getDelivery(locations, 0, 1, 2, 3, 1));
        //deliveries.add(getDelivery(locations, 0, 1, 2, 5, 3));
        

        /* Run method on inputs and test result. */

        // the expected minimum cost
        int expectedCost = -1;
        // the actual cost returned
        int actualCost = MinimumCostFinder.findMinimumCost(
                new HashSet<Location>(locations), source, ts, destination, td,
                deliveries);

        // compare the actual and expected outputs
        Assert.assertEquals(expectedCost, actualCost);
    }
    
    
    /**
     * TEST CASES
     * 
     * 	Time:
     * 		BoundsCheck - test that time is correctly being rejected when not in bounds	
     * 			1 tv(i) <= tu(i+1) < tv(i+1) (will this hold for all cases in the route if checked at every point?)
     * 			2 td == 0 (no delivery can take place if this is true)
     * 			3 ts == td (if this is true, then no delivery can execute if tu < tv)
     * 			4 0 <= tu < tv
     * 			does the requirment on deliveries stop the bounds 2 and 3 from needing checking? 
     * 				ts <= x.departure() < x.arrival() <= td.
     * 
     * DELIVERIES
     * 		Bounds check
     * 			smallest amount of deliveries, 1?
     * 			multiple copies of deliveries
     * 			Loops
     * 			SelfLoops
     * 			Sink
     * 
     * PLACES
     * 		BoundsCheck
     * 			2 distinct places
     * 				many deliveries
     * 				1 delivery
     * 				2
     * 				all/some invalid
     * 			3 distinct places
     * 				all/both/some invalid
     * 				1 del
     * 				2, 3
     * 
     * 			need to know how im changing delivery here though?
     */				
    
    /**
     * Need to test time aspect of graphs, this seems v subtly tricky
     */
    
    /*---Helper methods--------------------*/

    /**
     * Creates and returns a delivery from the ith location in locations to the
     * jth location in locations, departing at time departure and arriving at
     * time arrival, with the given cost.
     */
    private static Delivery getDelivery(List<Location> locations, int source,
            int destination, int departure, int arrival, int cost) {
        return new Delivery(locations.get(source), locations.get(destination),
                departure, arrival, cost);
    }

}
