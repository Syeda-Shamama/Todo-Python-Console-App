# Development Plan - Todo App Phase I
**Plan ID:** 002  
**Spec Link:** `specs/001-initial-spec.md`  
**Constitution Link:** `.specify/memory/CONSTITUTION.md`  
**Status:** Not Started  
**Estimated Total Time:** 6-8 hours

## 1. Objective
Build an in-memory command-line todo application following the initial specification and adhering to the project constitution. Implementation uses AI-assisted development (Gemini) with manual validation at each phase.

## 2. Methodology
- **Bottom-up approach**: Data layer → Business logic → Presentation layer
- **Validation gates**: Each phase must pass manual testing before proceeding
- **AI-assisted**: Use Gemini to implement each task based on this plan
- **Documentation**: Log all Gemini prompts and iterations in `GEMINI.md`

## 3. Task Breakdown

### Phase 1: Project Scaffolding & Configuration
*Goal: Establish project structure and dependency management*

| Task ID | Description | Files/Dirs | Time | Risk | Validation |
|---------|-------------|------------|------|------|------------|
| **T-01** | Initialize UV project | `pyproject.toml` | 15min | LOW | `uv --version` works |
| **T-02** | Configure Python 3.13+ | `pyproject.toml` | 10min | LOW | Check `python.version` |
| **T-03** | Create directory structure | `src/`, `src/models/`, `src/storage/`, `src/cli/` | 5min | NONE | Dirs exist |
| **T-04** | Create package `__init__.py` files | `src/__init__.py`, `src/models/__init__.py`, etc. | 5min | NONE | Python imports work |
| **T-05** | Create module skeleton files | `main.py`, `task.py`, `memory_store.py`, `interface.py`, `validators.py` | 10min | NONE | Files exist |
| **T-06** | Setup `.gitignore` | `.gitignore` | 5min | NONE | Excludes `__pycache__/`, `.venv/` |

**Phase Validation:** 
- [ ] UV project initializes without errors
- [ ] Directory structure matches constitution requirements
- [ ] Can import empty modules: `from src.models import task`

**Dependencies:** None  
**Total Phase Time:** ~50 minutes

---

### Phase 2: Core Data Model
*Goal: Implement the Task class with validation*

| Task ID | Description | Implementation Details | Time | Risk | Validation |
|---------|-------------|----------------------|------|------|------------|
| **T-07** | Implement `Task` dataclass | • Use `@dataclass` decorator<br>• Fields: `id: int`, `title: str`, `description: str`, `is_complete: bool`, `created_at: datetime`<br>• Add type hints<br>• Import `datetime` and `dataclasses` | 20min | LOW | Instance created successfully |
| **T-08** | Add `__post_init__` validation | • Validate `1 <= len(title) <= 100`<br>• Validate `len(description) <= 500`<br>• Raise `ValueError` with clear messages | 15min | MEDIUM | Invalid inputs rejected |
| **T-09** | Add `__str__` method | • Format: `"[✓] Title"` or `"[ ] Title"`<br>• Include description if present | 10min | LOW | Print looks correct |
| **T-10** | Add docstrings | • Class docstring (Google style)<br>• Method docstrings | 10min | NONE | Clear documentation |

**Gemini Prompt Template:**
```
Implement the Task class in src/models/task.py according to:
- Specification: [paste T-07 details]
- Constitution requirement: Type hints, docstrings, PEP 8
- Must raise ValueError for invalid title/description lengths
```

**Phase Validation:**
- [ ] Can create Task with valid data
- [ ] ValueError raised for title too short/long
- [ ] ValueError raised for description too long
- [ ] `__str__` displays correctly with checkmark
- [ ] All functions have type hints and docstrings

**Dependencies:** Phase 1  
**Total Phase Time:** ~55 minutes

---

### Phase 3: Storage Layer
*Goal: Implement CRUD operations for in-memory storage*

