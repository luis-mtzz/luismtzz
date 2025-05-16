#./setup.py
import os
import sys
import subprocess
import shutil

from pathlib import Path

def run(command, cwd=None, shell=False):
    print(f"\n> {command if isinstance(command, str) else ' '.join(command)}")
    try:
        subprocess.run(command, cwd=cwd, check=True, shell=shell)
    except subprocess.CalledProcessError as err:
        print(f"Command failed: {err}")
        sys.exit(1)

def copy_env(example, target):
    if not Path(target).exists() and Path(example).exists():
        print(f"Copying {example} -> {target}")
        shutil.copy(example, target)
    else:
        print(f"{target} already exists or {example} not found; skipping.")
    
def setup_backend():
    print("\n=== Setting up backend Python environment ===")
    backend_dir = Path("backend")
    env_example = backend_dir / ".env.example"
    env_target = backend_dir / ".env"
    copy_env(env_example, env_target)
    try:
        run(["uv", "--version"])
        print("Detected uv: installing Python depdencies...")
        run(["uv", "venv"], cwd="backend")
        run(["uv", "sync"], cwd="backend")
    except Exception:
        print("uv not found. Please install uv for pyproject.toml-based dependency management.")
        print("Or, install dependencies manually. Exiting.")
        sys.exit(1)

def setup_frontend():
    print("\n=== Setting up frontend Node environment ===")
    frontend_dir = Path("frontend")
    env_example = frontend_dir / ".env.example"
    env_target = frontend_dir / ".env"
    copy_env(env_example, env_target)
    npm_exec = shutil.which("npm")
    if not npm_exec:
        print("npm is not installed! Please install Node.js and npm.")
        sys.exit(1)
    run(["npm", "install"], cwd="frontend")

def main():
    print("\n=== Setting up project ===")
    setup_backend()
    setup_frontend()
    print("\n=== Set up complete ===")

if __name__ == "__main__":
    main()