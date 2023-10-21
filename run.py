from flask import Flask
import multiprocessing
from api import backendAPI 
from src.main import main



def run_app():
    backendAPI.app.run(debug=False,threaded=True)

def run_main():
    main()

if __name__ == "__main__":
    t1 = multiprocessing.Process(target=run_app)
    t2 = multiprocessing.Process(target=run_main)
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    if t1.is_alive():
        t1.terminate()
    if t2.is_alive():
        t2.terminate()
        

