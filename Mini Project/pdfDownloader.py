from reportlab.lib.pagesizes import A4 # type: ignore
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch

# Create PDF
pdf_path = "/mnt/data/DSA_Pattern_Recognition_FAANG.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=A4)
styles = getSampleStyleSheet()
story = []

# Title
story.append(Paragraph("<b>DSA Pattern Recognition Guide (FAANG / LeetCode Preparation)</b>", styles["Title"]))
story.append(Spacer(1, 0.2 * inch))

# Content (shortened version for PDF readability)
patterns = [
    ("Two Pointers", "Use for comparing elements from both ends efficiently. Example: Pair Sum, Valid Palindrome, 3Sum."),
    ("Sliding Window", "Use for subarrays/substrings problems. Example: Longest Substring Without Repeating Characters."),
    ("Fast & Slow Pointers", "Used for cycle detection and linked list middle finding."),
    ("Prefix Sum", "For range-sum or cumulative calculations. Example: Subarray Sum Equals K."),
    ("Binary Search", "Use when data or condition is sorted/monotonic. Example: Search in Rotated Sorted Array."),
    ("Sorting + Greedy", "Combine sorting with local optimization. Example: Merge Intervals, Meeting Rooms."),
    ("Linked List Manipulation", "For reversing, merging, and deleting nodes efficiently."),
    ("Stack / Monotonic Stack", "Use for next greater element or valid parentheses problems."),
    ("HashMap", "For quick lookups or frequency counts. Example: Two Sum, Group Anagrams."),
    ("Greedy", "Local optimum → global optimum. Example: Jump Game, Gas Station."),
    ("Backtracking", "Used for exploring all combinations or subsets. Example: N-Queens, Sudoku Solver."),
    ("Divide & Conquer", "Split → Solve → Merge. Example: Merge Sort, Maximum Subarray."),
    ("Dynamic Programming", "For overlapping subproblems and optimal substructure. Example: Knapsack, LCS, Coin Change."),
    ("Graph Traversal", "Use BFS/DFS for connectivity. Example: Number of Islands, Course Schedule."),
    ("Heap", "For top-k or stream problems. Example: Kth Largest, Merge K Lists."),
    ("Union-Find", "Detect connected components or cycles. Example: Redundant Connection."),
    ("Trie", "Prefix-based problems. Example: Word Search II."),
    ("Bit Manipulation", "Optimize with bitwise ops. Example: Single Number, Counting Bits."),
    ("Intervals", "Time range management. Example: Merge Intervals, Meeting Rooms II."),
    ("Topological Sort", "Ordering tasks with dependencies. Example: Course Schedule, Alien Dictionary.")
]

for title, desc in patterns:
    story.append(Paragraph(f"<b>{title}</b>: {desc}", styles["Normal"]))
    story.append(Spacer(1, 0.1 * inch))

# Strategy section
story.append(Spacer(1, 0.3 * inch))
story.append(Paragraph("<b>Strategy to Master These Patterns</b>", styles["Heading2"]))
story.append(Paragraph("""
1. Learn the pattern logic.<br/>
2. Solve 3–5 base problems per pattern.<br/>
3. Progress to medium-hard variants.<br/>
4. Keep a pattern-wise notes journal.<br/>
5. Mix topics in mock contests for FAANG interview simulation.
""", styles["Normal"]))

doc.build(story)

pdf_path # type: ignore
