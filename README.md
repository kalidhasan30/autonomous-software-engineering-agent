\# Autonomous Software Engineering \& Code Review Agent



\## Overview



The Autonomous Software Engineering \& Code Review Agent is an AI-powered software analysis system that helps automate common software engineering tasks.



The system analyzes a software repository, identifies possible bugs and security issues, generates tests, executes tests, and attempts to automatically fix detected test failures.



The project uses a local Large Language Model (LLM) through Ollama and Qwen2.5-Coder.



\## Features



\- Code understanding

\- Automated bug detection

\- Security analysis

\- AI-based test generation

\- Automated test execution

\- AI-powered bug fixing

\- Post-fix verification

\- GitHub repository cloning



\## System Workflow



```text

Repository

&#x20;   |

&#x20;   v

Code Understanding Agent

&#x20;   |

&#x20;   v

Bug Detection Agent

&#x20;   |

&#x20;   v

Security Analysis Agent

&#x20;   |

&#x20;   v

Test Generation Agent

&#x20;   |

&#x20;   v

Test Execution

&#x20;   |

&#x20;   v

AI Auto-Fix

&#x20;   |

&#x20;   v

Post-Fix Verification



Technologies Used

Python

Ollama

Qwen2.5-Coder

Pytest

GitPython

Project Structure

autonomous-code-agent/

|

├── agent.py

├── bug\_agent.py

├── security\_agent.py

├── test\_agent.py

├── test\_runner.py

├── fix\_agent.py

├── auto\_fix.py

├── orchestrator.py

├── repository.py

├── github\_loader.py

├── requirements.txt

|

└── demo\_project/

&#x20;   ├── calculator.py

&#x20;   └── test\_calculator.py

Requirements

Python 3.11 or later

Ollama

Qwen2.5-Coder 7B model



Install the required Python packages:



pip install -r requirements.txt



Install the AI model:



ollama pull qwen2.5-coder:7b

How to Run



Activate the virtual environment:



.\\.venv\\Scripts\\Activate.ps1



Run the autonomous software engineering agent:



python orchestrator.py demo\_project

Demonstration



The demo project contains a deliberately introduced bug in the is\_even() function.



The agent performs the following steps:



Runs the test suite.

Detects the failed tests.

Analyzes the source code and test failure using Qwen2.5-Coder.

Generates a corrected version of the source code.

Applies the proposed fix.

Runs the tests again.

Verifies the corrected code.



Expected final result:



3 passed

GitHub Repository Support



The project can clone a GitHub repository for analysis.



Run:



python github\_loader.py



Then enter the GitHub repository URL when prompted.



Objective



The objective of this project is to demonstrate how AI agents can automate software engineering activities such as code analysis, bug detection, security analysis, testing, debugging, and verification.



Project Type



Academic / Course Project
