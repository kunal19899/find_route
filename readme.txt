Name: Kunal Samant

ID: 1001534662

Programming Language: Python3

Code Structure:

    main() - 1. takes in the system arguments and stores them to use as parameters for the functions
             2. passes the input data into create_map() to properly read and store it in a 2D list
             3. extracts all the start and goal states to check if the command line arguments for start and goal cities exist
             4. calls uniform_cost_search() if heursitic text file isn't listed in command line arguments and a_star_search() if it is given
             5. calls create_heuristics() to read the heuristics text file, if given
             5. calls print_results() to print the results of the search

    create_map() - 1. takes the input filename as an arguments
                   2. parses the txt file by line and stores the data in a 2D list called "map" until "END OF INPUT" is achieved
                   3. return map
    
    create_heuristics() - 1. takes heuristics text file as an argument
                          2. parses the txt file by line and stores the data in a dictionary called "heuristics" until "END OF INPUT" is achieved
                          3. keys are the city names and values are the heuristic
                          3. return heuristics
    
    uniform_cost_search() - 1. takes map, start, and goal as arguments
                            2. uses a priority queue to perform uniform cost search on the map
                            3. calculates the number of nodes_generated, nodes_expanded, and the max_node_in_memory
                            4. returns path, cost, nodes_expanded, nodes_generated, max_node_in_memory in a list

    a_star_search() - 1. performs same function as uniform_cost_search(), however with the addition of a heuristic

    start_state_retrieval() - used to extract start states

    goal_state_retrieval() - extract goals states

    print_results() - print results of the search(es), prints out the results according to the format of the results

How to Run Code:

    python3 find_route.py <input_txt> <city1> <city2> (<heuristic_txt>)