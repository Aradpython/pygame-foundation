class Timer:
    ''' A class to create Timers that run a callback when finished. '''
    def __init__(self, duration:int, callback, loops:int=1, repeat=False):
        ''' 
        Initializes the Timer.

        Remember that duration must be in seconds not milliseconds. 
        '''
        if duration <= 0:
            raise ValueError("Timer duration must be greater than 0")

        if loops < 1:
            raise ValueError("Timer loops must be at least 1")
        
        self.duration = duration
        self.callback = callback
        self.loops = loops
        self.repeat = repeat

        self.elapsed = 0
        self.active = True

    def update(self, dt):
        ''' Updates the timer depending on whether it is active or not. Also handles loops and recurring timers. '''
        if not self.active:
            return
    
        self.elapsed += dt
    
        while self.active and self.elapsed >= self.duration:
            self.elapsed -= self.duration
            self.callback()

            if not self.repeat:
                self.loops -= 1

                if self.loops <= 0:
                    self.active = False
                    break

    def cancel(self):
        ''' Cancels the Timer. '''
        self.active = False


class TimerManager:
    ''' A class that acts as a manager for Timers. '''
    def __init__(self):
        ''' Initializes the Timer Manager. '''
        self.timers = []

    def add(self, *timers:Timer):
        ''' Adds one or more timers to the manager. '''
        for timer in timers:
            if timer in self:
                continue

            self.timers.append(timer)
        return timers[0] if len(timers) == 1 else timers

    def after(self, milliseconds:int, callback, loops:int=1):
        ''' Runs the callback after specified time. It creates a Timer object to do this'''
        seconds = milliseconds / 1000
        return self.add(Timer(seconds, callback, loops))

    def every(self, milliseconds:int, callback):
        ''' Runs the callback every time the duration ends and then resets the elapsed time to 0. Will go on indefinitely. It creates a Timer object to do this'''
        seconds = milliseconds / 1000
        return self.add(Timer(seconds, callback, repeat=True))

    def remove(self, timer:Timer):
        ''' Remove a Timer from the manager. '''
        if timer not in self:
            return
        
        self.timers.remove(timer)

    def clear(self):
        ''' Clear all Timers from the Manager. '''
        self.timers.clear()

    def update(self, dt):
        ''' Update all timers. Calls the update() method of the Timers. Automatically removes deactive timers. '''
        for timer in self.timers[:]:
            timer.update(dt)

            if not timer.active:
                self.timers.remove(timer)

    def __contains__(self, item):
        return item in self.timers 

    