from nemoguardrails.actions import action
from typing import Dict, Any

@action(name="check_sensitive_content")
async def check_sensitive_content(context: Dict[str, Any] = None) -> bool:
    """センシティブなコンテンツをチェックするアクション"""
    if not context or "user_message" not in context:
        return True

    sensitive_terms = ["習近平", "天安門", "くまのプーさん"]
    message = context["user_message"].lower()
    return not any(term.lower() in message for term in sensitive_terms)
