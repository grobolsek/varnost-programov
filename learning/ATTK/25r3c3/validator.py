from flask import Flask, render_template, request, redirect
import tempfile
import random
import threading
import os
import json
import subprocess

# Setup
app = Flask(__name__)
status = {}
flag = os.environ.get('FLAG', 'flag{fake_flag}')
with open("config.json", "r") as f:
    config = json.load(f)

# Helpers
def randid(n=8):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(chars) for _ in range(n))

# Validator
def runner_wrapper(status_id):
    try:
        runner(status_id)
    except Exception as e:
        print(f"[{status_id}] Exception occurred: {e}")
        status[status_id]['state'] = 'Error'
        status[status_id]['done'] = True

def runner(status_id):
    print(f"[{status_id}] Running validator for {status[status_id]['path']}")
    cwd = status[status_id]['path']
    build = config['build']['guard'] + config['build']['cmd']
    run = config['run']['guard'] + config['run']['cmd']
    print(f"[{status_id}] Build command: {" ".join(build)}")
    print(f"[{status_id}] Run command: {" ".join(run)}")
    
    # Build step
    child_build = subprocess.Popen(build, cwd=cwd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout_build, stderr_build = child_build.communicate()
    if child_build.returncode != 0:
        print(f"[{status_id}] Build stdout: {stdout_build.decode()}")
        print(f"[{status_id}] Build stderr: {stderr_build.decode()}")
        status[status_id]['state'] = 'Build Failed'
        status[status_id]['done'] = True
        return

    # Run step
    status[status_id]['state'] = 'Testing...'
    for test in config['inputs']['tests']:
        with open(f"{config["inputs"]["folder"]}/{test["name"]}.txt", 'r') as f:
            child = subprocess.Popen(run, cwd=cwd, shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = child.communicate(input=f.read().encode())
            if child.returncode != test["expect_status"]:
                print(f"[{status_id}] Test {test['name']} failed with status {child.returncode}")
                print(f"[{status_id}] stdout: {stdout.decode()}")
                print(f"[{status_id}] stderr: {stderr.decode()}")
                status[status_id]['state'] = f'Test {test["name"]} Failed'
                status[status_id]['done'] = True
                status[status_id]['results'].append({
                    "test": test['name'],
                    "status": "Failed",
                    "reason": f"Expected status {test['expect_status']}, got {child.returncode}",
                })
                return
            if test["expect_stdout"]:
                with open(f"{config["inputs"]["folder"]}/{test["name"]}_out.txt", 'r') as f:
                    expected_output = f.read().strip()
                    if stdout.decode().strip() != expected_output:
                        print(f"[{status_id}] Test {test['name']} failed with unexpected output")
                        print(f"[{status_id}] Expected: {expected_output}")
                        print(f"[{status_id}] Got: {stdout.decode().strip()}")
                        status[status_id]['state'] = f'Test {test["name"]} Failed'
                        status[status_id]['done'] = True
                        status[status_id]['results'].append({
                            "test": test['name'],
                            "status": "Failed",
                            "reason": "Output mismatch",
                        })
                        return
            status[status_id]['results'].append({
                "test": test['name'],
                "status": "Passed",
            })

    # All tests passed
    status[status_id]['state'] = 'Passed'
    status[status_id]['flag'] = flag
    status[status_id]['done'] = True

# Websites
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', config=config)

@app.route('/', methods=['POST'])
def upload():
    if 'file' not in request.files or request.files['file'].filename == '':
        return render_template('index.html', config=config, error='No file uploaded')

    with tempfile.TemporaryDirectory(delete=False) as temp_dir:
        with open(f"{temp_dir}/{config["src_name"]}", 'wb') as f:
            file = request.files['file']
            file.save(f)

        status_id = randid()
        status[status_id] = {
            "state": "Uploaded",
            "results": [],
            "path": temp_dir,
            "done": False,
        }

        threading.Thread(target=runner_wrapper, args=(status_id,)).start()

    return redirect('/status/' + status_id)

@app.route('/status', methods=['GET'])
def status_list():
    return render_template('status_list.html', status=status)

@app.route('/status/<status_id>', methods=['GET'])
def check_status(status_id):
    if status_id not in status:
        return render_template('status.html', status_id=None)
    return render_template('status.html', status_id=status_id, status=status[status_id])

# Run
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
