import matplotlib.pyplot as plt
from random import random, seed

def generate(config):
    """ This generates a velocity/time motion profile where the user can supply
    velocity, acceleration, distance travelled, and some noise to introduce

    This is a quick script that I can make nicer looking, but that's likely
    not realistic for anyone considering using this template... Sorry.

    Also thinking about adding comments to this just in case you're interested,
    but it's late and this is meant to be an example of a random script. Maybe
    tomorrow.

    Args:
        config (dict): Config that matches the UI elements added to QtScript.

    Returns:
        None

    """
    seed()
    idle_time = config['Max Idle']
    max_vel = config['Target Velocity']
    accel = config['Target Acceleration']
    decel = config['Target Deceleration']
    distance = config['Move Distance']
    frequency = config['Sampling Frequency']
    noise = config['Noise Amplitude']

    start_delay = idle_time*random()
    start_samples = start_delay * frequency
    end_delay = idle_time*random()
    end_samples = end_delay * frequency

    time_to_accel = max_vel/accel
    time_to_decel = max_vel/decel
    distance_during_accel = (1/2)*accel*time_to_accel**2
    distance_during_decel = (1/2)*decel*time_to_decel**2
    distance_at_velocity = distance - distance_during_accel - distance_during_decel
    time_at_velocity = distance_at_velocity/max_vel

    samples_during_accel = time_to_accel * frequency
    samples_during_decel = time_to_decel * frequency
    samples_during_vel = time_at_velocity * frequency
    print(samples_during_vel)

    output = []
    for i in range(int(start_samples)):
        vel = 0 + random()*noise - 0.5*noise
        output.append(vel)
    for i in range(int(samples_during_accel)):
        time = i/frequency
        vel = time * accel
        vel = vel + random()*noise - 0.5*noise
        output.append(vel)
    if samples_during_vel > 0:
        for i in range(int(samples_during_vel)):
            vel = max_vel + random()*noise - 0.5*noise
            output.append(vel)
    for i in range(int(samples_during_decel)):
        time = i/frequency
        vel = max_vel - time * decel
        vel = vel + random()*noise - 0.5*noise
        output.append(vel)
    for i in range(int(end_samples)):
        vel = 0 + random()*noise - 0.5*noise
        output.append(vel)
    plt.plot(output)
    plt.show()

    with open('motion_example.csv', 'w') as f:
        f.write('data\n')
        f.writelines([str(point)+'\n' for point in output])
