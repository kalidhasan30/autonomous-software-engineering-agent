# Autonomous Software Engineering & Code Review Agent

An AI-powered autonomous software engineering agent for code analysis, bug detection, security analysis, test generation, automated fixing, and verification.

---

## 🚀 Overview

The **Autonomous Software Engineering & Code Review Agent** is a Python-based academic project that uses a locally running Large Language Model (LLM) to automate common software engineering and code review activities.

The system analyzes a software project, identifies potential bugs and security issues, generates tests, executes them, and can automatically apply AI-generated fixes when tests fail.

The project uses **Ollama** with **Qwen2.5-Coder 7B** for AI-powered code analysis and automated fixing.

---

## ✨ Key Features

### 🔍 Code Understanding

The Code Understanding Agent analyzes the project and identifies:

- Programming languages
- Important source files
- Functions and classes
- Code relationships
- Potential areas that require investigation
- General architecture observations

### 🐛 Bug Detection

The Bug Detection Agent analyzes source code for potential:

- Logic errors
- Incorrect conditions
- Exception handling issues
- Edge-case problems
- Type-related issues
- Resource-related issues
- API usage problems

### 🔐 Security Analysis

The Security Analysis Agent checks source code for common security concerns, including:

- SQL injection
- Command injection
- Cross-site scripting (XSS)
- Path traversal
- Hardcoded secrets
- Insecure authentication
- Broken authorization
- Unsafe file operations
- Sensitive information exposure
- Weak cryptography
- Unsafe input handling

### 🧪 Test Generation

The Test Generation Agent generates test cases covering:

- Normal behavior
- Edge cases
- Invalid inputs
- Boundary conditions
- Exception handling
- Business logic

### ▶️ Automated Test Execution

The system executes tests using **Pytest** and determines whether the tests pass or fail.

Test results are then used by the automated fixing process when failures are detected.

### 🔧 Automated Bug Fixing

When tests fail, the system provides the source code and test failure information to the AI model.

The AI analyzes the failure and generates a corrected version of the source code.

The generated fix is then applied and tested again.

### ✅ Post-Fix Verification

After applying an AI-generated fix, the system executes the tests again to verify whether the issue has been resolved successfully.

---

## 🔄 System Workflow

