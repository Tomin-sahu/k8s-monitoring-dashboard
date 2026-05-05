from flask import Flask, render_template
import random
import subprocess

app = Flask(__name__)

def get_pods():
    try:
        output = subprocess.getoutput("kubectl get pods")
        return output
    except:
        return "Kubernetes not reachable"

def get_nodes():
    try:
        output = subprocess.getoutput("kubectl get nodes")
        return output
    except:
        return "Kubernetes not reachable"

@app.route("/")
def home():
    data = {
    "cpu": f"{random.randint(10, 90)}%",
    "memory": f"{random.randint(20, 80)}%",
    "pods": get_pods().splitlines(),
    "nodes": get_nodes().splitlines()
}
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
