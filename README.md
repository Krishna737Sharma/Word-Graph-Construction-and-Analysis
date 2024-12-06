# Word Graph Construction and Analysis

This Python program constructs an undirected weighted graph from a list of English words. The graph nodes represent words, and the edges are weighted based on the length of the longest common prefix between two words. The program performs the following tasks:

## Tasks

### 1. Constructing the Graph

The graph is constructed by computing the longest common prefix between each pair of words. The length of the longest common prefix (LCP) is used as the edge weight between two nodes. The graph is undirected, meaning if word A shares an LCP with word B, the edge weight between A and B is the same as between B and A.

#### Example:
For the words **"educate"** and **"education"**, the LCP is **"educate"**, so the edge weight between these two words would be **6** (the length of "educate").

### 2. Finding Neighbors with Threshold

Given a threshold **t** for the longest prefix length, the program will print the number of immediate neighbors (one hop) of each word that has an edge value (LCP length) greater than or equal to **t**.

#### Input:
- **Threshold**: A number specifying the minimum LCP length for valid edges.

#### Output:
A space-separated text file with two columns:
1. **Word**: The word node.
2. **Neighbors**: A list of neighbors that have an edge with weight ≥ threshold.

### 3. Finding N-Hop Neighbors

Given a word and a hop length **n**, the program will print all nodes that are **n-hop** neighbors of the given word. A **n-hop** neighbor is a word that can be reached by traversing exactly **n** edges.

#### Input:
- **Word**: The word node from which to find neighbors.
- **Hop Length (n)**: The number of hops to look for.

#### Output:
A list of **n-hop** neighbors of the given word.

## How to Run

### Prerequisites

Make sure you have Python 3 installed. The program requires no external libraries.

### Running the Program

1. **Prepare the input**: A text file containing one word per line.
2. **Input File Format**:
    - Each word is on a new line in a text file.
    - Example:
      ```
      educate
      education
      example
      export
      ```

3. **Running the Python Script**:
    - The script will prompt you for inputs based on the tasks.
    - Input examples:
      - For Task 2: Enter a threshold value, e.g., `3`.
      - For Task 3: Enter a word and hop length, e.g., `educate 2`.

### Example Usage

```bash
python word_graph.py
