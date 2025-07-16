# **To-Do List Project (Python)**  

## **Project Description**  
Students will build a **command-line To-Do List application** in Python. The program will allow users to **add, delete, and manage tasks**, with data persistence (saving tasks to a file).  

---

## **Functional Requirements**  

### **Core Features**  
✅ **Add a task**  
- Command: `add "Task Description"`  
- Example:  
  ```bash
  > add "Buy groceries"
  [SUCCESS] Task "Buy groceries" added (ID:1)
  ```  

✅ **Delete a task**  
- Command: `del <task_id>`  
- Example:  
  ```bash
  > del 1
  [SUCCESS] Task 1 deleted.
  ```  

✅ **List all tasks**  
- Command: `list`  
- Example output:  
  ```bash
  > list
  TODO LIST:
  ----------------------------
  1. [ ] Buy groceries (2024-03-10 14:30)  
  2. [✓] Finish homework (2024-03-10 15:00)  
  ----------------------------
  Total: 2 tasks (1 completed)
  ```  

✅ **Mark a task as done**  
- Command: `done <task_id>`  
- Example:  
  ```bash
  > done 1
  [SUCCESS] Task 1 marked as done.
  ```  

✅ **Exit & Save**  
- Command: `exit`  
- The program should save tasks to `todo.txt` before exiting.  

---

### **Advanced Features (Bonus)**  
🔹 **Filter tasks**  
- `list active` → Show only incomplete tasks  
- `list completed` → Show only completed tasks  

🔹 **Edit a task**  
- `edit <task_id> "New Description"` → Update task text  

🔹 **Clear all tasks**  
- `clear` → Delete all tasks  

🔹 **Task expiration warning**  
- If a task is **older than 3 days** and incomplete, mark it with `[!]` (e.g., `1. [!] Buy groceries`).  

---

## **File Storage Format (`todo.txt`)**  
The program should save tasks in the following format:  
```plaintext
ID,Status,Description,Added_Time
1,0,Buy groceries,2024-03-10 14:30
2,1,Finish homework,2024-03-10 15:00
```  
- **Status**: `1` = Done, `0` = Pending  
- **Time Format**: `YYYY-MM-DD HH:MM`  

---

## **Error Handling**  
The program should handle invalid inputs gracefully:  
- `del 99` → `[ERROR] Task 99 does not exist.`  
- `add` (no description) → `[ERROR] Usage: add "Task Description"`  
- `done abc` → `[ERROR] Task ID must be a number.`  

---

## **Sample Input/Output**  

### **Example Workflow**  
```bash
> add "Study Python"
[SUCCESS] Task "Study Python" added (ID:1)

> add "Go to the gym"
[SUCCESS] Task "Go to the gym" added (ID:2)

> list
TODO LIST:
----------------------------
1. [ ] Study Python (2024-03-10 16:00)  
2. [ ] Go to the gym (2024-03-10 16:05)  
----------------------------
Total: 2 tasks (0 completed)

> done 1
[SUCCESS] Task 1 marked as done.

> del 2
[SUCCESS] Task 2 deleted.

> exit
[INFO] Saved 1 task to todo.txt. Goodbye!
```

---

## **Grading Criteria**  
| Feature               | Points | Notes |
|-----------------------|--------|-------|
| **Add Task**          | 20     | Supports spaces in description |
| **Delete Task**       | 15     | Handles invalid IDs |
| **List Tasks**        | 20     | Proper formatting (status/time) |
| **Mark as Done**      | 10     | Updates task status |
| **Save/Load Tasks**   | 20     | Uses `todo.txt` correctly |
| **Error Handling**    | 15     | Handles 5+ error cases |
| **Bonus Features**    | +10 each | Up to 30 extra points |

---

## **How to Submit**  
1. **Fork** this repository.  
2. Implement the To-Do List app in Python.  
3. Ensure your code:  
   - Follows **PEP 8** style guidelines.  
   - Includes **comments** explaining key logic.  
   - Works with the commands specified above.  
4. **Push your code** and create a **Pull Request** for review.  

---

### **Tips for Success**  
- Use functions to organize code (e.g., `add_task()`, `delete_task()`).  
- Test edge cases (e.g., empty task list, invalid inputs).  
- Refer to Python’s `datetime` module for timestamps.  

Good luck! 🚀  

--- 
