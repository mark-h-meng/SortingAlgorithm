* **various sorting algorithms** (e.g. Heap Sort, Insertion Sort, Merge Sort, Selection Sort) (mainly on the time complexity) 
 * **Heap Sort** - O(nlgn), Unstable, very memory saving because of in-place sorting
  * BEST CHOICE when YOU CARE ABOUT THE WORST CASE & IN PLACE SORTING
 * **Quick Sort** - O(nlgn), Unstable, O(n^2) worst
  * BEST CHOICE when YOU JUST WANT A AVG FAST SORTING
 * **Merge Sort** - O(nlgn), Stable, O(n) in memory
  * BEST CHOICE when YOU NEED A STABLE SORTING
 * **Insertion Sort** (**Stable**, O(n) if best) -- **The best choice for normal sorting**
 * **Selection Sort** O(n^2) -- lots of add/remove -- suitable for linked list
  * Each round of loop it search the minimum
 * **Bubble Sort** O(n^2)
  * Each round of loop it search the maximum