| Task ID | Description | Implementation Details | Time | Risk | Validation |
|---------|-------------|----------------------|------|------|------------|
| **T-11** | Initialize `MemoryStore` class | • `tasks: list[Task] = []`<br>• `_next_id: int = 1`<br>• Constructor initializes empty list | 10min | LOW | Instance created |
| **T-12** | Implement `add_task()` | • Signature: `add_task(title: str, description: str = "") -> Task`<br>• Create Task with `_next_id`<br>• Increment `_next_id`<br>• Append to list<br>• Return created task | 20min | MEDIUM | Task added with correct ID |
| **T-13** | Implement `get_task()` | • Signature: `get_task(task_id: int) -> Task \| None`<br>• Search list by ID<br>• Return None if not found | 15min | LOW | Returns correct task or None |
| **T-14** | Implement `get_all_tasks()` | • Signature: `get_all_tasks() -> list[Task]`<br>• Return copy of tasks list | 10min | LOW | Returns all tasks |
| **T-15** | Implement `update_task()` | • Signature: `update_task(task_id: int, title: str \| None, description: str \| None) -> bool`<br>• Find task by ID<br>• Update only provided fields<br>• Return True if updated, False if not found | 25min | MEDIUM | Task updates correctly |
| **T-16** | Implement `delete_task()` | • Signature: `delete_task(task_id: int) -> bool`<br>• Remove task from list<br>• Return True if deleted, False if not found | 15min | LOW | Task deleted |
| **T-17** | Implement `toggle_complete()` | • Signature: `toggle_complete(task_id: int) -> bool`<br>• Flip `is_complete` boolean<br>• Return True if toggled, False if not found | 15min | LOW | Status toggles |
| **T-18** | Add helper methods | • `get_complete_tasks() -> list[Task]`<br>• `get_incomplete_tasks() -> list[Task]` | 15min | LOW | Filters work |
| **T-19** | Add docstrings to all methods | • Google style<br>• Include Args, Returns, Raises | 20min | NONE | Well documented |

