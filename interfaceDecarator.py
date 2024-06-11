def interface_decorator(interface):
    import inspect
    def decorator(cls):
        # Check if class is interface by name
        is_abstract = cls.__name__.startswith('I')
        
        # Get methods defined in interface
        interface_methods = {method_name for method_name, _ in inspect.getmembers(interface, inspect.isfunction)}
        
        # Get methods defined in class
        cls_methods = {method_name for method_name, _ in inspect.getmembers(cls, inspect.isfunction)}
        
        # If the class is interface, add the methods defined in the interface to the class
        if is_abstract:
            for method_name in interface_methods:
                if method_name not in cls_methods:
                    # Add missing methods to class
                    setattr(cls, method_name, lambda self, *args, **kwargs: None)
        else:
            # If the class is concrete and the methods defined in the interface are missing, throw an error
            for method_name in interface_methods:
                if method_name not in cls_methods:
                    raise NotImplementedError(f"Concrete class {cls.__name__} does not implement method {method_name} defined in {interface.__name__}")
        return cls
    return decorator
