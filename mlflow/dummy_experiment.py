"""
dummy_experiment.py
Logs a dummy experiment run using MLflow.

Run:
    pip install mlflow
    python mlflow/dummy_experiment.py
    mlflow ui   # then open http://localhost:5000
"""

import random
import mlflow

mlflow.set_experiment("devops-intern-final-demo")

with mlflow.start_run(run_name="dummy-run"):
    learning_rate = 0.01
    epochs = 5

    mlflow.log_param("learning_rate", learning_rate)
    mlflow.log_param("epochs", epochs)

    for epoch in range(1, epochs + 1):
        fake_accuracy = 0.5 + epoch * 0.08 + random.uniform(-0.02, 0.02)
        fake_loss = 1.0 - epoch * 0.15 + random.uniform(-0.02, 0.02)
        mlflow.log_metric("accuracy", fake_accuracy, step=epoch)
        mlflow.log_metric("loss", fake_loss, step=epoch)

    with open("mlflow/summary.txt", "w") as f:
        f.write("Dummy experiment completed successfully.\n")
    mlflow.log_artifact("mlflow/summary.txt")

print("Dummy MLflow experiment logged. Run 'mlflow ui' to view it.")