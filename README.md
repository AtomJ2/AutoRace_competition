# 🏎️ AutoRace 2023 Solution 🏆

This repository contains our solution for the **AutoRace 2023** competition.  
**Project developers:**
1. [Yaroslav Chekanov](https://github.com/AtomJ2)
2. [Sergey Mendrul](https://github.com/chukotskiyShaman)
3. [Svyatoslav Gubin](https://github.com/Porweks)

---

## 📋 Project Description

The repository includes code to launch autonomous robot movement in the AutoRace scene. The application uses **ROS2** to run nodes that process data and execute navigation commands.

---

## 🚀 How to Install Dependencies?

First, install all necessary dependencies by running:

```bash
pip install -r requirements.txt
```

---

## 🔧 How to Run the Project?

Follow these steps to build and launch the project:

1. **Build the project using `colcon`:**

   ```bash
   colcon build
   ```

2. **Source the environment after the build:**

   ```bash
   source install/setup.bash
   ```

3. **Launch the main application using `ros2 launch`:**

   ```bash
   ros2 launch XROS_move XROS_move.launch.py
   ```

---

## 🛠️ Dependencies

- Python 3.x
- ROS2 Humble
- RViz
- Gazebo Harmonic
- Libraries specified in `requirements.txt`
