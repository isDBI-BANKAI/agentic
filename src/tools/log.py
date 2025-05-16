from typing import Callable, Dict, Any

def logger_hook(function_name: str, function_call: Callable, arguments: Dict[str, Any]):
    """Pre-hook function that runs before the tool execution"""
    print(f"[Function Call: {function_name}] arguments: ({arguments})")
    result = function_call(**arguments)
    if isinstance(result, str):
        result_repr = result[:100] + "..." if len(result) > 100 else result
    elif isinstance(result, list):
        result_repr = f"SIZE: {len(result)}"
    print(f"[Function call completed!], result: {result_repr}")
    return result