#!/usr/bin/env python3
"""Test runner script for the GLAM SDK."""

import subprocess
import sys
from pathlib import Path


def run_tests():
    """Run all tests with coverage and formatting checks."""
    project_root = Path(__file__).parent

    print("🧪 Running GLAM SDK Tests...")
    print("=" * 50)

    # Run tests
    print("\n📋 Running pytest...")
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/", "-v", "--tb=short"], cwd=project_root
    )

    if result.returncode != 0:
        print("❌ Tests failed!")
        return result.returncode

    print("✅ All tests passed!")

    # Run linting
    print("\n🔍 Running Ruff linting...")
    lint_result = subprocess.run(
        [sys.executable, "-m", "ruff", "check", "glam/", "tests/"], cwd=project_root
    )

    if lint_result.returncode != 0:
        print("⚠️  Linting issues found!")
    else:
        print("✅ No linting issues!")

    # Run formatting check
    print("\n🎨 Checking code formatting...")
    format_result = subprocess.run(
        [sys.executable, "-m", "ruff", "format", "--check", "glam/", "tests/"], cwd=project_root
    )

    if format_result.returncode != 0:
        print("⚠️  Formatting issues found! Run 'ruff format glam/ tests/' to fix.")
    else:
        print("✅ Code is properly formatted!")

    print("\n" + "=" * 50)
    if result.returncode == 0 and lint_result.returncode == 0 and format_result.returncode == 0:
        print("🎉 All checks passed!")
        return 0
    else:
        print("⚠️  Some checks failed. See output above.")
        return 1


if __name__ == "__main__":
    sys.exit(run_tests())
