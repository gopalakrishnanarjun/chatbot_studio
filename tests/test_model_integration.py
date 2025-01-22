from ChatBot_Studio.core.model_integration import integrate_model

def test_integrate_model():
    model_name = "distilbert-base-uncased"
    task = "text-classification"

    model = integrate_model(model_name, task)
    assert model is not None
    assert model.model.name_or_path == model_name