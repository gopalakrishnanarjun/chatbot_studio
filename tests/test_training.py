from ChatBot_Studio.core.training import train_bot

def test_train_bot():
    data_path = "mock_data.json"
    model = "mock_model"

    trained_model = train_bot(data_path, model)
    assert trained_model == model