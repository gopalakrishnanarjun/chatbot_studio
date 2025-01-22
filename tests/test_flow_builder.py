from ChatBot_Studio.core.flow_builder import create_conversational_flow

def test_create_conversational_flow():
    flow_name = "Test Flow"
    steps = [
        {"question": "What is your name?", "responses": ["Option1", "Option2"]}
    ]

    flow = create_conversational_flow(flow_name, steps)
    assert flow["flow_name"] == flow_name
    assert len(flow["steps"]) == 1