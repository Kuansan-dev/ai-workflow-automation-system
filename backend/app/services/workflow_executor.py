import json

from app.services.ai_service import generate_summary, extract_action_items


def execute_workflow(definition_json: str, input_text: str):
    workflow_definition = json.loads(definition_json)
    steps = workflow_definition.get("steps", [])

    result = input_text

    for step in steps:
        if step == "summarize":
            result = generate_summary(result)

        elif step == "tasks":
            result = extract_action_items(result)

        else:
            result = f"Processed step {step}: {result}"

    return result