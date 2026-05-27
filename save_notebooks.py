import mlflow
target_run_id = "df9880aceb2a4d0981454be258475e13" 

mlflow.set_tracking_uri("http://localhost:5000")
with mlflow.start_run(run_id=target_run_id, nested=True):
    mlflow.log_artifact("model_test1.ipynb")
    mlflow.log_artifact("notebook1.ipynb")

print("Артефакт успешно добавлен.")

