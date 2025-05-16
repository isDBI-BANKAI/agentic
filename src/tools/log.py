from typing import Callable, Dict, Any

def logger_hook(function_name: str, function_call: Callable, arguments: Dict[str, Any]):
    """Pre-hook function that runs before the tool execution"""
    print(f"[Function Call: {function_name}] arguments: ({arguments})")
    result = function_call(**arguments)
    print(f"[Function call completed!]")
    return result