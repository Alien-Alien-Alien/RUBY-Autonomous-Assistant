def validate_intent(intent_data):

    intent = intent_data.get("intent")


    if intent == "open_app":

        if "target" not in intent_data:

            return False


    if intent == "google_search":

        if "query" not in intent_data:

            return False


    return True