```text
Repository / Project
        │
        ▼
Code Understanding
        │
        ├───────────────┐
        ▼               ▼
Bug Detection     Security Analysis
        │               │
        └───────┬───────┘
                ▼
        Test Generation
                │
                ▼
          Test Execution
                │
          ┌─────┴─────┐
          │           │
        PASS         FAIL
          │           │
          ▼           ▼
       Complete    Auto Fix
                      │
                      ▼
              Post-Fix Verification
                      │
                      ▼
                   Complete
🧠 AI Model

This project uses a locally running Large Language Model through Ollama.

Model
Qwen2.5-Coder 7B

Using a local model allows the project to perform AI-assisted code analysis without depending on a cloud-based AI API.

🛠️ Technologies Used
Technology	Purpose
Python	Core programming language
Ollama	Local LLM runtime
Qwen2.5-Coder 7B	AI code analysis and fixing
Pytest	Automated testing
GitPython	GitHub repository cloning
Git	Version control
📁 Project Structure
autonomous-software-engineering-agent/
│
├── agent.py
├── auto_fix.py
├── bug_agent.py
├── fix_agent.py
├── github_loader.py
├── orchestrator.py
├── repository.py
├── security_agent.py
├── test_agent.py
├── test_runner.py
│
├── demo_project/
│   ├── calculator.py
│   └── test_calculator.py
│
├── requirements.txt
├── README.md
└── .gitignore
Main Components
File	Description
orchestrator.py	Controls and coordinates the complete workflow
agent.py	Performs code understanding and repository analysis
bug_agent.py	Detects potential software bugs
security_agent.py	Performs security analysis
test_agent.py	Generates test cases
test_runner.py	Executes tests using Pytest
fix_agent.py	Analyzes failed tests and proposes fixes
auto_fix.py	Applies an AI-generated fix automatically
repository.py	Finds and reads source files
github_loader.py	Clones GitHub repositories
⚙️ Requirements

Before running the project, install:

Python 3.11 or later
Ollama
Git

Install the required Python packages:

pip install -r requirements.txt

Make sure the Qwen2.5-Coder model is available in Ollama:

ollama pull qwen2.5-coder:7b

Verify that the model is available:

ollama list
▶️ Running the Project

The project includes a demonstration project containing a calculator application.

Run the complete autonomous workflow with:

python orchestrator.py demo_project

The orchestrator performs:

1. Code Understanding
2. Bug Detection
3. Security Analysis
4. Test Generation
5. Test Execution
6. Automated Fixing (if tests fail)
7. Post-Fix Verification
🧪 Demonstration

The included demo_project contains a simple calculator application.

The project is intentionally configured with a bug in the is_even() function to demonstrate the automated fixing workflow.

Initial Bug

The incorrect implementation is:

def is_even(number):
    return number % 2 == 1

This condition incorrectly identifies even and odd numbers.

Initial Test Result

When the tests are executed, the system detects failures:

1 passed
2 failed

The orchestrator detects the failed tests and starts the automated repair process.

🤖 AI-Based Fix

The AI model analyzes the source code and test failure information and generates the corrected implementation:

def is_even(number):
    return number % 2 == 0

The corrected source code is automatically applied.

✅ Final Test Result

The system executes the tests again:

3 passed

The system then performs post-fix verification and confirms that the corrected implementation passes all tests.

AUTO-FIX SUCCESSFUL

POST-FIX VERIFICATION

3 passed

AUTONOMOUS ANALYSIS COMPLETE
🔗 GitHub Repository Support

The project includes a GitHub repository loader using GitPython.

A GitHub repository can be cloned and prepared for analysis using:

python github_loader.py

The cloned repository can then be provided to the analysis workflow.

📋 Example Workflow

A typical execution looks like:

Starting Autonomous Software Engineering Agent

        ↓

CODE UNDERSTANDING
Analyzing repository structure...

        ↓

BUG DETECTION
Analyzing source files...

        ↓

SECURITY ANALYSIS
Checking for security issues...

        ↓

TEST GENERATION
Generating test cases...

        ↓

TEST EXECUTION
Running Pytest...

        ↓

Tests Failed
        ↓
AUTOMATED FIX
AI analyzes failure and generates a fix

        ↓

POST-FIX VERIFICATION
Running tests again...

        ↓

3 passed

AUTONOMOUS ANALYSIS COMPLETE
⚠️ Current Limitations

This project is an academic/course project prototype and is not intended to replace professional software engineering or security tools.

Current limitations include:

Automated repair is primarily demonstrated with Python projects.
Test execution currently uses Pytest.
The automated fixing workflow focuses on top-level Python source files.
AI-generated fixes should be reviewed before being used in production systems.
Security analysis is based on LLM-assisted code inspection.
AI analysis may produce incorrect or incomplete findings.
The project is intended primarily as a demonstration of AI-assisted software engineering.
🔮 Future Enhancements

Possible future improvements include:

Support for additional programming languages
Improved multi-file automated fixing
Static analysis integration
Advanced test generation
GitHub Pull Request creation
Code quality metrics
Improved security scanning
Web-based user interface
Docker-based isolated execution
More advanced agent coordination
Detailed HTML/PDF analysis reports
🎯 Project Objective

The main objective of this project is to demonstrate how Artificial Intelligence and Large Language Models can assist in automating software engineering activities.

The project combines AI-powered code analysis with automated testing and repair to create a simple autonomous software engineering workflow.

🎓 Project Type

Academic / Course Project

This project was developed as an educational demonstration of AI-assisted autonomous software engineering using a locally running Large Language Model.

👨‍💻 Author

Kalidhasan A

B.Tech Information Technology