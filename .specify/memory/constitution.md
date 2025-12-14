# Todo App Constitution

## Project Identity
**Name:** Todo Console Application - Phase I  
**Purpose:** In-memory command-line task management system  
**Tech Stack:** Python 3.13+, UV package manager

## Core Principles

### 1. Development Philosophy
- Spec-driven development: Write spec → Generate plan → Implement
- No manual coding without specification
- AI-assisted implementation (using Gemini)
- Iterative refinement based on testing

### 2. Technical Constraints
- **Python Version:** 3.13+ only
- **Package Manager:** UV (no pip, no poetry)
- **Storage:** In-memory only (no files, no databases)
- **Interface:** Command-line only (no GUI, no web)
- **Dependencies:** Minimal (prefer standard library)

### 3. Code Quality Standards
- **Style Guide:** PEP 8 compliance mandatory
- **Type Safety:** Type hints required for all functions
- **Documentation:** Docstrings required (Google style)
- **Function Size:** Maximum 50 lines per function
- **Module Size:** Maximum 300 lines per file
- **Error Handling:** Explicit exception handling, no silent failures

### 4. Project Structure
```
src/
├── models/      # Data models (Task class)
├── storage/     # In-memory storage manager
├── cli/         # CLI interface and commands
└── main.py      # Entry point
```

### 5. User Experience
- Clear, friendly error messages
- Confirmation prompts for destructive actions (delete)
- Colored output for better readability (optional)
- Input validation on all user inputs

### 6. Testing Requirements
- Manual testing checklist for all features
- Edge case testing (empty lists, invalid IDs, etc.)
- User acceptance testing before completion

## Non-Negotiables
❌ No external databases  
❌ No file persistence in Phase I  
❌ No third-party CLI frameworks (use argparse/click only)  
❌ No skipping type hints  
❌ No commits without testing

## Success Criteria
✅ All 5 CRUD operations work flawlessly  
✅ Clean, readable code structure  
✅ Comprehensive README and documentation  
✅ Spec history properly maintained  
✅ Zero runtime errors on valid inputs


