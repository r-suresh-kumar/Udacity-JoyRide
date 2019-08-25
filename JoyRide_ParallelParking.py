# Before running any code changes make sure to click the button "Restart Connection" above first.
# Also make sure to click Reset in the simulator to refresh the connection.
# After making any code changes, make sure to click the button "Restart Connection" above first. Then re-run your code cell (Ctrl+Enter).
# You need to wait for the Kernel Ready message.
 
car_parameters = {"throttle": 0, "steer": 0, "brake": 0}
 
def control(pos_x, pos_y, time, velocity):
    """ Controls the simulated car"""
    global car_parameters
   
    if time < 1.8:
        car_parameters['throttle'] = 1
                
    elif  pos_y > 41.9:
        #car_parameters['steer'] = 0
        car_parameters['throttle'] = -1
        
    elif  pos_y > 36.8:
        car_parameters['steer'] = 40
        
    elif pos_y > 33.1: 
        car_parameters['throttle'] = -1
        car_parameters['steer'] = -37
         
    else:
        car_parameters['steer'] = 0
        car_parameters['throttle'] = 0
        car_parameters['brake'] = 1
   
    return car_parameters
   
import src.simulate as sim
sim.run(control)
