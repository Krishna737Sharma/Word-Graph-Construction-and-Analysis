import sys

"""# **Task-1**

1. Construct an undirected and weighted graph, where the nodes are the words and the edge weight between two nodes is the length of the longest common prefix between the words. For example, if the two words are “educate” and “education”, then the edge weight between the two nodes would be 6.
"""

# Construct the graph

def construct_graph(words):
  graph={}
  for word1 in words:
    graph[word1]={}
    for word2 in words:
      if word1!=word2:
        prefix_len=0
        for i in range(min(len(word1),len(word2))):
          if word1[i]==word2[i]:
            prefix_len+=1
          else:
            break
        graph[word1][word2]=prefix_len
  return graph

# Read the file
with open("/content/word.txt") as f:

  words=[line.strip() for line in f.readlines()]

words=words[:-1]
# Print the total number of words
print("Total number of words:",len(words))

graph=construct_graph(words)

print("Total number of nodes:",len(graph))
print("Total number of edges:",sum(len(neighbors) for neighbors in graph.values()))
print("Graph constructed successfully!")

"""# **Task-2**

2. Given a threshold (as input) on the longest prefix length (say t), print the number of immediate neighbours (one hop) of each node (in terms of words) that has edge value ≥ t. This should be saved in a two column space separated text file. Your program must ask for the input threshold from the user.
"""

# Print immediate neighbors with prefix length >=t

def print_neighbors(graph,threshold):
  with open('/content/neighbors.txt','w') as f:
    for word,neighbors in graph.items():
      count=sum(1 for _,prefix_len in neighbors.items() if prefix_len>=threshold)
      f.write(f"{word} {count}\n")

# Print the neighbors with prefix length >=t
threshold= int(input("\nEnter the prefix length thresold:"))
print_neighbors(graph,threshold)
print("\nNeighbors printed successfully!")

"""# **Task-3**

3. Given a word as input and hop length n, print the nodes which are n-hop neighbours of the given word. Your program must ask for the inputs from the user.
"""

# Print n-hop neighbors of a given word

def print_n_hop_neighbors(graph,word,n):
  visited=set()
  queue=[(word,0)]
  while queue:
    current_word,hop=queue.pop(0)
    if hop>n:
      break

    if current_word not in visited:
      visited.add(current_word)
      if hop>0:
        print(current_word)
      for neighbor,prefix_len in graph[current_word].items():
        if prefix_len>0 and hop<n:
          queue.append((neighbor,hop+1))

word=input("\nEnter the word:")

  # Check if the entered word exists in the graph
while word not in graph:
    print(f"Word '{word}' not found in the word list.")
    word = input("\nPlease enter a word from the list: ")

n=int(input("\nEnter the hop length:"))

print(f"\nThe {n}-hop neighbors of {word} are:")
print_n_hop_neighbors(graph,word,n)
