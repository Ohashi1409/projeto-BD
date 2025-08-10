#!/usr/bin/env python3
import subprocess
import sys
import os

scripts = [
    "init_mongodb.py",
    "problem_testCase1.py",
    "problem_testCase2.py", 
    "problem_testCase3.py",
    "problem_testCase4.py",
    "user_creates_blog1.py",
    "user_creates_blog2.py",
    "user_creates_blog3.py", 
    "user_creates_blog4.py",
    "user_creates_contest1.py",
    "user_creates_contest2.py",
    "user_creates_contest3.py",
    "user_creates_contest4.py",
    "user_cria_group1.py",
    "user_cria_group2.py",
    "user_cria_group3.py",
    "user_cria_group4.py",
    "user_participates_group1.py",
    "user_participates_group2.py",
    "user_participates_group3.py",
    "user_participates_group4.py",
    "user_sends_submission1.py",
    "user_sends_submission2.py",
    "user_sends_submission3.py",
    "user_sends_submission4.py"
]

def run_script(script_name):
    try:
        print(f"\n=== Executando {script_name} ===")
        result = subprocess.run([sys.executable, script_name], 
                              capture_output=True, text=True, cwd="/workspaces/projeto-BD/No-SQL")
        if result.returncode == 0:
            print(f"{script_name} executado com sucesso")
            if result.stdout:
                print(result.stdout)
        else:
            print(f"✗ Erro em {script_name}")
            if result.stderr:
                print(result.stderr)
    except Exception as e:
        print(f"ERRO ao executar {script_name}: {e}")

if __name__ == "__main__":
    for script in scripts:
        run_script(script)
