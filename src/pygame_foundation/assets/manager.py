from pygame.typing import FileLike
from pygame import Surface
import pygame

class ImageAsset:
    def __init__(self, path:FileLike, alpha:bool):
        self.path = path
        self.alpha = alpha
        self.surface = self.load()

    def load(self, path=None):
        if path is not None:
            self.path = path

        image = pygame.image.load(self.path)

        if self.alpha:
            self.surface = image.convert_alpha()
        else:
            self.surface = image.convert()

        return self.surface
    
    def reload(self):
        return self.load()

class AssetManager:
    def __init__(self):
        self.images = {}

    def load_image(self, name:str, image_path:FileLike, replace:bool=False, alpha:bool=True) -> Surface:
        ''' 
        Loads the given image from path and caches it and stores the name in AssetManager.images.
        If replace is True it will reassign the name with the image_path.
        The alpha is parameter is for loading in transparent or not transparent images. 
        Leave as True for transparent images.
        It also effects performance. 
        ''' 
        if name in self.images and replace is True:
                self.images[name] = ImageAsset(image_path, alpha) 
                return self.images[name].surface

        elif name in self.images and not replace:
            return self.images[name].surface

        else:
            self.images[name] = ImageAsset(image_path, alpha) 
            return self.images[name].surface

    def get_image_asset(self, name:str) -> ImageAsset:
        ''' Get a image asset by the specified name '''
        if not self.has_image(name):
            raise ValueError(f'Image "{name}" is not loaded.')
        
        return self.images[name]

    def get_image(self, name:str) -> Surface:
        ''' Get a image surface by the specified name '''
        if not self.has_image(name):
            raise ValueError(f'Image "{name}" is not loaded.')
        
        return self.images[name].surface

    def has_image(self, name:str) -> bool:
        ''' Checks if the image name exists in image assets. Returns a boolean '''
        return name in self.images

    def remove_image(self, name:str):
        ''' Remove specified image and metadata from image assets '''
        if self.has_image(name):
            return self.images.pop(name)

        else:
            raise ValueError(f'Image "{name}" is not loaded so it cannot be removed.')

    def clear_images(self):
        ''' Clear all images from assets '''
        self.images.clear()

    def reload_image(self, name:str):
        ''' Reloads specified image '''
        if self.has_image(name):
            self.get_image_asset(name).reload()

        else:
            raise ValueError(f'Image "{name}" is not loaded.')

    def reload_all_images(self):
        ''' Reload all images '''
        for image_asset in self.images.values():
            image_asset.reload()




