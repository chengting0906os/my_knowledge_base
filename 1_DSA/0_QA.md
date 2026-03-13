# DSA Interview Q&A

---

## Array

1. What is the difference between an array and a linked list?
   陣列和鏈結串列的差異是什麼？
   <details>
   <summary>Answer</summary>

   | | Array | Linked List |
   |---|---|---|
   | Memory | Contiguous | Scattered (pointers) |
   | Access by index | O(1) | O(n) |
   | Insert / Delete at middle | O(n) (shift) | O(1) given the node |
   | Cache friendliness | High (spatial locality) | Low (pointer chasing) |

   </details>

2. When would you use an array vs a linked list?
   什麼情況下選 array，什麼情況下選 linked list？
   <details>
   <summary>Answer</summary>

   - **Array**: frequent random access, fixed or predictable size, cache-sensitive code
   - **Linked List**: frequent insert/delete in the middle, dynamic size, no random access needed

   </details>

3. How does a dynamic array (e.g., Python list) resize?
   動態陣列（如 Python list）如何做 resize？
   <details>
   <summary>Answer</summary>

   - **Grow**: when full → allocate 1.5x~2x capacity → copy all elements → free old array
   - **Shrink**: when < 1/4 full → resize to 1/2 capacity (prevents thrashing)
   - Amortized O(1) per append because the expensive copy happens rarely

   </details>

4. Why is array access O(1)?
   為什麼陣列的 access 是 O(1)？
   <details>
   <summary>Answer</summary>

   Contiguous memory + fixed element size → `address = base + index × element_size`
   Direct calculation, no traversal needed.

   </details>

5. What is cache locality and why are arrays cache-friendly?
   什麼是 cache locality？為什麼 array 比 linked list 更 cache-friendly？
   <details>
   <summary>Answer</summary>

   - CPU loads 64-byte cache lines at a time. Array elements sit adjacently → next element is already in cache (spatial locality)
   - Linked List nodes are scattered in heap memory → each pointer dereference risks a cache miss → slower in practice even when complexity is equal

   </details>

6. How would you find duplicates in an array?
   如何找出陣列中的重複元素？
   <details>
   <summary>Answer</summary>

   - **HashSet**: iterate array, check if element exists in set → O(n) time, O(n) space
   - **No extra space**: sort first O(n log n), then compare adjacent elements
   - **Sorted array**: just check `nums[i] == nums[i+1]`

   </details>

7. How would you rotate an array by k positions?
   如何將陣列向右旋轉 k 格？
   <details>
   <summary>Answer</summary>

   - **Slicing** (Python): `nums[-k:] + nums[:-k]` → O(n) time, O(n) space
   - **Three-reverse** (in-place): reverse all → reverse first k → reverse rest → O(n) time, O(1) space

   </details>

8. How would you find the missing number in [0..n]?
   如何找出 [0..n] 中缺少的數字？
   <details>
   <summary>Answer</summary>

   - **Math** (optimal): `n*(n+1)/2 - sum(nums)` → O(n) time, O(1) space
   - **Counter**: count each number, find the one with count 0 → O(n) time, O(n) space

   </details>

9. How would you move all zeros to the end while keeping relative order?
   如何將所有 0 移到陣列末端，同時保持非零元素的相對順序？
   <details>
   <summary>Answer</summary>

   Two pointers: `slow` tracks the next write position, `fast` scans. When `fast` finds a non-zero, write it to `slow` and advance both. Fill rest with zeros. O(n), O(1).

   </details>

10. How would you find the maximum subarray sum?
    如何找出最大子陣列的總和？
    <details>
    <summary>Answer</summary>

    **Kadane's Algorithm**: `curr = max(num, curr + num)`, `best = max(best, curr)` → O(n), O(1)

    Key insight: extend the current subarray only if it improves the sum; otherwise start fresh.

    </details>

11. How would you find the intersection of two arrays?
    如何找出兩個陣列的交集？
    <details>
    <summary>Answer</summary>

    - **Set**: `list(set(a) & set(b))` → O(n+m) time
    - **Both sorted**: two pointers, advance the pointer pointing to the smaller value → O(n+m) time, O(1) space

    </details>

12. How would you merge two sorted arrays in-place?
    如何 in-place 合併兩個已排序的陣列？
    <details>
    <summary>Answer</summary>

    Fill from the back to avoid overwriting. Two pointers starting at the end of each valid range, write the larger element to the back of the result array. O(n+m), O(1).

    </details>

---

## String

1. Are strings mutable or immutable in Python/Java?
   Python / Java 的字串是 mutable 還是 immutable？
   <details>
   <summary>Answer</summary>

   Both are **immutable** — every modification creates a new string object.
   In Python, `str += "x"` allocates a new string each time.

   </details>

