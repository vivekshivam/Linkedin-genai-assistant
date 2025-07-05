# memory/memory_manager.py

memory = []

def update_memory(user_input, assistant_response):
    memory.append({"type": "user", "content": user_input})
    memory.append({"type": "assistant", "content": assistant_response})

def get_memory():
    return memory
