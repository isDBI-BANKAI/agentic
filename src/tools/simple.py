import random
from typing import Dict, Any, Callable, List, Optional
from agno.agent import Agent
from agno.tools import tool
from src.llm.llm import OpenAILLM
from src.tools.log import logger_hook


@tool(
    name="random_number_generator",
    description="Generate random numbers within a specified range",
    show_result=True,
    stop_after_tool_call=True,
    tool_hooks=[logger_hook],
    cache_results=False
)

def generate_random_numbers(
    min_value: int = 1, 
    max_value: int = 100, 
    count: int = 1, 
    unique: bool = False
) -> str:
    """
    Generate random numbers within a specified range.
    
    Args:
        min_value: Minimum value for random numbers (default: 1)
        max_value: Maximum value for random numbers (default: 100)
        count: Number of random numbers to generate (default: 1)
        unique: Whether the numbers should be unique (default: False)
        
    Returns:
        str: The generated random numbers in text format
    """
    if min_value >= max_value:
        return "Error: min_value must be less than max_value"
    
    if unique and count > (max_value - min_value + 1):
        return f"Error: Cannot generate {count} unique numbers in range [{min_value}, {max_value}]"
    
    if unique:
        # Generate unique random numbers
        numbers = random.sample(range(min_value, max_value + 1), count)
    else:
        # Generate random numbers (may contain duplicates)
        numbers = [random.randint(min_value, max_value) for _ in range(count)]
    
    # Format the output
    if count == 1:
        return f"Random number: {numbers[0]}"
    else:
        formatted_numbers = ", ".join(map(str, numbers))
        return f"Random numbers: {formatted_numbers}"

agent = Agent(model=OpenAILLM().get_openai_chat(), tools=[generate_random_numbers])

# Test the tool
agent.print_response("Generate 5 random numbers between 10 and 50")