2. What's the time complexity of string concatenation in a loop?
   在迴圈中做字串串接，時間複雜度是多少？
   <details>
   <summary>Answer</summary>

   - `+=` in a loop: O(n²) — each concatenation copies the entire string so far
   - Use `''.join(list)` → O(n)

   </details>

3. How would you check if a string is a palindrome?
   如何判斷一個字串是否為回文？
   <details>
   <summary>Answer</summary>

   Two pointers from both ends, compare until they meet → O(n), O(1)

   </details>

4. How would you find all anagrams of a pattern in a string?
   如何找出字串中所有與 pattern 同字母異序的子字串？
   <details>
   <summary>Answer</summary>

   Sliding window + frequency counter. Compare window counter to pattern counter; advance window one char at a time → O(n), O(1) (fixed alphabet size)

   </details>

---

## Linked List

1. How do you detect a cycle in a linked list?
   如何偵測 linked list 中是否有環？
   <details>
   <summary>Answer</summary>

   **Floyd's algorithm**: slow moves 1 step, fast moves 2. If they meet → cycle exists. O(n), O(1).

   </details>

2. How do you find the start of the cycle?
   如何找到環的起始節點？
   <details>
   <summary>Answer</summary>

   After slow and fast meet inside the cycle, reset one pointer to `head`. Move both 1 step at a time — they meet exactly at the cycle start. (Mathematical property of Floyd's algorithm.)

   </details>

3. How do you reverse a linked list?
   如何反轉一個 linked list？
   <details>
   <summary>Answer</summary>

   ```python
   prev, curr = None, head
   while curr:
       nxt = curr.next
       curr.next = prev
       prev = curr
       curr = nxt
   return prev
   ```

   O(n), O(1).

   </details>

4. What's the difference between singly and doubly linked list?
   singly linked list 和 doubly linked list 的差異是什麼？
   <details>
   <summary>Answer</summary>

   - **Singly**: one `next` pointer → O(n) delete without predecessor reference, less memory
   - **Doubly**: `prev` + `next` → O(1) delete given the node, 2× memory per node

   </details>

5. How do you find the middle of a linked list?
   如何找到 linked list 的中間節點？
   <details>
   <summary>Answer</summary>

   Slow/fast pointers: slow moves 1 step, fast moves 2. When fast reaches the end, slow is at the middle. O(n), O(1).

   </details>

---

## Stack

1. What data structures can implement a stack?
   可以用哪些資料結構實作 stack？
   <details>
   <summary>Answer</summary>

   - **Dynamic array**: append/pop from end → O(1) amortized
   - **Linked list**: push/pop at head → O(1) strict

   </details>

2. When would you use a stack?
   什麼情況下會用到 stack？
   <details>
   <summary>Answer</summary>

   Balanced parentheses, undo/redo, DFS (iterative), function call tracking, monotonic stack problems (next greater element, histogram area)

   </details>

3. How do you implement a queue using two stacks?
   如何用兩個 stack 實作 queue？
   <details>
   <summary>Answer</summary>

   - **inbox**: all pushes go here
   - **outbox**: all pops come from here; if empty, pour all from inbox → outbox

   Amortized O(1) per operation — each element is moved at most once.

   </details>

---

## Queue

1. What is FIFO?
   什麼是 FIFO？
   <details>
   <summary>Answer</summary>

   First In, First Out — the first element enqueued is the first to be dequeued.

   </details>

2. What's the difference between queue and deque?
   queue 和 deque 的差異是什麼？
   <details>
   <summary>Answer</summary>

   - **Queue**: insert at back, remove from front
   - **Deque**: insert/remove at both ends in O(1) — superset of queue

   </details>

3. When would you use a deque over a queue?
   什麼情況下選 deque 而不是 queue？
   <details>
   <summary>Answer</summary>

   When you need O(1) operations at both ends — e.g., sliding window maximum, palindrome checking.

   Python's `collections.deque` is a doubly linked list of fixed-size blocks: O(1) at both ends, O(n) random access.

   </details>

---

## Hashing

1. How does a hash map work internally?
   Hash map 內部是如何運作的？
   <details>
   <summary>Answer</summary>

   - Key → hash function → index in backing array → store `(key, value)` at that bucket
   - Average O(1) get/set; worst case O(n) if all keys collide
   - When load factor exceeds threshold → rehash (allocate new array, reinsert all entries)

   </details>

2. What is a hash collision and how is it resolved?
   什麼是 hash collision？如何解決？
   <details>
   <summary>Answer</summary>

   A collision occurs when two different keys produce the same hash index.

   **Chaining**: each bucket holds a linked list (or dynamic array) of all entries at that index
   - Simple, works well even at high load factors
   - Extra memory per entry; pointer chasing hurts cache performance

   **Open addressing**: on collision, probe for the next empty slot within the array
   - **Linear probing**: `(h + i) % n` — cache-friendly, but causes primary clustering
   - **Quadratic probing**: `(h + i²) % n` — reduces clustering
   - **Double hashing**: `(h + i × h2) % n` — best distribution, two hash functions

   </details>

3. What is load factor and why does it matter?
   什麼是 load factor？為什麼它很重要？
   <details>
   <summary>Answer</summary>

   `load factor = number of entries / number of buckets`

   - High load → more collisions → longer chains or more probing steps → slower ops
   - Python dict rehashes at ~⅔ load; Java HashMap at 0.75
   - Rehashing: allocate new array (2×) → recompute all hashes → reinsert all entries → O(n) one-time cost, amortized O(1) per insert

   </details>

4. What is overflow in hash tables?
   Hash table 的 overflow 是什麼？如何處理？
   <details>
   <summary>Answer</summary>

   - In **fixed-size bucket** schemes: overflow happens when a bucket's capacity is exceeded
   - In **chaining**: no hard overflow — the chain just grows, but performance degrades
   - In **open addressing**: if load factor approaches 1, no empty slots remain → must rehash before it fills completely
   - Resolution: rehash proactively before overflow, or use chaining to avoid hard limits

   </details>

5. What makes a good hash function?
   一個好的 hash function 需要具備哪些特性？
   <details>
   <summary>Answer</summary>

   - **Deterministic**: same key always produces same hash
   - **Uniform distribution**: keys spread evenly across buckets, minimizing collisions
   - **Fast to compute**: O(1) ideally
   - **Avalanche effect**: small change in key → large change in hash (avoids clustering)

   Bad hash example: `hash(key) = key % 10` — all multiples of 10 collide in bucket 0.

   </details>

6. Why can't mutable objects be dictionary keys in Python?
   為什麼 Python dict 的 key 不能是 mutable 物件？
   <details>
   <summary>Answer</summary>

   Keys must be hashable (immutable). If a key mutates after insertion, its hash value changes — the map looks in the wrong bucket and can no longer find the entry. Python enforces this by requiring `__hash__` and `__eq__` to be consistent: lists/dicts are unhashable, tuples/strings are hashable.

   </details>

7. What is the worst-case time complexity of hash map operations and when does it occur?
   Hash map 操作的最壞情況時間複雜度是多少？什麼時候會發生？
   <details>
   <summary>Answer</summary>

   O(n) — when all keys hash to the same bucket (adversarial input or poor hash function), the structure degenerates to a linear scan of one long chain. Modern implementations use randomized hashing or tree-backed buckets (Java HashMap uses red-black trees when chain length > 8) to limit worst-case to O(log n).

   </details>

8. What's the difference between HashMap and HashSet?
   HashMap 和 HashSet 的差異是什麼？
   <details>
   <summary>Answer</summary>

   - **HashMap**: stores key→value pairs
   - **HashSet**: stores keys only (internally a HashMap with dummy values); used for O(1) membership tests, deduplication

   </details>

9. How does Python's dict maintain insertion order?
   Python dict 如何維持插入順序？
   <details>
   <summary>Answer</summary>

   Since Python 3.7, `dict` uses a compact array that stores keys in insertion order, plus a separate sparse hash table for O(1) lookups. Iteration follows the compact array, giving guaranteed insertion-order traversal.

   </details>

---

## Graph

1. What are the main ways to represent a graph, and how do you choose?
   圖有哪些主要的表示法？如何選擇？
   <details>
   <summary>Answer</summary>

   | Representation | Space | Edge check (u,v) | Neighbor iteration | Use when |
   |---|---|---|---|---|
   | Adjacency List | O(n+E) | O(degree) | O(1) | Default — sparse graphs |
   | Adjacency Matrix | O(n²) | O(1) | O(n) | Dense graphs, frequent edge checks |
   | Edge List | O(E) | O(E) | O(E) | Edge-centric algorithms (Kruskal) |

   </details>

2. What is the difference between directed and undirected graphs?
   有向圖和無向圖的差異是什麼？
   <details>
   <summary>Answer</summary>

   - **Directed (digraph)**: edges have direction; u→v does not imply v→u
   - **Undirected**: edges are bidirectional; stored as both `graph[u].append(v)` and `graph[v].append(u)`

   </details>

3. What is the difference between BFS and DFS, and when do you use each?
   BFS 和 DFS 的差異是什麼？各自適用什麼情境？
   <details>
   <summary>Answer</summary>

   | | BFS | DFS |
   |---|---|---|
   | Data structure | Queue | Stack / recursion |
   | Traversal order | Level by level | Depth-first |
   | Shortest path (unweighted) | Yes | No |
   | Space | O(width) | O(depth) |

   - **BFS**: shortest path, level-order, spreading problems (infection, water flow)
   - **DFS**: cycle detection, topological sort, connected components, backtracking/maze

   </details>

4. How do you detect a cycle in a directed graph?
   如何偵測有向圖中的環？
   <details>
   <summary>Answer</summary>

   DFS with 3-color marking:
   - **WHITE**: unvisited
   - **GRAY**: currently in the DFS path (in-progress)
   - **BLACK**: fully processed

   If DFS reaches a **GRAY** node → back edge → cycle exists.

   </details>

5. How do you detect a cycle in an undirected graph?
   如何偵測無向圖中的環？
   <details>
   <summary>Answer</summary>

   - **DFS**: if you reach a visited node that isn't the direct parent → cycle
   - **Union-Find**: if both endpoints of an edge are already in the same component → adding the edge creates a cycle

   </details>

6. What is topological sort and when can you use it?
   什麼是拓撲排序？什麼情況下可以使用？
   <details>
   <summary>Answer</summary>

   A linear ordering of nodes in a **DAG** (Directed Acyclic Graph) such that for every edge u→v, u appears before v. Only valid if no cycles exist.

   **Kahn's algorithm (BFS)**:
   1. Compute in-degree of all nodes
   2. Enqueue all nodes with in-degree 0
   3. Process queue: dequeue u, for each neighbor v decrement in-degree; if 0, enqueue v
   4. If result length < n → cycle exists

   **DFS-based**: push to stack after all descendants are visited; reverse the stack.

   Use cases: build systems, course prerequisites, dependency resolution.

   </details>

7. What is Dijkstra's algorithm and when does it fail?
   Dijkstra 演算法是什麼？什麼情況下會失效？
   <details>
   <summary>Answer</summary>

   Greedy shortest path from a source node using a min-heap.
   - Time: O((V + E) log V)
   - **Fails with negative edge weights** — a greedy choice can be invalidated later
   - Use **Bellman-Ford** for negative weights (O(VE)); use **SPFA** as a practical optimization

   </details>

8. What is the difference between a tree and a graph?
   tree 和 graph 的差異是什麼？
   <details>
   <summary>Answer</summary>

   - **Tree**: connected, acyclic, undirected graph; n nodes, exactly n−1 edges; unique path between any two nodes
   - **Graph**: may have cycles, disconnected components, multiple paths between nodes

   A tree is a special case of a graph.

   </details>

9. What is a connected component?
   什麼是連通分量（connected component）？
   <details>
   <summary>Answer</summary>

   A maximal subgraph where every node is reachable from every other node.

   Find all components: BFS/DFS from each unvisited node (O(n+E)), or Union-Find (nearly O(n+E) with path compression + union by rank).

   </details>

10. What is Union-Find (Disjoint Set Union)?
    什麼是 Union-Find（並查集）？
    <details>
    <summary>Answer</summary>

    Tracks which nodes belong to the same component with near-O(1) operations:

    - `find(x)`: returns the root of x's component; **path compression** flattens the tree → amortized O(α(n))
    - `union(x, y)`: merges two components; **union by rank** keeps the tree flat

    Use cases: cycle detection, Kruskal's MST, connected components, network connectivity.

    ```python
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # path compression
        return parent[x]

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False  # already connected (cycle)
        if rank[rx] < rank[ry]:
            rx, ry = ry, rx
        parent[ry] = rx
        if rank[rx] == rank[ry]:
            rank[rx] += 1
        return True
    ```

    </details>

11. What is a Minimum Spanning Tree (MST)?
    什麼是最小生成樹（MST）？
    <details>
    <summary>Answer</summary>

    A spanning tree (connects all n nodes with n−1 edges, no cycles) with minimum total edge weight.

    - **Kruskal's**: sort all edges by weight, greedily add edge if it doesn't create a cycle (Union-Find) → O(E log E)
    - **Prim's**: grow MST from a start node using a min-heap, always pick the cheapest edge crossing the cut → O(E log V)

    Kruskal works better on sparse graphs (edge-centric), Prim on dense graphs (node-centric).

    </details>

12. What is Bellman-Ford and when do you use it over Dijkstra?
    什麼是 Bellman-Ford？什麼時候用它而不是 Dijkstra？
    <details>
    <summary>Answer</summary>

    Shortest path algorithm that handles **negative edge weights**.

    - Relax all edges V−1 times → guarantees shortest paths for graphs without negative cycles
    - Run one more pass: if any edge still relaxes → **negative cycle** exists
    - Time: O(VE) — slower than Dijkstra O((V+E) log V)

    Use when: graph has negative weights, or you need to detect negative cycles.

    </details>
