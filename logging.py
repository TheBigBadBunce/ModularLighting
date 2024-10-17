import builtins as __builtin__

def set_verbose(new_verbose):
    """Setter for verbose logging"""
    global verbose
    verbose = new_verbose

def set_silent(new_silent):
    """Setter to silence logging"""
    global silent
    silent = new_silent

def print(*args, **kwargs):
    """Print under normal (non-silent) circumstances"""
    global silent
    if not silent:
        return __builtin__.print(*args)
    
def print_verbose(*args, **kwargs):
    """Print only when verbose and non-silent"""
    global silent
    global verbose

    if (not silent) and verbose:
        return __builtin__.print(*args)