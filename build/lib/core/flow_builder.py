def create_conversational_flow(flow_name, steps):
    """
    Create a conversational flow.

    Args:
        flow_name (str): The name of the flow.
        steps (list): List of steps, each a dictionary with 'question' and 'responses'.

    Returns:
        dict: A structured conversational flow.
    """
    return {"flow_name": flow_name, "steps": steps}