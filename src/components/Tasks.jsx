import React from 'react'
import Task from "./Task";
import { useGlobalContext } from '../context/context'

const Tasks = () => {
  
  const {tasksState, query} = useGlobalContext();
  let tasks = tasksState.tasks;
  // console.log(tasks);
  
  if(query != "")
  {
    tasks = tasks.filter(task => task.text.includes(query));
  }
  
  return (
    <>
      <ul id="task-list">
        {tasks.map(task => (
          <Task key={task.id} task={task}/>
        ))}
      </ul>
    </>
  )
}

export default Tasks