**Phase Validation:**
- [ ] Can add multiple tasks with auto-incrementing IDs
- [ ] Can retrieve task by ID
- [ ] Returns None for non-existent ID
- [ ] Can update title only, description only, or both
- [ ] Can delete task (ID doesn't reuse)
- [ ] Can toggle completion status
- [ ] Filter methods return correct subsets
- [ ] All methods have type hints and docstrings

**Dependencies:** Phase 2  
**Total Phase Time:** ~2.5 hours

---

### Phase 4: Input Validation
*Goal: Build reusable validation functions*

| Task ID | Description | Implementation Details | Time | Risk | Validation |
|---------|-------------|----------------------|------|------|------------|
| **T-20** | Implement `validate_task_id()` | • Signature: `validate_task_id(input_str: str, store: MemoryStore) -> int \| None`<br>• Try to convert to int<br>• Check if task exists in store<br>• Return int or None | 20min | LOW | Valid/invalid IDs handled |
| **T-21** | Implement `validate_title()` | • Signature: `validate_title(title: str) -> tuple[bool, str]`<br>• Check 1-100 chars<br>• Return (is_valid, error_message) | 15min | LOW | Length checked |
| **T-22** | Implement `validate_description()` | • Signature: `validate_description(desc: str) -> tuple[bool, str]`<br>• Check max 500 chars<br>• Return (is_valid, error_message) | 10min | LOW | Length checked |
| **T-23** | Implement `get_yes_no()` | • Signature: `get_yes_no(prompt: str) -> bool`<br>• Loop until valid y/n input<br>• Return True for yes, False for no | 15min | LOW | Only accepts y/n |
| **T-24** | Add docstrings | • Document all validators | 10min | NONE | Clear docs |

**Phase Validation:**
- [ ] Valid task ID returns integer
- [ ] Invalid task ID returns None
- [ ] Title validation catches too short/long
- [ ] Description validation catches too long
- [ ] Yes/no prompt loops on invalid input
- [ ] All functions documented

**Dependencies:** Phase 3  
**Total Phase Time:** ~1 hour

---

### Phase 5: CLI Interface
*Goal: Build user-facing command handlers*

| Task ID | Description | Implementation Details | Time | Risk | Validation |
|---------|-------------|----------------------|------|------|------------|
| **T-25** | Implement `handle_add_task()` | • Signature: `handle_add_task(store: MemoryStore) -> None`<br>• Prompt for title (loop until valid)<br>• Prompt for description (optional)<br>• Call `store.add_task()`<br>• Print success message with ID | 30min | MEDIUM | Task added successfully |
| **T-26** | Implement `handle_list_tasks()` | • Signature: `handle_list_tasks(store: MemoryStore) -> None`<br>• Get all tasks<br>• Format as per spec: numbered, checkmarks<br>• Show "No tasks" if empty<br>• Show count summary | 30min | MEDIUM | Displays correctly |
| **T-27** | Implement `handle_update_task()` | • Prompt for task ID (validate)<br>• Show current values<br>• Prompt for new values (Enter to skip)<br>• Call `store.update_task()`<br>• Handle task not found | 40min | HIGH | Updates work, errors handled |
| **T-28** | Implement `handle_delete_task()` | • Prompt for task ID<br>• Show task title<br>• Confirm with yes/no<br>• Call `store.delete_task()`<br>• Handle task not found | 25min | MEDIUM | Deletion confirmed |
| **T-29** | Implement `handle_toggle_complete()` | • Prompt for task ID<br>• Call `store.toggle_complete()`<br>• Show new status<br>• Handle task not found | 20min | LOW | Toggle works |
| **T-30** | Implement `show_menu()` | • Print menu options 1-6<br>• Include command names | 10min | NONE | Menu displays |
| **T-31** | Add error handling to all handlers | • Try-except blocks<br>• User-friendly error messages | 20min | MEDIUM | No crashes |

**Phase Validation:**
- [ ] Add task: prompts work, validation works, success message shown
- [ ] List tasks: empty list handled, formatting correct, summary shown
- [ ] Update task: shows defaults, accepts Enter to skip, updates correctly
- [ ] Delete task: shows confirmation, cancellation works, deletion works
- [ ] Toggle: status changes and displays correctly
- [ ] All errors show friendly messages

**Dependencies:** Phase 4  
**Total Phase Time:** ~2.5 hours

---

### Phase 6: Main Application
*Goal: Wire everything together*

| Task ID | Description | Implementation Details | Time | Risk | Validation |
|---------|-------------|----------------------|------|------|------------|
| **T-32** | Implement `main()` function | • Create `MemoryStore` instance<br>• `while True` loop<br>• Show menu<br>• Get user input<br>• Route to handlers with if/elif<br>• Handle "exit" command | 30min | HIGH | App runs without errors |
| **T-33** | Add input validation in main loop | • Validate menu choice is 1-6<br>• Show error for invalid input<br>• Don't crash on any input | 15min | MEDIUM | Invalid input handled |
| **T-34** | Add `if __name__ == "__main__"` | • Call `main()` | 5min | NONE | App starts |
| **T-35** | Add welcome message | • Show app title<br>• Brief instructions | 10min | NONE | Looks professional |

**Phase Validation:**
- [ ] App starts without errors
- [ ] Menu displays and loops
- [ ] All 5 features accessible from menu
- [ ] Exit command works cleanly
- [ ] Invalid menu choices handled gracefully

**Dependencies:** Phase 5  
**Total Phase Time:** ~1 hour

---

### Phase 7: Testing & Documentation
*Goal: Verify all requirements met*

| Task ID | Description | Checklist Location | Time | Validation |
|---------|-------------|-------------------|------|------------|
| **T-36** | Execute manual test checklist | `specs/001-initial-spec.md` Section 9 | 45min | All tests pass |
| **T-37** | Create `README.md` | • Project description<br>• Setup with UV<br>• How to run<br>• Feature list<br>• Example usage | 30min | Clear instructions |
| **T-38** | Create `GEMINI.md` | • Document all prompts used<br>• Note iterations/fixes<br>• Lessons learned | 20min | Complete log |
| **T-39** | Final code review | • Check PEP 8 compliance<br>• Verify all type hints present<br>• Verify all docstrings present<br>• Check constitution compliance | 30min | Passes all standards |

**Phase Validation:**
- [ ] All 14 manual tests pass
- [ ] README allows new user to run app
- [ ] GEMINI.md documents development process
- [ ] Code meets constitution standards

**Dependencies:** Phase 6  
**Total Phase Time:** ~2 hours

---

## 4. Risk Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Invalid user input crashes app | HIGH | HIGH | Comprehensive try-except blocks in Phase 5 |
| Task ID logic fails (duplicate IDs) | MEDIUM | HIGH | Thorough testing of `_next_id` in Phase 3 |
| Update logic overwrites with empty values | MEDIUM | MEDIUM | Careful None checking in T-15 |
| Gemini generates non-compliant code | MEDIUM | LOW | Manual review against constitution after each task |

## 5. Rollback Strategy

If a task fails validation:
1. Document the failure in `GEMINI.md`
2. Revise the Gemini prompt with more specific requirements
3. Re-implement the task
4. If still failing after 3 attempts, escalate for human debugging

## 6. Dependencies
- **Runtime:** Python 3.13+
- **Package Manager:** UV
- **AI Assistant:** Gemini (any interface)
- **Version Control:** Git

## 7. Success Criteria

✅ All 7 phases completed  
✅ All phase validations passed  
✅ 14/14 manual tests passed  
✅ Constitution compliance verified  
✅ Documentation complete (README + GEMINI.md)  
✅ Code pushed to GitHub  

## 8. Estimated Timeline

- **Best case:** 6 hours (everything works first try)
- **Expected:** 8 hours (some iterations needed)
- **Worst case:** 12 hours (multiple debugging sessions)

---

**Ready for Implementation:** ✓ Yes  
**Next Step:** Begin Phase 1 - Task T-01