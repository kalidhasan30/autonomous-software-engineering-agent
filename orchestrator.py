import sys
import subprocess
from pathlib import Path


def run_command(name, command):

    print("\n" + "=" * 70)
    print(name)
    print("=" * 70)

    result = subprocess.run(
        command,
        text=True
    )

    if result.returncode != 0:
        print(f"\n[FAILED] {name}")
        return False

    print(f"\n[COMPLETED] {name}")
    return True


def run_analysis_agent(name, script, repository):

    print("\n" + "=" * 70)
    print(name)
    print("=" * 70)

    result = subprocess.run(
        [sys.executable, script],
        input=repository + "\n",
        text=True
    )

    if result.returncode != 0:
        print(f"\n[FAILED] {name}")
        return False

    print(f"\n[COMPLETED] {name}")
    return True


def main():

    if len(sys.argv) < 2:
        print("Usage:")
        print("python orchestrator.py <repository_path_or_github_url>")
        return

    repository = sys.argv[1]

    # GitHub repository
    if repository.startswith(("https://github.com/", "http://github.com/")):

        print("\nGitHub repository detected.")
        print("Cloning repository...")

        try:
            from github_loader import clone_repository

            repository = str(clone_repository(repository))

        except Exception as error:
            print(f"\n[ERROR] GitHub clone failed: {error}")
            return

    # Local repository
    else:

        if not Path(repository).exists():
            print(f"[ERROR] Repository not found: {repository}")
            return

    print("=" * 70)
    print("AUTONOMOUS SOFTWARE ENGINEERING AGENT")
    print("=" * 70)

    print(f"\nTarget repository: {repository}")

    # 1. Code understanding
    run_analysis_agent(
        "CODE UNDERSTANDING",
        "agent.py",
        repository
    )

    # 2. Bug detection
    run_analysis_agent(
        "BUG DETECTION",
        "bug_agent.py",
        repository
    )

    # 3. Security analysis
    run_analysis_agent(
        "SECURITY ANALYSIS",
        "security_agent.py",
        repository
    )

    # 4. Test generation
    run_analysis_agent(
        "TEST GENERATION",
        "test_agent.py",
        repository
    )

    # 5. Run tests
    tests_passed = run_command(
        "TEST EXECUTION",
        [
            sys.executable,
            "-m",
            "pytest",
            repository,
            "-v"
        ]
    )

    # 6. Automatic repair if tests fail
    if not tests_passed:

        print("\nTests failed.")
        print("Starting autonomous repair...")

        run_analysis_agent(
            "AUTO-FIX",
            "auto_fix.py",
            repository
        )

        # 7. Verify repaired code
        run_command(
            "POST-FIX VERIFICATION",
            [
                sys.executable,
                "-m",
                "pytest",
                repository,
                "-v"
            ]
        )

    else:

        print("\nAll tests passed. No repair required.")

    print("\n" + "=" * 70)
    print("AUTONOMOUS ANALYSIS COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()