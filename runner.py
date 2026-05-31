import json
import os
import shutil
import subprocess
import time

from llm_agent import call_llm
from metrics import Metrics
from failure_analysis import classify_failure

def run_cmd(cmd, cwd=None, env=None):
    return subprocess.run(
        cmd,
        shell=True,
        cwd=cwd,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

def evaluate(task, exp_name):
    base_repo = f"repos/{task['repo']}"
    workdir = f"workspaces/{task['task_id']}_{exp_name}"

    print(f"\n=== RUN {exp_name} {task['task_id']} ({task['difficulty']}) ===")

    if os.path.exists(workdir):
        shutil.rmtree(workdir)

    shutil.copytree(base_repo, workdir)
    code_path = os.path.join(workdir, "target.py")

    with open(code_path, "r", encoding="utf-8") as f:
        code = f.read()

    start = time.time()
    new_code = call_llm(code, task["problem"], variant=exp_name)
    with open(code_path, "w", encoding="utf-8") as f:
        f.write(new_code.strip())

    env = os.environ.copy()
    env["PYTHONPATH"] = workdir

    result = run_cmd(
        "python -m unittest test_target.py",
        cwd=workdir,
        env=env
    )

    success = result.returncode == 0
    latency = time.time() - start
    failure_type = None if success else classify_failure(result.stderr)

    return {
        "task_id": task["task_id"],
        "difficulty": task["difficulty"],
        "exp": exp_name,
        "success": success,
        "latency": latency,
        "failure_type": failure_type
    }

def run_experiment(exp_name):
    print(f"\n===== START EXPERIMENT {exp_name} =====")
    tasks = json.load(open("tasks.json", encoding="utf-8"))
    results = [evaluate(t, exp_name) for t in tasks]
    os.makedirs("results", exist_ok=True)
    json.dump(results, open(f"results/run_{exp_name}.json", "w"), indent=2)
    return results

def build_metrics(runA, runB):
    metrics = Metrics()
    A = {x["task_id"]: x for x in runA}
    B = {x["task_id"]: x for x in runB}

    for task_id in A:
        metrics.log_task(
            task_id,
            A[task_id]["success"],
            B[task_id]["success"],
            A[task_id]["latency"],
            B[task_id]["latency"]
        )

    overall = metrics.summary()

    diff = {}
    for r in runA:
        diff.setdefault(r["difficulty"], {"A": [], "B": []})
        diff[r["difficulty"]]["A"].append(r["success"])
    for r in runB:
        diff[r["difficulty"]]["B"].append(r["success"])

    by_diff = {}
    for d, v in diff.items():
        by_diff[d] = {
            "A_success_rate": sum(v["A"]) / len(v["A"]),
            "B_success_rate": sum(v["B"]) / len(v["B"])
        }

    delta = {"B_better_tasks": [], "A_better_tasks": [], "tie_tasks": []}
    for task_id in A:
        a = A[task_id]["success"]
        b = B[task_id]["success"]
        if a < b:
            delta["B_better_tasks"].append(task_id)
        elif a > b:
            delta["A_better_tasks"].append(task_id)
        else:
            delta["tie_tasks"].append(task_id)

    return {"overall": overall, "by_difficulty": by_diff, "delta_analysis": delta}

def main():
    print("\n=== PIPELINE START ===")
    runA = run_experiment("A")
    runB = run_experiment("B")

    summary = build_metrics(runA, runB)
    os.makedirs("results", exist_ok=True)
    json.dump(summary, open("results/summary.json", "w"), indent=2)

    print("\n===== FINAL SUMMARY =====")
    print(summary)

if __name__ == "__main__":
    main()