import  unittest

dir="./case/"

suit =unittest.defaultTestLoader.discover(start_dir=dir,pattern="exam*.py")

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suit)