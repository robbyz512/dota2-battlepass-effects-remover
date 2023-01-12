import os
import sys
import shutil
import traceback

import helper

rootDire  = os.getcwd()
sourceDir = os.path.join(rootDire, 'source')
buildDir  = os.path.join(rootDire, 'build')

class App():
    def __init__(self):
        self.pak01_dir = None
        self.keep_cosmetic_effects = None
        self.cleanFiles()
        self.getSettings()
        self.patch()
        self.createVPK()
    
    def cleanFiles(self):
        shutil.rmtree(buildDir, ignore_errors=True)
        open('log.txt', 'w').close()

    def getSettings(self):

        if not os.path.exists('settings.txt'):
            input("settings.txt not found, extract it to where battlepass-patcher.exe is")

        with open('settings.txt') as file:
            lines = file.readlines()

            for line in lines:
                if line.startswith('#') or line.isspace():
                    continue
                else:
                    line = line.strip().split('=')
                    if line[0] == 'path': 
                        self.pak01_dir = line[1]
                        self.pak01_dir = os.path.join(self.pak01_dir + "\\game\\dota\\pak01_dir.vpk")
                    if line[0] == 'keep_cosmetic_effects': self.keep_cosmetic_effects = line[1]

    def patch(self):
        print(r"""
        battlepass-patcher
        Github: https://github.com/robbyz512/
        -------------------------------------------------""")

        if not os.path.exists(self.pak01_dir):
            input("Path does not exist: " + self.pak01_dir)
            sys.exit(1)

        for index, item in enumerate(helper.mods):
            folders = os.path.join(sourceDir, os.path.dirname(helper.mods[index]))
            if not os.path.exists(folders): os.makedirs(folders)

            print("Extracting: " + helper.mods[index])
            helper.vpkExtractor(self.pak01_dir, helper.mods[index], os.path.join(sourceDir, helper.mods[index]))
        
        with open(os.path.join(sourceDir, 'scripts/items/items_game.txt'), 'r', encoding='utf8') as file:
            for line in file:
                for index, item in enumerate(helper.mods):
                    if helper.trimExtension(helper.mods[index]) in line:

                        path = next(file, '').strip().split("\"")
                        path = path[3]

                        if 'items' in os.path.dirname(path) and self.keep_cosmetic_effects == 'true': continue

                        build_path = os.path.join(buildDir, helper.addExtension(path))
                        source_path = os.path.join(sourceDir, helper.mods[index])

                        os.makedirs(os.path.dirname(build_path), exist_ok=True)
                        shutil.copy(source_path, build_path)

                        print("Replaced: " + os.path.basename(build_path) + " >> " + os.path.basename(helper.mods[index]))
            
    def createVPK(self):
        helper.vpkCreator(buildDir)
        print('-----')
        input('Done, created pak01_dir.vpk. Read "adding vpk files" in settings.txt for how to use it.')

if __name__ == '__main__':
    try:
        app = App()
    except Exception:
        with open('log.txt', 'w+') as file:
            file.write(traceback.format_exc())
            input("Failed to patch, read log.txt for details.")