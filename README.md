# PatientFlow | Hospital Waiting Room Management System

A robust, CLI-based management system designed to handle patient queues using a **Doubly Circular Linked List** with a dummy head. This system ensures efficient patient registration, serving, and data management with an emphasis on manual data structure implementation.

---

# PatientFlow | Hospital Waiting Room Management System
<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge" />
  <br />
  <img src="https://img.shields.io/badge/Data_Structure-Linked_List-blue?style=flat-square" alt="Structure" />
</p>

---

## Features

* **Patient Registration:** Add patients to the queue with ID, Name, Age, and Blood Group details.
* **Serve Patient:** Automatically processes the next patient in line (FIFO) and allows for detail viewing.
* **Advanced Queue Control:** * **Reverse the Line:** Instantly flip the waiting order using pointer manipulation.
    * **Cancel All:** Wipe all scheduled appointments and reset the waiting room.
* **Live Statistics:** Real-time check to see if the doctor has cleared the queue and can go home.
* **Terminal UI:** Color-coded status messages (Red/Green/Yellow) for an intuitive CLI experience.

---

## Technical Stack

* **Language:** Python 3
* **Core Logic:** Object-Oriented Programming (OOP)
* **Data Structure:** Doubly Circular Linked List with a Dummy Head.


---

## Installation & Setup

1. **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/Hospital-Waiting-Room-Management.git](https://github.com/your-username/Hospital-Waiting-Room-Management.git)
    ```

2. **Project Structure:**
    Ensure your files are organized as follows:
    ```text
    /hospital-management-system
    └── main.py              # The complete Python/Logic code
    ```

3. **Run the Application:**
    Navigate to the folder and run:
    ```bash
    python main.py
    ```

---

## How It Works

1. **Adding a Patient:** The system creates a `Patient` node. It links the `tail` to the new node and the new node back to the `head`, maintaining the circularity.
2. **Serving Patients:** The node immediately following the `dummy` head is removed. Pointers of the `dummy` and the `third` node are reconnected to bridge the gap.
3. **Reversal Logic:** Instead of rebuilding the list, the system swaps the `info` strings between the front and back nodes iteratively until they meet in the middle.
4. **Doctor Status:** The system checks if `tail.info` is `None`, signaling that no active patients are in the circular chain.

---

## License
This project is open-source and available under the MIT License.
