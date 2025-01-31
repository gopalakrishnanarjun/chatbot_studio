# core/model_integration.py
from transformers import pipeline

def integrate_model(model_name="bert-base-uncased", task="text-classification"):
    """
    Integrate with a Hugging Face model.

    Args:
        model_name (str): Name of the Hugging Face model.
        task (str): NLP task.

    Returns:
        pipeline: A Hugging Face pipeline object.
    """
    return pipeline(task, model=model_name)