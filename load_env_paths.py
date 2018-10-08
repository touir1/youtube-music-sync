import os


class EnvPathLoader:

    @staticmethod
    def load_env_paths():
        os.environ['PATH'] = os.environ['PATH']+";"+os.getcwd()+"/ffmpeg/bin"