# Autonomous Software Engineering & Code Review Agent

An AI-powered software engineering agent that analyzes source code, detects bugs and security issues, generates tests, executes tests, and automatically fixes detected failures using a local Large Language Model.

## 🚀 Overview

The **Autonomous Software Engineering & Code Review Agent** is a Python-based academic project designed to automate common software engineering and code review tasks.

The system uses **Ollama** with the **Qwen2.5-Coder 7B** model to analyze a repository and assist with:

- Code understanding
- Bug detection
- Security analysis
- Test generation
- Test execution
- Automated bug fixing
- Post-fix verification

The project demonstrates how Large Language Models (LLMs) can be integrated into an automated software engineering workflow.

---

## ✨ Key Features

### 🔍 Code Understanding
Analyzes the repository structure and identifies:

- Programming languages
- Important source files
- Functions and classes
- Code relationships
- Potential areas requiring investigation

### 🐛 Bug Detection
AI analyzes source files for possible:

- Logic errors
- Incorrect conditions
- Exception handling problems
- Edge-case issues
- Type-related problems
- Resource-related issues

### 🔐 Security Analysis
The security agent checks for common security concerns such as:

- SQL injection
- Command injection
- Cross-site scripting (XSS)
- Path traversal
- Hardcoded secrets
- Unsafe file operations
- Insecure authentication and authorization
- Sensitive information exposure

### 🧪 Test Generation
The system uses the AI model to generate tests covering:

- Normal behavior
- Edge cases
- Invalid inputs
- Boundary conditions
- Exceptions
- Business logic

### ▶️ Automated Test Execution
Generated or existing tests are executed using **Pytest**.

The system determines whether the tests pass or fail and uses the results for further analysis.

### 🔧 Automated Bug Fixing
When tests fail, the system sends the source code and test failure information to the AI model.

The AI proposes a corrected version of the source code, which is then applied and tested again.

### ✅ Post-Fix Verification
After applying an AI-generated fix, the system runs the tests again to verify whether the problem has been resolved.

---

## 🔄 System Workflow

```text
                Repository / Project
                        │
                        ▼
              ┌───────────────────┐
              │ Code Understanding │
              │      Agent         │
              └─────────┬─────────┘
                        │
          ┌─────────────┴─────────────┐
          ▼                           ▼
 ┌─────────────────┐         ┌─────────────────┐
 │  Bug Detection  │         │ Security        │
 │      Agent      │         │ Analysis Agent  │
 └────────┬────────┘         └────────┬────────┘
          │                           │
          └─────────────┬─────────────┘
                        ▼
              ┌───────────────────┐
              │  Test Generation  │
              │       Agent       │
              └─────────┬─────────┘
                        ▼
              ┌───────────────────┐
              │   Test Runner     │
              │      Pytest       │
              └─────────┬─────────┘
                        │
                 Tests Failed?
                    /       \
                  Yes        No
                   │          │
                   ▼          ▼
          ┌──────────────┐   Complete
          │  Auto Fix    │
          │    Agent     │
          └──────┬───────┘
                 │
                 ▼
          ┌──────────────┐
          │ Verification │
          │    Tests     │
          └──────┬───────┘
                 │
                 ▼
              Complete

###🧠 AI Model

This project uses a locally running Large Language Model through Ollama.

Model:

Qwen2.5-Coder 7B

Using a local model allows the project to perform code analysis without depending on a cloud-based AI API.

###🛠️ Technologies Used
Technology	Purpose
Python	Core programming language
Ollama	Local LLM runtime
Qwen2.5-Coder 7B	AI code analysis and fixing
Pytest	Automated testing
GitPython	GitHub repository cloning
Git	Version control

###📁 Project Structure
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
orchestrator.py	Controls the complete workflow
agent.py	Performs code understanding
bug_agent.py	Detects potential bugs
security_agent.py	Performs security analysis
test_agent.py	Generates test cases
test_runner.py	Executes Pytest
fix_agent.py	Analyzes failed tests and proposes fixes
auto_fix.py	Applies an AI-generated fix automatically
repository.py	Reads and analyzes repository source files
github_loader.py	Clones GitHub repositories

###⚙️ Requirements

Make sure the following are installed:

Python 3.11+
Ollama
Git

Install the required Python packages:

pip install -r requirements.txt

Make sure the Qwen model is available in Ollama:

ollama pull qwen2.5-coder:7b

###▶️ Running the Project

Run the demonstration project using:

python orchestrator.py demo_project

The orchestrator will perform the following steps:

1. Code Understanding
2. Bug Detection
3. Security Analysis
4. Test Generation
5. Test Execution
6. Automated Fixing (if tests fail)
7. Post-Fix Verification

###🧪 Demonstration

The included demo project contains a simple calculator application.

A bug is intentionally introduced into the is_even() function.

Initial Bug
def is_even(number):
    return number % 2 == 1

The function incorrectly identifies even and odd numbers.

The test execution produces failures:

1 passed
2 failed

The system then starts the automated repair process.

AI-Based Fix

The AI agent identifies the incorrect condition and generates the corrected implementation:

def is_even(number):
    return number % 2 == 0

The tests are executed again.

Final Result
3 passed

The system then performs post-fix verification and confirms that the tests pass successfully.

AUTO-FIX SUCCESSFUL

POST-FIX VERIFICATION

3 passed

AUTONOMOUS ANALYSIS COMPLETE

###🔗 GitHub Repository Support

The system can also clone a GitHub repository using the GitHub loader.

Example:

python github_loader.py

The repository is cloned locally and can then be analyzed by the agent workflow.

###⚠️ Current Limitations

This is an academic/course project prototype.

Current limitations include:

Automated repair is primarily demonstrated with Python projects.
Test execution currently uses Pytest.
The automated fixing workflow focuses on top-level Python source files.
AI-generated fixes should be reviewed before being used in real production systems.
Security analysis is based on LLM-assisted inspection and is not a replacement for professional security testing.

###🔮 Future Enhancements

Possible future improvements include:

Support for additional programming languages
Improved multi-file automated fixing
Static analysis integration
GitHub pull request generation
Better test generation
Code quality metrics
Improved security scanning
Web-based user interface
Docker-based execution
More advanced agent coordination

###🎯 Project Objective

The main objective of this project is to demonstrate how Artificial Intelligence and Large Language Models can automate software engineering activities, including code analysis, bug detection, security review, testing, automated repair, and verification.

###🎓 Project Type

Academic / Course Project

Developed as a demonstration of AI-assisted autonomous software engineering using local Large Language Models.