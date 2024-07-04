import React from 'react'
import { useGlobalContext } from '../context/context'

const TaskStats = () => {
  
  const { tasksState } = useGlobalContext();
  const tasks = tasksState.tasks;
  const completedNoOfTasks = tasks.filter(task => task.isCompleted).length;
  const pendingNoOfTasks = tasks.length - completedNoOfTasks;
  
  return (
    <div style={{margin: "15px"}}>{pendingNoOfTasks} pending, {completedNoOfTasks} completed</div>
  )
}

export default TaskStats