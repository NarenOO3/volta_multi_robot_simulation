def generate_launch_file(num_robots, save_path):
    launch_content = f'''<launch>

  <!-- start world -->
    <include file="$(find gazebo_ros)/launch/empty_world.launch">
    <arg name="world_name" value="$(find volta_multi_robot_simulation)/worlds/basic_world.world"/>  
    <arg name="paused" value="false"/>
    <arg name="use_sim_time" value="true"/>
    <arg name="gui" value="true"/>
    <arg name="recording" value="false"/>
    <arg name="debug" value="false"/>
  </include>

  <!-- include our robots -->'''
    
    for i in range(1, num_robots + 1):
        launch_content += f'''
  <node name="robot{i}_joint_state_publisher" pkg="joint_state_publisher" type="joint_state_publisher" respawn="true" output="screen">
      <remap from="joint_states" to="robot{i}/joint_states"/>
  </node>'''
    
    launch_content += '''
  <!-- Launch the TF publisher node -->
  <include file="$(find volta_multi_robot_simulation)/launch/robots.launch"/>
</launch>'''
    
    with open(save_path, "w") as file:
        file.write(launch_content)


# Example usage
num_robots = 8
save_path = "/home/pixeldude/PixelDude.../workspaces/catkin_ws/src/volta_multi_robot_simulation/temp/main.launch"
generate_launch_file(num_robots, save_path)
print("Launch file generated successfully.")