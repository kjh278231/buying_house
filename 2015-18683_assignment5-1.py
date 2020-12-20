import ast

def load_args(txt_path):
    with open(txt_path, 'r') as f:
        lines = f.readlines()
        n = int(lines[0])
        edge_list = ast.literal_eval(lines[1])
        D = int(lines[2])

    return n, edge_list, D

def build_graph(edge_list,n):
    '''
    ############################ Function description ############################
    Design a function that returns the graph, given edge_list.
    A graph can be of any type, such as list, dict or class.
    ##############################################################################
    '''
    graph = None
    ##### Please write your code down here #####
    graph = [0]*n
    for i in range(n):
      graph[i] = [-1]*n
    for i in range(n):
      graph[i][i] = 0
    for edge in edge_list:
        st, end, w = edge
        graph[st-1][end-1] = w

    ##### Please write your code down here #####
    return graph

def planning_a_date(n, edge_list, D):
    '''
    ############################ Function description ############################
    Design a function that returns best city with given n, edge_list and D.
    If there is no available path, update D to D+1 and search again.
    Usage for the variables are as follows for the example in the problem description: 
    best_city = 4
    paths = [[4,2,1], [4,2], [4,3]]
    dist = {'1': 4, '2': 1, '3': 1}
    ##############################################################################
    '''
    paths = [] 
    dist = {} 
    graph = build_graph(edge_list,n)
    pi = [0]*n
    for i in range(n):
      pi[i] = [-1]*n
    ##### Please write your code down here #####
    # for lin in graph:
    #   print(lin)
     
    
    L = graph.copy()
    m=1
    for i in range(n):
      for j in range(n):
        if L[i][j] != 0 and L[i][j] != -1:
          pi[i][j] = i+1


    # print("\n Initial Path matrix: ")
    # for line in pi:
    #   print(line)
    # print("\n Initial Cost matrix: ")
    # for line in L:
    #   print(line)


    while(m<n):
      L_old = L.copy()
      W = L.copy()
      for j in range(n):
        L[j] = [-1]*n
        L[j][j]=0
      # for line in L:
      #   print(line)
      for j in range(n):
        for k in range(n):
          MIN = L_old[j][k]
          for l in range(n):
            if L_old[j][l]!=-1 and W[l][k] != -1:
              if MIN > L_old[j][l]+W[l][k] or (MIN == -1 and L_old[j][l]+W[l][k] <=D):
                pi[j][k] = l+1
                MIN = L_old[j][l]+W[l][k]
          if MIN <=D:
            L[j][k] =MIN
      # print("\n Path matrix: ")
      # for line in pi:
      #   print(line)
      # print("\n Cost matrix: ")
      # for line in L:
      #   print(line)
      m*=2
    MAX = 0
    MAX_index = 0
    MAX_weight = D*n
    for i in range(n):
      comp =0
      weight = 0
      for j in range(n):
        if L[i][j] != 0 and L[i][j]!=-1:
          comp+=1
          weight+=L[i][j]
      if ((comp > MAX) or (comp==MAX and weight < MAX_weight)):
        MAX_index = i
        MAX = comp
        MAX_weight = weight
    for i in range(n):
      if L[MAX_index][i] !=0 and L[MAX_index][i]!=-1:
        dist[str(i+1)] = L[MAX_index][i]
    best_city = MAX_index+1
    
    for i in range(n):
      if pi[best_city-1][i] == -1:
        continue
      li = []
      li.append(i+1)
      k = best_city-1
      while(pi[k][i] != k+1):
        k = pi[k][i]-1
        li.append(k+1)
      li.append(best_city)
      paths.append(li[::-1])
   
          
    return best_city, paths, dist

if __name__ == '__main__':
    '''
    # The input will be randomly changed by TAs when grading.    
    # You can freely define a new function or class.
    # You should "not" modify the "main" function
    # Only the python standard library(https://python.readthedocs.io/en/stable/library/index.html) and numpy are available.
    '''
    input_txt = 'input.txt'
    args = load_args(input_txt)
    best_city, paths, dist = planning_a_date(*args)

    print("Best city: {} with the total distance: {}".format(best_city, sum(dist.values())))
    for path in paths:
        print('Path from {} to {}: {} with distance {}'.format(best_city, path[-1], path, dist[str(path[-1])]))
