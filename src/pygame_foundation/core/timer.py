class Timer:
    def __init__(self, duration:int, callback, loops:int=1, repeat=False):
        ''' Remember that duration must be in seconds not milliseconds. '''
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
        self.active = False


class TimerManager:
    def __init__(self):
        self.timers = []

    def add(self, *timers:Timer):
        for timer in timers:
            if timer in self:
                continue

            self.timers.append(timer)
        return timers[0] if len(timers) == 1 else timers

    def after(self, milliseconds:int, callback, loops:int=1):
        ''' Run the callback after specified time. '''
        seconds = milliseconds / 1000
        return self.add(Timer(seconds, callback, loops))

    def every(self, milliseconds:int, callback):
        ''' Run the callback every time the duration ends and then resets to 0. Will go on forever. '''
        seconds = milliseconds / 1000
        return self.add(Timer(seconds, callback, repeat=True))

    def remove(self, timer:Timer):
        if timer not in self:
            return
        
        self.timers.remove(timer)

    def clear(self):
        self.timers.clear()

    def update(self, dt):
        for timer in self.timers[:]:
            timer.update(dt)

            if not timer.active:
                self.timers.remove(timer)

    def __contains__(self, item):
        return item in self.timers 

    