# DevOps Intern Final Assessment

**Name:** Balla Veera Venkata Satya Narayana
**Date:** July 8, 2026

## Project Description

End-to-end DevOps pipeline: Git → Linux scripting → Docker → CI/CD (GitHub Actions) → Nomad deployment → Monitoring (Loki).

[![CI](https://github.com/Satya23BDS0326/devops-intern-final/actions/workflows/ci.yml/badge.svg)](https://github.com/Satya23BDS0326/devops-intern-final/actions/workflows/ci.yml)

## How to Run

# 1. Run the basics
python3 hello.py
chmod +x scripts/sysinfo.sh && ./scripts/sysinfo.sh

# 2. Build & run the container
docker build -t devops-intern-final .
docker run --rm devops-intern-final

# 3. Deploy with Nomad (needs local Nomad dev agent)
nomad agent -dev &
nomad job run nomad/hello.nomad

# 4. Start Loki for monitoring
docker run -d --name=loki -p 3100:3100 grafana/loki:2.9.0 -config.file=/etc/loki/local-config.yaml

# 5. (Optional) Extra credit MLflow run
pip install mlflow && python mlflow/dummy_experiment.py