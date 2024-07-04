import React from 'react'
import { useGlobalContext } from '../context/context'

const Task = ({ task }) => {
  
  const {tasksDispatch} = useGlobalContext();
  
  const handleDelete = () => {
    tasksDispatch({ type: "DELETE_TASK", payload: {id: task.id} });
  }
  
  const toggleTaskStatus = () => {
    tasksDispatch({ type: "TOGGLE_TASK_STATUS", payload: { id: task.id } });
  }
  
  return (
    <li style={{ display: "flex", alignItems: "center", borderLeft: (task.isCompleted ? "3px solid green" : "3px solid red") }}>
      <span style={{flex: 1, textDecoration: (task.isCompleted ? "line-through" : "none" )}}>
        {task.text}
      </span>
      <span>
        <button className="task-btn mark-comp-btn" onClick={toggleTaskStatus} style={{background: (task.isCompleted ? "green" : "none")}}>&#x2714;</button>
        <button className="task-btn delete-btn" onClick={handleDelete}>X</button>
      </span>
    </li>
  )
}

export default Task