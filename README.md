# Social Network Friend Recommendation System
------------------------------------------
Project Description

The Social Network Friend Recommendation System is a Python-based project that uses a graph structure and Breadth-First Search (BFS) to manage social connections and suggest potential friends based on mutual connections. 
------------------------------------------
Features

•Represent Social Network as a Graph  
•Traverse Network using Breadth-First Search (BFS)  
•Calculate Mutual Friends Count  
•Rank Recommendations in Descending Order  
•Prevent Duplicate and Cyclic Node Visits  
•Clean Terminal Output 
------------------------------------------
Data Structure

•Graph (Adjacency List using Dictionary)  
•Queue (collections.deque for BFS traversal)  
•Set (visited set to track visited users)
------------------------------------------
Recommendation Logic

Breadth-First Search (BFS) explores connected users level-by-level to identify users who are not direct friends and calculates their mutual connections. 
------------------------------------------ 
Example:

​Selected User: Vedant  
​Direct Friends: A, B  
​Mutual Connections Calculation:
​Candidate C shares friends A and B --> 2 mutual connections  
​Candidate E shares friend C --> 1 mutual connection  
​Result: Candidate C is ranked first, followed by candidate E.
------------------------------------------
Technology Used
------------------------------------------
•Python  
•Graph Data Structure  
•Breadth-First Search (BFS)  
•Git  
•GitHub 
------------------------------------------
