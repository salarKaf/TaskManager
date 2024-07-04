import React from 'react'
import SearchTask from "./SearchTask"
import Tasks from "./Tasks";
import AddTask from "./AddTask";
import TaskStats from './TaskStats';

const TaskContainer = () => {
  return (
    <div id="task-container">
      <SearchTask />
      <TaskStats />
      <Tasks />
      <AddTask />
    </div>
  )
}

export default TaskContainer