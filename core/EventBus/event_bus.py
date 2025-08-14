from typing import Callable, Dict, List

class EventBus:
    """
    This class is a simple event bus for registering, removing and triggering event listeners.

    Middleware is called before event listeners.
    If middleware returns false event is NOT called.
    """

    def __init__(self):
        """
        This defines the lists which store al the listeners and middlewares.
        """
        self._listeners: Dict[str, List[Callable]] = {}
        self._middleware_register: Dict[str, Callable] = {}
        self._active_middleware: List[Callable] = []

    def register_middleware(self, name: str, middleware_function: Callable):
        """
        This function registers a middleware.
        """
        if not self._middleware_register.get(name):
            self._middleware_register[name] = middleware_function

    def register_middleware_dict(self, middleware_dict: Dict[str, Callable]):
        """
        This function registers multiple middleware at once.
        """
        for name, function in middleware_dict.items():
            self.register_middleware(name, function)

    def activate_middleware(self, name: str):
        """
        This function activates a middleware from the middleware register.
        """
        middleware = self._middleware_register.get(name)
        if middleware and middleware not in self._active_middleware:
            self._active_middleware.append(middleware)
        else:
            print(f"Middleware {name} already activated or isn't registered")

    def deactivate_middleware(self, name: str):
        """
        This function deactivates a middleware from the active middleware.
        """
        middleware = self._middleware_register.get(name)
        if middleware and middleware in self._active_middleware:
            self._active_middleware.remove(middleware)
        else:
            print(f"Middleware {name} not activated or isn't registered")

    def activate_middleware_preset(self, preset: List[str]):
        """
        This function activates a middleware preset.

        It removes all current middleware from the active middleware and replaces them with the preset.
        You can add additional middleware to a preset after the preset has been applied.
        """
        middleware_list = []
        for mw_name in preset:
            if mw_name in self._middleware_register:
                middleware_list.append(self._middleware_register[mw_name])
            else:
                print(f"Warning: Middleware '{mw_name}' not registered.")

        self._active_middleware = middleware_list

    def on(self, event: str, callback: Callable):
        """
        This function creates an event listener for a certain event.

        It will create the event if not already made.
        """
        if event not in self._listeners:
            self._listeners[event] = []
        self._listeners[event].append(callback)

    def off(self, event: str, callback: Callable):
        """
        This function removes an event listener from a certain event.

        It will automatically remove the event if there are no event listeners.
        """
        if event in self._listeners:
            try:
                self._listeners[event].remove(callback)
                if not self._listeners[event]:
                    del self._listeners[event]
            except ValueError:
                pass

    def once(self, event: str, callback: Callable):
        """
        This function creates an event listener that will remove itself after it is triggered.
        """
        def _wrapper(*args, **kwargs):
            callback(*args, **kwargs)
            self.off(event, _wrapper)

        self.on(event, _wrapper)

    def emit(self, event: str, *args, **kwargs):
        """
        This function emits an event which calls all event listeners for the specific event and calls the middleware.

        If middleware returns false event is NOT called.
        """
        for mw in self._active_middleware:
            result = mw(event, *args, **kwargs)
            if result is False:
                print("Event cancelled by middleware")
                return # cancels event

        if event in self._listeners:
            for callback in self._listeners[event][:]: # creates a copy of the item in case the listeners change while looping through (will happen with once event listeners)
                try:
                    callback(*args, **kwargs)
                except Exception as e:
                    print(f"Error in callback. Event: {event} Callback: {callback} Exception: {e}")

    def off_all(self, event: str):
        """
        This function clears all event listeners for the specific event.
        """
        if event in self._listeners:
            del self._listeners[event]

    def full_wipe(self):
        """
        This function wipes all events, event listeners and active middleware.

        It does not remove registered middleware.
        DO NOT USE UNLESS YOU WANT TO RESET EVERYTHING.
        """
        self._listeners = {}
        self._active_middleware = []
