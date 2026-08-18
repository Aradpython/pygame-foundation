from .scene import SceneStatus 

class SceneManager:
    ''' A class used for managing Scenes. '''
    def __init__(self, game):
        self.game = game
        self.current_scenes = []

    def _activate_scene(self, scene):
        scene.enter()
        scene.status = SceneStatus.ACTIVE
        self.game.input_manager.set_context(scene.input_context)

    def change_scene(self, scene):
        """Replace the active scene or set it to one if none where selected before. """
        if self.current_scenes:
            old_scene = self.current_scenes.pop()
            old_scene.exit()

        self.current_scenes.append(scene)
        self._activate_scene(scene)

    def push_scene(self, scene):
        """
        Overlay a scene, preserving the current one underneath. 
        The attributes configured in the overlayed Scene will determine whether to draw and/or update the underlaying scenes. 
        """

        self.current_scenes.append(scene)
        self._activate_scene(scene)

        if len(self.current_scenes) > 1:
            previous_scene = self.current_scenes[-2]

            if scene.blocks_updates:
                previous_scene.pause()

    def pop_scene(self):
        """
        Close the active scene and return to the one below it. 
        If there is no overlaying Scene, it will raise an IndexError.
        """
        if not self.current_scenes:
            return

        old_scene = self.current_scenes.pop()
        old_scene.exit()

        if self.current_scenes:
            scene = self.current_scenes[-1]
            scene.resume()
            self.game.input_manager.set_context(scene.input_context)

    def update(self, dt, events):
        ''' Updates the current Scene or Scenes. '''
        if not self.current_scenes:
            return

        self.game.input_manager.update(events)

        start = len(self.current_scenes) - 1

        for i in range(start, -1, -1):
            scene = self.current_scenes[i]

            if scene.is_active:
                scene.update(dt, events)

            if scene.blocks_updates:
                break

    def draw(self, screen):
        ''' Draws the current Scene or Scenes.  '''
        if not self.current_scenes:
            return

        start = 0

        for i in range(len(self.current_scenes) - 1, -1, -1):
            scene = self.current_scenes[i]

            if scene.blocks_drawings:
                start = i
                break

        for scene in self.current_scenes[start:]:
            scene.draw(screen)

