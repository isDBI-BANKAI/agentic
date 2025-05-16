from agno.tools import tool
from src.tools.log import logger_hook
from src.vector_store.retrieve import query_vdb

# TODO: given a doc_type [fas, ss] and an operation [musharakah, murabaha, etc.], get the outline of the document for an agentic guided retreival
@tool(
    name="get_outline",
    description="Get the outline of a document based on its type and operation",
    show_result=True,
    stop_after_tool_call=False,
    tool_hooks=[logger_hook],
    cache_results=False
)
def get_outline(doc_type: str, operation: str) -> str:
    """
    Get the outline of a document based on its type and operation.
    
    Args:
        doc_type: Type of the document, select from ['fas', 'ss']
        operation: Operation related to the document, select from ['musharaka', 'murabaha', 'ijarah', 'salam', 'salam'(only for fas)]
        
    Returns:
        str: The outline of the document, the elements between [] are the tags of the content in the vector store
    """
    
    base_dir = "data/processed"
    
    with open(f"{base_dir}/{doc_type}/{operation}/outline.txt", "r") as f:
        outline = f.read()
        
    return outline

@tool(
    name="retrieve",
    description="Retrieve content from the vector store (Pinecone) based on the outline insights",
    show_result=True,
    stop_after_tool_call=False,
    tool_hooks=[logger_hook],
    cache_results=False
)
# TODO: a tool for the agent to retrieve the content from the vector store, the filter is the intelligence of the agent to get specific chunks based on the outline insights
def retrieve(query: str, top_k: int = 5, filter: dict = None) -> list[str]:
    """
    Retrieve content from the vector store (Pinecone) based on the query.
    
    Args:
        query: The query to search for in the vector store
        top_k: Number of top results to retrieve (default: 5)
        filter: Optional filter to apply to the query (default: None), you will mainly need to use: {"tags": {"$in": [...]}} to filter the results based on the tags
        
    Returns:
        list[str]: List of retrieved content
    """
    
    results = query_vdb(query, top_k=top_k, filter=filter)
    
    return results

def retrieve_test(query: str, top_k: int = 5, filter: dict = None) -> list[str]:
    """
    Retrieve content from the vector store (Pinecone) based on the query.
    
    Args:
        query: The query to search for in the vector store
        top_k: Number of top results to retrieve (default: 5)
        filter: Optional filter to apply to the query (default: None), you will mainly need to use: {"tags": {"$in": [...]}} to filter the results based on the tags
        
    Returns:
        list[str]: List of retrieved content
    """
    
    results = query_vdb(query, top_k=top_k, filter=filter)
    
    return results


print(retrieve_test(query="Definitions in FAS 28 for Murabaha operations", filter={'tags': {'$in': ['Definitions']}}))
print(retrieve_test(query="Related Accounting Treatments in FAS 28 Murabaha operations", filter={'tags': {'$in':['Related Accounting Treatments']}}))