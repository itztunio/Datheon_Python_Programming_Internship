
import re

RESPONSES = {
    "greeting": "Hello! Welcome to Customer Support. How can I help you?",
    "hours": "Our business hours are Monday to Saturday, 9 AM to 6 PM.",
    "price": "Our product prices depend on the item. Which product are you interested in?",
    "delivery": "Delivery usually takes 3 to 5 business days.",
    "return": "You can request a return within 7 days of receiving your product.",
    "payment": "We accept cash on delivery and online payments.",
    "thanks": "You're welcome! Is there anything else I can help you with?",
    "fallback": "Sorry, I didn't understand. Ask me about hours, products, delivery, returns, or payments."
}

INTENT_PATTERNS = {
    "hours": r"\b(hours|timing|open|opening|closing)\b",
    "price": r"\b(price|prices|cost|product|products)\b",
    "delivery": r"\b(delivery|shipping|parcel|shipment)\b",
    "return": r"\b(return|refund|exchange)\b",
    "payment": r"\b(payment|payments|pay|cash|card)\b",
    "thanks": r"\b(thanks|thank you|thankyou)\b"
}

EXIT_PATTERN = r"\b(bye|goodbye|exit|quit)\b"
GREETING_PATTERN = r"\b(hello|hi|hey)\b"


class SupportChatbot:
    def __init__(self):
        # Conversation state and history
        self.state = "greeting"
        self.history = []

    def identify_intents(self, message):
        intents = []

        for intent, pattern in INTENT_PATTERNS.items():
            if re.search(pattern, message):
                intents.append(intent)

        return intents

    def get_response(self, user_input):
        message = user_input.lower().strip()

        if not message:
            return "Please enter a message.", False

        if re.fullmatch(EXIT_PATTERN, message):
            self.state = "exit"
            return "Goodbye! Thank you for contacting us.", True

        if re.search(GREETING_PATTERN, message):
            self.state = "intent_identification"
            self.history.append(("user", message))
            self.history.append(("bot", RESPONSES["greeting"]))
            return RESPONSES["greeting"], False

        intents = self.identify_intents(message)

        if intents:
            self.state = "resolution"
            reply = "\n".join(RESPONSES[intent] for intent in intents)
        else:
            self.state = "fallback"
            reply = RESPONSES["fallback"]

        self.history.append(("user", message))
        self.history.append(("bot", reply))

        # Return to the stage where the user can ask another question
        if self.state == "resolution" or self.state == "fallback":
            self.state = "intent_identification"

        return reply, False

    def run(self):
        print("=" * 42)
        print("       CUSTOMER SUPPORT CHATBOT")
        print("=" * 42)
        print("Ask about hours, prices, delivery, returns, or payments.")
        print("Commands to exit: bye, exit, quit")

        print("\nBot:", RESPONSES["greeting"])

        while True:
            try:
                user_input = input("\nYou: ")
                response, should_exit = self.get_response(user_input)
                print("Bot:", response)

                if should_exit:
                    break

            except (KeyboardInterrupt, EOFError):
                print("\nBot: Chat ended. Goodbye!")
                break
            except Exception:
                print("Bot: Something went wrong. Please try again.")


if __name__ == "__main__":
    try:
        chatbot = SupportChatbot()
        chatbot.run()
    except Exception as error:
        print(f"Unable to start chatbot: {error}")
