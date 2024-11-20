from crazyflie_py import Crazyswarm
from cflib.crazyflie.log import LogConfig

TAKEOFF_DURATION = 2.5

def log_cb(timestamp, data, log_config):
    print('[%d][%s]: %s' % (timestamp, log_config.name, data))

def main():
    print("Working!")
    
    # Initialize the crazyflie
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    cf = swarm.allcfs.crazyflies[0]

    # Set up logger
    # log_config = LogConfig(name='State Estimate', period_in_ms=10)
    # log_config.add_variable('stateEstimate.x', 'float')
    # log_config.add_variable('stateEstimate.y', 'float')
    # log_config.add_variable('stateEstimate.z', 'float')
    # log_config.add_variable('stateEstimate.vx', 'float')
    # log_config.add_variable('stateEstimate.vy', 'float')
    # log_config.add_variable('stateEstimate.vz', 'float')
    # log_config.add_variable('stateEstimate.qx', 'float')
    # log_config.add_variable('stateEstimate.qy', 'float')
    # log_config.add_variable('stateEstimate.qz', 'float')
    # log_config.add_variable('stateEstimate.qw', 'float')
    # log_config.add_variable('stateEstimateZ.rateRoll', 'int16_t')
    # log_config.add_variable('stateEstimateZ.ratePitch', 'int16_t')
    # log_config.add_variable('stateEstimateZ.rateYaw', 'int16_t')
    # cf.log.add_config(log_config)
    # log_config.data_received_cb.add_callback(log_cb)
    # log_config.start()

    # Fly
    cf.takeoff(targetHeight=1.0, duration=TAKEOFF_DURATION)
    timeHelper.sleep(TAKEOFF_DURATION)

    cf.goTo([1.0, 0.0, 1.0], 0, 2.0)
    timeHelper.sleep(5)
    cf.goTo([0.0, 1.0, 1.0], 0, 2.0)
    timeHelper.sleep(5)
    cf.goTo([-1.0, 0.0, 2.0], 0, 2.0)
    timeHelper.sleep(5)
    cf.goTo([0.0, -1.0, 1.0], 0, 2.0)
    timeHelper.sleep(5)

    cf.land(targetHeight=0.04, duration=TAKEOFF_DURATION)
    timeHelper.sleep(TAKEOFF_DURATION)

    # log_config.stop()

if __name__ == '__main__':
    main()
