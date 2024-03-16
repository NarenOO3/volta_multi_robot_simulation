#!/usr/bin/env python3

def generate_robot_launch(robot_num, init_pose):
    return f"""

    <group ns="robot{robot_num}">
      <param name="tf_prefix" value="robot{robot_num}_tf" />
      <include file="$(find volta_multi_robot_simulation)/launch/one_robot.launch">
        <arg name="init_pose" value="{init_pose}" />
        <arg name="robot_name"  value="Robot{robot_num}" />
      </include>
    </group>
      
    """
def anticlockwise_spiral(n):
    if n <= 0:
        return []

    x, y = 0, 0
    dx, dy = 0, -1
    result = []

    for _ in range(n):
        result.append((x, y))
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
            dx, dy = -dy, dx
        x, y = x + dx, y + dy

    return result

def fill_init_poses(n):
    spiral_coords = anticlockwise_spiral(n)
    init_poses = []

    for coord in spiral_coords:
        x, y = coord
        init_poses.append("-x {} -y {} -z 0".format(x, y))

    return init_poses

def generate_launch_file(num_robots):
    init_poses = fill_init_poses(num_robots)    
    launch_code = """
    <launch>
        <!-- No namespace here as we will share this description. Access with slash at the beginning -->
        <param name="robot_description" command="xacro \'$(find volta_multi_robot_simulation)/urdf/volta.urdf.xacro\'"/>
        """
    
    for i in range(num_robots):
        launch_code += generate_robot_launch(i + 1, init_poses[i % len(init_poses)])

    launch_code += "</launch>\n"

    return launch_code

def main():
    num_robots = 8 #No of robot that should be generated
    launch_code = generate_launch_file(num_robots)

    # Specify the file path to save the launch file
    file_path = "/home/pixeldude/PixelDude.../workspaces/catkin_ws/src/volta_multi_robot_simulation/temp/robots.launch"

    # Write the generated launch code to the file
    with open(file_path, "w") as f:
        f.write(launch_code)

    print(f"Launch file saved to: {file_path}")

if __name__ == "__main__":
    main()